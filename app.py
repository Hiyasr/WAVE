import streamlit as st
from gtts import gTTS
import os

def generate_sound(text):
    # Generate audio using gTTS
    tts = gTTS(text=text, lang='en')
    tts.save("generated_sound.mp3")
    return "generated_sound.mp3"

def main():
    st.title("Wave: AI Sound Generator")
    user_input = st.text_input("Enter text to generate sound:")

    if st.button("Generate Sound"):
        if user_input:
            audio_file = generate_sound(user_input)
            st.audio(audio_file)  # Play the generated audio
        else:
            st.warning("Please enter some text!")

if __name__ == "__main__":
    main()
