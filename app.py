# app.py

from flask import Flask, render_template, request, jsonify
from flask_migrate import Migrate
from config import Config
from models import db, UserData  # Import db and UserData from models.py

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config.from_object(Config)
db.init_app(app)  # Initialize db with the Flask app
migrate = Migrate(app, db)
app.debug = False
# Routes
@app.route('/')
def home():
    # Fetch all users from the database
    users = UserData.query.all()
    return render_template('index.html', users=users)


@app.route('/get_users', methods=['GET'])
def get_users():
    users = UserData.query.all()
    user_data = [{'name': user.name, 'email': user.email} for user in users]
    return jsonify(user_data)


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']

    # Save new user data to the database
    new_user_data = UserData(name=name, email=email)
    db.session.add(new_user_data)
    db.session.commit()

    # Fetch updated list of users after adding a new user
    users = UserData.query.all()
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
