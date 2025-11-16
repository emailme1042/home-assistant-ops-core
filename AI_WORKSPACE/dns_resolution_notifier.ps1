# DNS Resolution Notification Script
# Checks dns_monitor.log for successful ui.nabu.casa resolution
# When found, sends notification to Home Assistant

$logFile = "S:\AI_WORKSPACE\dns_monitor.log"
$haUrl = "http://localhost:8123/api/services/persistent_notification/create"
$haToken = Get-Content "S:\secrets.yaml" | Select-String "ha_token:" | ForEach-Object { $_.Line -replace "ha_token: ", "" }  # Assuming token is in secrets.yaml

while ($true) {
  if (Test-Path $logFile) {
    $lastLines = Get-Content $logFile -Tail 10
    if ($lastLines -match "Address.*\d+\.\d+\.\d+\.\d+" -and $lastLines -notmatch "No answer") {
      # DNS resolved successfully
      $timestamp = Get-Date -Format 'yyyy-MM-dd HH:mm:ss'
      $message = "DNS Resolution Restored: ui.nabu.casa is now resolving at $timestamp"
      
      # Send notification to HA
      $headers = @{
        "Authorization" = "Bearer $haToken"
        "Content-Type" = "application/json"
      }
      $body = @{
        title = "DNS Resolution Alert"
        message = $message
      } | ConvertTo-Json
      
      try {
        Invoke-RestMethod -Uri $haUrl -Method Post -Headers $headers -Body $body
        Write-Host "Notification sent to HA: $message"
      } catch {
        Write-Host "Failed to send notification: $_"
      }
      
      # Exit after notification
      break
    }
  }
  Start-Sleep -Seconds 300  # Check every 5 minutes
}