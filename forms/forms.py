from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField, FloatField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired


class AddIzdForm(FlaskForm):
    book_name = StringField('Название издания', validators=[DataRequired()])
    vid_izd = SelectField('Вид издания', choices=['Монография', 'Учебное пособие', 'Методичка', 'Сборник', 'Периодика',
                                                  'Прочее'])
    ISBN = StringField('ISBN')
    tip_perep = SelectField('Тип переплета', choices=['Брошюра', 'Брошюра + цв.обл.', 'Книга', 'Книга+цв.обл.'])
    kol_str = IntegerField('Количество страниц', validators=[DataRequired()])
    format = SelectField('Формат', choices=['А4', 'А5'])
    tirazh = IntegerField('Тираж', validators=[DataRequired()])
    data_izg = DateField('Дата изготовления', format='%Y-%m-%d')
    god_izd = IntegerField('Год издания', validators=[DataRequired()])
    status = SelectField('Статус', choices=['ГОТОВ', 'НЕ ГОТОВ'])
    stoim = FloatField('Стомость издания', validators=[DataRequired()])
    submit = SubmitField('Сохранить')


class AddAuthorForm(FlaskForm):
    author_name = StringField('Имя автора', validators=[DataRequired()])
    submit = SubmitField('Сохранить')
