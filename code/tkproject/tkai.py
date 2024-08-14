''' this is tk ai module '''
import sys
import os
import datetime
from openai import OpenAI

# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.gameitems.gamefunctions import credscheck

MODEL_ENGINE = "gpt-3.5-turbo-instruct"
ASSISTANT_ENGINE = "gpt-4-turbo-preview"
IMAGE_ENGINE = "dall-e-3"
IMAGE_SIZE = "1024x1024"
IMAGE_QUALITY = "standard"
MAX_TOKENS = 1024
TEMPERATURE = 0.5
STOP = None
TODAY = datetime.datetime.now().strftime('%Y%m%d_%H%M')


def write_output_file(wof_filename, wof_data):
    ''' Write data to a file '''
    with open(wof_filename, 'w', encoding='utf-8-sig') as wof_file:
        wof_file.write(wof_data)


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
        cr_result = cr_completions.choices[0].text
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
                                                        instructions=ca_intruction,
                                                        model=ASSISTANT_ENGINE,
                                                        tools=[{"type": "file_search"}])
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
    with open(cvs_file_paths[0], "rb") as cvs_file_stream:
        try:
            cvs_file = cvs_client.beta.vector_stores.files.upload(cvs_vector_store.id,
                                                                  file=cvs_file_stream)
        except Exception as e:
            cvs_result = f'Error in uploading file : {e}'
    if cvs_result != '':
        print(f'[x] {cvs_result}')
    print(f'[o] File batch ID : {cvs_file.id}')
    print(f'[o] File batch status : {cvs_file.status}')
    return cvs_vector_store


def main():
    ''' main function '''
    print('[*] main: start')
    mw_credid = credscheck('Z:/pyproject/secrets/secrets.json')

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
    mw_client = OpenAI(api_key=mw_credid['OpenAI_API_Key'])
    mw_response = chat_response(mw_client, mw_messages)
    mw_ir_prompt = "Detailed wacky caricature of a little tired brunette" \
                   " woman with long curly hair and piercings in her ears," \
                   " pale brown eyes, black clothes, holding a kitten," \
                   " VRay render, UHD, professional lighting, bright " \
                   " colours, details! White background"

    mw_image = image_response(mw_client, mw_ir_prompt)
    mw_instruction = "You are a designer of RPG game." \
                     "Use your knowledge base to help" \
                     "write a scenario for a new game."
    mw_assistant = create_assistant(mw_client,
                                    'Delta Green Assistant',
                                    mw_instruction)
    mw_filelist = ['Z:/Store/deltagreen.txt']
    try:
        mw_vector_store = create_vector_store(mw_client,
                                              'Delta Green Vector Store',
                                              mw_filelist)
    except Exception as e:
        print(f'[x] Error in creating vector store : {e}')

    try:
        mw_assistant = mw_client.beta.assistants.update(assistant_id=mw_assistant.id,
                                                        tool_resources={"file_search": {"vector_store_ids": [mw_vector_store.id]}})
    except Exception as e:
        print(f'[x] Error in updating assistant : {e}')
    mw_image_check = 'https://images.nightcafe.studio/jobs/KEW9N1NcIb4xiejYM4oH/KEW9N1NcIb4xiejYM4oH--1--ci4ap.jpg'

    mw_message = [
        {
            "role": "user",
            "content": [
                {"type": "text",
                 "text": "Analyse this image and generate a prompt for dall-e-3"},
                {"type": "image_url",
                 "image_url": {
                     "url": mw_image_check,
                     },
                 },
                ],
            }
        ]
    write_output_file(f"Z:/Store/{TODAY}_{mw_credid['OpenAI_Org_ID']}_image.txt",
                      mw_image)
    write_output_file(f"Z:/Store/{TODAY}_{mw_credid['OpenAI_Org_ID']}_response.txt",
                      mw_response)
    mw_response = chat_response(mw_client, mw_message)
    write_output_file(f"Z:/Store/{TODAY}_{mw_credid['OpenAI_Org_ID']}_prompt.txt",
                      mw_response)
    print('[*] main: end')


if __name__ == '__main__':
    main()
