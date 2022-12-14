from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired

class ClassificationForm(FlaskForm):
    card = SelectField('Jenis Kartu', choices=[(0, 'Prabayar'), (1, 'Pascabayar')], validators=[DataRequired()])
    call = SelectField('Panggilan', choices=[(0, 'Sedikit'), (1, 'Sedang'), (2, 'Banyak')], validators=[DataRequired()])
    block = SelectField('Blok', choices=[(0, 'Rendah'), (1, 'Sedang'), (2, 'Tinggi')], validators=[DataRequired()])
    submit = SubmitField('Submit')