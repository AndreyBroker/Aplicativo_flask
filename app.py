from flask import Flask, render_template, request, redirect, url_for, session
from server import Database
from secret_key import encrypted_key

app = Flask(__name__)
app.secret_key = encrypted_key()


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/auth', methods=['POST'])
def auth():
    username = request.form.get('username')
    password = request.form.get('password')

    db = Database()
    validation = db.user_validation(username, password)

    if validation:

        session["username"] = validation
        return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))
    
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/home')
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    else:
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)