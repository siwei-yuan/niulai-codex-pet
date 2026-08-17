#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
pet_root="${CODEX_HOME:-$HOME/.codex}/pets/niulai"

mkdir -p "$pet_root"
install -m 0644 "$repo_root/pet.json" "$pet_root/pet.json"
install -m 0644 "$repo_root/spritesheet.webp" "$pet_root/spritesheet.webp"

printf '牛来已安装到 %s\n' "$pet_root"
printf '请在 Codex Desktop 的 Settings → Pets 中点击 Refresh。\n'
