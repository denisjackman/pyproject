'''
pip install chatgpt 
https://github.com/labteral/chatgpt-python
'''
from chatgpt import Conversation

conversation = Conversation(config_path={somewhere_you_specified})

for chunk in conversation.stream("Hello"):
    print(chunk, end="")