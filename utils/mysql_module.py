import pymysql.cursors, json
from utils import parsing, output


class Mysql:

    def __init__(self):
        config = parsing.parse_json('config.json')

        self.host = config["db_host"]
        self.port = int(config["db_port"])
        self.db_user = config["db_user"]
        self.db_pass = config["db_pass"]
        self.db = config["db"]

        self.connection = None
        self.cursor = None
        print("ok")

    def connect(self):
        self.connection = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.db_user,
            password=self.db_pass,
            db=self.db)
        print("ok2")
        return self.connection

    def cursor(self):
        self.cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        return self.cursor

