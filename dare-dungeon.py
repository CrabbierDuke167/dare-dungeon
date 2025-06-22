import streamlit as st
import time
import random

st.set_page_config(page_title="Dare Dungeon", layout="centered")
st.divider()

st.title("Dare Dungeon")
st.caption("""✅dare dungeon is a game where u will get a random dare to accomplish;
best way to kill your boredom""")
st.divider()

dares = [
    "Sing the chorus of your favorite song out loud.",
    "Do 10 jumping jacks right now.",
    "Try to touch your nose with your tongue.",
    "Say the alphabet backward as fast as you can.",
    "Send a funny selfie to your best friend.",
    "Talk in a cartoon voice for the next 1 minute.",
    "Do your best dance move for 30 seconds.",
    "Text someone: 'Guess what? I just ate a lemon... whole!'",
    "Try to juggle with 3 soft things around you.",
    "Draw a quick self-portrait with your non-dominant hand."
]

gif_slot = st.empty()

with st.form("dare_form"):
    st.caption("Click the button below to get a random dare")
    submitted = st.form_submit_button("Reveal the Dare")

if submitted:
    gif_slot.image("https://i.ibb.co/W4DStV0W/icegif-1268.gif", caption="Wait for it...")
    time.sleep(2.5)
    gif_slot.empty()

    selected_dare = random.choice(dares) 
    st.success(f"🔥 Dare: {selected_dare}")
else:
    st.info("Clik the button to reveal the dare :)")