from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello():
    conn=psycopg2.connect(dbname="docker", user="docker", host="db", port='5432')
    cur=conn.cursor()
    cur.execute("select * from docker")
    one = cur.fetchone()
    return format(one)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
