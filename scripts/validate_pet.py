#!/usr/bin/env python3
"""Validate the shareable Niulai Codex pet package."""

from __future__ import annotations

import json
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parent.parent
MANIFEST_PATH = ROOT / "pet.json"
SPRITESHEET_PATH = ROOT / "spritesheet.webp"


def main() -> None:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    assert manifest == {
        "id": "niulai",
        "displayName": "牛来",
        "description": "一头粗制滥造、表情严肃的金黄色牛来。",
        "spritesheetPath": "spritesheet.webp",
    }

    with Image.open(SPRITESHEET_PATH) as spritesheet:
        assert spritesheet.format == "WEBP"
        assert spritesheet.size == (1536, 1872)
        assert spritesheet.mode == "RGBA"

        cell_width, cell_height = 192, 208
        used_frames = (6, 8, 8, 4, 5, 8, 6, 6, 6)
        alpha = spritesheet.getchannel("A")
        for row, used_count in enumerate(used_frames):
            for column in range(used_count, 8):
                box = (
                    column * cell_width,
                    row * cell_height,
                    (column + 1) * cell_width,
                    (row + 1) * cell_height,
                )
                assert alpha.crop(box).getbbox() is None, (
                    f"unused cell row={row} column={column} is not transparent"
                )

    print("牛来 Codex 桌宠包验证通过。")


if __name__ == "__main__":
    main()
