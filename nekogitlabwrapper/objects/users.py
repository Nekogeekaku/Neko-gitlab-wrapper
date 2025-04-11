import requests
from nekogitlabwrapper import gitlab

class Users:
    def __init__(
        self,gitlabclient):
        self._gitlabclient = gitlabclient
    def get_user_by_username(self,username):
        headers = {'Authorization': f'Bearer {self._gitlabclient._private_token}'}
        url = f'{self._gitlabclient._url}/users?username={username}'
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            # Assuming the username is unique and only one user should be returned
            return response.json()[0] if response.json() else None
        else:
            print(f"Error: Received status code {response.status_code}")
            return None    