# Windows REST API Snapshot Script
# Reads HA token from secrets.yaml and exports entity data

$OUT = "AI_WORKSPACE/SHARED_CONTEXT/SESSION_ESSENTIALS"
Write-Host "🔍 Reading token from secrets.yaml..."

# Read secrets.yaml and extract token
$secretsContent = Get-Content 'secrets.yaml' -Raw
if ($secretsContent -match 'vscode-home-assistant\.longLivedAccessToken:\s*"([^"]+)"') {
    $TOKEN = $matches[1].Trim()
    Write-Host "✅ Found vscode-home-assistant.longLivedAccessToken"
} elseif ($secretsContent -match 'ha_token:\s*(.+)') {
    $TOKEN = $matches[1].Trim()
    Write-Host "✅ Found ha_token"
} elseif ($secretsContent -match 'ha_long_lived_token:\s*(.+)') {
    $TOKEN = $matches[1].Trim()
    Write-Host "✅ Found ha_long_lived_token"
} else {
    Write-Error "❌ No HA token found in secrets.yaml"
    Write-Host "Looking for: vscode-home-assistant.longLivedAccessToken, ha_token, or ha_long_lived_token"
    exit 1
}

# Create output directory
New-Item -ItemType Directory -Force -Path $OUT | Out-Null

# Setup API connection
$BASE = "http://192.168.1.217:8123/api"
$H = @{ Authorization = "Bearer $TOKEN" }

Write-Host "🌐 Connecting to Home Assistant at 192.168.1.217:8123..."

# Download configuration
try {
    Invoke-RestMethod -Headers $H -Uri "$BASE/config" -OutFile "$OUT/config.json"
    Write-Host "✅ Config downloaded"
} catch {
    Write-Error "❌ Failed /api/config - check token or HA connectivity: $($_.Exception.Message)"
    exit 1
}

# Download entity states
try {
    Invoke-RestMethod -Headers $H -Uri "$BASE/states" -OutFile "$OUT/entities.json"
    Write-Host "✅ Entity states downloaded"
} catch {
    Write-Error "❌ Failed /api/states: $($_.Exception.Message)"
    exit 1
}

# Download registries (optional)
try {
    $entityRegistry = Invoke-RestMethod -Headers $H -Method Post -Uri "$BASE/config/entity_registry/list"
    $entityRegistry | ConvertTo-Json -Depth 8 | Out-File "$OUT/entity_registry.json" -Encoding utf8
    Write-Host "✅ Entity registry downloaded"
} catch {
    Write-Warning "⚠️ Entity registry failed (may not be available): $($_.Exception.Message)"
}

try {
    $deviceRegistry = Invoke-RestMethod -Headers $H -Method Post -Uri "$BASE/config/device_registry/list"
    $deviceRegistry | ConvertTo-Json -Depth 8 | Out-File "$OUT/device_registry.json" -Encoding utf8
    Write-Host "✅ Device registry downloaded"
} catch {
    Write-Warning "⚠️ Device registry failed (may not be available): $($_.Exception.Message)"
}

try {
    $areaRegistry = Invoke-RestMethod -Headers $H -Uri "$BASE/config/area_registry/list"
    $areaRegistry | ConvertTo-Json -Depth 8 | Out-File "$OUT/area_registry.json" -Encoding utf8
    Write-Host "✅ Area registry downloaded"
} catch {
    Write-Warning "⚠️ Area registry failed (may not be available): $($_.Exception.Message)"
}

# Process entities
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

# Export CSV
$rows | Export-Csv -NoTypeInformation -Encoding UTF8 "$OUT/entities.csv"
Write-Host "✅ entities.csv created"

# Create domain summary
$counts = $rows | Group-Object domain | Sort-Object Count -Descending | Select-Object Name, Count
$counts | Format-Table | Out-String | Out-File "$OUT/entity_counts_by_domain.txt" -Encoding utf8
Write-Host "✅ entity_counts_by_domain.txt created"

# Show results
Write-Host ""
Write-Host "🎉 Windows REST API snapshot complete!"
Write-Host "Files available for GPT analysis:"
Write-Host "📁 Location: $OUT"
Write-Host "📄 entities.csv - Complete entity list with states"
Write-Host "📄 entity_counts_by_domain.txt - Summary by domain"
Write-Host "📄 config.json - HA configuration and components"

if (Test-Path "$OUT/entity_registry.json") {
    Write-Host "📄 entity_registry.json - Entity registry details"
}
if (Test-Path "$OUT/device_registry.json") {
    Write-Host "📄 device_registry.json - Device registry details"
}
if (Test-Path "$OUT/area_registry.json") {
    Write-Host "📄 area_registry.json - Area registry details"
}

Write-Host ""
Write-Host "🎯 Next: Drag entities.csv and entity_counts_by_domain.txt to GPT chat for analysis"