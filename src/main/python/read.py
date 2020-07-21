from util import get_connection



def get_column_names(cursor, db_type):
    if db_type == 'mysql':
        column_names = cursor.column_names
    elif db_type == 'postgres':
        column_names = []
        for column_name in cursor.description:
            column_names.append(column_name[0])
    return column_names


def read_table(db_details,DB_USER,DB_PASS ,table_name, limit=0):
    read_db = db_details['RETAIL']
    connection = get_connection(db_type=read_db['DB_TYPE'],
                                db_host=read_db['DB_HOST'],
                                db_port=read_db['DB_PORT'],
                                db_name=read_db['DB_NAME'],
                                db_user=DB_USER,
                                db_pass=DB_PASS
                                )
    cursor = connection.cursor()
    if limit == 0:
        query = f'SELECT * FROM {table_name}'
    else:
        query = f'SELECT * FROM {table_name} LIMIT {limit}'
    cursor.execute(query)
    data = cursor.fetchall()
    column_names = get_column_names(cursor, read_db['DB_TYPE'])

    connection.close()

    return data, column_names