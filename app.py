from flask import render_template, redirect, request, abort
from forms.forms import AddIzdForm, AddAuthorForm
from datetime import datetime
from appvars import db, app
from models import Izd, Authors


def converter(data):  # функция для присваивания id для данных
    vidi_izd = {'Монография': 1, 'Учебное пособие': 2, 'Методичка': 3, 'Сборник': 4, 'Периодика': 5, 'Прочее': 6}
    tipi_perep = {'Брошюра': 1, 'Брошюра+цв.обл.': 2, 'Книга': 3, 'Книга+цв.обл.': 4}
    formats = {'А4': 1, 'А5': 2}
    status = {'ГОТОВ': 1, 'НЕ ГОТОВ': 2}
    if data in vidi_izd.keys():
        data_id = vidi_izd[data]
    elif data in tipi_perep.keys():
        data_id = tipi_perep[data]
    elif data in formats.keys():
        data_id = formats[data]
    else:
        data_id = status[data]
    return data_id


@app.route('/')  # главная страница
def index():
    izds = Izd.query.all()
    return render_template('index.html', izds=izds)


@app.route('/add_izd', methods=['POST', 'GET'])  # добавление издания
def add_izd():
    form = AddIzdForm()
    if form.validate_on_submit():
        vid_izd_id = converter(form.vid_izd.data)
        tip_perep_id = converter(form.tip_perep.data)
        format_id = converter(form.format.data)
        status_id = converter(form.status.data)
        izd = Izd(
            book_name=form.book_name.data,
            vid_id=vid_izd_id,
            ISBN=form.ISBN.data,
            perep_id=tip_perep_id,
            kol_str=form.kol_str.data,
            format_id=format_id,
            tirazh=form.tirazh.data,
            data_izg=form.data_izg.data,
            god_izd=form.god_izd.data,
            status_id=status_id,
            stoim=form.stoim.data
        )
        db.session.add(izd)
        db.session.commit()
        return redirect('/')
    if request.method == 'POST':
        return render_template('author_choice.html', title='Выбор авторов', izd_form=form)
    return render_template('add_izd.html', title='Добавление издания', form=form)


@app.route('/author_choice', methods=['POST', 'GET'])  # выбор автора
def author_choice():
    form = AddIzdForm()
    if request.method == 'POST':
        authors_id = request.form.getlist('authors')
        return render_template('add_izd.html', title='Добавление издания', form=form, authors_id=authors_id)
    authors = Authors.query.all()
    return render_template('author_choice.html', authors=authors, title='Выбор авторов')


@app.route('/add_author', methods=['POST', 'GET'])  # добавление автора
def add_author():
    form = AddAuthorForm()
    if form.validate_on_submit():
        author = Authors(author_name=form.author_name.data)
        db.session.add(author)
        db.session.commit()
        return redirect('/author_choice')
    return render_template('add_author.html', title='Добавление автора', form=form)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
