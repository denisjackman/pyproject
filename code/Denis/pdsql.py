''' pd sql connection '''
import os
import sys
import glob
import pandas as pd
import sqlalchemy
# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.gameitems.gamefunctions import credscheck

OUTPUT_FILE = "Z:/Logs/djoutput.csv"
INPUT_FILE = "Z:/Logs/djinput.csv"
BOOKS_FILE = 'Z:/Datasets/sf_*.csv'
SECRETS_FILE = 'Z:/pyproject/secrets/secrets.json'
DATABASE_NAME = 'test'
NEW_BOOK_FILE = 'Z:/Datasets/books.csv'


def main():
    ''' main function '''
    ps_files = glob.glob(BOOKS_FILE)
    ps_creds = credscheck(SECRETS_FILE)
    ps_username = ps_creds["BotUsername"]
    ps_password = ps_creds["BotPassword"]
    ps_hostname = ps_creds["hostname2"]
    ps_database = DATABASE_NAME
    ps_db = sqlalchemy.create_engine(f'mysql+mysqlconnector://{ps_username}:{ps_password}@{ps_hostname}:3306/{ps_database}')

    ps_query = "SELECT * FROM fruit"

    if ps_db is None:
        print("[-] database issues closing")
    else:
        pd_query_result = pd.read_sql(ps_query, ps_db)
        pd_query_result.to_csv(OUTPUT_FILE)
        book_df = pd.DataFrame()
        for file in ps_files:
            temp_df = pd.read_csv(file)
            book_df = pd.concat([book_df, temp_df])
        book_df.to_sql(con=ps_db, name='sf_books', if_exists='replace', index=False)

        new_boof_df = pd.read_csv(NEW_BOOK_FILE)
        new_boof_df.to_sql(con=ps_db, name='other_books', if_exists='replace', index=False)


if __name__ == '__main__':
    main()
