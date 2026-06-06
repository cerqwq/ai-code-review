"""
AI Code Review - AI代码审查工具
支持代码审查、质量分析、安全扫描
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AICodeReviewTools:
    """
    AI代码审查工具
    支持：审查、质量、安全
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def review_code(self, code: str, language: str, focus: List[str] = None) -> Dict:
        """审查代码"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        focus_text = ", ".join(focus or ["质量", "安全", "性能"])

        prompt = f"""请审查以下{language}代码，重点关注{focus_text}：

```{language}
{code[:2000]}
```

请返回JSON格式：
{{
    "score": 1-100,
    "issues": [
        {{"severity": "high/medium/low", "type": "类型", "line": "行号", "description": "描述", "fix": "修复"}}
    ],
    "strengths": ["优点"],
    "improvements": ["改进建议"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"review": content}

    def analyze_complexity(self, code: str, language: str) -> Dict:
        """分析代码复杂度"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请分析以下{language}代码的复杂度：

```{language}
{code[:2000]}
```

请返回JSON格式：
{{
    "cyclomatic_complexity": "圈复杂度",
    "cognitive_complexity": "认知复杂度",
    "maintainability_index": "可维护性指数",
    "hotspots": ["热点代码"],
    "suggestions": ["简化建议"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"complexity": content}

    def suggest_refactoring(self, code: str, language: str) -> List[Dict]:
        """建议重构"""
        if not self.client:
            return [{"error": "LLM客户端未配置"}]

        prompt = f"""请为以下{language}代码提供重构建议：

```{language}
{code[:2000]}
```

请返回JSON格式：
[
    {{"pattern": "模式", "description": "描述", "before": "重构前", "after": "重构后", "benefit": "收益"}}
]"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\[.*\]', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return [{"suggestions": content}]

    def generate_review_report(self, reviews: List[Dict]) -> str:
        """生成审查报告"""
        if not self.client:
            return "LLM客户端未配置"

        reviews_text = json.dumps(reviews, ensure_ascii=False)

        prompt = f"""请根据以下审查结果生成报告：

{reviews_text}

要求：
1. 执行摘要
2. 关键问题
3. 改进建议
4. 优先级排序"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def check_best_practices(self, code: str, language: str) -> Dict:
        """检查最佳实践"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请检查以下{language}代码是否遵循最佳实践：

```{language}
{code[:2000]}
```

请返回JSON格式：
{{
    "score": 1-100,
    "practices": [
        {{"name": "实践", "status": "pass/fail", "description": "描述"}}
    ],
    "improvements": ["改进建议"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"practices": content}

    def generate_ci_review_config(self, language: str, tool: str = "github") -> str:
        """生成CI审查配置"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请生成{tool}的{language}代码审查CI配置：

要求：
1. 代码质量检查
2. 安全扫描
3. 测试覆盖
4. 自动评论"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content


def create_tools(**kwargs) -> AICodeReviewTools:
    """创建代码审查工具"""
    return AICodeReviewTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI Code Review Tools")
    print()

    # 测试
    review = tools.review_code("def add(a, b): return a + b", "Python")
    print(json.dumps(review, ensure_ascii=False, indent=2))
