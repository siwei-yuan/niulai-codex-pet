# 牛来 Codex 桌宠

一只为 Codex 官方 Pets 动画协议制作的「牛来」桌宠：金橙色、半睁眼、表情严肃，保留刻意的低分辨率、弱纹理和早期 CGI 质感。

![牛来 Codex 桌宠动画接触表](previews/contact-sheet.png)

## 安装

macOS / Linux：

```bash
./scripts/install.sh
```

Windows PowerShell：

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install.ps1
```

安装后打开 Codex Desktop 的 `Settings → Pets`，点击 `Refresh`，然后选择「牛来」。

也可以手动把 `pet.json` 和 `spritesheet.webp` 放入：

```text
${CODEX_HOME:-$HOME/.codex}/pets/niulai/
```

## 包含的动画

- idle：待机、呼吸和眨眼
- running-right / running-left：向右/向左移动
- waving：挥手
- jumping：跳跃
- failed：任务失败
- waiting：等待输入
- running：任务执行中
- review：检查结果

## 验证

```bash
python3 scripts/validate_pet.py
```

已验证的格式：1536×1872 WebP、RGBA、8 列×9 行，未使用的单元格为全透明。

## 分享说明

GitHub 仓库只是分发方式，Codex 运行桌宠并不依赖 GitHub。其他人下载这两个核心文件后即可安装。

这是粉丝向、非商业的二次创作桌宠，与原作版权方、制作方及 OpenAI 无官方关联。公开分发前请自行确认相关角色和名称的授权范围。
