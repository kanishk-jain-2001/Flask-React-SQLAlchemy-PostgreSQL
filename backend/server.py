# imports 
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

if __name__ == '__main__':
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost/mydatabase'
    db = SQLAlchemy(app)

    class User(db.Model):

        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(80), unique=True, nullable=False)
        email = db.Column(db.String(120), unique=True, nullable=False)

        def __repr__(self):
            return '<User %r>' % self.username
        
    @app.route('/add_user', methods=['POST'])
    def add_user():
        data = request.json
        new_user = User(username=data['username'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        # Convert new_user to a dictionary 
        user_data = {
        'id': new_user.id,  # Assuming the User model has an id field
        'username': new_user.username,
        'email': new_user.email
        }
        return jsonify(user_data), 201
    
    @app.route('/find_user', methods=['GET'])
    def find_user():
        username = request.args.get('username')
        if not username:
            return jsonify({"message": "Username is required"}), 400
        user = User.query.filter_by(username=username).first()
        if user:
            return jsonify({"email": user.email}), 200
        else:
            return jsonify({"message": "User not found"}), 404

    with app.app_context():
        db.create_all()

    app.run(debug=True)


