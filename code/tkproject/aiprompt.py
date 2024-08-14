''' this is tk ai module '''
import sys
import os
from openai import OpenAI

# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.gameitems.gamefunctions import credscheck


def summarize_text_with_openai(text, model="text-davinci-003"):
    """ Generate a summary for the text using OpenAI's GPT model """
    response = OpenAI.Completion.create(
        engine=model,
        prompt=f"Summarize this text: {text}",
        max_tokens=150
    )
    return response.choices[0].text.strip()


def generate_prompt(directory, file_count, openai_api_key):
    '''
    Generate a prompt for a discussion based on
    summaries of files in a directory
    '''
    OpenAI.api_key = openai_api_key
    files = os.listdir(directory)
    prompt_parts = []

    for file_name in files[:file_count]:
        path = os.path.join(directory, file_name)
        try:
            with open(path, 'r', encoding='utf-8') as file:
                text = file.read()
                summary = summarize_text_with_openai(text)
                prompt_parts.append(summary)
        except Exception as e:
            print(f"Failed to process {file_name}: {str(e)}")
            continue

    prompt = "Generate a discussion based on these summaries: " + " ".join(prompt_parts)
    return prompt


def main():
    ''' main function '''
    ap_credid = credscheck('Z:/pyproject/secrets/secrets.json')
    openai_api_key = ap_credid['OpenAI_API_Key']
    directory = "Z:/Store/prompt"
    file_count = 3
    prompt = generate_prompt(directory, file_count, openai_api_key)
    print(prompt)


if __name__ == '__main__':
    main()
