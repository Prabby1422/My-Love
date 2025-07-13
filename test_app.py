import requests
import streamlit as st
from streamlit _lottie import st_lottie

#for more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
        return r.json()

# ---- LOAD ASSET ----
lottie_coding = load_lottieurl"https://lottiefiles.com/free-animation/heart-confetti-bbVxVhWsmG"

# ---- HEADER SECTION ----
st.subheader("Hi My love :wave:, I'm your little baby Prabby :kiss:")
st.title("This site I'm creating just to let you know that I love you the most")
st.write("To know how I want you right now [click here](https://www.instagram.com/p/DK_1oCUJLqJ/)"), ("[and click here](https://www.instagram.com/p/DDl0xuVpklW/)")