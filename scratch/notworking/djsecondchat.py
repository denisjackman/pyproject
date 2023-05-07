'''
pip install chatgpt
https://github.com/labteral/chatgpt-python
'''
from chatgpt import Conversation
SOMEHERE_YOU_SPECIFIED = "y:/pyproject/secrets/secrets.json"
conversation = Conversation(config_path=SOMEHERE_YOU_SPECIFIED)

for chunk in conversation.stream("Hello"):
    print(chunk, end="")
