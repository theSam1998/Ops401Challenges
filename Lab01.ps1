#Author: Samuel Allan
#Date of last revision: 08/15/2023
#Script: Lab 01 automation script
#Purpose: download and install antivirus

#Variables:

#url variable to store the url of the download
$url = "https://www.avast.com/en-us/download-thank-you.php?product=FAV-PPC&locale=en-us&direct=1"

#outpath variable to store the output path of the download, to make it easier to run later
$outpath = "$PSScriptRoot/avast_installer.exe"

# Downloading the installer
Invoke-WebRequest -Uri $url -OutFile $outpath

# Running the downloaded installer in silent mode
Start-Process -Filepath $outpath -ArgumentList "/verysilent"
