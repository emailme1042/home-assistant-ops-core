# PowerShell Script: Check All Resource Paths for Working JS Files
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
        $size = (Get-Item $fullPath).Length
        if ($size -gt 0) {
            $results += "OK: $fullPath ($size bytes)"
        } else {
            $results += "EMPTY: $fullPath"
        }
    } else {
        $results += "MISSING: $fullPath"
    }
}

Write-Host "--- JS Resource Path Check Results ---"
$results | ForEach-Object { Write-Host $_ }
Write-Host "\n--- Validation Complete ---"
