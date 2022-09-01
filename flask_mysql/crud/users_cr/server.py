from flask import Flask, render_template, request, redirect, session
from user import User
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('users.html', users = User.get_all())

@app.route('/users_add', methods=['POST'])
def new_user():
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email']
    }
    User.save(data)
    return redirect('/')

@app.route('/users/new')
def result():
    return render_template('create.html')

if __name__ == "__main__":
    app.run(debug=True)