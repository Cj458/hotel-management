from locust import HttpUser, task, between
from django.urls import reverse

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)
    @task(4)
    def view_rooms(self):
        print('View rooms')
        self.client.get('/rooms', name='/rooms')


    

