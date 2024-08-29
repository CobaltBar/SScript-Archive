param(
  [Parameter(Mandatory=$true)]
  [string] $version
)

$version = $version.Replace('.', ',')

$url = "https://github.com/CobaltBar/SScript-Archive/raw/main/archives/SScript-$version.zip"
$zipName = "SScript-$version.zip"
$downloadPath = "$env:TEMP\$zipName"

Write-Host "Downloading $url..."
Invoke-WebRequest -Uri $url -OutFile $downloadPath

if (!(Test-Path $downloadPath)) {
  Write-Error "Failed to download SScript."
  exit 1
}

Write-Host "Download complete."

Write-Host "Installing $zipName..."
haxelib install $downloadPath

if ($LastExitCode -ne 0) {
  Write-Error "Failed to install SScript."
  exit 1
}

Write-Host "Installation complete."