# Proyecto-Final-Churn-ABC-benitez-maria-laura
"Análisis del dataset Bank Marketing ABC para el proyecto final ".
# 💼 Proyecto Final - Predicción de Cancelación de Clientes Bancarios (Churn)

Este proyecto utiliza técnicas de Machine Learning para predecir qué clientes de una entidad bancaria tienen más probabilidades de cerrar sus cuentas. A partir de un análisis de 10.000 registros, se desarrolló un modelo predictivo, se exploraron visualmente los datos y se propusieron estrategias correctivas con simulación de impacto financiero.

---

## 🧠 Objetivo

Detectar patrones y características en los clientes que abandonan el banco, con el fin de:

- Anticiparse a la cancelación de cuentas (churn)
- Implementar acciones preventivas
- Estimar el impacto económico de la fuga y retención de clientes

---

## 📂 Contenido del Repositorio

| Archivo | Descripción |
|--------|-------------|
| `Proyecto_Final_Churn.ipynb` | Notebook principal con el análisis, EDA, modelado y visualizaciones. |
| `Bank Customer Churn Prediction.xlsx` | Dataset original con información de clientes. |
| `Informe_Final_Churn.pdf` | Informe profesional en PDF con visualizaciones, conclusiones y simulación de retención. |
| `README.md` | Este archivo de presentación del proyecto. |

---

## 🧪 Tecnologías utilizadas

- Python (Google Colab)
- Pandas
- Matplotlib / Seaborn
- Scikit-learn
- XGBoost
- FPDF (para generar informe)
- Visualizaciones profesionales

---

## 📈 Resultados clave

- Modelo XGBoost entrenado con `scale_pos_weight` para clases desbalanceadas.
- ROC AUC Score: **0.846**
- Simulación de recuperación de clientes con impacto financiero estimado:
  - 🧍‍♂️ Abandonan: **1656**
  - ✅ Recuperados simulados (60%): **993**
  - 💸 Pérdida estimada sin acción: **$153M**
  - 💚 Recuperación posible: **$91.7M**

---

## 📊 Visualizaciones

Incluye:
- Histogramas
- Boxplots y violinplots por variable
- Matriz de correlación
- Importancia de variables (XGBoost)
- Infografía final tipo figura humana para simulación

---

## 📌 Cómo usar

1. Abrí el archivo `.ipynb` en Google Colab.
2. Subí el archivo `Bank Customer Churn Prediction.xlsx` en tu sesión.
3. Ejecutá el notebook paso a paso para reproducir el análisis.

---

## ✍️ Autor

**[Benietz Maria Laura]**  
Proyecto Final - Curso: *Machine Learning para la Ciencia de Datos*

---
