---
name: mineru
description: 使用 MinerU API 将 PDF/Word/PPT/图片解析为结构化 Markdown，公式保留为 LaTeX，表格保留结构，支持 OCR。适合论文解析、教材提取、扫描件文字识别等场景。
argument-hint: <文件URL或本地路径> [语言: en/ch/auto] [模型: pipeline/vlm]
---

# MinerU 文档解析

通过 MinerU API（v4）将文档解析为 Markdown。调用前确认环境变量 `MINERU_TOKEN` 已设置。

## 支持的输入

| 类型 | 格式 |
|------|------|
| PDF | 论文、书籍、扫描件 |
| Word | .docx |
| PPT | .pptx |
| 图片 | .jpg、.png（OCR） |

## 工作流程

### 1. 检查 Token

```powershell
# Windows（PowerShell）
echo $env:MINERU_TOKEN
# 若为空，设置 Token
$env:MINERU_TOKEN = "your_api_key_here"
```

```bash
# Linux/macOS
echo $MINERU_TOKEN
export MINERU_TOKEN="your_api_key_here"
```

### 2. 提交解析任务

```bash
curl -X POST "https://mineru.net/api/v4/extract/task" \
  -H "Authorization: Bearer $MINERU_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "<文件URL>",
    "enable_formula": true,
    "enable_table": true,
    "layout_model": "doclayout_yolo",
    "language": "auto"
  }'
# 返回 task_id
```

**参数选择指南：**

| 场景 | 推荐配置 |
|------|----------|
| 英文论文（arXiv） | `language: en`, `layout_model: doclayout_yolo` |
| 中文论文/教材 | `language: ch`, `layout_model: doclayout_yolo` |
| 复杂表格/特殊版面 | `model_version: vlm`（较慢但更准确） |
| 快速预览 | `model_version: pipeline`（默认） |

### 3. 轮询结果

```bash
curl "https://mineru.net/api/v4/extract/task/<task_id>" \
  -H "Authorization: Bearer $MINERU_TOKEN"
# status: pending → running → done
```

重复调用直到 `"status": "done"`，然后从返回的 `result.zip_url` 下载。

### 4. 下载并解压

```powershell
# PowerShell
Invoke-WebRequest -Uri "<zip_url>" -OutFile "result.zip"
Expand-Archive -Path "result.zip" -DestinationPath "./output"
```

```bash
# bash
curl -o result.zip "<zip_url>"
unzip result.zip -d ./output
```

解压后结构：

```
output/
├── full.md           # 完整 Markdown（主要使用此文件）
├── content_list.json # 结构化内容列表
├── images/           # 提取的图片
└── layout.json       # 版面分析结果
```

## 批量解析（多文件）

```bash
# 1. 获取预签名上传 URL
curl -X POST "https://mineru.net/api/v4/file-urls/batch" \
  -H "Authorization: Bearer $MINERU_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"file_names": ["paper1.pdf", "paper2.pdf"]}'

# 2. 将文件 PUT 到返回的 presigned URL

# 3. 批量提交
curl -X POST "https://mineru.net/api/v4/extract/task/batch" \
  -H "Authorization: Bearer $MINERU_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"files": [{"url": "...", "name": "paper1.pdf"}, ...]}'
```

## 限制

| 项目 | 限制 |
|------|------|
| 单文件大小 | 200 MB |
| 单文件页数 | 600 页 |

## 参考资源

- API 文档：https://mineru.net/apiManage/docs
- GitHub：https://github.com/opendatalab/MinerU
