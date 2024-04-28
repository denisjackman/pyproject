''' this is tk ai module '''
import sys
import os
from openai import OpenAI

# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.gameitems.gamefunctions import credscheck  # noqa: E402

MODEL_ENGINE = "gpt-3.5-turbo-instruct"
MAX_TOKENS = 7
TEMPERATURE = 0.5
STOP = None


def chat_response(cr_client, cr_prompt):
    ''' Use the ChatGPT model to generate a response '''
    cr_model_engine = MODEL_ENGINE
    cr_prompt = f"{cr_prompt}\n"
    cr_message = ''
    try:
        cr_completions = cr_client.completions.create(model=cr_model_engine,
                                                      prompt=cr_prompt,
                                                      max_tokens=MAX_TOKENS,
                                                      n=1,
                                                      stop=STOP,
                                                      temperature=TEMPERATURE)
    except Exception as e:
        cr_message = f'Error in generating response : {e}'
    if cr_message == '':
        cr_message = cr_completions.choices[0].text
    return cr_message.strip()


def create_assistant(cr_client, cr_name, cr_intruction):
    ''' Create a new assistant '''
    as_assistant = cr_client.create_assistant(name=cr_name,
                                              instruction=cr_intruction,
                                              model=MODEL_ENGINE,
                                              tools=[{"type": "file_search"}])
    return as_assistant


def create_vector_store(cvs_client, cvs_name, cvs_filelist):
    ''' Create a new vector store '''
    vs_vector_store = cvs_client.beta.vector_stores.create(name=cvs_name)
    vs_file_paths = cvs_filelist
    vs_file_streams = [open(file_path, "rb") for file_path in vs_file_paths]  # noqa: E501
    vs_file_batch = cvs_client.beta.vector_stores.file_batches.upload_and_poll(vs_vector_store.id,  # noqa: E501
                                                                               files=vs_file_streams)  # noqa: E501
    print(f'[o] Vector Store ID : {vs_vector_store.id}')
    print(f'[o] File Batch ID   : {vs_file_batch.id}')
    return vs_vector_store


def main():
    ''' main function '''
    print('[*] main: start')
    credid = credscheck('Z:/pyproject/secrets/secrets.json')
    open_ai_key = credid['OpenAI_API_Key']
    open_ai_org = credid['OpenAI_Org_ID']
    mw_prompt = "explain to me the concept of the Delta Green roleplaying game"
    mw_client = OpenAI(api_key=open_ai_key)
    mw_response = chat_response(mw_client, mw_prompt)
    # mw_instruction = "You are a designer of RPG game." \
    #                  "Use your knowlegdge base to help" \
    #                  "write a scenario for a new game."
    # mw_assistant = create_assistant(mw_client,
    #                                 'Delta Green Assistant',
    #                                 mw_instruction)
    # mw_filelist = ['Z:/pyproject/jackmanimation/gameitems/deltagreen.txt']
    # mw_vector_store = create_vector_store(mw_client,
    #                                       'Delta Green Vector Store',
    #                                       mw_filelist)
    # mw_assistant = mw_client.beta.asssisstants.update(assistant_id=mw_assistant.id,  # noqa: E501
    #                                                   tool_resources={"file_search":{"vector_sctore_ids": [mw_vector_store.id]}})  # noqa: E501
    print(f'[o] OpenAI Org ID  : {open_ai_org}')
    print(f'[o] Prompt         : {mw_prompt}')
    print(f'[o] Response       : {mw_response}')
    print('[*] main: end')


if __name__ == '__main__':
    main()
