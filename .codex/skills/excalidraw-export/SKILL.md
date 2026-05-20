---
name: excalidraw-export
description: "Use when: 需要将 Obsidian Excalidraw 文件（.excalidraw.md）导出为 PNG 或 SVG 图片。支持批量导出、嵌入图片自动注入、嵌入 MD 笔记渲染（含 KaTeX 数学公式）、配对语法为每个文件单独指定输出路径。关键词：excalidraw 导出、Obsidian 画图导出、excalidraw to png、excalidraw to svg。"
argument-hint: "要导出的文件或目录路径（可含 =输出路径 配对语法）"
---

# Excalidraw 导出工具

将 Obsidian Excalidraw 文件（`.excalidraw.md`）导出为 PNG 或 SVG。

**脚本位置（绝对路径）：** `D:\PROJECTS\ExcalidrawExporter\export.js`

## 调用格式

```bash
node "D:\PROJECTS\ExcalidrawExporter\export.js" <输入...> [选项]
```

### 输入格式（3 种）

| 格式 | 说明 |
|------|------|
| `file.excalidraw.md` | 单文件，输出到 `-o` 兜底目录，自动以文件名命名 |
| `file.excalidraw.md=./out/name.png` | **配对语法**，为该文件单独指定输出路径 |
| `./drawings/` | 目录，递归批量导出所有 `.excalidraw.md` |

### 选项

| 选项 | 说明 | 默认值 |
|------|------|--------|
| `-o <目录>` | 兜底输出目录（无配对的文件使用此目录） | `./exports` |
| `-f <格式>` | `png` 或 `svg` | `png` |
| `-s <倍数>` | PNG 缩放倍数（2 = 2×分辨率） | `2` |
| `-v <目录>` | Obsidian vault 根目录，可多次指定 | — |
| `--dark` | 暗色主题 | 否 |
| `--transparent` | 透明背景（仅 PNG） | 否 |

## 操作步骤

### 1. 确认输入路径

- 若用户给出的是 Obsidian vault 内的路径，先确认文件是否存在
- 若只给出笔记名，在用户提供的 vault 路径下查找 `.excalidraw.md` 文件
- Obsidian 默认将 Excalidraw 文件存放在 vault 内的 `Excalidraw/` 子目录

### 2. 确定 vault 路径

如果文件中可能包含**嵌入图片**或**嵌入 MD 笔记**（`[[wiki-link]]`），必须通过 `-v` 指定 vault 根目录，否则可能找不到嵌入内容。

MoMoJee 的 vault 路径：`D:\PROJECTS\MoMoJeeObsidian\MoMoJeeOsidian`

### 3. 构造并运行命令

```bash
# 单文件导出，指定输出路径
node "D:\PROJECTS\ExcalidrawExporter\export.js" \
  "D:\path\to\Drawing.excalidraw.md=./output/result.png" \
  -v "D:\PROJECTS\MoMoJeeObsidian\MoMoJeeOsidian"

# 批量导出 vault 内全部 Excalidraw 文件
node "D:\PROJECTS\ExcalidrawExporter\export.js" \
  "D:\PROJECTS\MoMoJeeObsidian\MoMoJeeOsidian\Excalidraw" \
  -o ./exports \
  -v "D:\PROJECTS\MoMoJeeObsidian\MoMoJeeOsidian"

# 多文件分别指定输出路径
node "D:\PROJECTS\ExcalidrawExporter\export.js" \
  "file1.excalidraw.md=./out/a.png" \
  "file2.excalidraw.md=./out/b.png" \
  -v "D:\PROJECTS\MoMoJeeObsidian\MoMoJeeOsidian"

# 导出为高清 SVG
node "D:\PROJECTS\ExcalidrawExporter\export.js" \
  "D:\path\to\Drawing.excalidraw.md" \
  -o ./exports -f svg \
  -v "D:\PROJECTS\MoMoJeeObsidian\MoMoJeeOsidian"
```

### 4. 验证输出

- 成功时输出 `✅ filename.png (xxx KB)`
- 若有嵌入 MD 渲染，会显示 `📄 渲染 MD: 笔记名.md (宽×高px)...`
- 退出码 0 = 全部成功，非 0 = 存在失败项

## 常见问题

**嵌入图片没有渲染**
→ 必须指定 `-v <vault根目录>`，脚本会在 vault 内递归（深度 6）查找图片文件

**嵌入 MD 笔记没有渲染**
→ 同上，确保 `-v` 包含笔记所在目录；需要网络访问 CDN（KaTeX + marked.js）

**找不到 Chrome**
→ 脚本硬编码 `D:\TOOLS\chrome-win\chrome.exe`；如需更换，修改 `D:\PROJECTS\ExcalidrawExporter\src\renderer.js` 中的 `LOCAL_CHROMIUM` 常量

**Windows 路径中的反斜杠**
→ 在 PowerShell 中路径正常使用反斜杠；在 bash/cmd 中注意转义

## 技术说明

- 使用 **Playwright + 本地 Chromium** 无头渲染
- Excalidraw CDN：`@excalidraw/excalidraw@0.17.6`
- 嵌入 MD 渲染：KaTeX 0.16.9 + marked 9（CDN）
- 原始 `.excalidraw.md` 文件**不会被修改**
