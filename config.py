class Config(object):
    """Base config, uses staging database server."""
    DEBUG = False
    TESTING = False
    MYSQL_DATABASE_USER = 'root'
    MYSQL_DATABASE_PASSWORD = 'password'
    MYSQL_DATABASE_DB = 'streamviz'
    MYSQL_DATABASE_HOST = 'localhost'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost/streamviz'
