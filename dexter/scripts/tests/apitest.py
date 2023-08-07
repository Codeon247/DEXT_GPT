import requests
import json

class APITest:
    APP_SERVER_ADDRESS = "http://localhost:8888"

    def __init__(self):
        self.access_token = None
        self.refresh_token = None
        self.instance_id = None

    def signup(self):
        url = f"{self.APP_SERVER_ADDRESS}/signup/"
        headers = {'Content-Type': 'application/json'}
        data = {
            "email": "demo1@example.com",
            "password": "demo1@example.com"
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))
        return response.json()

    def login(self):
        url = f"{self.APP_SERVER_ADDRESS}/login/"
        headers = {'Content-Type': 'application/json'}
        data = {
            "email": "demo1@example.com",
            "password": "demo1@example.com"
        }
        response = requests.post(url, headers=headers, data=json.dumps(data)).json()
        self.access_token = response.get('payload').get('access')
        self.refresh_token = response.get('payload').get('refresh')
        return response

    def refresh_token_api(self):
        url = f"{self.APP_SERVER_ADDRESS}/token/refresh/"
        headers = {'Content-Type': 'application/json'}
        data = {
            "refresh": self.refresh_token
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))
        return response.json()

    def prepare(self):
        url = f"{self.APP_SERVER_ADDRESS}/create/dex/"
        headers = {'Content-Type': 'application/json'}
        data = {
            "key": "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"
        }
        response = requests.post(url, headers=headers, data=json.dumps(data)).json()
        self.instance_id = response.get('payload').get('instance_id')

    def query(self, query_text):
        url = f"{self.APP_SERVER_ADDRESS}/query/"
        headers = {'Content-Type': 'application/json'}
        data = {
            "instance_id": self.instance_id,
            "query": query_text
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))
        return response.json()

    def change_prompt(self, prompt_id):
        url = f"{self.APP_SERVER_ADDRESS}/change/prompt/"
        headers = {'Content-Type': 'application/json'}
        data = {
            "instance_id": self.instance_id,
            "prompt_id": prompt_id
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))
        return response.json()

    def add_prompt(self, prompt_data):
        url = f"{self.APP_SERVER_ADDRESS}/add/prompt/"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.access_token}'
        }
        response = requests.post(url, headers=headers, data=json.dumps(prompt_data))
        return response.json()

    def prompts(self):
        url = f"{self.APP_SERVER_ADDRESS}/prompts/"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.access_token}'
        }
        response = requests.get(url, headers=headers)
        return response.json()
