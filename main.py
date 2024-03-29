from flask import Flask, request,render_template
import forms
from flask import flash
from flask_wtf.csrf import CSRFProtect
from flask import g
app = Flask(__name__)
app.secret_key = 'clavesecreta'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/maestros")
def maestros():
    return render_template("maestros.html")

@app.route("/alumnos",methods=["GET","POST"])
def alumnos():
    alumnos_form=forms.UserForm(request.form)
    nom=""
    apaterno=""
    correo=""
    if request.method == "POST":
        nom=alumnos_form.nombre.data
        apaterno=alumnos_form.apaterno.data
        correo=alumnos_form.email.data
        print(f"nombre:{nom}")
        print(f"nombre:{apaterno}")
        print(f"nombre:{correo}")
    return render_template("alumnos.html", form=alumnos_form, nom=nom)

def hola():
    return "<p> Hola Mundo</p>"

@app.route("/hola")
def func():
    return "<h1>Saludo desde hola --UTL</h1>"

@app.route("/saludo")
def func1():
    return "<h1>Saludo desde saludo</h1>"

@app.route("/nombre/<string:nom>")
def nombre(nom):
    return f"<h1>Hola {nom}</h1>"

@app.route("/numero/<int:n1>")
def numero(n1):
    return f"<h1>El valor es {n1}</h1>"

@app.route("/user/<string:nom>/<int:id>")
def user(nom,id):
    return f"<h1>ID: {id} NOMBRE: {nom}</h1>"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return f"<h1>La suma de  {n1} + {n2} = {n1+n2}</h1>"

@app.route("/multiplica",methods=["GET","POST"])
def mul():
        if request.method=="POST":
            num1=(request.form.get("n1"))
            num2=(request.form.get("n2"))
            return f"<h1>El resultado es  {str(int(num1)*int(num2))}</h1>"
        else:
            return f'''
                    <form action="/multiplica" method="POST">
                        <label >N1:</label>
                        <input type="number" name="n1"></input>
                        <label >N2:</label>
                        <input type="number" name="n2"></input>
                        <input type="submit" value="Calcular"></input>
                        
                    </form>
                    
                    '''

@app.route("/formulario1")
def calculo():
    return render_template("formulario1.html")

@app.route("/resultado",methods=["GET","POST"])
def mult2():
        if request.method=="POST":
            num1=(request.form.get("n1"))
            num2=(request.form.get("n2"))
            return f"<h1>El resultado es  {str(int(num1)*int(num2))}</h1>"
        else:
            pass

@app.route("/alum",methods=["GET","POST"])
def alum():
    alumnos_form=forms.UsersForm(request.form)
    nom=""
    apaterno=""
    amaterno=""
    edad=""
    correo=""
    if request.method == "POST" and alumnos_form.validate():
        nom=alumnos_form.nombre.data
        apaterno=alumnos_form.apaterno.data
        amaterno=alumnos_form.amaterno.data
        edad=alumnos_form.edad.data
        correo=alumnos_form.correo.data
        print(f"nombre:{nom}")
        print(f"nombre:{apaterno}")
        print(f"nombre:{correo}")
    return render_template("alumnos.html", form=alumnos_form, nom=nom, apa=apaterno, ama=amaterno, edad=edad, correo=correo)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

@app.before_request
def before_request():
    g.prueba='Hola'
    print("Antes de la petición")

@app.route("/alum3",methods=["GET","POST"])
def alum3():
    print("Antes de la petición")
    valor=g.prueba
    print(f'Este es el dato: {valor}')
    alumnos_form=forms.UsersForm(request.form)
    nom=""
    apaterno=""
    amaterno=""
    edad=""
    correo=""
    if request.method == "POST" and alumnos_form.validate():
        nom=alumnos_form.nombre.data
        apaterno=alumnos_form.apaterno.data
        amaterno=alumnos_form.amaterno.data
        edad=alumnos_form.edad.data
        correo=alumnos_form.correo.data
        mensaje='Bienvenido: {}'.format(nom)
        flash(mensaje)
        print(f"nombre:{nom}")
        print(f"nombre:{apaterno}")
        print(f"nombre:{correo}")
    return render_template("alumnos.html", form=alumnos_form, nom=nom, apa=apaterno, ama=amaterno, edad=edad, correo=correo)

    
@app.after_request
def after_request(response):
    print("Después de la petición")
    return response


if __name__ == "__main__":
    app.run(debug=True)