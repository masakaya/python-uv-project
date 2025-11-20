#!/usr/bin/env python3
"""mypy型チェックのレビューレポート生成スクリプト

mypyの型チェック結果を解析し、見やすいMarkdown形式のレポートを生成します。
型エラーはすべて手動修正が必要なため、詳細な情報とともにレポートします。
"""

import json
import subprocess
import sys
from pathlib import Path
from typing import Any

# 型エイリアス
MypyError = dict[str, Any]


def run_mypy_check(path: str = ".") -> list[MypyError]:
    """mypyで型チェックを実行し、エラー情報を取得

    Args:
        path: チェック対象のパスまたはディレクトリ

    Returns:
        型エラーのリスト
    """
    result = subprocess.run(
        ["uv", "run", "mypy", path, "--show-column-numbers", "--no-error-summary"],
        capture_output=True,
        text=True,
    )

    errors: list[MypyError] = []

    # mypyの出力をパース（形式: file.py:line:col: error: message）
    for line in result.stdout.strip().split("\n"):
        if not line or line.startswith("Success:") or line.startswith("Found "):
            continue

        parts = line.split(":", 4)
        if len(parts) >= 5:
            file_path = parts[0].strip()
            line_num = parts[1].strip()
            col_num = parts[2].strip()
            error_type = parts[3].strip()  # "error" or "note"
            message = parts[4].strip()

            if error_type == "error":
                errors.append(
                    {
                        "file": file_path,
                        "line": line_num,
                        "column": col_num,
                        "message": message,
                        "severity": "error",
                    }
                )

    return errors


def generate_markdown_report(errors: list[MypyError], target_path: str) -> str:
    """Markdown形式のレビューレポートを生成

    Args:
        errors: 型エラーのリスト
        target_path: チェック対象パス

    Returns:
        Markdown形式のレポート
    """
    report_lines = [
        "# mypy型チェックレビュー",
        "",
        f"**チェック対象:** `{target_path}`",
        "",
        "---",
        "",
        "## 📊 サマリー",
        "",
        f"- **総エラー数:** {len(errors)}",
        f"- **手動修正が必要:** {len(errors)} 🔴",
        "",
        "> **注意:** mypyの型エラーはすべて手動修正が必要です。",
        "> 詳細な修正方法は [docs/MYPY.md](docs/MYPY.md) を参照してください。",
        "",
        "---",
        "",
    ]

    if not errors:
        report_lines.extend(
            [
                "## ✅ 型チェック結果",
                "",
                "型エラーは見つかりませんでした！",
                "",
            ]
        )
    else:
        report_lines.extend(
            [
                "## 🔴 型エラー（手動修正が必要）",
                "",
            ]
        )

        # ファイルごとにグループ化
        errors_by_file: dict[str, list[MypyError]] = {}
        for error in errors:
            file_path = error["file"]
            if file_path not in errors_by_file:
                errors_by_file[file_path] = []
            errors_by_file[file_path].append(error)

        # ファイルごとにエラーを出力
        for file_path, file_errors in sorted(errors_by_file.items()):
            report_lines.extend(
                [
                    f"### 📄 `{file_path}`",
                    "",
                ]
            )

            for error in sorted(
                file_errors, key=lambda e: (int(e["line"]), int(e["column"]))
            ):
                location = f"{file_path}:{error['line']}:{error['column']}"
                report_lines.extend(
                    [
                        f"#### {location}",
                        "",
                        f"**エラー:** {error['message']}",
                        "",
                        "**修正方法:**",
                        "- 適切な型アノテーションを追加してください",
                        "- 詳細は [mypy型チェックガイド](docs/MYPY.md) を参照",
                        "- 型ヒントの書き方: https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html",
                        "",
                        "---",
                        "",
                    ]
                )

    report_lines.extend(
        [
            "## 🛠️ 修正の進め方",
            "",
            "1. **エラーを確認**",
            "   ```bash",
            "   poe typecheck",
            "   ```",
            "",
            "2. **型アノテーションを追加**",
            "   - 関数の引数と戻り値に型を追加",
            "   - 変数の型を明示的に指定",
            "   - `docs/MYPY.md` の例を参照",
            "",
            "3. **再チェック**",
            "   ```bash",
            "   poe typecheck",
            "   ```",
            "",
            "4. **段階的な導入**",
            "   - すべてのエラーを一度に修正する必要はありません",
            "   - ファイル単位で修正: `poe typecheck <file>`",
            "   - 重要な公開APIから優先的に型を追加",
            "",
            "---",
            "",
            "## 📚 参考リンク",
            "",
            "- [プロジェクトのmypyガイド](docs/MYPY.md)",
            "- [mypy公式ドキュメント](https://mypy.readthedocs.io/)",
            "- [Python型ヒントチートシート](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)",
            "",
        ]
    )

    return "\n".join(report_lines)


def main() -> None:
    """メイン処理"""
    # コマンドライン引数からチェック対象パスを取得
    target_path = sys.argv[1] if len(sys.argv) > 1 else "."

    print(f"🔍 mypyで型チェック中: {target_path}")

    # mypy実行
    errors = run_mypy_check(target_path)

    # レポート生成
    report = generate_markdown_report(errors, target_path)

    # ファイルに書き込み
    output_file = Path("MYPY_REVIEW.md")
    output_file.write_text(report, encoding="utf-8")

    print(f"✅ レビューレポートを生成しました: {output_file}")
    print(f"📊 型エラー数: {len(errors)}")

    if errors:
        print("\n💡 修正方法は MYPY_REVIEW.md および docs/MYPY.md を参照してください")
        sys.exit(1)  # エラーがある場合は終了コード1
    else:
        print("🎉 型エラーはありません！")
        sys.exit(0)


if __name__ == "__main__":
    main()
