$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent $PSScriptRoot
$CodexRoot = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME ".codex" }
$PetRoot = Join-Path $CodexRoot "pets/niulai"

New-Item -ItemType Directory -Force -Path $PetRoot | Out-Null
Copy-Item -Force (Join-Path $RepoRoot "pet.json") (Join-Path $PetRoot "pet.json")
Copy-Item -Force (Join-Path $RepoRoot "spritesheet.webp") (Join-Path $PetRoot "spritesheet.webp")

Write-Host "牛来已安装到 $PetRoot"
Write-Host "请在 Codex Desktop 的 Settings → Pets 中点击 Refresh。"
