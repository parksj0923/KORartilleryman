from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
     con = sql.connect("database.db")
     cur = con.cursor()
     cur.execute("CREATE TABLE mask(number INTEGER, name TEXT, time TEXT, address TEXT)")
     con.close()
     return None

if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True)