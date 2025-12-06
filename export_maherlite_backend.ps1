# ============================================
# MAHERLITE BACKEND CODE EXPORT (FINAL FIXED VERSION)
# ============================================

# Root project path
$projectPath = "C:\D Drive Files\BSIT-B-F23\5th Semester\Advanced Web (Python Based)\Zulqarnain\MaherLite"

# Backend folder (empty because manage.py is directly in MaherLite)
$backendFolder = ""

# Build target path
if ($backendFolder -eq "") {
    $targetPath = $projectPath
} else {
    $targetPath = Join-Path $projectPath $backendFolder
}

# Output file path
$outputFile = Join-Path $projectPath "backend_project_code.txt"

# Validate path
if (-not (Test-Path $targetPath)) {
    Write-Host "❌ Backend folder not found at: $targetPath"
    pause
    exit
}

# Ignore lists
$ignoreFolders = @("__pycache__", ".venv", "venv", "env", "migrations", "build", "dist", "node_modules", ".git")
$ignoreExtensions = @(".sqlite3", ".db")
$includeExtensions = @(".py", ".js", ".jsx", ".css", ".html")

# Helper functions
function Should-SkipFolder {
    param([string]$path)
    foreach ($skip in $ignoreFolders) {
        if ($path -like "*\$skip*") { return $true }
    }
    return $false
}

function Should-IncludeFile {
    param([System.IO.FileInfo]$file)
    $ext = $file.Extension.ToLowerInvariant()
    if ($ignoreExtensions -contains $ext) { return $false }
    if ($includeExtensions -contains $ext) { return $true }
    return $false
}

# Prepare output
if (Test-Path $outputFile) { Remove-Item $outputFile -Force }
New-Item -Path $outputFile -ItemType File | Out-Null

Write-Host "📁 Exporting backend code from: $targetPath"
Write-Host "⚙️  Please wait, this might take a few minutes..."
Write-Host "--------------------------------------------------"

# Collect source files safely
$files = Get-ChildItem -Path $targetPath -File -Recurse -Force -ErrorAction SilentlyContinue |
    Where-Object { -not (Should-SkipFolder $_.FullName) -and (Should-IncludeFile $_) }

$total = $files.Count
$processed = 0

foreach ($file in $files) {
    $processed++
    if ($processed % 20 -eq 0) { Write-Host "📄 Processed $processed of $total files..." }

    Add-Content $outputFile "========================================"
    Add-Content $outputFile "FILE: $($file.FullName)"
    Add-Content $outputFile "========================================"

    try {
        $reader = [System.IO.StreamReader]::new($file.FullName)
        while (-not $reader.EndOfStream) {
            $line = $reader.ReadLine()
            Add-Content $outputFile $line
        }
        $reader.Close()
        Add-Content $outputFile "`n`n"
    } catch {
        Add-Content $outputFile "[ERROR READING FILE: $($_.Exception.Message)]`n`n"
    }
}

Write-Host "--------------------------------------------------"
Write-Host "✅ DONE! Exported $processed files successfully."
Write-Host "📄 Output saved at:" $outputFile
Write-Host "--------------------------------------------------"
pause
