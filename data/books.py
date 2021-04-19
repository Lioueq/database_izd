from main import db


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
