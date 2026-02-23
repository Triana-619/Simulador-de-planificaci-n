import time
from collections import deque

class Proceso:
    def __init__(self, nombre, tiempo_irrupcion, prioridad_alerta, tamaño_datos):
        self.nombre = nombre
        self.tiempo_irrupcion = tiempo_irrupcion
        self.tiempo_restante = tiempo_irrupcion
        self.prioridad_alerta = prioridad_alerta
        self.tamaño_datos = tamaño_datos
        self.estado = "Nuevo"
        self.tiempo_espera = 0
        self.tiempo_finalizacion = 0

    def __str__(self):
        return f"{self.nombre} | Estado: {self.estado} | Restante: {self.tiempo_restante}"

# ALGORITMO ROUND ROBIN
def round_robin(procesos, quantum):
    print("\n===== ROUND ROBIN =====\n")
    cola = deque(procesos)
    tiempo = 0

    while cola:
        proceso = cola.popleft()

        if proceso.estado == "Nuevo":
            proceso.estado = "Listo"

        proceso.estado = "En ejecución"
        print(f"Tiempo {tiempo}: {proceso.nombre} ejecutándose")

        ejecucion = min(quantum, proceso.tiempo_restante)
        time.sleep(0.5)

        proceso.tiempo_restante -= ejecucion
        tiempo += ejecucion

        if proceso.tiempo_restante > 0:
            proceso.estado = "Listo"
            cola.append(proceso)
        else:
            proceso.estado = "Terminado"
            proceso.tiempo_finalizacion = tiempo
            print(f"{proceso.nombre} terminó en tiempo {tiempo}")

    print("\nResultados Round Robin:")
    for p in procesos:
        print(f"{p.nombre} finalizó en {p.tiempo_finalizacion}")


# ==============================
# ALGORITMO PRIORIDAD
# ==============================
def prioridad(procesos):
    print("\n===== PLANIFICACIÓN POR PRIORIDAD =====\n")

    procesos_ordenados = sorted(procesos, key=lambda x: x.prioridad_alerta)
    tiempo = 0

    for proceso in procesos_ordenados:
        proceso.estado = "En ejecución"
        print(f"Tiempo {tiempo}: {proceso.nombre} ejecutándose (Prioridad {proceso.prioridad_alerta})")

        time.sleep(0.5)

        tiempo += proceso.tiempo_irrupcion
        proceso.estado = "Terminado"
        proceso.tiempo_finalizacion = tiempo

        print(f"{proceso.nombre} terminó en tiempo {tiempo}")

    print("\nResultados Prioridad:")
    for p in procesos_ordenados:
        print(f"{p.nombre} finalizó en {p.tiempo_finalizacion}")


# ==============================
# PROCESOS DEL SIGET
# ==============================
p1 = Proceso("Monitoreo_Trafico", 8, 3, 500)
p2 = Proceso("Alerta_Accidente", 4, 1, 200)
p3 = Proceso("Reporte_Estadistico", 6, 2, 800)

procesos_rr = [Proceso("Monitoreo_Trafico", 8, 3, 500),
               Proceso("Alerta_Accidente", 4, 1, 200),
               Proceso("Reporte_Estadistico", 6, 2, 800)]

procesos_pr = [p1, p2, p3]

# Ejecutar simulaciones
round_robin(procesos_rr, quantum=2)
prioridad(procesos_pr)