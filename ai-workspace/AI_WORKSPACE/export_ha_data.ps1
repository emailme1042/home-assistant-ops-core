# Home Assistant Data Export Script
# Reads token from secrets.yaml and exports data via REST API

$OUT = "AI_WORKSPACE/SHARED_CONTEXT/SESSION_ESSENTIALS"
$BASE = "http://192.168.1.217:8123/api"

Write-Host "🔍 Reading token from secrets.yaml..."

# Read secrets.yaml and find the VSCode HA token
$secretsContent = Get-Content 'secrets.yaml' -Raw
if ($secretsContent -match 'vscode-home-assistant\.longLivedAccessToken:\s*["\']?([^"\'\r\n]+)["\']?') {
    $TOKEN = $matches[1].Trim()
    Write-Host "✅ Found vscode-home-assistant token"
} elseif ($secretsContent -match 'ha_token:\s*["\']?([^"\'\r\n]+)["\']?') {
    $TOKEN = $matches[1].Trim()
    Write-Host "✅ Found ha_token"
} elseif ($secretsContent -match 'ha_long_lived_token:\s*["\']?([^"\'\r\n]+)["\']?') {
    $TOKEN = $matches[1].Trim()
    Write-Host "✅ Found ha_long_lived_token"
} else {
    Write-Error "❌ No HA token found in secrets.yaml"
    Write-Host "Looking for: vscode-home-assistant.longLivedAccessToken, ha_token, or ha_long_lived_token"
    exit 1
}

# Create output directory
New-Item -ItemType Directory -Force -Path $OUT | Out-Null
Write-Host "📁 Output directory: $OUT"

# Set up headers
$Headers = @{
    Authorization = "Bearer $TOKEN"
    "Content-Type" = "application/json"
}

Write-Host "🌐 Connecting to Home Assistant..."

# Download config
try {
    Invoke-RestMethod -Headers $Headers -Uri "$BASE/config" -OutFile "$OUT/config.json"
    Write-Host "✅ Config downloaded"
} catch {
    Write-Error "❌ Failed to download config: $($_.Exception.Message)"
    exit 1
}

# Download all entity states
try {
    Invoke-RestMethod -Headers $Headers -Uri "$BASE/states" -OutFile "$OUT/entities.json"
    Write-Host "✅ Entity states downloaded"
} catch {
    Write-Error "❌ Failed to download entity states: $($_.Exception.Message)"
    exit 1
}

# Try to download registries (optional)
try {
    $entityRegistry = Invoke-RestMethod -Headers $Headers -Method Post -Uri "$BASE/config/entity_registry/list"
    $entityRegistry | ConvertTo-Json -Depth 8 | Out-File "$OUT/entity_registry.json" -Encoding utf8
    Write-Host "✅ Entity registry downloaded"
} catch {
    Write-Warning "⚠️ Entity registry failed (may not be available)"
}

try {
    $deviceRegistry = Invoke-RestMethod -Headers $Headers -Method Post -Uri "$BASE/config/device_registry/list"
    $deviceRegistry | ConvertTo-Json -Depth 8 | Out-File "$OUT/device_registry.json" -Encoding utf8
    Write-Host "✅ Device registry downloaded"
} catch {
    Write-Warning "⚠️ Device registry failed (may not be available)"
}

try {
    $areaRegistry = Invoke-RestMethod -Headers $Headers -Uri "$BASE/config/area_registry/list"
    $areaRegistry | ConvertTo-Json -Depth 8 | Out-File "$OUT/area_registry.json" -Encoding utf8
    Write-Host "✅ Area registry downloaded"
} catch {
    Write-Warning "⚠️ Area registry failed (may not be available)"
}

# Process entities
Write-Host "📊 Processing entities..."
$states = Get-Content "$OUT/entities.json" -Raw | ConvertFrom-Json
Write-Host "Found $($states.Count) entities"

# Create CSV
$rows = foreach($s in $states) {
    $domain = $s.entity_id.Split('.')[0]
    [pscustomobject]@{
        entity_id = $s.entity_id
        domain = $domain
        state = "$($s.state)"
        device_class = "$($s.attributes.device_class)"
        unit_of_measurement = "$($s.attributes.unit_of_measurement)"
        friendly_name = "$($s.attributes.friendly_name)"
    }
}

$rows | Export-Csv -NoTypeInformation -Encoding UTF8 "$OUT/entities.csv"
Write-Host "✅ entities.csv created"

# Create domain summary
$domainCounts = $rows | Group-Object domain | Sort-Object Count -Descending | Select-Object Name, Count
$domainCounts | Format-Table | Out-String | Out-File "$OUT/entity_counts_by_domain.txt" -Encoding utf8
Write-Host "✅ entity_counts_by_domain.txt created"

# Create unavailable entities summary
$unavailable = $rows | Where-Object { $_.state -eq "unavailable" }
$unavailableByDomain = $unavailable | Group-Object domain | Sort-Object Count -Descending | Select-Object Name, Count
"Unavailable Entities Summary" | Out-File "$OUT/unavailable_entities.txt" -Encoding utf8
"Total unavailable: $($unavailable.Count)" | Add-Content "$OUT/unavailable_entities.txt"
"" | Add-Content "$OUT/unavailable_entities.txt"
$unavailableByDomain | Format-Table | Out-String | Add-Content "$OUT/unavailable_entities.txt"
Write-Host "✅ unavailable_entities.txt created"

Write-Host ""
Write-Host "🎉 Export complete!"
Write-Host "📁 Files created in: $OUT"
Write-Host "📄 entities.csv - Complete entity list ($($rows.Count) entities)"
Write-Host "📄 entity_counts_by_domain.txt - Domain summary"
Write-Host "📄 unavailable_entities.txt - Unavailable entity analysis ($($unavailable.Count) unavailable)"
Write-Host "📄 config.json - HA configuration"

if (Test-Path "$OUT/entity_registry.json") { Write-Host "📄 entity_registry.json - Entity registry" }
if (Test-Path "$OUT/device_registry.json") { Write-Host "📄 device_registry.json - Device registry" }
if (Test-Path "$OUT/area_registry.json") { Write-Host "📄 area_registry.json - Area registry" }

Write-Host ""
Write-Host "🎯 Next: Drag entities.csv and unavailable_entities.txt to GPT chat for analysis"