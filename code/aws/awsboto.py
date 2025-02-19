import pymysql
import sys
import boto3
import os

ENDPOINT = "jackmanimation-dbserver.cniy4i088yxc.eu-west-1.rds.amazonaws.com"
PORT = "3306"
USER = "jackmanimation"
REGION = "eu-west-1"
DBNAME = "jackmanimation-dbserver"
os.environ['LIBMYSQL_ENABLE_CLEARTEXT_PLUGIN'] = '1'

# gets the credentials from .aws/credentials
session = boto3.Session(profile_name='default')
client = session.client('rds')

token = client.generate_db_auth_token(DBHostname=ENDPOINT,
                                      Port=PORT,
                                      DBUsername=USER,
                                      Region=REGION)

try:
    conn = pymysql.connect(auth_plugin_map={'mysql_clear_password': None},
                           host=ENDPOINT,
                           user=USER,
                           password=token,
                           port=PORT,
                           database=DBNAME,
                           ssl_ca='SSLCERTIFICATE',
                           ssl_verify_identity=True)
    cur = conn.cursor()
    cur.execute("""SELECT now()""")
    query_results = cur.fetchall()
    print(query_results)
except Exception as e:
    print("Database connection failed due to {}".format(e))
