from wtforms import Form
from wtforms import StringField, TextAreaField, TextField, SelectField, RadioField
from wtforms import EmailField
class UserForm(form):
    nombre=StringField("nombre")
    email=EmailField("correo")
    apaterno=TextField("apaterno")
    materias=SelectField(choices=[('Español','Esp'),('Mat','Matematicas'),('Ingles','Ing')])
    radios= RadioField('Curso',choices=[('1','1'),('2','2'),('3','3')])