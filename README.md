# Python Project Template with uv

Modern Python プロジェクトテンプレート - 高速パッケージマネージャ `uv` とコード品質ツールの統合

## 📋 概要

このテンプレートは、Pythonプロジェクトを素早く立ち上げるための最新のベストプラクティスを統合したものです。

### 主な特徴

- ✅ **高速パッケージ管理**: [uv](https://github.com/astral-sh/uv) による爆速の依存関係管理
- ✅ **自動コード品質チェック**: Ruff による linting とフォーマット
- ✅ **静的型チェック**: mypy による型安全性の保証
- ✅ **自動テスト**: pytest + カバレッジレポート
- ✅ **タスクランナー**: Poe the Poet による統一されたコマンド
- ✅ **GitHub Actions 統合**: reviewdog による自動コードレビュー
- ✅ **自動フォーマット**: PR時に自動的にコード整形＋コミット
- ✅ **依存関係自動更新**: Renovate による定期的な依存関係更新

---

## 🚀 クイックスタート

### 前提条件

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) がインストール済み

### セットアップ

```bash
# リポジトリをクローン
git clone <your-repo-url>
cd python-uv-project

# 依存関係をインストール
uv sync --all-groups

# 開発準備完了！
```

---

## 🛠️ 利用可能なツール

### コード品質

| ツール | 用途 | ドキュメント |
|-------|------|-------------|
| **Ruff** | Linting & Formatting | [docs/RUFF.md](docs/RUFF.md) |
| **mypy** | 静的型チェック | [docs/MYPY.md](docs/MYPY.md) |
| **pytest** | テスティング | [docs/TESTING.md](docs/TESTING.md) |
| **Renovate** | 依存関係自動更新 | [docs/RENOVATE.md](docs/RENOVATE.md) |

### タスク管理

**Poe the Poet** - プロジェクト全体で統一されたタスクコマンド

```bash
# 利用可能なタスク一覧
poe

# よく使うコマンド
poe lint         # Ruff linting
poe format       # コードフォーマット
poe typecheck    # 型チェック
poe test         # テスト実行
poe check        # 全チェック実行
```

---

## 📚 ドキュメント

各ツールの詳細な使い方とベストプラクティスは、以下のドキュメントを参照してください：

### Ruff（コード品質）
**[docs/RUFF.md](docs/RUFF.md)**
- Ruffの基本的な使い方
- IDE統合（VSCode、PyCharmなど）
- コマンドライン実行
- GitHub Actions 自動フォーマット
- reviewdog 連携

### mypy（型チェック）
**[docs/MYPY.md](docs/MYPY.md)**
- mypyの概要とメリット
- 型チェックの実行方法
- 型アノテーションの書き方
- 段階的な型導入
- よくあるエラーと対処法
- GitHub Actions 統合

### pytest（テスト）
**[docs/TESTING.md](docs/TESTING.md)**
- テストの書き方
- テスト実行方法
- カバレッジレポート
- マーカーの使い方
- ベストプラクティス

---

## 🤖 GitHub Actions

このテンプレートには4つの自動化ワークフローが含まれています：

### 1. Ruff ワークフロー (`.github/workflows/ruff.yml`)
- **自動実行**: push/PR時
- **処理内容**:
  - コード品質チェック（reviewdog）
  - 自動フォーマット＋コミット
  - PRへの指摘コメント

### 2. mypy ワークフロー (`.github/workflows/mypy.yml`)
- **自動実行**: push/PR時
- **手動実行**: 可能
- **処理内容**:
  - 型チェック（reviewdog）
  - PRへの型エラー指摘

### 3. Test ワークフロー (`.github/workflows/test.yml`)
- **自動実行**: push/PR時
- **手動実行**: 可能
- **処理内容**:
  - テスト実行
  - カバレッジレポート
  - Codecov連携

### 4. Renovate ワークフロー (`.github/workflows/renovate.yml`)
- **自動実行**: 毎週土曜日 3:00 JST
- **手動実行**: 可能
- **処理内容**:
  - 依存関係の更新チェック
  - 更新PRの自動作成
  - マイナー・パッチ更新の自動マージ

---

## 💻 開発ワークフロー

### 日常的な開発

```bash
# 1. コード編集
#    - VSCodeなら保存時に自動フォーマット

# 2. コミット前チェック
poe check  # lint + format + typecheck + test

# 3. 自動修正
poe fix    # lint-fix + format

# 4. コミット
git add .
git commit -m "feat: 新機能追加"
git push
```

