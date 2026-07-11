from app import db


class Url(db.Model):
    __tablename__ = 'urls'

    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.Text, nullable=False)
    short_code = db.Column(db.String(10), nullable=False, unique=True)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False)

