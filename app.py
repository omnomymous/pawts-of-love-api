from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow 
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = 
db = SQLAlchemy(app)
ma = Marshmallow(app)


class User(db.Model):    
    id = db.Column(db.Integer, primary_key=True)
    shelter = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    
        
    
    


    def __init__(self, shelter, email, password):        
        self.shelter = shelter
        self.email = email
        self.password = password        
        
        
    
    
        

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'shelter', 'email', 'password')

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@app.route('/user', methods=["POST"])
def add_user():
    shelter = request.json.get('shelter')
    email = request.json.get('email')
    password = request.json.get('password')
        
    new_user = User(shelter, email , password)

    db.session.add(new_user)
    db.session.commit()

    user = User.query.get(new_user.id)
    return user_schema.jsonify(user)

@app.route('/users', methods=["GET"])
def get_users():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result)


class Dogs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String,  nullable=False)
    breed = db.Column(db.String, nullable=False)
    behavior = db.Column(db.String)
    age = db.Column(db.Integer)
    contact_email = db.Column(db.String, nullable=False)
    shelter_name = db.Column(db.String, nullable=False)
    dog_image = db.Column(db.String)
    
    

    def __init__(self, name, breed, behavior, age, contact_email, shelter_name, dog_image):        
        self.name = name
        self.breed = breed
        self.behavior = behavior
        self.age = age
        self.contact_email = contact_email
        self.shelter_name = shelter_name
        self.dog_image = dog_image

class DogsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'breed', 'behavior', 'age', 'contact_email', 'shelter_name', 'dog_image')

dog_schema = DogsSchema()
dogs_schema = DogsSchema(many=True)




@app.route('/dog', methods=["POST"])
def add_dog():
    name = request.json.get('name')
    breed = request.json.get('breed')
    behavior = request.json.get('behavior')
    age = request.json.get('age')
    contact_email = request.json.get('contact_email')
    shelter_name = request.json.get('shelter_name')
    dog_image = request.json.get('dog_image')
    

    new_dog = Dogs(name, breed, behavior, age, contact_email, shelter_name, dog_image)

    db.session.add(new_dog)
    db.session.commit()

    dog = Dogs.query.get(new_dog.id)

    return dog_schema.jsonify(dog)


@app.route('/dogs', methods=["GET"])
def get_dogs():
    all_dogs = Dogs.query.all()
    result = dogs_schema.dump(all_dogs)    
    return jsonify(result)


@app.route("/dog/<id>", methods=["DELETE"])
def dog_delete(id):
    dog = Dogs.query.get(id)
    db.session.delete(dog)
    db.session.commit()

    return dog_schema.jsonify(dog)


class Cats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    breed = db.Column(db.String, nullable=False)
    behavior = db.Column(db.String)
    age = db.Column(db.Integer)
    contact_email = db.Column(db.String, nullable=False)
    shelter_name = db.Column(db.String, nullable=False)
    cat_image = db.Column(db.String)

    def __init__(self, name, breed, behavior, age,  contact_email, shelter_name, cat_image):        
        self.name = name
        self.breed = breed
        self.behavior = behavior
        self.age = age
        self.contact_email = contact_email
        self.shelter_name = shelter_name
        self.cat_image = cat_image
    

class CatsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'breed', 'behavior', 'age', 'contact_email', 'shelter_name', 'cat_image')

cat_schema = CatsSchema()
cats_schema = CatsSchema(many=True)


@app.route('/cat', methods=["POST"])
def add_cat():
    name = request.json.get('name')
    breed = request.json.get('breed')
    behavior = request.json.get('behavior')
    age = request.json.get('age')
    contact_email = request.json.get('contact_email')
    shelter_name = request.json.get('shelter_name')
    cat_image = request.json.get('cat_image')
    
    new_cat = Cats(name, breed, behavior, age, contact_email, shelter_name, cat_image)

    db.session.add(new_cat)
    db.session.commit()

    cat = Cats.query.get(new_cat.id)
    return cat_schema.jsonify(cat)


@app.route('/cats', methods=["GET"])
def get_cats():
    all_cats = Cats.query.all()
    result = cats_schema.dump(all_cats)
    return jsonify(result)


@app.route("/cat/<id>", methods=["DELETE"])
def cat_delete(id):
    cat = Cats.query.get(id)
    db.session.delete(cat)
    db.session.commit()

    return cat_schema.jsonify(cat)


if __name__ == "__main__":
    app.run(debug=True)
