# UnityPackage Tree

`.unitypackage` ファイルの中身を解凍することなく、**フォルダのツリー構造（階層）**としてターミナル上に可視化する軽量な Python スクリプトです。

Unityのプレハブ（`.prefab`）ファイルを自動でカラーハイライトし、パッケージ内にどのようなアセットが含まれているかを直感的に素早く把握できます。

---

## 使用例
![代替テキスト（使用例）](./使用例.png)

## 🌟 特徴 (Features)
- **解凍不要**: `.unitypackage`（内部は tar.gz）を指定するだけで中身のパス構造を解析。
- **ツリー表示**: Linuxの `tree` コマンドのように、ネストされたフォルダ階層を綺麗に描画。
- **カラーハイライト**: `.prefab` などの特定拡張子のファイルをカラー表示（ANSIエスケープシーケンスを使用）。
- **依存ライブラリなし**: Pythonの標準ライブラリ（`tarfile`, `sys` 等）のみで動作するため、面倒なインストールが不要。

---

## 🛠️ 動作環境 (Prerequisites)
- Python 3.x

---

## 🚀 使い方 (Usage)

1. スクリプトファイル（例: `unitypackage_tree.py`）をダウンロード・保存します。
2. ターミナル（コマンドプロンプト）でスクリプトを実行します。
```bash
python unitypackage_tree.py
```
3. プロンプトが表示されたら、調査したい `.unitypackage` のファイル名（またはパス）を入力して Enter を押します。
```text
input unitypackage: sample.unitypackage
```

---

## 📜 ライセンス (License)
This project is open-source under the [MIT License](LICENSE).
