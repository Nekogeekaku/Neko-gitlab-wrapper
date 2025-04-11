from typing import Optional, Union
from nekogitlabwrapper import objects
from nekogitlabwrapper.objects import users


class DoStuff:
    def __init__(self, something):
        print(f"init called {something}")
    def someFunction(self, int):
        return (int + int)



class GitlabCli:
    """
    Represent the core class of the library
    """
    def __init__(
            self,
            url: Optional[str] = None,
            private_token: Optional[str] = None,
            ssl_verify: Union[bool, str] = True,
            api_version: str = "4",
        ):
        self._base_url = url
        self._url = f"{self._base_url}/api/v{api_version}"
        self._private_token = private_token
        self._ssl_verify = ssl_verify
        self.users = users.Users(self)