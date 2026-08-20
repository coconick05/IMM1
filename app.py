import streamlit as st
import os
import time
import glob
import os
from gtts import gTTS
from PIL import Image
import base64

st.title("Conversión de Texto a Audio")
image = Image.open('gato_raton.png')
st.image(image, width=350)
with st.sidebar:
    st.subheader("Esrcibe y/o selecciona texto para ser escuchado.")


try:
    os.mkdir("temp")
except:
    pass

st.subheader("Lo que quedó del corazón.")
st.write('Lo que quedó del corazón

El diablillo llevaba tanto tiempo con el tridente en alto que ya no recordaba para qué servía. Solo sabía que debía sostenerlo así, apuntando al cielo, como si algo importante fuera a caer de un momento a otro.

El querubín tampoco recordaba de dónde había sacado el corazón que llevaba entre las manos. Solo sabía que no era suyo. Latía distinto, a destiempo, como si perteneciera a otra persona que lo estuviera buscando desde hace años.

Se encontraron sin querer, uno corriendo hacia adelante y el otro girando sobre sí mismo, y por un segundo ninguno de los dos se sorprendió de estar ahí, en un fondo blanco que no era cielo ni tierra ni nada.

—¿Es tuyo esto? —preguntó el querubín, ofreciendo el corazón.

El diablillo lo miró. Sonreía, como sonreía siempre, con esa sonrisa pintada que no se le movía aunque quisiera.

—No sé —dijo—. ¿Es tuyo el tenedor?

Ninguno soltó lo que tenía. Y así se quedaron, congelados a mitad de un gesto que empezó hace mucho —una advertencia, una ofrenda, quién sabe— y que nadie, ni ellos mismos, terminaría jamás.

Porque algunas figuras solo existen a medias: un brazo levantado que nunca llega a golpear, una mano abierta que nunca llega a entregar. Y el fondo blanco se queda ahí, esperando que alguien decida qué fue lo que realmente pasó entre ellos.'
        
        )
           
st.markdown(f"Quieres escucharlo?, copia el texto")
text = st.text_area("Ingrese El texto a escuchar.")

tld='com'
option_lang = st.selectbox(
    "Selecciona el lenguaje",
    ("Español", "English"))
if option_lang=="Español" :
    lg='es'
if option_lang=="English" :
    lg='en'

def text_to_speech(text, tld,lg):
    
    tts = gTTS(text,lang=lg) # tts = gTTS(text,'en', tld, slow=False)
    try:
        my_file_name = text[0:20]
    except:
        my_file_name = "audio"
    tts.save(f"temp/{my_file_name}.mp3")
    return my_file_name, text


#display_output_text = st.checkbox("Verifica el texto")

if st.button("convertir a Audio"):
     result, output_text = text_to_speech(text, 'com',lg)#'tld
     audio_file = open(f"temp/{result}.mp3", "rb")
     audio_bytes = audio_file.read()
     st.markdown(f"## Tú audio:")
     st.audio(audio_bytes, format="audio/mp3", start_time=0)

     #if display_output_text:
     
     #st.write(f" {output_text}")
    
#if st.button("ElevenLAabs",key=2):
#     from elevenlabs import play
#     from elevenlabs.client import ElevenLabs
#     client = ElevenLabs(api_key="a71bb432d643bbf80986c0cf0970d91a", # Defaults to ELEVEN_API_KEY)
#     audio = client.generate(text=f" {output_text}",voice="Rachel",model="eleven_multilingual_v1")
#     audio_file = open(f"temp/{audio}.mp3", "rb")

     with open(f"temp/{result}.mp3", "rb") as f:
         data = f.read()

     def get_binary_file_downloader_html(bin_file, file_label='File'):
        bin_str = base64.b64encode(data).decode()
        href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
        return href
     st.markdown(get_binary_file_downloader_html("audio.mp3", file_label="Audio File"), unsafe_allow_html=True)

def remove_files(n):
    mp3_files = glob.glob("temp/*mp3")
    if len(mp3_files) != 0:
        now = time.time()
        n_days = n * 86400
        for f in mp3_files:
            if os.stat(f).st_mtime < now - n_days:
                os.remove(f)
                print("Deleted ", f)


remove_files(7)
