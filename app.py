from flask import Flask, render_template, request, redirect
from gastos import agregar_gasto, obtener_gastos, calcular_total

app = Flask(__name__)

@app.route("/")
def inicio():
    gastos = obtener_gastos()
    total = calcular_total()
    return render_template(
        "index.html",
        gastos=gastos,
        total=total
    )

@app.route("/agregar", methods=["POST"])
def agregar():
    descripcion = request.form["descripcion"]
    monto = float(request.form["monto"])

    agregar_gasto(descripcion, monto)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
