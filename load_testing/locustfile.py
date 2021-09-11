from locust import HttpUser, between, task


# sanik
#  locust -H http://0.0.0.0:8000 -u 500 -r 5 -t 300s --autostart -P 8089

# flask
#  locust -H http://0.0.0.0:5000 -u 500 -r 5 -t 300s --autostart -P 8090

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    def on_start(self):
        ...

    def on_stop(self):
        ...

    @task
    def hello_world(self):
        self.client.get("/")
