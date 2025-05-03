import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post

# Set up Streamlit page
st.set_page_config(page_title="LinkedIn Post Generator", page_icon="🔗", layout="centered")

# Dropdown options
length_options = ["Short ✨", "Medium 📄", "Long 📜"]
language_options = ["English 🇬🇧", "Hinglish 🇮🇳"]

# Custom CSS for styling
st.markdown("""
    <style>
        .main-title {
            font-size: 36px;
            color: #0A66C2;
            text-align: center;
            font-weight: 700;
            margin-bottom: 10px;
        }

        .subtitle {
            font-size: 18px;
            color: #555;
            text-align: center;
            margin-bottom: 30px;
        }

        .stSelectbox > label {
            font-weight: bold;
            color: #333;
        }

        .stButton>button {
            background-color: #0A66C2;
            color: white;
            border: none;
            border-radius: 10px;
            padding: 0.6em 1.2em;
            font-weight: 600;
            transition: 0.3s ease;
        }

        .stButton>button:hover {
            background-color: #084d99;
            transform: scale(1.02);
        }

        .post-box {
            background-color: #F3F2EF;
            padding: 1.5em;
            border-radius: 10px;
            color: #333;
            font-size: 17px;
            line-height: 1.6;
            margin-top: 20px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }

        .emoji-label {
            font-size: 18px;
            margin-bottom: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Main app logic
def main():
    st.markdown('<div class="main-title">🔗 LinkedIn Post Generator</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Generate engaging, professional posts in seconds!</div>', unsafe_allow_html=True)

    # Input fields in three columns
    col1, col2, col3 = st.columns(3)
    fs = FewShotPosts()
    tags = fs.get_tags()

    with col1:
        st.markdown('<div class="emoji-label">📌 Choose a Topic</div>', unsafe_allow_html=True)
        selected_tag = st.selectbox("", options=tags)

    with col2:
        st.markdown('<div class="emoji-label">📝 Select Length</div>', unsafe_allow_html=True)
        selected_length = st.selectbox("", options=length_options)

    with col3:
        st.markdown('<div class="emoji-label">🌍 Choose Language</div>', unsafe_allow_html=True)
        selected_language = st.selectbox("", options=language_options)

    # Generate button
    if st.button("🚀 Generate Post"):
        post = generate_post(selected_length.split()[0], selected_language.split()[0], selected_tag)
        st.success("✨ Here's your LinkedIn post!")
        st.markdown(f"<div class='post-box'>{post}</div>", unsafe_allow_html=True)

# Run app
if __name__ == "__main__":
    main()
