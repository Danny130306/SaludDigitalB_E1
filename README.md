⚙️ Arquitectura del Proyecto
# 🏦 Proyecto Big Data – Análisis de Pacientes, MongoDB y GitHub
## 📘 Descripción General

El proyecto simula un caso real del sector Salud, desde la creación y depuración de datos, hasta su almacenamiento en una base de datos NoSQL y visualización analítica, aplicando buenas prácticas de versionamiento con GitHub e integración continua con Jenkins.

## 🗂️ Estructura del Proyecto

```bash
SaludDigitalB_E1/
│
├── data/
│   └── pacientes.csv
│   └── base.csv
│
├── database/
│   └── pacientes_clean.csv
│
├── reports/
│   └── pacientes_atendidos_por_servicio.png
│   └── distribución_por_sexo.png
│   └── distribución_de_edades.png
│   └── promedio_de_montos_por_distrito.png
│
├── ci/
│   └── job_jenkins1.png
│   └── job_jenkins2.png
│   └── job_jenkins3.png
│   └── job_jenkins4.png
│   └── job_jenkins5.png
│
├── git/
│   └── 1er_commit.png
│   └── 2do_commit.png
│   └── 3er_commit.png
│   └── 4to_commit.png
│   └── 5to_commit.png
│   └── 6to_commit.png
│
├── scripts/
│   └── 1_Crear_Carpetas.ipynb
│   └── 2_Crear_Estructura.ipynb
│   └── 3_Generar_Data_Turismo.ipynb
│   └── 4_Proceso_ETL.ipynb
│   └── 5_Loading_MongoDB.ipynb
│   └── 6_Reportes.ipynb
│
├── README.md
```
## 👨‍🏫 Autor

```bash
Proyecto desarrollado aplicando conceptos de Big Data, Vs Code, Python, MongoDB y Jenkins.
Jaime Llanos Bardales
Fecha: 17.10.2025
```
## 🧱 Estructura de Datos Simulada
Archivo: pacientes.csv
Crear un archivo pacientes.csv en la carpeta /data con la siguiente estructura:
id_paciente	nombre	edad	sexo	distrito	servicio	fecha_atencion	monto
P001	Ana Torres	34	F	Miraflores	Odontología	2024-11-15	150
P002	Luis Pérez	42	M	Surco	Pediatría	2024-10-21	250
### 🔍 Fases del Proyecto
#### 🧩 Fase 1 – Creación de Archivos
    Crear carpetas data, database, reports, ci, git y scripts y estructura base del proyecto usando os y pathlib en tiempo de ejecución
#### 🧩 Fase 2 – Definición de Esquema
    Generar un archivo base CSV (base.csv) con la estructura indicada.
#### 🧩 Fase 3 – Generación de Datos Aleatorios
    Generar un archivo CSV (pacientes.csv) con 3000 registros simulados, que incluya campos nulos, NA, entre otros
#### 🧩 Fase 4 – ETL (Limpieza de Datos)
    •	Eliminar duplicados
    •	Rellenar valores nulos en campos de transporte o destino
    •	Formatear fechas
    •	Validar tipos de datos
    Guardar como pacientes_clean.csv.
#### 🧩 Fase 5 – Carga en MongoDB
    Crear base de datos SaludDigital_2025 y colección pacientes
    Insertar los registros limpios desde CSV.
#### 🧩 Fase 6 – Visualización de Datos
    Usar matplotlib y pandas para mostrar:
    1.	Gráfico de barras: número de pacientes atendidos por servicio.
    2.	Gráfico circular: distribución por sexo.
    3.	Histograma: distribución de edades.
    4.	Reporte tabular: promedio de montos por distrito.