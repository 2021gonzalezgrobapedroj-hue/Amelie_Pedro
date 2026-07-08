# Lista donde se guardan los gastos
gastos = []

# Función para agregar un gasto
def agregar_gasto(gastos, descripcion, monto):
    gasto = {
        "descripcion": descripcion,
        "monto": monto
    }
    gastos.append(gasto)

# Función para calcular el total
def calcular_total(gastos):
    total = 0

    for gasto in gastos:
        total += gasto["monto"]

    return total

# Función para mostrar los gastos
def mostrar_gastos(gastos):
    return gastos
