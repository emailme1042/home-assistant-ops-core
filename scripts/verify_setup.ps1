Write-Host "ðŸ” Verifying GitHub HA Integration Setup" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan

Write-Host "Git Status:" -ForegroundColor Yellow
git status --short

Write-Host "Remote Repository:" -ForegroundColor Yellow
git remote -v

Write-Host "Recent Commits:" -ForegroundColor Yellow
git log --oneline -5

Write-Host "Repository Structure:" -ForegroundColor Yellow
Get-ChildItem -Recurse -File | Where-Object { $_.Extension -in @('.yaml','.md') } | Select-Object FullName | Format-Table -AutoSize

Write-Host "âœ… Setup verification complete!" -ForegroundColor Green
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "1. Check GitHub repository for uploaded files" -ForegroundColor White
Write-Host "2. Enable GitHub Actions in repository settings" -ForegroundColor White
Write-Host "3. Configure VS Code with GitHub Copilot" -ForegroundColor White
Write-Host "4. Connect ChatGPT to GitHub repository" -ForegroundColor White
Write-Host "5. Set up GitHub Backup add-on in HA" -ForegroundColor White
