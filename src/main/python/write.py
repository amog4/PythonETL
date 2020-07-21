from util import get_connection


def build_insert_query(table_name, column_names):
    column_names_string = ', '.join(column_names)
    column_values = tuple(map(lambda column: column.replace(column, '%s'), column_names))
    column_values_string = ', '.join(column_values)
    query = (f'''
        INSERT INTO {table_name} ({column_names_string}) VALUES ({column_values_string})
    ''')
    return query


def insert_data(connection, cursor, query, data, batch_size=100):
    recs = []
    count = 1
    for rec in data:
        recs.append(rec)
        if count % batch_size == 0:
            cursor.executemany(query, recs)
            connection.commit()
            recs = []
        count = count + 1
    cursor.executemany(query, recs)
    connection.commit()


def load_table(db_details,DB_USER,DB_PASS, data, column_names, table_name):
    TARGET_DB = db_details['TARGET_DB']

    connection = get_connection(db_type=TARGET_DB['DB_TYPE'],
                                db_host=TARGET_DB['DB_HOST'],
                                db_name=TARGET_DB['DB_NAME'],
                                db_port=TARGET_DB['DB_PORT'],
                                db_user=DB_USER,
                                db_pass=DB_PASS
                                )
    cursor = connection.cursor()
    query = build_insert_query(table_name, column_names)
    print(query)
    insert_data(connection, cursor, query, data)

    connection.close()


def write_df_to_file(base_dir, table_name, df):
    file_path = f'{base_dir}/{table_name}/'
    df.to_csv(file_path, index=False)