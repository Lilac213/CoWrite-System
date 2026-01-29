# AI Writing Assistant - Windows Build Script
# Build executable on Windows

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "AI Writing Assistant - Windows Build Script" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ScriptDir

# Check Python
Write-Host ""
Write-Host "1. Checking Python environment..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host $pythonVersion -ForegroundColor Green
} catch {
    Write-Host "Error: Python not found, please install Python 3.9+" -ForegroundColor Red
    exit 1
}

# Check Node.js
Write-Host ""
Write-Host "2. Checking Node.js environment..." -ForegroundColor Yellow
try {
    $nodeVersion = node --version 2>&1
    Write-Host $nodeVersion -ForegroundColor Green
} catch {
    Write-Host "Error: Node.js not found, please install Node.js 18+" -ForegroundColor Red
    exit 1
}

# Create venv and install dependencies
Write-Host ""
Write-Host "3. Installing backend dependencies..." -ForegroundColor Yellow
if (-not (Test-Path "venv")) {
    python -m venv venv
}
& .\venv\Scripts\Activate.ps1
pip install -r requirements.txt

# Build frontend
Write-Host ""
Write-Host "4. Building frontend..." -ForegroundColor Yellow
Set-Location frontend
npm install
npm run build
Set-Location ..

# Copy frontend build artifacts
Write-Host ""
Write-Host "5. Copying frontend build artifacts..." -ForegroundColor Yellow
if (Test-Path "static") {
    Remove-Item -Recurse -Force static
}
Copy-Item -Recurse frontend\dist static

# Package with PyInstaller
Write-Host ""
Write-Host "6. Packaging with PyInstaller..." -ForegroundColor Yellow
pyinstaller app.spec --clean

Write-Host ""
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "Build Complete!" -ForegroundColor Green
Write-Host "Executable location: dist\AI学术写作助手.exe" -ForegroundColor Green
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "How to run:" -ForegroundColor Yellow
Write-Host "1. Copy dist\AI学术写作助手.exe to any directory"
Write-Host "2. First run will automatically create .env config file"
Write-Host "3. Edit .env file, fill in API Key etc."
Write-Host "4. Run again, browser will open automatically"
Write-Host ""
