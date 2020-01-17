# API-1 -> IP
# api1 = https://127.0.0.1:8080/ip
import flask

app = flask.Flask('MyApp2')


@app.route('/ip', methods=['GET'])
def api_ip():
    import sqlite3
    con = sqlite3.connect('Mydb.sqlite3')
    cur = con.cursor()
    cur.execute('SELECT ip FROM logdata')
    result = cur.fetchall()
    result = [i[0] for i in result]
    D = {k: v for k, v in enumerate(result)}
    return D


# api2 - http://127.0.0.0.1:8080/emp
@app.route('/emp', methods=['POST'])
def empdetails():
    details = flask.request.args
    details = dict(details)
    return details


@app.route('/json')
def fromjson():
    F = open('Mydata.json', 'w')
    D = {"course": "python", "loc": "Blr"}
    import json
    json.dump(D, F)
    F.close()
    F = open('Mydata.json')
    r = json.load(F)
    F.close()
    return r


app.run()
