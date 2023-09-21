import re

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, ValidationError
from wtforms.validators import DataRequired, Optional

from .constants import PATTERN
from .models import URLMap


def is_correct_short_url(custom_id):
    match = re.findall(PATTERN, custom_id)
    return ''.join(match) == custom_id


class URLForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[DataRequired(message='Обязательное поле')]
    )

    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[Optional()]
    )

    submit = SubmitField(
        'Создать'
    )

    def validate_short_url(form, field):
        if not is_correct_short_url(field.data):
            raise ValidationError(
                'Указано недопустимое имя для короткой ссылки'
            )
        if URLMap.query.filter_by(short=field.data).first():
            raise ValidationError(f'Имя "{field.data}" уже занято!')
