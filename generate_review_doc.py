#!/usr/bin/env python3
"""Ruffのチェック結果からレビュードキュメントを生成する"""

from datetime import datetime
import json
from pathlib import Path
import subprocess
import sys
from typing import Any

RuffIssue = dict[str, Any]


def run_ruff_check(path: str = ".") -> list[RuffIssue]:
    """Ruffでチェックを実行し、JSON形式で結果を取得"""
    result = subprocess.run(
        ["uv", "run", "ruff", "check", path, "--output-format=json"],
        capture_output=True,
        text=True,
    )

    if result.stdout:
        data: list[RuffIssue] = json.loads(result.stdout)
        return data
    return []


def categorize_issues(issues: list[RuffIssue]) -> dict[str, list[RuffIssue]]:
    """問題を自動修正可能/不可能で分類"""
    auto_fixable = []
    manual_fix_required = []
    unsafe_fixes = []

    for issue in issues:
        if issue["fix"] is None:
            manual_fix_required.append(issue)
        elif issue["fix"]["applicability"] == "unsafe":
            unsafe_fixes.append(issue)
        else:
            auto_fixable.append(issue)

    return {
        "auto_fixable": auto_fixable,
        "unsafe_fixes": unsafe_fixes,
        "manual_fix_required": manual_fix_required,
    }


def generate_markdown_report(
    categorized: dict[str, list[RuffIssue]], output_path: str = "RUFF_REVIEW.md"
) -> None:
    """Markdownレポートを生成"""
    total = sum(len(v) for v in categorized.values())

    md_lines = [
        "# Ruff Code Review Report",
        f"\n**生成日時:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"\n**総問題数:** {total}",
        f"\n- 🟢 自動修正可能: {len(categorized['auto_fixable'])}",
        f"\n- 🟡 安全でない修正可能: {len(categorized['unsafe_fixes'])}",
        f"\n- 🔴 手動修正が必要: {len(categorized['manual_fix_required'])}",
        "\n---\n",
    ]

    # 手動修正が必要な問題（最優先）
    if categorized["manual_fix_required"]:
        md_lines.append("\n## 🔴 手動修正が必要な問題\n")
        md_lines.append(
            "これらの問題は自動修正できません。開発者による対応が必要です。\n"
        )

        for issue in categorized["manual_fix_required"]:
            md_lines.extend(_format_issue(issue))

    # 安全でない修正が可能な問題
    if categorized["unsafe_fixes"]:
        md_lines.append("\n## 🟡 安全でない修正が可能な問題\n")
        md_lines.append(
            "これらは `--unsafe-fixes` オプションで自動修正可能ですが、"
            "意味が変わる可能性があるため確認が必要です。\n"
        )

        for issue in categorized["unsafe_fixes"]:
            md_lines.extend(_format_issue(issue, show_fix=True))

    # 自動修正可能な問題
    if categorized["auto_fixable"]:
        md_lines.append("\n## 🟢 自動修正可能な問題\n")
        md_lines.append("これらは `ruff check --fix` で自動的に修正されます。\n")

        for issue in categorized["auto_fixable"]:
            md_lines.extend(_format_issue(issue))

    # レポートをファイルに書き込み
    Path(output_path).write_text("\n".join(md_lines), encoding="utf-8")
    print(f"✅ レポートを生成しました: {output_path}")


def _format_issue(issue: RuffIssue, show_fix: bool = False) -> list[str]:
    """個別の問題をMarkdown形式にフォーマット"""
    lines = [
        f"\n### [{issue['code']}] {issue['message']}\n",
        f"**ファイル:** `{Path(issue['filename']).relative_to(Path.cwd())}`",
        f"\n**場所:** 行 {issue['location']['row']}, 列 {issue['location']['column']}",
        f"\n**詳細:** {issue['url']}\n",
    ]

    if show_fix and issue.get("fix"):
        lines.append("\n**提案される修正:**")
        lines.append(f"\n> {issue['fix']['message']}\n")

    return lines


def main():
    """メイン処理"""
    # デフォルトではカレントディレクトリをチェック
    target_path = sys.argv[1] if len(sys.argv) > 1 else "."

    print(f"🔍 Ruffでコードをチェック中: {target_path}")
    issues = run_ruff_check(target_path)

    if not issues:
        print("✨ 問題は見つかりませんでした！")
        return

    print(f"📋 {len(issues)}個の問題を検出しました")

    categorized = categorize_issues(issues)
    generate_markdown_report(categorized)

    # サマリーを表示
    print("\n📊 サマリー:")
    print(f"  - 🟢 自動修正可能: {len(categorized['auto_fixable'])}")
    print(f"  - 🟡 安全でない修正可能: {len(categorized['unsafe_fixes'])}")
    print(f"  - 🔴 手動修正が必要: {len(categorized['manual_fix_required'])}")


if __name__ == "__main__":
    main()
