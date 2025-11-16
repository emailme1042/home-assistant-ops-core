# PowerShell Script: Verify JS Paths vs resources.yaml
# Usage: Run in PowerShell from S:\www\community

$yamlPath = "S:\resources.yaml"
$yamlLines = Get-Content $yamlPath | Where-Object { $_ -match "- url:" }

$results = @()
foreach ($line in $yamlLines) {
    $url = ($line -replace "- url: ", "").Trim()
    $parts = $url -split "/"
    $folder = $parts[-2]
    $file = $parts[-1]
    $fullPath = "S:\www\community\$folder\$file"
    if (Test-Path $fullPath) {
        $results += "OK: $fullPath"
    } else {
        $results += "MISSING: $fullPath"
    }
}

Write-Host "--- JS Path Validation Results ---"
$results | ForEach-Object { Write-Host $_ }
Write-Host "\n--- Validation Complete ---"
