"""
This is an SSH key gen tool
"""
import subprocess
import sys
import os

HOST = "server"
# Ports are handled in ~/.ssh/config since we use OpenSSH
COMMAND = "ls -al"
os.system("say What is your command my master ?")
os.system("say starting ssh session")

with subprocess.Popen(["ssh",
                       f"{HOST}",
                       COMMAND],
                      shell=False,
                      stdout=subprocess.PIPE,
                      stderr=subprocess.PIPE) as ssh:
    result = ssh.stdout.readlines()
    if result == []:
        error = ssh.stderr.readlines()
        print(f"ERROR: {sys.stderr}")
        os.system("say Oh Oh another problem")
    else:
        print("\n")
        print(result)
        print("\n")
        os.system("say All good here")

os.system("say Reactor online, Computer online, All systems functional")
os.system("say Operation complete shutting down")
