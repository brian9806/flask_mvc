import mariadb


config = {
    'host':'localhost',
    'port':3608,
    'user':'root',
    'password':'',
    'database':'tienda'
}

DB = mariadb.connect(**config)
DB.autocommit = True