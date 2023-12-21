# imports 
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

if __name__ == '__main__':
    app = Flask(__name__)
    CORS(app)

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
        return jsonify(new_user.to_dict()), 201

    with app.app_context():
        db.create_all()
        
    app.run(debug=True)


