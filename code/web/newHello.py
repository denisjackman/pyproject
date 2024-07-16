'''
    cgi handling
'''
import os

print("Content-type: text/html\r\n\r\n")
print("<font size=+1>Environment</font><\br>")
for name, value in os.environ.items():
    print(f"<b>{name}</b>:{value}<\br>")
