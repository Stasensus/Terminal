from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/auth')
def auth():
    return render_template('auth.html')

@app.route('/account', methods = ['GET', 'POST'])
def account():
    if request.method == 'GET':
        return render_template('account.html')
    project = request.form.get('project')
    login = request.form.get('login')
    password = request.form.get('password')
    print(project, login, password)

    return render_template('account.html')

@app.route('/end')
def end():
    return render_template('end.html')

if __name__ == '__main__':
    app.run()
