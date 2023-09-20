from random import sample
from string import ascii_letters, digits

from flask import abort, flash, render_template, redirect

from . import app, db

from .forms import URLForm
from .models import URLMap


def get_unique_short_id():
    symbols = ascii_letters + digits
    short_url_symbols = ''.join(sample(symbols, 6))
    if URLMap.query.filter_by(short=short_url_symbols).first():
        get_unique_short_id()
    return short_url_symbols


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLForm()
    if form.validate_on_submit():
        short_name = form.custom_id.data
        if URLMap.query.filter_by(short=short_name).first():
            flash(message=f'Имя {short_name} уже занято!')
            form.custom_id.data = None
            return render_template('url.html', form=form)
        if short_name is None or short_name == '':
            form.custom_id.data = get_unique_short_id()
        if len(form.custom_id.data) > 16:
            flash(message='Указано недопустимое имя для короткой ссылки')
            form.custom_id.data = None
            return render_template('url.html', form=form)

        urlmap = URLMap(
            original=form.original_link.data,
            short=form.custom_id.data
        )
        db.session.add(urlmap)
        db.session.commit()

    return render_template('url.html', form=form)


@app.route('/<string:short>')
def redirect_view(short):
    urlmap = URLMap.query.filter_by(short=short).first()
    if urlmap is not None:
        original_link = urlmap.original
        return redirect(original_link)
    abort(404)
