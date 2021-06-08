from flask import Flask
from db_connection import engine_postgres, engine_mysql
import pandas as pd

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/PostgreSQL', methods=['GET'])
def getPostgresData():
    try:
        connection1 = engine_postgres.connect()
        data = pd.read_sql_query("select * from Employee", connection1)
        return  data.to_json(orient="records")
    except Exception as e:
        print(e)

@app.route('/MySQL', methods=['GET'])
def getMySqlData():
    try:
        connection2 = engine_mysql.connect()
        data = pd.read_sql_query("select * from course", connection2)
        return  data.to_json(orient="records")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    # serve(app, port=5050)