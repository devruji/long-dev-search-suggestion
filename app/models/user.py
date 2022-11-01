from app.extensions import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    keyword = db.Column(db.String(200), unique=True)
    score = db.Column(db.Float)

    def __str__(self):
        return f"ID is {self.id} | Keyword is {self.Keyword} | Score is {self.score}"

    def __repr__(self):
        return f"Users(id={self.id}, keyword={self.keyword}, score={self.score})"
