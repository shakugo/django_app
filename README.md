# slack的なものを作る



## 作業フロー

### ブランチ
- `master` 本番環境に上げれる状態
- `develop` ステージング環境に上げれる状態
- `fix` 既存部分の修正
- `feature` 追加機能の実装
`develop`を基軸に`fix`または`feature`ブランチを切っていく感じになります

### フロー
- `develop`から`fix`または`feature`を切る（`fix/user_search`または`feature/user_search`など）
- 作業を進めながらcommitを作成する（コミットメッセージは作業内容がわかりやすいようにかつ簡潔にお願いします）
- 実装が完了したら`% git pull --rebase origin develop`してからリモートにpush
- 作成したブランチから`develop`に対してPRを作成
- レビュー後に`develop`にマージ
