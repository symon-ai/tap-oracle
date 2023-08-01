import singer
import cx_Oracle
from tap_oracle.symon_exception import SymonException

LOGGER = singer.get_logger()

def fully_qualified_column_name(schema, table, column):
    return '"{}"."{}"."{}"'.format(schema, table, column)

def make_dsn(config):
   return cx_Oracle.makedsn(config["host"], config["port"], config["sid"])

def open_connection(config):
    LOGGER.info("dsn: %s", make_dsn(config))
    try:
        conn = cx_Oracle.connect(config["user"], config["password"], make_dsn(config))
    except cx_Oracle.DatabaseError as e:
        message = str(e)
        if 'ORA-01017' in message:
            raise SymonException('The username and password provided are incorrect. Please try again.', 'odbc.AuthenticationFailed')
        if 'ORA-12545' in message:
            raise SymonException(f'The host "{config["host"]}" was not found. Please check the host name and try again.', 'odbc.HostNotFound')
        if 'ORA-12505' in message:
            raise SymonException(f'The SID "{config["sid"]}" does not exist. Please ensure it is correct.', 'odbc.DatabaseDoesNotExist')
        if 'ORA-12170' in message:
            raise SymonException('Timed out connecting to database. Please ensure all the connection form values are correct.', 'odbc.ConnectionTimeout')
        # ORA-12541: TNS:no listener, ORA-12543: TNS:destination host unreachable
        if 'ORA-12541' in message or 'ORA-12543' in message:
            raise SymonException(f'Sorry, we couldn\'t connect to the host "{config["host"]}". Please ensure all the connection form values are correct.', 'odbc.ConnectionFailed')
        raise
    return conn
