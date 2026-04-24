"""Image upload endpoint — Pillow resize + WebP."""

import uuid
from pathlib import Path

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from slugify import slugify

from app.core.auth import get_current_admin

router = APIRouter(prefix="/upload", tags=["upload"])

ALLOWED_MIME = {"image/jpeg", "image/png", "image/webp", "image/gif"}
MAX_SIZE_MB = 10
BACKEND_DIR = Path(__file__).resolve().parent.parent.parent
UPLOADS_DIR = BACKEND_DIR / "uploads"
UPLOADS_DIR.mkdir(exist_ok=True)

# Rozmiary do wygenerowania
SIZES = {
    "hero": (1200, 630),     # artykuł hero, OG image
    "card": (800, 450),      # card na liście
    "thumb": (400, 225),     # thumbnail
}


@router.post("/image")
async def upload_image(file: UploadFile = File(...), _: str = Depends(get_current_admin)):
    if file.content_type not in ALLOWED_MIME:
        raise HTTPException(400, f"Nieobsługiwany format: {file.content_type}")

    content = await file.read()
    if len(content) > MAX_SIZE_MB * 1024 * 1024:
        raise HTTPException(400, f"Plik za duży (max {MAX_SIZE_MB} MB)")

    try:
        from PIL import Image
        from io import BytesIO
    except ImportError:
        raise HTTPException(500, "Pillow nie zainstalowany — uruchom: pip install Pillow")

    # Unikalny base name
    base = slugify(Path(file.filename).stem, max_length=80) or "image"
    unique_id = uuid.uuid4().hex[:8]
    base_name = f"{base}-{unique_id}"

    img = Image.open(BytesIO(content))
    if img.mode in ("RGBA", "LA", "P"):
        # WebP obsługuje alpha, ale dla JPG fallback na RGB
        img_rgba = img.convert("RGBA")
    else:
        img_rgba = img.convert("RGB")

    result = {"base": base_name, "variants": {}}

    for size_name, (w, h) in SIZES.items():
        # Thumbnail zachowuje aspect ratio
        variant = img_rgba.copy()
        variant.thumbnail((w, h), Image.Resampling.LANCZOS)

        # WebP (preferowany)
        webp_path = UPLOADS_DIR / f"{base_name}-{size_name}.webp"
        if variant.mode == "RGBA":
            variant.save(webp_path, "WEBP", quality=85, method=6)
        else:
            variant.save(webp_path, "WEBP", quality=85, method=6)

        # JPG fallback (dla starszych przeglądarek i social media)
        jpg_path = UPLOADS_DIR / f"{base_name}-{size_name}.jpg"
        (variant.convert("RGB") if variant.mode == "RGBA" else variant).save(jpg_path, "JPEG", quality=88, optimize=True, progressive=True)

        result["variants"][size_name] = {
            "webp": f"/uploads/{base_name}-{size_name}.webp",
            "jpg": f"/uploads/{base_name}-{size_name}.jpg",
            "width": variant.width,
            "height": variant.height,
        }

    # Zwróć URL głównego obrazka (hero-jpg, bo kompatybilność OG)
    result["image_url"] = result["variants"]["hero"]["jpg"]
    return result


@router.delete("/image/{filename}")
def delete_image(filename: str, _: str = Depends(get_current_admin)):
    # Usuń wszystkie warianty tego base_name
    base = filename.rsplit("-", 1)[0] if "-" in filename else filename
    deleted = []
    for p in UPLOADS_DIR.glob(f"{base}-*"):
        p.unlink()
        deleted.append(p.name)
    return {"deleted": deleted}
