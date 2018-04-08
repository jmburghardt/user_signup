from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/signup', methods=['post'])
def get_username():
    username = request.form['username']
    if (not username) or (username.strip() == ''):
        error = "That's not a valid username"
        return render_template('options.html', error=error)

    if len(username) < 3 or len(username) > 20:
        error = "Your username must be between 3 and 20 characters."
        return render_template('options.html', error=error)
    else:
        return render_template('options.html', value=username)

def get_password():
    password = request.form['password']
    if (not password) or (password.strip() == ''):
        error = "That's not a valid password"
        return render_template('options.html', error=error)
    if len(password) < 3 or len(password) > 20:
        error = "Your password must be between 3 and 20 characters"
        return render_template('options.html', error=error)

def validate_password():
    verify = request.form['verify']
    password = request.form['password']
    if verify != password:
        error = "Passwords don't match"
        return render_template('options.html', error=error)

def email():
    email = request.form['email']
    if not email:
        error = "That's not a valid email"
        return render_template('options.html', error=error)

@app.route('/')
def index():
    error = request.args.get('error')
    if error:
        error_esc = cgi.escape(error, quote=True)
        error_element = '<p class="error">' + error_esc + '</p>'
    else:
        error_element = ''
    return render_template('options.html', error_msg=error)

app.run()
