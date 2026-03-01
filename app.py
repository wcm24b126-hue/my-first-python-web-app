import streamlit as st

# 1. Page Configuration: Sets the browser tab title and the favicon (emoji)
st.set_page_config(page_title="Ashan's Web App", page_icon="🚀")

# 2. Header Section: Displays a large title on the page
st.title("Welcome to my first Web App! 🇱🇰")

# 3. Informational Text: Basic text output to tell users about the project
st.write("I built this using Python and the GitHub Student Pack.")

# 4. Input Widgets: These allow users to interact with your app
# st.text_input returns whatever the user types into the box
name = st.text_input("What's your name?", "Guest")

# st.selectbox creates a dropdown menu and returns the selected option
major = st.selectbox("What are you studying?", ["CS", "Engineering", "Business", "Other"])

# 5. Logic & Interactivity: The code inside the 'if' block only runs when the button is clicked
if st.button("Say Hello"):
    # Trigger a fun animation of balloons floating up the screen
    st.balloons()
    
    # Display a green success box with a personalized message
    # We use f-strings (f"...") to inject the 'name' and 'major' variables into the text
    st.success(f"Hello {name}! It's awesome that you're studying {major}!")
    
    # Final call to action text
    st.write("Next step: Let's build something even bigger!")
