
"""
dockermysqlex.py

This program is a template for python programs
All this stuff at the top of the script is just optional metadata;

For the bot:

https://discordpy.readthedocs.io

For reading from Excel:

https://pypi.org/project/openpyxl/

(Although I would recommend using pretty much any other data source instead of using Excel)

"""
import os
import sys
import json
import mysql.connector
import docker

sys.path.append(os.path.realpath('../..'))


def open_mysql_db(omd_mysqlusername,
                  omd_mysqlpassword,
                  omd_mysqlhostname,
                  omd_dbdatabase=None,
                  omd_mysqlport=3306):
    ''' open mysql db '''
    try:
        omd_client = mysql.connector.connect(host=omd_mysqlhostname,
                                             user=omd_mysqlusername,
                                             password=omd_mysqlpassword,
                                             database=omd_dbdatabase,
                                             port=omd_mysqlport)
    except mysql.connector.errors.ProgrammingError as omd_err:
        print(f"[-] Error: {omd_err}")
        return None
    return omd_client


def get_secrets(gs_file_details):
    """
        This function gathers the credentials needed to open anything
    """
    try:
        with open(gs_file_details, encoding="utf8") as gs_secrets_file:
            gs_secrets = json.load(gs_secrets_file)
    except Exception as gs_err:
        gs_message = f'[-] Danger! Danger! Will Robinson!: {gs_err}'
        print(gs_message)
        return []
    gs_secrets_file.close()
    return gs_secrets


def mysql_query(mq_connection, mq_query):
    ''' mysql query'''
    mq_resultcursor = mq_connection.cursor(dictionary=True)
    mq_resultcursor.execute(mq_query)
    return mq_resultcursor


def docker_information():
    '''This displays docker information '''
    di_client = docker.from_env()
    for di_line in di_client.containers.list():
        print(f"{di_line.id} : {di_line.name} {di_line.status}")
        if di_line.name != "jackmanimation-mysql":
            di_line.kill()
            di_line.remove()

    for di_image_item in di_client.images.list():
        print(f"{di_image_item.tags[0]}")

    di_client.containers.run("ubuntu",
                             ["sleep",
                              "infinity"],
                             detach=True,
                             ports={'80/tcp': 8080},
                             name="Xavi-play-one")
    for _ in range(10):
        di_client.containers.run("ubuntu",
                                 ["sleep",
                                  "infinity"],
                                 detach=True)
    di_client.close()


def main():
    """ This is the main routine for the program """
    docker_information()
    maincredid = get_secrets('../../secrets/nusecrets.json')
    mysqlusername = maincredid["mysqluser"]
    mysqlpassword = maincredid["mysqlpassword"]
    mysqlhostname = maincredid["mysqlhost"]
    mysqlport = maincredid["mysqlport"]

    mysqlclient = open_mysql_db(mysqlusername,
                                mysqlpassword,
                                mysqlhostname,
                                "employees",
                                mysqlport)
    if mysqlclient is None:
        print("[-] oops baby nothing to do ")
        return None

    mycursor = mysql_query(mysqlclient, "select count(*) as numemployees from employees;")
    print(f'{mycursor.fetchall()[0]["numemployees"]}')
    mycursor.close()

    mysqlclient.close()
    return None


if __name__ == '__main__':
    main()
