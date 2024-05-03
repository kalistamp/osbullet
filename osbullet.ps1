# Get the installed Edge version
$edgeInstallPath = "${env:ProgramFiles(x86)}\Microsoft\Edge\Application"
$edgeVersions = Get-ChildItem -Path $edgeInstallPath | Where-Object { $_.PSIsContainer }

if ($edgeVersions.Count -eq 0) {
    Write-Host "Microsoft Edge is not installed on this system."
    exit
}

# Sort the versions in descending order and use the latest version
$latestEdgeVersion = $edgeVersions | Sort-Object -Property Name -Descending | Select-Object -First 1

# Construct the uninstall command
$edgeUninstallPath = Join-Path -Path $edgeInstallPath -ChildPath "$($latestEdgeVersion.Name)\Installer"
$uninstallCommand = Join-Path -Path $edgeUninstallPath -ChildPath "setup.exe"
$uninstallArgs = "--uninstall --system-level --verbose-logging --force-uninstall"

# Execute the uninstall command
Write-Host "Uninstalling Microsoft Edge version $($latestEdgeVersion.Name)..."
Start-Process -FilePath $uninstallCommand -ArgumentList $uninstallArgs -Wait

Write-Host "Microsoft Edge has been uninstalled."
