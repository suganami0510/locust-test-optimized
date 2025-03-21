from locust import task, run_single_user
from locust import FastHttpUser


class SampleScenario(FastHttpUser):
    host = "https://alpha-new.zexy.in"
    default_headers = {
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "ja",
        "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
    }

    @task
    def t(self):
        # 各リクエストでは、default_headersに含まれていない追加のヘッダーのみを指定すればよい
        # default_headersは自動的にマージされる
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
            pass
        
        with self.client.request(
            "GET",
            "/favicon.ico",
            headers={
                "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
                "if-modified-since": "Thu, 20 Feb 2025 08:56:28 GMT",
                "if-none-match": '"67b6ee3c-10bf"',
                "priority": "u=1, i",
                "referer": "https://alpha-new.zexy.in/",
                "sec-fetch-dest": "image",
                "sec-fetch-mode": "no-cors",
                "sec-fetch-site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
            
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
            pass
            
        # 以下同様に、他のすべてのリクエストでもdefault_headers以外のヘッダーのみを指定する
        # （この例では最初の3つのリクエストのみを示しています）


if __name__ == "__main__":
    run_single_user(SampleScenario)