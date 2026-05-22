import os
import sys
import json
import argparse
from pathlib import Path
from datetime import datetime
from typing import Optional


class ProjectTemplate:
    """Python 项目模板"""

    def __init__(self, name: str, path: Optional[Path] = None):
        self.name = name
        self.path = path or Path.cwd() / name
        self.created_at = datetime.now()

    def create(self) -> Path:
        """创建项目骨架"""
        dirs = ["src", "tests", "docs", "scripts"]
        for d in dirs:
            (self.path / d).mkdir(parents=True, exist_ok=True)
        self._write_gitignore()
        self._write_readme()
        print(f"[OK] 项目已创建: {self.path}")
        return self.path

    def _write_gitignore(self):
        content = "\n".join([
            "__pycache__/", "*.pyc", ".venv/", "venv/",
            ".env", "dist/", "*.egg-info/", ".pytest_cache/",
        ])
        (self.path / ".gitignore").write_text(content)

    def _write_readme(self):
        content = f"# {self.name}\n\nCreated: {self.created_at.date()}\n"
        (self.path / "README.md").write_text(content)


def main():
    parser = argparse.ArgumentParser(description="Python 项目模板生成器")
    parser.add_argument("name", help="项目名称")
    parser.add_argument("-p", "--path", help="项目路径")
    args = parser.parse_args()

    template = ProjectTemplate(args.name, Path(args.path) if args.path else None)
    template.create()


if __name__ == "__main__":
    main()
