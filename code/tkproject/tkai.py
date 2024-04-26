''' this is tk ai module '''
import sys
import os
import openai

# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.gameitems.gamefunctions import credscheck  # noqa: E402


def generate_response(gr_prompt):
    ''' Use the ChatGPT model to generate a response '''
    model_engine = "gpt-3.5-turbo-instruct"
    gr_prompt = f"{gr_prompt}\n"
    gr_message = ''
    try:
        completions = openai.Completion.create(engine=model_engine,
                                               prompt=gr_prompt,
                                               max_tokens=1024,
                                               n=1,
                                               stop=None,
                                               temperature=0.5)
    except Exception as e:
        gr_message = f'Error in generating response : {e}'
    if gr_message == '':
        gr_message = completions.choices[0].text
    return gr_message.strip()


def main():
    ''' main function '''
    print('[*] main: start')
    credid = credscheck('Z:/pyproject/secrets/secrets.json')
    open_ai_key = credid['OpenAI_API_Key']
    open_ai_org = credid['OpenAI_Org_ID']
    openai.api_key = open_ai_key
    mw_prompt = "explain to me the concept of the Delta Green roleplaying game"
    mw_response = generate_response(mw_prompt)
    print(f'[o] OpenAI Org ID  : {open_ai_org}')
    print(f'[o] Prompt         : {mw_prompt}')
    print(f'[o] Response       : {mw_response}')
    print('[*] main: end')


if __name__ == '__main__':
    main()
