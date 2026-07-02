# 错误和复测记录

## 2026-06-28：PowerShell 中文输出乱码

### 现象

在 PowerShell 终端中读取中文 Markdown 时，输出出现乱码。

### 原因

终端编码显示与文件 UTF-8 内容不一致。文件内容本身可由 Python 按 UTF-8 正常读取。

### 修复 / 规避

- 文件写入继续使用 UTF-8。
- 需要精确检查中文内容时，用 Python `Path.read_text(encoding="utf-8")` 读取。
- 需要定位行号时，可用 Python 输出 `unicode_escape` 或只输出行号和关键词。

### 复测命令

```powershell
& 'C:\Users\admin\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -c "from pathlib import Path; print(Path(r'F:\code\x文章\WRITING_STYLE.md').read_text(encoding='utf-8').splitlines()[0])"
```

### 当前状态

已规避。该问题影响终端显示，不影响 Markdown 文件内容。

## 2026-06-30：GitHub / agent-reach 命令环境边界

### 现象

学习 `ponyodong2026/ponyo-cover-anchor-system` 时：

- `gh repo view` 和 `gh api` 提示需要 `gh auth login` 或 `GH_TOKEN`。
- `agent-reach check-update` 提示 `agent-reach` 不是可识别命令。

### 原因

- 当前环境里的 GitHub CLI 未登录。
- `agent-reach` 可读 skill 文档存在，但命令行入口未在当前 PowerShell PATH 中。

### 修复 / 规避

- 读取公开 GitHub 仓库时，优先使用：
  - `git ls-remote`
  - GitHub REST API：`https://api.github.com/repos/<owner>/<repo>/...`
  - raw 文件：`https://raw.githubusercontent.com/<owner>/<repo>/<branch>/<path>`
- 不依赖 `gh` 登录态读取公开仓库。
- `agent-reach check-update` 暂时跳过，后续如需使用，需要先确认可执行文件路径或安装方式。

### 复测命令

```powershell
git ls-remote https://github.com/ponyodong2026/ponyo-cover-anchor-system.git HEAD
curl.exe -L 'https://raw.githubusercontent.com/ponyodong2026/ponyo-cover-anchor-system/main/cover-anchor-system/SKILL.md'
```

### 当前状态

已规避。公开仓库内容已通过 GitHub API 和 raw URL 成功读取。
