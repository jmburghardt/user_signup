from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/signup', methods=['post'])
def signup():
    username = get_username()
    password = get_password()
    verify = validate_password()
    email = get_email()
    if username[1] == '' and password[1] == '' and email == '' and verify == '':
        return render_template('Welcome.html', username=username[0])
    else:
        return render_template('options.html', value=username[0], error=username[1], 
            valuepass=password[0], errorpass=password[1], errorverify=verify, erroremail=email)

def get_username():
    username = request.form['username']
    if (not username) or (username.strip() == ''):
        error = "That's not a valid username"
        return  ('', error)

    if len(username) < 3 or len(username) > 20:
        error = "Your username must be between 3 and 20 characters."
        return ('', error)
    else:
        return (username, '')

def get_password():
    password = request.form['password']
    if (not password) or (password.strip() == ''):
        error = "That's not a valid password"
        return ('', error)
    if len(password) < 3 or len(password) > 20:
        error = "Your password must be between 3 and 20 characters"
        return ('', error)
    else:
        return (password, '')

def validate_password():
    verify = request.form['verify']
    password = request.form['password']
    if verify != password or verify == '':
        error = "Passwords don't match"
        return (error)
    else:
        return ''

def get_email():
    email = request.form['email']
    error = "That's not a valid email"
    if len(email) < 3 or len(email) > 20:
        return error
    if "@" in email and "." in email or email == '':
        return ''
    else:
        return error

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
