🎙️ Python Text-to-Speech (TTS) Saver
A lightweight and efficient Python script that converts text into audio files using the pyttsx3 library. 
This tool works completely offline, meaning you don't need an internet connection or external API keys to generate your voiceovers.

🛠️ Key Features
Offline Processing: No cloud services required.
Customizable Speech: Easily adjust speech rate, volume, and voice types.
Direct Export: Saves output directly to a high-quality .mp3 file.

📋 Prerequisites
Before running the script, ensure you have Python installed and the pyttsx3 library:
Bashpip install pyttsx3

[!TIP]Linux users: 
You might need to install the espeak synthesizer for compatibility:
sudo apt-get install espeak

🚀 How to Use
Clone or copy the script to your local machine.
Edit the text variable in the code with the content you want to convert.
Run the script:
python main.py

⚙️ Configuration
You can fine-tune the output by modifying these parameters in the code:
Parameter  Description                               Default Value
Rate       Speed of the speech.                      160
Volume     Loudness level (0.0 to 1.0).              1.0
Voice      Selection of installed system voices.     voices[0].id

Console Output
Once the process is finished, you will see:
✅ Audio saved successfully as 'voz_guardada.mp3'
