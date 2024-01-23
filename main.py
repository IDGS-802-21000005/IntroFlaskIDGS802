from flask import Flask, request,render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/maestros")
def maestros():
    return render_template("maestros.html")

@app.route("/alumnos")
def alumnos():
    return render_template("alumnos.html")

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



if __name__ == "__main__":
    app.run(debug=True)