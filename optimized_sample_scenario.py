from locust import task, run_single_user
from locust import FastHttpUser


class OptimizedSampleScenario(FastHttpUser):
    """
    最適化されたLocustテストシナリオのサンプル
    すべてのリクエストで共通して使用されるヘッダーはdefault_headersに定義し、
    個別のリクエストでは固有のヘッダーのみを指定します。
    """
    
    host = "https://alpha-new.zexy.in"
    
    # 共通のヘッダー情報（すべてのリクエストに自動的に適用される）
    default_headers = {
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "ja",
        "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
    }

    @task
    def user_flow(self):
        """ユーザーフローのシミュレーション"""
        
        # トップページへのアクセス
        with self.client.request(
            "GET",
            "/",
            headers={
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "if-modified-since": "Thu, 20 Feb 2025 08:56:28 GMT",
                "priority": "u=0, i",
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "none",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
            },
            catch_response=True,
        ) as resp:
            # レスポンスの検証などが必要な場合はここに追加
            pass
            
        # ログイン処理
        with self.rest(
            "POST",
            "/api/users/sign_in.json",
            headers={
                "accept": "application/json, text/javascript, */*; q=0.01",
                "origin": "https://alpha-new.zexy.in",
                "priority": "u=1, i",
                "referer": "https://alpha-new.zexy.in/",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "x-requested-with": "XMLHttpRequest",
            },
            json={
                "login": "269623",
                "password": "ams20250306",
                "client_attributes": {
                    "tanto_eigyo_name": "",
                    "opened_at": "",
                    "closed_at": "",
                },
                "csrf_token": "e7b6b080-644b-4ea4-a32f-9e0fa64a79b5",
            },
        ) as resp:
            # ログインの成功確認などが必要な場合はここに追加
            pass
            
        # クライアント情報の取得
        with self.rest(
            "GET",
            "/api/clients.json?p=1&pp=100&state_in%5B%5D=active&state_in%5B%5D=passive&s=s_code&csrf_token=8e7e6b38-3d56-49ff-8576-b3976c4d85ef",
            headers={
                "accept": "application/json, text/javascript, */*; q=0.01",
                "priority": "u=1, i",
                "referer": "https://alpha-new.zexy.in/",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "x-requested-with": "XMLHttpRequest",
            },
        ) as resp:
            pass
            
        # クライアント選択処理
        with self.rest(
            "POST",
            "/api/current_client.json",
            headers={
                "accept": "application/json, text/javascript, */*; q=0.01",
                "origin": "https://alpha-new.zexy.in",
                "priority": "u=1, i",
                "referer": "https://alpha-new.zexy.in/",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "x-requested-with": "XMLHttpRequest",
            },
            json={
                "tanto_eigyo_name": "",
                "opened_at": "",
                "closed_at": "",
                "client_id": 3140,
                "csrf_token": "8e7e6b38-3d56-49ff-8576-b3976c4d85ef",
            },
        ) as resp:
            pass
            
        # 顧客一覧の取得
        with self.client.request(
            "POST",
            "/api/customers/index.json",
            headers={
                "accept": "application/json, text/javascript, */*; q=0.01",
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                "origin": "https://alpha-new.zexy.in",
                "priority": "u=1, i",
                "referer": "https://alpha-new.zexy.in/",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "x-requested-with": "XMLHttpRequest",
            },
            data="p=1&pp=100&s=visited_booked_at+desc&set_search=filter&state_total=true&summary_total=true&tab=all&label-print-border=label-print-border&label-print-size=label-print-medium&label-print-xy=y&notice=&planners_dropdown=false&filter=false&w=visited_booked_at~2022-03-15..%2Bouter_flg~0%2C1&id=&current_client_id=3140&csrf_token=8e7e6b38-3d56-49ff-8576-b3976c4d85ef",
            catch_response=True,
        ) as resp:
            pass
            
        # 顧客詳細の取得
        with self.rest(
            "GET",
            "/api/customers/5117251.json?current_client_id=3140&csrf_token=8e7e6b38-3d56-49ff-8576-b3976c4d85ef",
            headers={
                "accept": "application/json, text/javascript, */*; q=0.01",
                "priority": "u=1, i",
                "referer": "https://alpha-new.zexy.in/",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "x-requested-with": "XMLHttpRequest",
            },
        ) as resp:
            pass
            
        # 履歴データの取得
        with self.rest(
            "GET",
            "/api/histories.json?p=1&pp=100&s=id&customer_id_eq=5117251&current_client_id=3140&csrf_token=8e7e6b38-3d56-49ff-8576-b3976c4d85ef",
            headers={
                "accept": "application/json, text/javascript, */*; q=0.01",
                "priority": "u=1, i",
                "referer": "https://alpha-new.zexy.in/",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "x-requested-with": "XMLHttpRequest",
            },
        ) as resp:
            pass


if __name__ == "__main__":
    run_single_user(OptimizedSampleScenario)