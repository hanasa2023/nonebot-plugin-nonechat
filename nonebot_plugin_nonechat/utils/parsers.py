import re


class MarkdownOutputParser:
    """对于Markdown输出的解析类"""

    def parser(self, text: str) -> str:
        pattern = r'```markdown\n(.*?)\n```'
        replaced_string = re.sub(pattern, lambda m: m.group(1), text, flags=re.DOTALL)
        return replaced_string
