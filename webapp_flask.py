import flask

# how to create a website

app = flask.Flask('MyApp')


# app.run()

@app.errorhandler(404)
def errorpage(err):
    return 'Page Under Construction'


@app.route('/')
def indexpage():
    return 'Welcome'


@app.route('/about')
def aboutpage():
    return '<b>This is about </b>'


@app.route('/login')
def loginpage():
    return '''
    <form action='/verify' method='POST'>
        username:<input type='text' name='uname' /><br/>
        password:<input type='password' name='pw' /><br/>
        <input type='submit' value='LOG IN' />            
    </form>'''


@app.route('/verify', methods=['post'])
def verifypage():
    u = flask.request.form.get('uname')
    p = flask.request.form.get('pw')
    if not (u == 'abc' and p == 'xyz'):
        return 'LOGIN FAILED'
    else:
        import sqlite3
        con = sqlite3.connect('Mydb.Sqlite3')
        cur = con.cursor()
        cur.execute('SELECT * FROM LOGDATA')
        result = cur.fetchall()
        return flask.render_template('report.html', res=result)


@app.route('/download/<filename>')
def staticfile(filename):
    return flask.send_from_directory(directory=r'C:\Users\lab365\Desktop\Python Training\bin', filename=filename)


@app.route('/empid/<int:eid>')
def empid(eid):
    D = {'name': 'abc', 'EMpId': eid}
    return D


@app.route('/logdata')
def logdata():
    return flask.redirect('/login')


@app.route('/passwords')
def passwords():
    return flask.abort(201, 'Access Denied')


app.run(host='192.168.3.191', port=8080)
