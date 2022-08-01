import os
import subprocess
from cubeserver_api_wrapper import CubeServer, Temperature

SERVER_HOST = "127.0.0.1:8081"

if not os.path.exists("trusted.pem"):
    subprocess.run(["/usr/bin/env", "bash", "../scripts/getcert.sh", SERVER_HOST])

server = CubeServer("My Team", "$e(r3t!", "https://"+SERVER_HOST)
r = server.post(Temperature(100.0))

print(r)
