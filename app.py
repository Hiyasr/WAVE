import streamlit as st
from gtts import gTTS
import io
from tempfile import NamedTemporaryFile

def generate_sound(text, lang='en'):
    """
    Generates audio using gTTS and returns a byte stream.

    Args:
        text (str): The text to convert to audio.
        lang (str, optional): The language for the generated audio. Defaults to 'en'.

    Returns:
        bytes: The audio data as a byte stream.
    """

    tts = gTTS(text=text, lang=lang)
    with NamedTemporaryFile(delete=False) as audio_file:
        tts.write_to_fp(audio_file)
        audio_file.seek(0)
        audio_data = audio_file.read()
    return audio_data

def main():
    st.title("Wave: your words, your voice")
    user_input = st.text_input("Enter text to convert to speech:")
    language = st.selectbox("Select language:", ["en", "es", "fr", "de", "ja"], format_func=lambda x: {
        'en': 'English',
        'es': 'Spanish',
        'fr': 'French',
        'de': 'German',
        'ja': 'Japanese'
    }[x])

    if st.button("Generate Speech"):
        if user_input:
            audio_data = generate_sound(user_input, language)
            st.audio(audio_data, format='audio/mpeg')
        else:
            st.warning("Please enter some text.")

if __name__ == "__main__":
    main()
