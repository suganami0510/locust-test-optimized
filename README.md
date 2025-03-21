# Locust テスト最適化サンプル

このリポジトリは、Locustを使用して負荷テストを実施する際の最適化されたサンプルコードを提供します。

## default_headers の活用方法

Locustの `FastHttpUser` クラスは、`default_headers` プロパティを持っています。このプロパティに設定したヘッダー情報は、自動的に全てのリクエストにマージされます。これにより、共通のヘッダー情報を各リクエストで繰り返し指定する必要がなくなります。

### 使用方法

```python
class MyUser(FastHttpUser):
    host = "https://example.com"
    default_headers = {
        "user-agent": "Mozilla/5.0...",
        "accept-language": "ja",
        # その他の共通ヘッダー
    }
    
    @task
    def my_task(self):
        # default_headersはここで自動的にマージされる
        # 追加のヘッダーのみを指定すればよい
        with self.client.request(
            "GET", 
            "/path", 
            headers={
                "referer": "https://example.com/",
                # リクエスト固有のヘッダーのみ
            }
        ) as resp:
            pass
```

### ヘッダーのマージルール

1. `default_headers`に定義されたすべてのヘッダーは、各リクエストに自動的に適用されます
2. 個別のリクエストで同じヘッダー名が指定された場合、そちらが優先されます（オーバーライド）
3. 個別のリクエストにしか存在しないヘッダーは、そのまま追加されます

### メリット

- コードの重複を減らせます
- メンテナンス性が向上します
- ヘッダー情報の一元管理が可能になります

## サンプルコード

`sample_scenario_optimized.py` は、最適化されたシナリオの例を示しています。