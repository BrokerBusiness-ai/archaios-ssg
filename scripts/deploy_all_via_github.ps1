# Deploy WSZYSTKICH satelit Archaios SSG via GitHub Actions
# Triggeruje workflow .github/workflows/deploy.yml przez git push do main
# Każda domena buduje się i deployuje równolegle (matrix strategy)
# Wymagania: git skonfigurowany z poprawnym remote i credentials

$ErrorActionPreference = "Stop"
$RepoRoot = Split-Path -Parent $PSScriptRoot

Write-Host ""
Write-Host "===== DEPLOY ALL SATELITES via GitHub Actions =====" -ForegroundColor Cyan
Write-Host ""

Set-Location $RepoRoot

# Krok 1: weryfikacja git
Write-Host "[1/6] Git status check..." -ForegroundColor Yellow
$gitStatus = git status --porcelain 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "  ERROR: git nie odpowiada w katalogu $RepoRoot" -ForegroundColor Red
    exit 1
}

if ([string]::IsNullOrWhiteSpace($gitStatus)) {
    Write-Host "  Brak zmian do scommitowania." -ForegroundColor Yellow
    $resp = Read-Host "  Chcesz wymusic deploy (workflow_dispatch z GitHub UI)? [t/N]"
    if ($resp -ne 't' -and $resp -ne 'T') {
        Write-Host "  Anulowane." -ForegroundColor Gray
        exit 0
    }
} else {
    Write-Host "  Wykryto zmiany:" -ForegroundColor Green
    Write-Host ""
    git status --short
    Write-Host ""
}

# Krok 2: wybor branch i remote
Write-Host "[2/6] Branch + remote check..." -ForegroundColor Yellow
$currentBranch = git rev-parse --abbrev-ref HEAD
$remoteUrl = git remote get-url origin 2>$null
Write-Host "  Branch:   $currentBranch" -ForegroundColor White
Write-Host "  Remote:   $remoteUrl" -ForegroundColor White

if ($currentBranch -ne "main") {
    Write-Host "  UWAGA: jestes na '$currentBranch', nie 'main'." -ForegroundColor Yellow
    $resp = Read-Host "  Switchnac na main i pchnac stamtad? [t/N]"
    if ($resp -eq 't' -or $resp -eq 'T') {
        git checkout main
        git merge $currentBranch --no-edit
        $currentBranch = "main"
    } else {
        Write-Host "  GH Actions deploy.yml triggeruje sie tylko z 'main'. Anulowane." -ForegroundColor Red
        exit 2
    }
}

# Krok 3: stage all
Write-Host ""
Write-Host "[3/6] Stage zmian (git add)..." -ForegroundColor Yellow
git add -A
$staged = git diff --cached --name-only
$stagedCount = ($staged | Measure-Object).Count
Write-Host "  Zastagowane pliki: $stagedCount" -ForegroundColor Green

# Krok 4: commit
if ($stagedCount -gt 0) {
    Write-Host ""
    Write-Host "[4/6] Commit..." -ForegroundColor Yellow
    $defaultMsg = "deploy: aktualizacja satelit ($(Get-Date -Format 'yyyy-MM-dd HH:mm'))"
    $msg = Read-Host "  Wiadomosc commita [Enter = '$defaultMsg']"
    if ([string]::IsNullOrWhiteSpace($msg)) { $msg = $defaultMsg }

    git commit -m $msg
    if ($LASTEXITCODE -ne 0) {
        Write-Host "  Commit nie udal sie." -ForegroundColor Red
        exit 3
    }
    Write-Host "  OK: $msg" -ForegroundColor Green
} else {
    Write-Host ""
    Write-Host "[4/6] Brak nowego commita (workflow_dispatch dla wymuszenia)." -ForegroundColor Gray
}

# Krok 5: push
Write-Host ""
Write-Host "[5/6] Push do origin/main..." -ForegroundColor Yellow
git push origin main
if ($LASTEXITCODE -ne 0) {
    Write-Host "  Push nie udal sie. Sprawdz credentials/network." -ForegroundColor Red
    exit 4
}
Write-Host "  OK: pushed" -ForegroundColor Green

# Krok 6: link do Actions
Write-Host ""
Write-Host "[6/6] Otwieram GitHub Actions w przegladarce..." -ForegroundColor Yellow
$actionsUrl = $remoteUrl `
    -replace '\.git$', '' `
    -replace '^git@github\.com:', 'https://github.com/' `
    -replace '^https://github\.com/', 'https://github.com/'
$actionsUrl = "$actionsUrl/actions"
Write-Host "  URL: $actionsUrl" -ForegroundColor White
Start-Process $actionsUrl

Write-Host ""
Write-Host "===== ZROBIONE =====" -ForegroundColor Green
Write-Host ""
Write-Host "Co teraz dzieje sie w tle:" -ForegroundColor Cyan
Write-Host "  1. matrix-setup job czyta domains/*.yaml -> generuje liste 18 domen" -ForegroundColor White
Write-Host "  2. Dla kazdej domeny startuje rownolegle:" -ForegroundColor White
Write-Host "     - pip install zaleznosci (~1 min)" -ForegroundColor Gray
Write-Host "     - python build.py --domain <X> --clean (~30 sek)" -ForegroundColor Gray
Write-Host "     - lftp mirror -> /home/bestios/domains/<X>/public_html (~1-2 min)" -ForegroundColor Gray
Write-Host "  3. Calosc 18 domen: typowo 5-8 minut do skonczenia" -ForegroundColor White
Write-Host ""
Write-Host "Status zobaczysz w otwartej przegladarce - GitHub Actions." -ForegroundColor Yellow
Write-Host ""
Write-Host "Po sukcesie sprawdz:" -ForegroundColor Cyan
Write-Host "  curl.exe -sI https://skanujfirme.pl" -ForegroundColor White
Write-Host "  curl.exe -sI https://testnis2.pl" -ForegroundColor White
Write-Host "  curl.exe -sI https://audytzespolu.pl" -ForegroundColor White
Write-Host "  (i kazda inna domena z domains/*.yaml)" -ForegroundColor White
Write-Host ""
