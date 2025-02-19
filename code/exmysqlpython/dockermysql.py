"""
examplemysql.py

This program is a template for python programs
All this stuff at the top of the script is just optional metadata;

"""
import os
import sys

# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.gameitems.gamefunctions import credscheck
from jackmanimation.dbfunctions.mysqlfunctions import open_mysql
from jackmanimation.dbfunctions.mysqlfunctions import mysqlquery

NEW_SETUP = True
DB_HOSTNAME = '127.0.0.1'
DB_PORT = 3307
DB_SCRIPT = ('USE newclassicmodels;',
             'DROP TABLE IF EXISTS productlines;',
             'DROP TABLE IF EXISTS products;',
             'DROP TABLE IF EXISTS offices;',
             'DROP TABLE IF EXISTS employees;',
             'DROP TABLE IF EXISTS customers;',
             'DROP TABLE IF EXISTS payments;',
             'DROP TABLE IF EXISTS orders;',
             'DROP TABLE IF EXISTS orderdetails;',
             'CREATE TABLE productlines (productLine varchar(50),textDescription varchar(4000) DEFAULT NULL,htmlDescription mediumtext,image mediumblob, PRIMARY KEY (productLine));',
             "insert  into productlines(productLine,textDescription,htmlDescription,image) values ('Classic Cars','Attention car enthusiasts: Make your wildest car ownership dreams come true. Whether you are looking for classic muscle cars, dream sports cars or movie-inspired miniatures, you will find great choices in this category. These replicas feature superb attention to detail and craftsmanship and offer features such as working steering system, opening forward compartment, opening rear trunk with removable spare wheel, 4-wheel independent spring suspension, and so on. The models range in size from 1:10 to 1:24 scale and include numerous limited edition and several out-of-production vehicles. All models include a certificate of authenticity from their manufacturers and come fully assembled and ready for display in the home or office.',NULL,NULL),('Motorcycles','Our motorcycles are state of the art replicas of classic as well as contemporary motorcycle legends such as Harley Davidson, Ducati and Vespa. Models contain stunning details such as official logos, rotating wheels, working kickstand, front suspension, gear-shift lever, footbrake lever, and drive chain. Materials used include diecast and plastic. The models range in size from 1:10 to 1:50 scale and include numerous limited edition and several out-of-production vehicles. All models come fully assembled and ready for display in the home or office. Most include a certificate of authenticity.',NULL,NULL),('Planes','Unique, diecast airplane and helicopter replicas suitable for collections, as well as home, office or classroom decorations. Models contain stunning details such as official logos and insignias, rotating jet engines and propellers, retractable wheels, and so on. Most come fully assembled and with a certificate of authenticity from their manufacturers.',NULL,NULL),('Ships','The perfect holiday or anniversary gift for executives, clients, friends, and family. These handcrafted model ships are unique, stunning works of art that will be treasured for generations! They come fully assembled and ready for display in the home or office. We guarantee the highest quality, and best value.',NULL,NULL),('Trains','Model trains are a rewarding hobby for enthusiasts of all ages. Whether you are looking for collectible wooden trains, electric streetcars or locomotives, you will find a number of great choices for any budget within this category. The interactive aspect of trains makes toy trains perfect for young children. The wooden train sets are ideal for children under the age of 5.',NULL,NULL),('Trucks and Buses','The Truck and Bus models are realistic replicas of buses and specialized trucks produced from the early 1920s to present. The models range in size from 1:12 to 1:50 scale and include numerous limited edition and several out-of-production vehicles. Materials used include tin, diecast and plastic. All models include a certificate of authenticity from their manufacturers and are a perfect ornament for the home and office.',NULL,NULL),('Vintage Cars','Our Vintage Car models realistically portray automobiles produced from the early 1900s through the 1940s. Materials used include Bakelite, diecast, plastic and wood. Most of the replicas are in the 1:18 and 1:24 scale sizes, which provide the optimum in detail and accuracy. Prices range from $30.00 up to $180.00 for some special limited edition replicas. All models include a certificate of authenticity from their manufacturers and come fully assembled and ready for display in the home or office.',NULL,NULL);",  # pylint: disable=C0301
             'commit;'
             )


def dockersqlmain():
    """ This is the main routine for the program """
    dsm_dbredid = credscheck('Z:/pyproject/secrets/secrets.json')
    dsm_mysqlusername = dsm_dbredid["BotUsername"]
    dsm_mysqlpassword = dsm_dbredid["BotPassword"]
    dsm_use_db = open_mysql(dsm_mysqlusername,
                            dsm_mysqlpassword,
                            DB_HOSTNAME,
                            None,
                            DB_PORT)

    if dsm_use_db is None:
        return None
    return dsm_use_db


def create_db_entries(cde_db):
    ''' create db entries '''
    cde_databasecount = 0
    for cde_query in DB_SCRIPT:
        mysqlquery(cde_db, cde_query)
        cde_databasecount += 1
    print('[-] Looking at databases')
    print(f'[-] There are {cde_databasecount} lines')


if __name__ == '__main__':
    print("[+] Starting the sequence.")
    main_db = dockersqlmain()
    if NEW_SETUP:
        create_db_entries(main_db)
    else:
        print("[+] Not creating new")
    print("[+] Finishing up and closing down.")
