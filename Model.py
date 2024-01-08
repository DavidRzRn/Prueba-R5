import pandas as pd
from sklearn.ensemble import IsolationForest

# Cargar el archivo CSV
df = pd.read_csv("dataset.csv")

# Seleccionar las columnas relevantes para la detección de anomalías (puedes ajustar esto según tus necesidades)
features = ["disc_number", "duration_ms"]

# Crear un DataFrame con solo las características seleccionadas
X = df[features]

# Crear y entrenar el modelo de Isolation Forest
model = IsolationForest(contamination=0.01)  # Puedes ajustar el parámetro de contaminación según tus necesidades
model.fit(X)

# Predecir anomalías en los datos
df['anomaly'] = model.predict(X)

# Filtrar las filas que contienen anomalías
anomalies = df[df['anomaly'] == -1]

# Imprimir las filas con anomalías
print("Filas con anomalías:")
print(anomalies)
