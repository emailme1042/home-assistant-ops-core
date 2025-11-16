# ===============================
# scan_dashboard_entities.ps1
# ===============================

$dashboardPath = "S:\dashboards"

# Get all YAML files
$files = Get-ChildItem -Path $dashboardPath -Recurse -Include *.yaml

$entities = @()

foreach ($file in $files) {
    $content = Get-Content $file.FullName
    foreach ($line in $content) {
        if ($line -match "entity:\s*(\S+)") {
            $entity = $matches[1]
            $entities += $entity
            Write-Host "Found entity: $entity in $($file.Name)" -ForegroundColor Green
        }
    }
}

$uniqueEntities = $entities | Sort-Object -Unique
Write-Host "`n===== Summary of Unique Entities =====" -ForegroundColor Cyan
$uniqueEntities | ForEach-Object { Write-Host $_ }
