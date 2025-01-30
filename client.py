import requests

class SolvexClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.solvex.ai"

    def get_leaderboard(self):
        response = requests.get(f"{self.base_url}/leaderboard", headers={"Authorization": f"Bearer {self.api_key}"})
        return response.json()

    def submit_model(self, model_path):
        files = {"model": open(model_path, "rb")}
        response = requests.post(f"{self.base_url}/submit", headers={"Authorization": f"Bearer {self.api_key}"}, files=files)
        return response.json()
