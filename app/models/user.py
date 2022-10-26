from app.extensions import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(200), unique=True)
    website = db.Column(db.String(200), unique=True)

    def __str__(self):
        return f"Person ID is {self.name} | Name is {self.name} | Website is {self.website}"

    def __repr__(self):
        return f"Person(id={self.id}, name={self.name}, website={self.website})"
