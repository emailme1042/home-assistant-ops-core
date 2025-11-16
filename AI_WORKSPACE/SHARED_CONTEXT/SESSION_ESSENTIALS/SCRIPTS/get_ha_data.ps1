# Simple HA REST API data export script
# Uses ha_long_lived_token from secrets.yaml

$OUT = "AI_WORKSPACE/SHARED_CONTEXT/SESSION_ESSENTIALS"
$BASE = "http://192.168.1.217:8123/api"

Write-Host "Reading token from secrets.yaml..."
$secretsContent = Get-Content 'S:\secrets.yaml' -Raw
if ($secretsContent -match 'ha_long_lived_token:\s*(.+)') {
    $TOKEN = $matches[1].Trim()
    Write-Host "✅ Token found"
} else {
    Write-Error "❌ Could not find ha_long_lived_token in secrets.yaml"
    exit 1
}

New-Item -ItemType Directory -Force -Path $OUT | Out-Null
$H = @{Authorization = "Bearer $TOKEN"}

Write-Host "Downloading HA data..."

try {
    Invoke-RestMethod -Headers $H -Uri "$BASE/config" -OutFile "$OUT/config.json"
    Write-Host "✅ Config downloaded"
} catch {
    Write-Error "❌ Failed to download config: $($_.Exception.Message)"
    exit 1
}

try {
    Invoke-RestMethod -Headers $H -Uri "$BASE/states" -OutFile "$OUT/entities.json"
    Write-Host "✅ Entity states downloaded"
} catch {
    Write-Error "❌ Failed to download entity states: $($_.Exception.Message)"
    exit 1
}

Write-Host "Processing entity data..."
$states = Get-Content "$OUT/entities.json" -Raw | ConvertFrom-Json
Write-Host "📊 Processing $($states.Count) entities..."

$rows = foreach($s in $states) {
    $domain = $s.entity_id.Split('.')[0]
    [pscustomobject]@{
        entity_id = $s.entity_id
        domain = $domain
        state = "$($s.state)"
        device_class = "$($s.attributes.device_class)"
        unit_of_measurement = "$($s.attributes.unit_of_measurement)"
    }
}

$rows | Export-Csv -NoTypeInformation -Encoding UTF8 "$OUT/entities.csv"
Write-Host "✅ entities.csv created"

$counts = $rows | Group-Object domain | Sort-Object Count -Descending | Select-Object Name,Count
$counts | Format-Table | Out-String | Out-File "$OUT/entity_counts_by_domain.txt" -Encoding utf8
Write-Host "✅ entity_counts_by_domain.txt created"

Write-Host ""
Write-Host "🎉 SUCCESS! Files ready for GPT analysis:"
Write-Host "📁 Location: $OUT"
Write-Host "📄 entities.csv - Complete entity list ($($rows.Count) entities)"
Write-Host "📄 entity_counts_by_domain.txt - Summary by domain"
Write-Host "📄 config.json - HA configuration"
Write-Host ""
Write-Host "Next: Drag entities.csv to GPT chat for analysis"