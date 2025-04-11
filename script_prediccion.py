import pickle
import pandas as pd

# Cargar el modelo
try:
    with open("modelo_churn.pkl", "rb") as file:
        model = pickle.load(file)
    print("Modelo cargado exitosamente.")
except Exception as e:
    print(f"Error al cargar el modelo: {e}")
    exit()

# Pedir al usuario la ruta del archivo CSV
archivo = input("\nIngrese la ruta del archivo CSV con los datos: ").strip()

try:
    # Cargar los datos
    datos_nuevos = pd.read_csv(archivo)

    # Verificar que los datos tengan las columnas necesarias
    columnas_esperadas = ['credit_score', 'age', 'balance', 'products_number', 'credit_card', 'active_member', 'estimated_salary', 'country_Germany', 'country_Spain', 'gender_Male']
    if not all(col in datos_nuevos.columns for col in columnas_esperadas):
        print("Error: El archivo CSV no contiene todas las columnas necesarias.")
        exit()

    # Realizar la predicción
    prediccion = model.predict(datos_nuevos)
    print(f"\nPredicción de Churn: {'Abandona' if prediccion[0] == 1 else 'Permanece'}")

except Exception as e:
    print(f"Error al cargar o procesar el archivo: {e}")
