from appvars import db


association_table = db.Table('association',
                             db.Column('author_id', db.Integer, db.ForeignKey('authors.author_id')),
                             db.Column('nom_zak', db.Integer, db.ForeignKey('izd.Nom_zak')))


class Izd(db.Model):
    def __repr__(self):
        return f'{self.Nom_zak}|{self.book_name}|{self.vid_id}|{self.perep_id}|{self.kol_str}|{self.format_id}|' \
               f'{self.tirazh}|{self.data_izg}'
    __tablename__ = 'izd'
    Nom_zak = db.Column(db.Integer(), primary_key=True, auto_increment=True)
    book_name = db.Column(db.String(100))
    vid_id = db.Column(db.Integer(), db.ForeignKey('vidi_izd.vid_id'))
    ISBN = db.Column(db.String(100))
    perep_id = db.Column(db.Integer(), db.ForeignKey('tipi_perep.perep_id'))
    kol_str = db.Column(db.String(40))
    format_id = db.Column(db.Integer(), db.ForeignKey('formati.format_id'))
    tirazh = db.Column(db.String(100))
    data_izg = db.Column(db.Date())
    god_izd = db.Column(db.String(40))
    status_id = db.Column(db.Integer(), db.ForeignKey('statusi.status_id'))
    stoim = db.Column(db.Integer())
    authors = db.relationship('Authors', secondary=association_table, back_populates='izds')


class Authors(db.Model):
    def __repr__(self):
        return f'{self.author_id}|{self.author_name}'
    __tablename__ = 'authors'
    author_id = db.Column(db.Integer(), primary_key=True)
    author_name = db.Column(db.String(100))
    izds = db.relationship("Izd", secondary=association_table, back_populates="authors")


class VidiIzd(db.Model):
    __tablename__ = 'vidi_izd'
    vid_id = db.Column(db.Integer(), primary_key=True)
    vid_name = db.Column(db.String(100))
    izd = db.relationship('Izd', backref='vid_izd')


class TipiPerep(db.Model):
    __tablename__ = 'tipi_perep'
    perep_id = db.Column(db.Integer(), primary_key=True)
    perep_name = db.Column(db.String(100))
    izd = db.relationship('Izd', backref='tip_perep')


class Formats(db.Model):
    __tablename__ = 'formati'
    format_id = db.Column(db.Integer(), primary_key=True)
    format_name = db.Column(db.String(40))
    izd = db.relationship('Izd', backref='format')


class Statusi(db.Model):
    __tablename__ = 'statusi'
    status_id = db.Column(db.Integer(), primary_key=True)
    status_name = db.Column(db.String(100))
    izd = db.relationship('Izd', backref='status')
