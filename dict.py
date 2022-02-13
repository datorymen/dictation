import pyttsx3
import streamlit as st

# engine = pyttsx3.init()
# engine.say("Good")
# engine.runAndWait()

# voices = engine.getProperty("voices")
# for item in voices:
#     print(item.id, item.languages)

if st.button('开始'):
    text_book = ['你今天吃過飯了嗎？', '跳蚤市場', '散心']
    engine = pyttsx3.init()
    engine.setProperty("voice", "com.apple.speech.synthesis.voice.tingting")
    engine.say(text_book[1])
    engine.runAndWait()

