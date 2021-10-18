import singer
import cx_Oracle

LOGGER = singer.get_logger()

def fully_qualified_column_name(schema, table, column):
    return '"{}"."{}"."{}"'.format(schema, table, column)

def make_dsn(config):
   return cx_Oracle.makedsn(config["host"], config["port"], config["sid"])

def open_connection(config):
    LOGGER.info("dsn: %s", make_dsn(config))
    conn = cx_Oracle.connect(config["user"], config["password"], make_dsn(config))
    return conn

def send_error(message):
    LOGGER.info("error: %s", message)
    cx_Oracle.close()
    raise cx_Oracle.DatabaseError({_Error.code: 'ORA-12345', _Error.message: 'No Database found'})
