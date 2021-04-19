from flask import Flask, render_template, redirect, request, abort
from flask_sqlalchemy import SQLAlchemy
from forms.add_book import AddBookForm
from datetime import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = '7N9WLBw8?PcRuy*j2X@EdVkwyp-Y@@xk'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


class Book(db.Model):
    def __repr__(self):
        return f'{self.Nom_zak}|{self.autor_name}|{self.book_name}|{self.vid_izd}|{self.ISBN}|{self.tip_perep}|' \
               f'{self.kol_str}|{self.format}|{self.tirazh}|{self.data_izg}|{self.god_izd}|{self.status}|{self.stoim}'
    Nom_zak = db.Column(db.Integer, primary_key=True)
    autor_name = db.Column(db.String(100))
    book_name = db.Column(db.String(100))
    vid_izd = db.Column(db.String(100))
    ISBN = db.Column(db.String(100))
    tip_perep = db.Column(db.String(100))
    kol_str = db.Column(db.String(40))
    format = db.Column(db.String(40))
    tirazh = db.Column(db.String(100))
    data_izg = db.Column(db.DateTime)
    god_izd = db.Column(db.String(40))
    status = db.Column(db.String(100))
    stoim = db.Column(db.Integer)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        flags = request.form.getlist('flags')
        search_flag = request.form.get('search')
        text = request.form.get('text')
        date_from = datetime.strptime(request.form.get('date_from'), '%Y-%m-%d')
        date_to = datetime.strptime(request.form.get('date_to'), '%Y-%m-%d')
        if search_flag == 'Номер заказа':
            book = Book.query.filter(Book.Nom_zak == text).all()
            return render_template('index.html', books=book, flags=flags, search_flag=search_flag, text=text)
        elif search_flag == 'Автор':
            books = Book.query.filter(Book.autor_name.like(f'%{text}%'), Book.vid_izd.in_(flags)).all()
            return render_template('index.html', books=books, flags=flags, search_flag=search_flag, text=text)
        elif search_flag == 'Название издания':
            books = Book.query.filter(Book.book_name.like(f'%{text}%'), Book.vid_izd.in_(flags)).all()
            return render_template('index.html', books=books, flags=flags, search_flag=search_flag, text=text)
        elif search_flag == 'Дата':
            books = Book.query.filter(Book.data_izg > date_from, Book.data_izg < date_to, Book.vid_izd.in_(flags)).all()
            return render_template('index.html', books=books, flags=flags, search_flag=search_flag, text=text)
        books = Book.query.filter(Book.vid_izd.in_(flags)).all()
        return render_template('index.html', books=books, flags=flags, search_flag=search_flag, text=text)
    book = Book.query.all()
    return render_template('index.html', books=book)


@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    form = AddBookForm()
    if form.validate_on_submit():
        book = Book(
            autor_name=form.autor_name.data,
            book_name=form.book_name.data,
            vid_izd=form.vid_izd.data,
            ISBN=form.ISBN.data,
            tip_perep=form.tip_perep.data,
            kol_str=form.kol_str.data,
            format=form.format.data,
            tirazh=form.tirazh.data,
            data_izg=form.data_izg.data,
            god_izd=form.god_izd.data,
            status=form.status.data,
            stoim=form.stoim.data
        )
        db.session.add(book)
        db.session.commit()
        return redirect('/')
    return render_template('add_book.html', title='Добавление книги', form=form)


@app.route('/book/<int:id>', methods=['GET', 'POST'])
def edit_job(id):
    form = AddBookForm()
    if request.method == "GET":
        book = Book.query.filter_by(Nom_zak=id).first()
        if book:
            form.autor_name.data = book.autor_name
            form.book_name.data = book.book_name
            form.vid_izd.data = book.vid_izd.capitalize()
            form.ISBN.data = book.ISBN
            form.tip_perep.data = book.tip_perep.capitalize()
            form.kol_str.data = book.kol_str
            form.format.data = book.format.capitalize()
            form.tirazh.data = book.tirazh
            form.data_izg.data = book.data_izg
            form.god_izd.data = book.god_izd
            form.status.data = book.status.capitalize()
            form.stoim.data = book.stoim
        else:  # поменять
            abort(404)
    if form.validate_on_submit():
        book = Book.query.filter_by(Nom_zak=id).first()
        if book:
            book.autor_name = form.autor_name.data
            book.book_name = form.book_name.data
            book.vid_izd = form.vid_izd.data
            book.ISBN = form.ISBN.data
            book.tip_perep = form.tip_perep.data
            book.kol_str = form.kol_str.data
            book.format = form.format.data
            book.tirazh = form.tirazh.data
            book.data_izg = form.data_izg.data
            book.god_izd = form.god_izd.data
            book.status = form.status.data
            book.stoim = form.stoim.data
            db.session.commit()
            return redirect('/')
        else:
            abort(404)  # поменять
    return render_template('add_book.html', title='Редактирование книги', form=form)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
