from locust import HttpUser, between, task

from api_client_locust_compatible import ApiClient


class LocustClient(HttpUser, ApiClient):
    wait_time = between(1, 5)

    def on_start(self):
        self.create()

    def on_stop(self):
        self.reset()

    @task
    def task_books_get(self):
        self.books_get()

    @task
    def task_user_get(self):
        self.user_get()
