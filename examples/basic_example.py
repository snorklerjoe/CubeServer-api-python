import os
import subprocess
import platform
from cubeserver_api_wrapper import CubeServer, Temperature

# (Fill in the credentials):
TEAM_NAME = "The Yodlers"
TEAM_SECRET = "6934a"


# Set to localhost for debugging purposes.
# If going over the access point, set this to 192.168.252.1:8081
SERVER_HOST = "127.0.0.1:8081"

if platform.system() == "Linux":
    # Key verification:
    if not os.path.exists("trusted.pem"):
        subprocess.run(["/usr/bin/env", "bash", "../scripts/getcert.sh", SERVER_HOST])
    server = CubeServer(
        TEAM_NAME,
        TEAM_SECRET,
        "https://"+SERVER_HOST
    )
else:
    server = CubeServer(
        TEAM_NAME,
        TEAM_SECRET,
        "https://"+SERVER_HOST,
        False  # TODO: Support key verification on other systems...
    )

print(server.get_status())

if server.post(Temperature(100.0)):
    print("Success!")
else:
    print("Something went wrong...")
