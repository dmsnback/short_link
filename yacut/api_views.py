from flask import jsonify, request

from . import app, db
from .error_handlers import InvalidAPIUsage
from .forms import is_correct_short_url
from .models import URLMap
from .views import get_unique_short_id


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_url(short_id):
    url = URLMap.query.filter_by(short=short_id).first()

    if url is None:
        raise InvalidAPIUsage('Указанный id не найден', 404)

    return jsonify(url=url.original), 200


@app.route('/api/id/', methods=['POST'])
def create_id():
    data = request.get_json()

    if data is None:
        raise InvalidAPIUsage('Отсутствует тело запроса')

    if 'url' not in data:
        raise InvalidAPIUsage('\"url\" является обязательным полем!')

    if 'custom_id' not in data or data['custom_id'] == '' or data['custom_id'] is None:
        custom_id = get_unique_short_id()
    else:
        custom_id = data['custom_id']

    if len(custom_id) > 16:
        raise InvalidAPIUsage(
            'Указано недопустимое имя для короткой ссылки',
            400
        )

    if URLMap.query.filter_by(short=custom_id).first() is not None:
        raise InvalidAPIUsage(f'Имя "{custom_id}" уже занято.')

    if is_correct_short_url(custom_id):

        url = URLMap()
        data['original'] = data['url']
        data['short'] = custom_id
        url.from_dict(data)
        db.session.add(url)
        db.session.commit()
        return jsonify(
            url=url.original, short_link='http://localhost/' + url.short
        ), 201
    else:
        raise InvalidAPIUsage(
            'Указано недопустимое имя для короткой ссылки',
            400
        )
