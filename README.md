# 🔍 AI Code Review

AI代码审查工具，支持代码审查、质量分析、安全扫描。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 🔍 代码审查
- 📊 复杂度分析
- ♻️ 重构建议
- 📋 审查报告
- ✅ 最佳实践检查
- 🔄 CI审查配置

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from ai_code_review import create_tools

tools = create_tools()

# 代码审查
review = tools.review_code(code, "Python", ["质量", "安全"])

# 复杂度分析
complexity = tools.analyze_complexity(code, "Python")

# 重构建议
refactoring = tools.suggest_refactoring(code, "Python")

# 审查报告
report = tools.generate_review_report(reviews)

# 最佳实践
practices = tools.check_best_practices(code, "Python")

# CI配置
ci = tools.generate_ci_review_config("Python", "github")
```

## 📁 项目结构

```
ai-code-review/
├── tools.py       # 代码审查工具核心
└── README.md
```

## 📄 许可证

MIT License
