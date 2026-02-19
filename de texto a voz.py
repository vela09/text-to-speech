import pyttsx3

engine = pyttsx3.init()

# Texto a convertir
texto = " "

engine.setProperty('rate', 160)     
engine.setProperty('volume', 1.0)  
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  
nombre_archivo = "voz_guardada.mp3"
engine.save_to_file(texto, nombre_archivo)
engine.runAndWait()
print(f"✅ Audio guardado correctamente como '{nombre_archivo}'")