### PR作成時

1. **PR作成**
2. **自動実行される処理**:
   - Ruff が自動的にコードをフォーマット＋コミット
   - reviewdog が該当行にコメント
   - テストが自動実行
3. **レビュー**: 整形済みのコードをレビュー

### コミットメッセージ規約（重要）

**このプロジェクトは Conventional Commits を使用した自動バージョニングを採用しています。**

すべてのコミットメッセージは以下の形式に従う必要があります：

```
<type>: <description>
```

#### タイプ一覧

| Type | 説明 | バージョン影響 |
|------|------|---------------|
| `feat` | 新機能 | MINOR (0.1.0 → 0.2.0) |
| `fix` | バグ修正 | PATCH (0.1.0 → 0.1.1) |
| `feat!` | 破壊的変更 | MAJOR (0.1.0 → 1.0.0) |
| `chore` | メンテナンス | なし |
| `docs` | ドキュメント | なし |
| `refactor` | リファクタリング | なし |
| `test` | テスト | なし |
| `ci` | CI/CD変更 | なし |

#### 例

```bash
# 新機能追加（マイナーバージョンアップ）
git commit -m "feat: ユーザー認証機能を追加"

# バグ修正（パッチバージョンアップ）
git commit -m "fix: ログイン時のメモリリークを修正"

# 破壊的変更（メジャーバージョンアップ）
git commit -m "feat!: 設定APIを再設計

BREAKING CHANGE: 設定ファイルのフォーマットが変更されました"
```

**重要**:
- production へのマージ時に release-please がコミット履歴を解析してバージョンを自動決定
- 不適切なコミットメッセージは誤ったバージョニングの原因となります
- 詳細は [Conventional Commits](https://www.conventionalcommits.org/) を参照

#### コミットメッセージの強制

このプロジェクトでは **gitlint + pre-commit** でコミットメッセージ形式を強制しています。

```bash
# 初回セットアップ（一度だけ実行）
poe setup-hooks

# これで不正なコミットメッセージは自動的に拒否されます
git commit -m "Added feature"  # ❌ エラー
git commit -m "feat: add feature"  # ✅ 成功
```

---

## 📦 プロジェクト構成

```
.
├── .github/
│   ├── scripts/          # ワークフロー用スクリプト
│   │   ├── ruff-review.sh
│   │   └── mypy-review.sh
│   └── workflows/        # GitHub Actions
│       ├── ruff.yml
│       ├── mypy.yml
│       └── test.yml
├── docs/                 # ドキュメント
│   ├── RUFF_INTEGRATION.md
│   ├── MYPY.md
│   └── TESTING.md
├── tests/                # テストファイル
├── pyproject.toml        # プロジェクト設定
├── ruff.toml            # Ruff設定
├── uv.lock              # 依存関係ロック
└── README.md            # このファイル
```

---

## 🔧 カスタマイズ

### プロジェクト情報の更新

`pyproject.toml` を編集：

```toml
[project]
name = "your-project-name"
version = "0.1.0"
description = "Your project description"
requires-python = ">=3.12"
```

### Ruffルールの調整

`ruff.toml` を編集してルールをカスタマイズ

### mypy設定の変更

`pyproject.toml` の `[tool.mypy]` セクションで調整

---

## 📝 タスクコマンド一覧

```bash
# Linting
poe lint              # チェックのみ
poe lint-fix          # 自動修正
poe lint-unsafe       # 安全でない修正も実行

# フォーマット
poe format            # フォーマット実行
poe format-check      # チェックのみ

# 型チェック
poe typecheck         # 全体チェック
poe typecheck <file>  # 特定ファイル
poe typecheck-strict  # 厳格モード
poe typecheck-review  # reviewdogで確認

# テスト
poe test              # テスト実行
poe test-cov          # カバレッジ付き
poe test-verbose      # 詳細出力

# reviewdog（ローカル）
poe review-local      # Ruff reviewdog
poe typecheck-review  # mypy reviewdog

# 統合
poe check             # 全チェック
poe fix               # 自動修正可能なもの全て
poe ci                # CI用チェック

# その他
poe clean             # キャッシュ削除
poe install           # 依存関係インストール
poe update            # 依存関係更新
```

---

## 🤝 コントリビューション

このテンプレートの改善提案は Issue または Pull Request でお願いします。

---

## 📄 ライセンス

このテンプレートは自由に使用・改変できます。