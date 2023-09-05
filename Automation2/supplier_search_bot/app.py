from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
import requests

app = Flask(__name__)
app.secret_key = 'YOUR_SECRET_KEY_HERE'  # Change this to a random and secure key.

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin):
    # This class represents a user for Flask-Login.
    pass

@login_manager.user_loader
def user_loader(user_id):
    user = User()
    user.id = user_id
    return user

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Simplistic example, replace with proper authentication like checking from a database.
        username = request.form['username']
        password = request.form['password']

        if username == 'YOUR_USERNAME_HERE' and password == 'YOUR_PASSWORD_HERE':  # Replace these values
            user = User()
            user.id = username
            login_user(user)
            return redirect(url_for('index'))

        return 'Invalid credentials', 401

    return '''
    <form method="post">
        Username: <input type="text" name="username"><br>
        Password: <input type="password" name="password"><br>
        <input type="submit" value="Login">
    </form>
    '''

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/')
@login_required
def index():
    return render_template('index.html')

SUPPLIER_API_URL = 'https://api.supplier.com/search'  # Replace with the actual supplier API endpoint.
HEADERS = {
    'Authorization': 'Bearer YOUR_API_TOKEN',  # Replace with your actual API token.
    'Content-Type': 'application/json'
}

@app.route('/search')
@login_required
def search():
    sku = request.args.get('sku')
    response = requests.get(SUPPLIER_API_URL, headers=HEADERS, params={'sku': sku})

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Unable to fetch data from supplier.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
