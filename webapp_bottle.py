import bottle

# how to create a website

app = bottle.Bottle()


# app.run()

@app.error(404)
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


@app.route('/verify', method='post')
def verifypage():
    u = bottle.request.forms.get('uname')
    p = bottle.request.forms.get('pw')
    if not (u == 'abc' and p == 'xyz'):
        return 'LOGIN FAILED'
    else:
        bottle.TEMPLATE_PATH.append(r'C:\Users\lab365\Desktop\Python Training\bin')
        import sqlite3
        con = sqlite3.connect(r'C:\Users\lab365\Desktop\Python Training\bin\Mydb.Sqlite3')
        cur = con.cursor()
        cur.execute('SELECT * FROM logdata')
        result = cur.fetchall()
        return bottle.template('report.tpl', res=result)


@app.route('/download/<filename>')
def staticfile(filename):
    return bottle.static_file(root=r'C:\Users\lab365\Desktop\Python Training\bin', filename=filename, download=True)


@app.route('/empid/<eid:int>')
def empid(eid):
    D = {'name': 'abc', 'EMpId': eid}
    return D


@app.route('/nameid/<nid:re:[a-z0-9]+>')
def name_id(nid):
    return str(nid)


@app.route('/logdata')
def logdata():
    return bottle.redirect('/login')


@app.route('/passwords')
def passwords():
    return bottle.abort(201, 'Access Denied')


app.run()
