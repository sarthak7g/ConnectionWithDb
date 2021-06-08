from sqlalchemy import create_engine

engine_postgres = create_engine('postgresql://postgres:123456@localhost/postgres')
engine_mysql = create_engine('mysql+mysqldb://root:123456@localhost/courses')
