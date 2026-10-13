import sys
import tarfile

GREEN = '\033[32m'
RESET = '\033[0m'

def add_to_tree(tree, path_parts):
    """パスを分解してネストされた辞書（ツリー構造）を作成する"""
    current = tree
    for part in path_parts:
        current = current.setdefault(part, {})

def print_tree(tree, prefix=''):
    """ツリー構造を再帰的にきれいにターミナル出力する"""
    keys = sorted(tree.keys())
    for i, key in enumerate(keys):
        is_last = (i == len(keys) - 1)
        connector = '└── ' if is_last else '├── '
        
        # .prefabで終わる場合は緑色にする
        if key.endswith('.prefab'):
            display_key = f"{GREEN}{key}{RESET}"
        else:
            display_key = key
            
        print(f"{prefix}{connector}{display_key}")
        
        # 子要素（さらに下の階層やファイル）がある場合
        if tree[key]:
            extension = '    ' if is_last else '│   '
            print_tree(tree[key], prefix + extension)

if __name__ == '__main__':
    target_package = input('input unitypackage: ').replace('"','')
    
    if not target_package.endswith('.unitypackage'):
        print("unitypackageではありません")
        input()
        sys.exit()
        
    with tarfile.open(target_package, 'r:gz') as tar:
        members = tar.getmembers()
        
        # GUIDごとにメンバーをグループ化
        guid_dirs = {}
        for member in members:
            parts = member.name.split('/')
            if len(parts) >= 2:
                guid = parts[0]
                guid_dirs.setdefault(guid, []).append(member)
        
        paths = []
        for guid, files in guid_dirs.items():
            pathname_member = None
            for file in files:
                if file.name.endswith('/pathname'):
                    pathname_member = file
                    break
            
            if pathname_member:
                f = tar.extractfile(pathname_member)
                if f:
                    original_path = f.read().decode('utf-8').strip()
                    paths.append(original_path)
                    f.close()
        
        print(f"\n--- フォルダツリー構造 (全 {len(paths)} 件) ---\n")
        
        # 取得したパスからツリーを構築
        tree = {}
        for path in paths:
            parts = path.split('/')
            add_to_tree(tree, parts)
            
        # ツリーを描画
        print_tree(tree)
        input()