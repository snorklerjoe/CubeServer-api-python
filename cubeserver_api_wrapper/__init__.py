"""A wrapper for the API"""

from typing import Union, Iterable
from requests import Session
from requests.auth import HTTPDigestAuth
from os.path import exists

from .datapoints import __all__ as _datapoints_all
from .datapoints import *

__all__ = [
    "CubeServer"
] + _datapoints_all

class CubeServer:
    """A class for the server"""
    def __init__(
        self,
        team_name: str,
        team_secret: str,
        server_addr: str = "https://192.168.1.1",
        server_verify: Union[str, bool] = "./trusted.pem"
    ):
        """Initializes the connection for the API server
        Please provide the case-sensitive team name and the secret key
        If needed, the server's address can be defined with the server_addr
        kwarg
        If no other server_verify value is given as a kwarg, this looks for
        a file called trusted.pem. If the file exists or if a boolean value is
        given, the requests.Session().verify value will be set to this
        value."""
        self.session = Session()
        self.session.auth = HTTPDigestAuth(team_name, team_secret)
        if isinstance(server_verify, str) and exists(server_verify) or \
            isinstance(server_verify, bool):
            self.session.verify = server_verify
        self.addr = server_addr

    def post(
        self,
        data: Union[Iterable[DataPoint], DataPoint]
    ) -> bool:
        """Posts a datapoint to the server, returns True on success"""
        if isinstance(data, Iterable):  # Send multiple datapoints:
            return all(
                self.send(point) for point in data
            )
        # Just send one datapoint:
        response = self.session.post(
            f"{self.addr}/data", data={"data":data.dumps}
        )
        if response.status_code != 201:
            print(response.status_code)
            print(response.text)
            return False
        return True
