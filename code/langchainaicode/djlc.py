''' test mongo db connection '''
import os
import sys
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings

# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.gameitems.gamefunctions import credscheck


def main():
    ''' main function '''
    credid = credscheck('Z:/pyproject/secrets/secrets.json')
    os.environ["OPENAI_API_KEY"] = credid["OpenAIKey"]
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = credid["HuggingFaceKey"]
    lc_chat = ChatOpenAI(temperature=0,
                         max_tokens=100)
    lc_message = [("system", "You are a helpful assistant that translates English into French."),
                  ("human", "I Love Programming.")]
    lc_response = lc_chat.invoke(lc_message)
    lc_embeddings_model = OpenAIEmbeddings(model="text-embedding-3-large")
    lc_text = "this is the text you are going to embed"
    lc_query_result = lc_embeddings_model.embed_query(lc_text)

    print(lc_response.content)
    print(len(lc_query_result))


if __name__ == '__main__':
    main()
