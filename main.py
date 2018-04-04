from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

app.route('/username', methods=['post'])
def get_username():
    username = request.form['username']
    if (not username) or (username.strip() == ''):
        error = "That's not a valid username."
        return redirect('/?error=' + cgi.escape(error, quote=True))

    if len(username) < 3 or len(username) < 20:
        error = "Your username must be between 3 and 20 characters."
        return redirect('/?error=' + cgi.escape(error, quote=True))

app.route('/')
def index():
    error = request.args.get('error')
    if error:
        error_esc = cgi.escape(error, quote=True)
        error_element = '<p class="error">' + error_esc + '</p>'
    else:
        error_element = ''
    return render_template('edit.html')
    
    
     








app.run()
