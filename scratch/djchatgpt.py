''' chatgpt python script
    apikey = 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
    pip install openai
    pip install chatgpt
'''

import openai

# Set up the OpenAI API client
openai.api_key = "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"

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
