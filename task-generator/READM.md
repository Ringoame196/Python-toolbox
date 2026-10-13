# Course Task Generator for Todoist

Generate lecture and course tasks in Todoist using the Todoist API.

[Todoist](https://app.todoist.com/app/today) に講義・授業のタスクを一括登録するためのシンプルな Python スクリプトです。

## Features

* 複数の授業を一括登録
* 指定回数分のタスクを自動生成
* Todoist API を利用
* GitHub Actions に対応
* API キーを GitHub Secrets で安全に管理

## Example

以下の設定で実行すると、

```python
SUBJECTS = [
    "経済入門",
    "情報科学",
    "プログラミング"
]

CLASS_NUM = 15
```

次のようなタスクが作成されます。

```text
経済入門 第1回
経済入門 第2回
...
経済入門 第15回

情報科学 第1回
...
プログラミング 第15回
```

## Setup

### 1. Clone Repository

```bash
git clone https://github.com/USERNAME/course-task-generator-for-todoist.git
cd course-task-generator-for-todoist
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

#### Required

```text
TODOIST_API_KEY
```

#### Optional

```text
TODOIST_PROJECT_ID
```

プロジェクトIDを指定しない場合は Todoist の受信トレイへ追加されます。

## GitHub Actions

GitHub Secrets に以下を設定してください。

| Name               | Required |
| ------------------ | -------- |
| TODOIST_API_KEY    | Yes      |
| TODOIST_PROJECT_ID | No       |

Actions タブから Workflow を実行できます。

## 免責事項

このプロジェクトはDoistおよびTodoist公式とは一切関係ありません。
また、Doistによって作成・承認・サポートされたものではありません。

This project is not created by, affiliated with, or supported by Doist.

Users of this software must comply with Todoist's Terms of Service and API policies.

## License

MIT License
