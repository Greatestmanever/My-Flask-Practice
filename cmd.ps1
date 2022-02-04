# Don't forget to change execution policies
# Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope CurrentUser
# More info https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7

if (Test-Path env:VIRTUAL_ENV) {
    deactivate  
}

$env = .\venv\Scripts\activate.ps1

# use $env to set variables, for instance $env:FLASK_APP = "main.py"