# Deploy zdrowie.fit to Cyber_Folks SFTP server
# Pure ASCII — Windows PowerShell 5.1 + 7.x compatible
# Uses OpenSSH (ssh, scp) which is built-in on Win10 1809+

$ErrorActionPreference = "Stop"

# ─── Config ────────────────────────────────────────────
$SshHost = "s159.cyber-folks.pl"
$SshPort = 222
$SshUser = "bestios"
$RemoteRoot = "/home/bestios/domains/zdrowie.fit"
$RemotePath = "$RemoteRoot/public_html"
$LocalBuild = "C:\PYTHON\ARCHAIOS Demand Engine\zdrowie-fit-generator\output\zdrowie-fit"
$ProductionUrl = "https://zdrowie.fit"

Write-Host ""
Write-Host "===== DEPLOY zdrowie.fit -> Cyber_Folks =====" -ForegroundColor Cyan
Write-Host ""

# ─── Krok 1: lokalny build ─────────────────────────────
Write-Host "[1/6] Local build check..." -ForegroundColor Yellow
if (-not (Test-Path "$LocalBuild\index.html")) {
    Write-Host "  ERROR: missing $LocalBuild\index.html" -ForegroundColor Red
    Write-Host "  Run first: python build.py --domain zdrowie.fit --clean" -ForegroundColor Red
    exit 1
}
$fileCount = (Get-ChildItem -Path $LocalBuild -Recurse -File).Count
$totalKB = [math]::Round((Get-ChildItem -Path $LocalBuild -Recurse -File | Measure-Object Length -Sum).Sum / 1KB, 1)
Write-Host "  OK: $fileCount files, $totalKB KB" -ForegroundColor Green

# ─── Krok 2: OpenSSH check ─────────────────────────────
Write-Host ""
Write-Host "[2/6] OpenSSH client check..." -ForegroundColor Yellow
$sshCmd = Get-Command ssh -ErrorAction SilentlyContinue
$scpCmd = Get-Command scp -ErrorAction SilentlyContinue
if (-not $sshCmd -or -not $scpCmd) {
    Write-Host "  MISSING: install as Admin:" -ForegroundColor Red
    Write-Host "    Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0" -ForegroundColor White
    exit 2
}
Write-Host "  OK: ssh + scp available" -ForegroundColor Green

# ─── Krok 3: SSH test (1 password prompt) ──────────────
Write-Host ""
Write-Host "[3/6] SSH connection test (1 attempt - careful with fail2ban!)..." -ForegroundColor Yellow
Write-Host "  You will be asked for password (DirectAdmin password)." -ForegroundColor Cyan
Write-Host ""

$testResult = & ssh -p $SshPort -o "StrictHostKeyChecking=accept-new" -o "ConnectTimeout=10" "$SshUser@$SshHost" "echo CONNECTED && hostname && pwd"
if ($LASTEXITCODE -ne 0) {
    Write-Host "  SSH FAILED. Aborting before more attempts (fail2ban risk)." -ForegroundColor Red
    exit 3
}
Write-Host "  OK: $testResult" -ForegroundColor Green

# ─── Krok 4: server-side backup (1 password prompt) ────
$timestamp = Get-Date -Format "yyyyMMdd-HHmmss"
$backupName = "public_html_backup_$timestamp"
Write-Host ""
Write-Host "[4/6] Server backup: public_html -> $backupName ..." -ForegroundColor Yellow

$backupCmd = "cp -a $RemotePath $RemoteRoot/$backupName && echo BACKUP_OK && ls -la $RemoteRoot/ | head -8"
& ssh -p $SshPort "$SshUser@$SshHost" $backupCmd
if ($LASTEXITCODE -ne 0) {
    Write-Host "  Backup FAILED" -ForegroundColor Red
    exit 4
}
Write-Host "  OK: backup saved" -ForegroundColor Green

# ─── Krok 5: clean + upload (2 password prompts) ───────
Write-Host ""
Write-Host "[5/6] Clean remote + upload new build..." -ForegroundColor Yellow

# Clean (zachowujemy parent katalog public_html, czyscimy zawartosc)
$cleanCmd = "find $RemotePath -mindepth 1 -delete 2>/dev/null; echo CLEAN_OK"
& ssh -p $SshPort "$SshUser@$SshHost" $cleanCmd
if ($LASTEXITCODE -ne 0) {
    Write-Host "  Clean FAILED" -ForegroundColor Red
    exit 5
}
Write-Host "  Cleaned remote public_html/" -ForegroundColor Green

# Upload — scp -r preserve dir structure
Write-Host "  Uploading $fileCount files ($totalKB KB)..." -ForegroundColor Cyan
& scp -P $SshPort -r "$LocalBuild\*" "${SshUser}@${SshHost}:$RemotePath/"
if ($LASTEXITCODE -ne 0) {
    Write-Host "  Upload FAILED" -ForegroundColor Red
    exit 6
}
Write-Host "  OK: upload complete" -ForegroundColor Green

# ─── Krok 6: HTTP 200 check ────────────────────────────
Write-Host ""
Write-Host "[6/6] HTTP check $ProductionUrl ..." -ForegroundColor Yellow
Start-Sleep -Seconds 2
try {
    $r = Invoke-WebRequest -Uri $ProductionUrl -Method Head -MaximumRedirection 5 -UseBasicParsing -TimeoutSec 15
    Write-Host "  OK: HTTP $($r.StatusCode) $($r.StatusDescription)" -ForegroundColor Green
    Write-Host "  Server: $($r.Headers['Server'])" -ForegroundColor Cyan
} catch {
    Write-Host "  WARN: $($_.Exception.Message)" -ForegroundColor Yellow
    Write-Host "  Check manually in browser." -ForegroundColor Yellow
}

Write-Host ""
Write-Host "===== DEPLOY DONE =====" -ForegroundColor Green
Write-Host ""
Write-Host "Check in browser:" -ForegroundColor Cyan
Write-Host "  $ProductionUrl" -ForegroundColor White
Write-Host "  $ProductionUrl/artykuly.html" -ForegroundColor White
Write-Host "  $ProductionUrl/artykuly/cztery-filary-odpornosci-psychicznej.html" -ForegroundColor White
Write-Host ""
Write-Host "Server backup name: $backupName" -ForegroundColor Cyan
Write-Host "Rollback (if needed):" -ForegroundColor Cyan
Write-Host "  ssh -p $SshPort $SshUser@$SshHost ""find $RemotePath -mindepth 1 -delete; cp -a $RemoteRoot/$backupName/. $RemotePath/""" -ForegroundColor Gray
Write-Host ""
