from flask import request, jsonify, redirect
from app import app, utils, db
from app.models import Url
from sqlalchemy.exc import IntegrityError


@app.route('/shorten', methods=['POST'])
def shorten():
    body = request.get_json()

    if not body or not 'URL' in body:
        return jsonify({'message': 'Wrong data'}), 400

    while True:
        short_code = utils.generate_short_code()
        new_entry = Url(short_code=short_code, original_url=body['URL'])
        try:
            db.session.add(new_entry)
            db.session.commit()

            break
        except IntegrityError:
            db.session.rollback()

    return jsonify({'url': request.host_url + short_code}), 201


@app.route('/<short_code>', methods=['GET'])
def get_short_url(short_code):
    datas = Url.query.filter_by(short_code=short_code).first()

    if not datas:
        return jsonify({'message': 'Short link not found'}), 404

    return redirect(datas.original_url, code=302)