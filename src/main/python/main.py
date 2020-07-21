import sys
import configparser  as cp
from util import get_tables,load_db_details
from config import DB_DETAILS
from read import read_table
import pandas as pd
from write import write_df_to_file,load_table
from config import DB_DETAILS

props = cp.ConfigParser()
props.read('src/main/resources/application.properties')
env = sys.argv[1]

DB_USER_MYSQL = props[env]['DB_USER_MYSQL']
DB_PASS_MYSQL = props[env]["DB_PASS_MYSQL"]

DB_USER_POSTGRES = props.get(env,"DB_USER_POSTGRES")
DB_PASS_POSTGRES = props.get(env,"DB_PASS_POSTGRES")

print(DB_PASS_MYSQL)

def main():
    """Program takes at least one arguments"""

    #a_database = sys.argv[2]
    #a_table = sys.argv[3]

    db_details = load_db_details(env)
    tables = get_tables(path = 'src/main/python/table_list.csv',table_list = 'all')
    for table in tables['table_name']:
        table_n = table

    data,columns = read_table(db_details,DB_USER=DB_USER_MYSQL, DB_PASS = DB_PASS_MYSQL ,table_name = table_n )

    #db_details_write = load_db_details(env)['CUSTOMER_DB']
    load_table(db_details = db_details  , DB_USER = DB_USER_POSTGRES, DB_PASS  = DB_PASS_POSTGRES,
               data=data, column_names =columns, table_name=table_n)


if __name__ == '__main__':
    main()