import os
from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv
import matplotlib.pyplot as plt

# load the .env file variables
load_dotenv()


import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

results = spotify.artist_albums(birdy_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])


shakira= 'spotify:artist:0EmeFodog0BfCgMzAIvKQp'

results = spotify.artist_albums(birdy_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])

results = spotify.artist_top_tracks(shakira)

nombre_cancion = []
popularidad = []
duracion_minutos = []

for track in results['tracks'][:10]:
    nombre_cancion.append(track['name'])
    popularidad.append(track['popularity'])
    duracion_ms = track['duration_ms']  # Duración en milisegundos
    # Convertir la duración de milisegundos a minutos 
    duracion_minutos.append(duracion_ms / 60000)  # 1 minuto = 60000 miliseg
    print()

    print("Nombre:", nombre_cancion)
    print("Popularidad:", popularidad)
    print("Duración (minutos):", duracion_minutos)
    print()
    # Crear un DataFrame de Pandas
df = pd.DataFrame({'Nombre': nombre_cancion, 'Popularidad': popularidad, 'Duración (minutos)': duracion_minutos})

# Imprimir el DataFrame
print(df)

import seaborn as sns

# Graficar el scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['duracion_minutos'], df['popularidad'], color='blue', alpha=0.7)
plt.title('Relación entre Duración y Popularidad de Canciones de Shakira')
plt.xlabel('Duración (minutos)')
plt.ylabel('Popularidad')
plt.grid(True)
plt.show()