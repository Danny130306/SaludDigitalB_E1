import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import os

# Función para ejecutar notebooks
def ejecutar_notebook(ruta_notebook):
    """
    Ejecuta un archivo .ipynb usando nbconvert.
    """
    if not os.path.exists(ruta_notebook):
        print(f" No se encontró el archivo: {ruta_notebook}")
        return
    print(f"\n Ejecutando: {ruta_notebook}")
    try:
        with open(ruta_notebook, "r", encoding="utf-8") as f:
            nb = nbformat.read(f, as_version=4)
            ep = ExecutePreprocessor(timeout=None, kernel_name="python3")
            ep.preprocess(nb, {"metadata": {"path": os.path.dirname(ruta_notebook)}})
        print(f"{os.path.basename(ruta_notebook)} ejecutado correctamente.\n")
    except Exception as e:
        print(f"Error al ejecutar {ruta_notebook}: {e}\n")

# Fases del Proyecto
def fase_1():
    ejecutar_notebook("../scripts/1_Crear_Carpetas.ipynb")
def fase_2():
    ejecutar_notebook("../scripts/2_Crear_Estructura.ipynb")
def fase_3():
    ejecutar_notebook("../scripts/3_Generar_Data_Pacientes.ipynb")
def fase_4():
    ejecutar_notebook("../scripts/4_Proceso_ETL.ipynb")
def fase_5():
    ejecutar_notebook("../scripts/5_Loading_MongoDB.ipynb")
def fase_6():
    ejecutar_notebook("../scripts/6_Reportes.ipynb")

# Ejecución total del pipeline
def ejecutar_todo():
    fase_1()
    fase_2()
    fase_3()
    fase_4()
    fase_5()
    fase_6()

# Menú principal
def main():
    print("""
=======================================
PROYECTO BIG DATA - ANÁLISIS DE PACIENTES
=======================================
Seleccione una fase a ejecutar:
1. Crear estructura de carpetas
2. Crear archivo base de datos
3. Generar datos aleatorios de pacientes
4. Procesar ETL y limpiar datos
5. Integrar datos en MongoDB (NoSQL)
6 .Visualización de reportes
7. Ejecutar TODO el flujo completo
0. Salir
""")
    opcion = input("Ingrese una opción (0-7): ")
    if opcion == "1":
        fase_1()
    elif opcion == "2":
        fase_2()
    elif opcion == "3":
        fase_3()
    elif opcion == "4":
        fase_4()
    elif opcion == "5":
        fase_5()
    elif opcion == "6":
        fase_6()
    elif opcion == "7":
        ejecutar_todo()
    elif opcion == "0":
        print("Saliendo del programa...")
    else:
        print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
