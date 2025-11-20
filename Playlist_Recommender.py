import streamlit as st
st.set_page_config(page_title="Mood Media Recommender", page_icon='🎬', layout='centered')

st.title("🎶 Mood Based Music Recommender")
st.write("How are you feeling today!! and I'll match your vibe with a playlist!")

selectMood= st.selectbox("How are you feeling now!!",['Happy', 'Sad', 'Lazy & Bored', 'Excited & Motivated', 'Romantic'])

recommendations = {

    "Happy": {
        "music" : "Gallan Goodiyan"

    },

    "Excited & Motivated" : {
        
        "music": "Sultan Title Track"
    },

    "Lazy & Bored" : {
        
        "music": "Channa Mereya"
    },

    "Sad" : {
        
        "music" : "Fix You"
    },

    "Romantic": {
       
        "music" : "Perfect"
    }

}

if selectMood:
    st.subheader(f"🔥 Recommendation for your {selectMood} selectMood")
    st.info(f"🎵 **Music:** {recommendations[selectMood]['music']}")

st.caption("Made with ❤️ using Streamlit")


