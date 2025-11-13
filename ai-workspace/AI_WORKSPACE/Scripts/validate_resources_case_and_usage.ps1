# Bulk Validator Script: Check for Case Mismatches and Unused JS Entries
# Usage: Run in PowerShell from S:\www\community

# List all JS files and folders in community (recursively)
$files = Get-ChildItem -Path "S:\www\community" -Recurse -Filter *.js | Select-Object -ExpandProperty FullName

# Load resources.yaml entries
$yamlPath = "S:\resources.yaml"
$yamlLines = Get-Content $yamlPath | Where-Object { $_ -match "- url:" }

# Normalize to lowercase for comparison
$yamlUrls = $yamlLines | ForEach-Object { ($_ -replace "- url: ", "") -replace "/local", "S:" } | ForEach-Object { $_.ToLower() }
$filesLower = $files | ForEach-Object { $_.ToLower() }

# Find mismatches: YAML entries not matching any file
$mismatches = $yamlUrls | Where-Object { $url = $_; -not ($filesLower | Where-Object { $file = $_; $file -like "*$($url.Split('/')[-1])" }) }

# Find unused JS files: Files not referenced in YAML
$unused = $filesLower | Where-Object { $file = $_; -not ($yamlUrls | Where-Object { $url = $_; $file -like "*$($url.Split('/')[-1])" }) }

Write-Host "--- Case Mismatches / Missing Files ---"
$mismatches | ForEach-Object { Write-Host $_ }

Write-Host "\n--- Unused JS Files ---"
$unused | ForEach-Object { Write-Host $_ }

Write-Host "\n--- Validation Complete ---"
