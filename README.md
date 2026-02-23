# 🚦 Simulador de Planificación de CPU – SIGET

## 📖 Descripción
Este proyecto implementa un simulador de planificación de procesos de CPU aplicado al contexto del **SIGET (Sistema de Gestión de Tráfico)**.  
El simulador permite analizar cómo distintos algoritmos de planificación gestionan procesos con diferentes características, evaluando la latencia de respuesta ante emergencias y la eficiencia en el procesamiento de datos.

---

## 🎯 Objetivos
- Simular el funcionamiento de un planificador de CPU.  
- Representar los estados de un proceso:  
  - Nuevo  
  - Listo  
  - En ejecución  
  - Bloqueado  
  - Terminado  
- Aplicar y comparar distintos algoritmos de planificación.  
- Visualizar la ejecución mediante un diagrama de tiempo (Gantt).  
- Analizar el desempeño en un entorno tipo SIGET.  

---

## ⚙️ Algoritmos Implementados
### Round Robin
- Usa un quantum fijo.  
- Distribuye el CPU de forma equitativa.  
- Evita la inanición.  
- Presenta mayor latencia en procesos críticos.  

### Prioridad
- Ejecuta primero los procesos más urgentes.  
- Reduce el tiempo de respuesta ante emergencias.  
- Puede postergar procesos de baja prioridad.  

---

## 🧩 Procesos Simulados
| Proceso            | Tiempo CPU | Prioridad | Descripción          |
|--------------------|------------|-----------|----------------------|
| Monitoreo_Trafico  | 8          | 3         | Proceso rutinario    |
| Alerta_Accidente   | 4          | 1         | Emergencia crítica   |
| Reporte_Estadistico| 6          | 2         | Análisis de datos    |


