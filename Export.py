import pandas as pd
import json

# Importar el archivo JSON
with open("taylor_swift_spotify.json", 'r') as file:
    data = json.load(file)


# Normalizar los datos y convertir a un DataFrame de pandas
df = pd.json_normalize(data, record_path=['albums', 'tracks'], 
                   meta=['artist_id', 'artist_name', 'artist_popularity', 
                         ['albums', 'album_id'], ['albums', 'album_name'], ['albums', 'album_release_date'], ['albums', 'album_total_tracks']],
                   sep='_')


# Exporta el archivo CSV
df.to_csv("dataset.csv", index=False)
