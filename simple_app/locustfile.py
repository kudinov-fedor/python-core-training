from locust import HttpUser, between, task

# locust -H http://127.0.0.1:5000  --autostart -u 1000 -r 2 -t 600s RestApiTest

class RestApiTest(HttpUser):
    wait_time = between(1, 5)

    @task
    def task_sample(self):
        self.client.get("/users")


# locust -H http://127.0.0.1:5000  --autostart -u 1000 -r 2 -t 600s WebTestClient
# locust -H http://127.0.0.1:1337  --autostart -u 1000 -r 2 -t 600s WebTestClient


def fetch_static_assets(session, response):
    from bs4 import BeautifulSoup

    resource_urls = set()
    soup = BeautifulSoup(response.text, "html.parser")

    # img
    for res in soup.find_all(src=True):
        url = res['src']
        if "/static" in url:
            resource_urls.add(url)
        else:
            print("Skipping: " + url)

    # css
    for res in soup.find_all(rel="stylesheet", href=True):
        url = res['href']
        if "/static" in url:
            resource_urls.add(url)
        else:
            print("Skipping: " + url)

    for url in set(resource_urls):
        session.client.get(url, name="Static File")


class WebTestClient(HttpUser):
    wait_time = between(1, 5)

    @task
    def task_sample(self):
        res = self.client.get("/")
        fetch_static_assets(self, res)


class WebTestClientNoResources(HttpUser):
    wait_time = between(1, 5)

    @task
    def task_sample(self):
        self.client.get("/")
