import streamlit as st

# Set page config
st.set_page_config(
    page_title="🎉 Lucky Draw Prize Claim",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Inject custom CSS to remove top padding + add colorful background
st.markdown("""
    <style>
        /* Remove Streamlit's top padding */
        .block-container {
            padding-top: 1rem;
        }

        /* Fullscreen animated gradient background */
        body {
            background: linear-gradient(-45deg, #ff9a9e, #fad0c4, #fbc2eb, #a1c4fd);
            background-size: 400% 400%;
            animation: gradient 15s ease infinite;
        }
        @keyframes gradient {
            0% {background-position: 0% 50%;}
            50% {background-position: 100% 50%;}
            100% {background-position: 0% 50%;}
        }

        /* Main card styling */
        .main {
            background-color: rgba(255, 255, 255, 0.95);
            padding: 2rem;
            border-radius: 1.5rem;
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
            max-width: 600px;
            margin: 2rem auto;
        }

        h1, h2, h3 {
            text-align: center;
            color: #333;
        }

        .stTextInput input {
            font-size: 1.1rem;
        }

        .stButton button {
            background-color: #ff6f61;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 0.6rem 1.5rem;
            transition: 0.3s;
        }
        .stButton button:hover {
            background-color: #e8574f;
            transform: scale(1.05);
        }
    </style>
""", unsafe_allow_html=True)

# Main container
st.markdown('<div class="main">', unsafe_allow_html=True)

# Title and subtitle
st.title("🎁 Lucky Draw Claim Portal")
st.subheader("✨ Claim your prize by entering your details below")

# Session state to check if already submitted
if "submitted" not in st.session_state:
    st.session_state.submitted = False

# Show form if not submitted
if not st.session_state.submitted:
    with st.form("claim_form"):
        full_name = st.text_input("👤 Full Name")
        phone_number = st.text_input("📞 Phone Number")
        bank_account = st.text_input("🏦 Bank Account Number")
        submit = st.form_submit_button("🎯 Submit Claim")

        if submit:
            if full_name and phone_number and bank_account:
                st.session_state.submitted = True
            else:
                st.warning("🚨 Please complete all fields to proceed.")
else:
    st.success("🎉 You'll receive your prize within 24 hours!")
    st.balloons()

st.markdown("</div>", unsafe_allow_html=True)