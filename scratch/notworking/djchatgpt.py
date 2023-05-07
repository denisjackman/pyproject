''' chatgpt python script
    pip install openai
    pip install chatgpt
'''

import openai
from djgamemodule import security as sec

# Set up the OpenAI API client
credid = sec.credscheck('y:/pyproject/secrets/secrets.json')
openai.api_key = credid["OpenAI_API_Key"]

# Set up the model and prompt
MODEL_ENGINE = "text-davinci-003"
MODEL_PROMPT = "Hello, how are you today?"

# Generate a response
completion = openai.Completion.create(
    engine=MODEL_ENGINE,
    prompt=MODEL_PROMPT,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

response = completion.choices[0].text
print(response)
