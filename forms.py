from flask_wtf import FlaskForm
from wtforms import DateField, StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Optional
from datetime import date


class LoginForm(FlaskForm):
    username = StringField('Użytkownik', validators=[DataRequired()])
    password = PasswordField('Hasło', validators=[DataRequired()])
    remember_me = BooleanField('Zapamiętaj')
    submit = SubmitField('Zaloguj')


class AddUser(FlaskForm):
    name = StringField('Imię')
    surname = StringField('Nazwisko')
    submit = SubmitField('Dodaj')


class AddTask(FlaskForm):
    task_name = StringField('Nazwa', validators=[DataRequired()])
    task_description = StringField('Opis', validators=[DataRequired()])
    task_creator = StringField('Uworzył', validators=[DataRequired(), ])
    task_contractor = StringField('Wykonawca')
    task_date_created = DateField('Utworzone', default=date.today(), render_kw={'disabled': 'True'})
    task_date_finished = DateField('Zakończono', validators=[Optional()])
    submit = SubmitField('Dodaj')
