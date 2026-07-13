# Lista donde se guardan los gastos
gastos = []

# Agregar un gasto
def agregar_gasto(descripcion, monto):
    gasto = {
        "descripcion": descripcion,
        "monto": monto
    }
    gastos.append(gasto)

# Obtener la lista de gastos
def obtener_gastos():
    return gastos

# Calcular el total
def calcular_total():
    total = 0

    for gasto in gastos:
        total += gasto["monto"]

    return total
