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
    if not(u == 'abc' and p == 'xyz'):
        return 'LOGIN FAILED'
    else:
        return 'LOGIN SUCCESSFUL'


app.run(host='192.168.3.191', port=8080)
