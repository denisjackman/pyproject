''' this is tk ai module '''
import sys
import os
from openai import OpenAI

# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.gameitems.gamefunctions import credscheck  # noqa: E402

MODEL_ENGINE = "gpt-3.5-turbo-instruct"
ASSISTANT_ENGINE = "gpt-4-turbo-preview"
IMAGE_ENGINE = "dall-e-3"
IMAGE_SIZE = "1024x1024"
IMAGE_QUALITY = "standard"
MAX_TOKENS = 1024
TEMPERATURE = 0.5
STOP = None


def chat_response(cr_client, cr_prompt):
    ''' Use the ChatGPT model to generate a response '''
    cr_model_engine = MODEL_ENGINE
    cr_prompt = f"{cr_prompt}\n"
    cr_result = ''
    try:
        cr_completions = cr_client.completions.create(model=cr_model_engine,
                                                      prompt=cr_prompt,
                                                      max_tokens=MAX_TOKENS,
                                                      n=1,
                                                      stop=STOP,
                                                      temperature=TEMPERATURE)
    except Exception as e:
        cr_result = f'Error in generating response : {e}'
    if cr_result == '':
        cr_result = cr_completions.choices
    return cr_result


def image_response(ir_client, ir_prompt):
    ''' Use the DALL-E model to generate an image '''
    ir_model_engine = IMAGE_ENGINE
    ir_prompt = f"{ir_prompt}\n"
    ir_result = ''
    try:
        ir_completions = ir_client.images.generate(model=ir_model_engine,
                                                   prompt=ir_prompt,
                                                   size=IMAGE_SIZE,
                                                   quality=IMAGE_QUALITY,
                                                   n=1)
    except Exception as e:
        ir_result = f'Error in generating image : {e}'
    if ir_result == '':
        ir_result = ir_completions.data[0].url
    return ir_result


def create_assistant(ca_client, ca_name, ca_intruction):
    ''' Create a new assistant '''
    ca_result = ''
    try:
        ca_assistant = ca_client.beta.assistants.create(name=ca_name,
                                                        instructions=ca_intruction,  # noqa: E501
                                                        model=ASSISTANT_ENGINE,
                                                        tools=[{"type": "file_search"}])  # noqa: E501
    except Exception as e:
        ca_result = f'Error in creating assistant : {e}'
    if ca_result == '':
        ca_result = ca_assistant
    return ca_result


def create_vector_store(cvs_client, cvs_name, cvs_filelist):
    ''' Create a new vector store '''
    cvs_result = ''
    try:
        cvs_vector_store = cvs_client.beta.vector_stores.create(name=cvs_name)
    except Exception as e:
        cvs_result = f'Error in creating vector store : {e}'
    if cvs_result != '':
        print(f'[x] {cvs_result}')
    cvs_file_paths = cvs_filelist
    cvs_file_streams = [open(file_path, "rb") for file_path in cvs_file_paths]  # noqa: E501
    try:
        cvs_file_batch = cvs_client.beta.vector_stores.file_batches.upload_and_poll(cvs_vector_store.id,  # noqa: E501
                                                                                    files=cvs_file_streams)  # noqa: E501
    except Exception as e:
        cvs_result = f'Error in uploading files : {e}'
    if cvs_result != '':
        print(f'[x] {cvs_result}')
    print(f'[o] File batch ID : {cvs_file_batch.id}')
    print(f'[o] File batch status : {cvs_file_batch.status}')
    return cvs_vector_store


def main():
    ''' main function '''
    print('[*] main: start')
    mw_credid = credscheck('Z:/pyproject/secrets/secrets.json')
    mw_open_ai_key = mw_credid['OpenAI_API_Key']
    mw_open_ai_org = mw_credid['OpenAI_Org_ID']
    mw_prompt = "You are a games designer." \
                " Design a fantasy roleplay scenario" \
                " based in a library for players to explore." \
                " The players will be level 1." \
                " The library is a vast, ancient building" \
                " with many rooms and hidden secrets." \
                " The players will encounter a variety of" \
                " challenges and puzzles as they explore." \
                " The library is home to many magical" \
                " artifacts and creatures."
    mw_messages = [
        {"role": "user",
         "content": mw_prompt}
        ]
    mw_client = OpenAI(api_key=mw_open_ai_key)
    mw_response = chat_response(mw_client, mw_messages)
    mw_image = image_response(mw_client, "a white siamese cat")
    mw_instruction = "You are a designer of RPG game." \
                     "Use your knowlegdge base to help" \
                     "write a scenario for a new game."
    mw_assistant = create_assistant(mw_client,
                                    'Delta Green Assistant',
                                    mw_instruction)
    mw_filelist = ['Z:/pyproject/jackmanimation/gameitems/deltagreen.txt']
    mw_vector_store = create_vector_store(mw_client,
                                          'Delta Green Vector Store',
                                          mw_filelist)
    try:
        mw_assistant = mw_client.beta.asssistants.update(assistant_id=mw_assistant.id,  # noqa: E501
                                                         tool_resources={"file_search": {"vector_sctore_ids": [mw_vector_store.id]}})  # noqa: E501
    except Exception as e:
        print(f'[x] Error in updating assistant : {e}')

    print(f'[o] OpenAI Org ID  : {mw_open_ai_org}')
    print(f'[o] Prompt         : {mw_prompt}')
    print(f'[o] Response       : {mw_response}')
    print(f'[o] Image URL      : {mw_image}')
    print(f'[o] Assistant ID   : {mw_assistant.id}')
    print('[*] main: end')


if __name__ == '__main__':
    main()
