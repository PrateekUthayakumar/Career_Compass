import streamlit as st

# --- Page Configuration for Certification Page ---
st.set_page_config(
    page_title="Enroll - AI Career Catalyst",
    page_icon="🎓",
    layout="wide"
)

# --- Custom CSS for this specific page ---
st.markdown("""
<style>
/* Header/Title */
h1 {
    color: #32cd32; /* Lime Green for enrollment focus */
    text-align: center;
    font-size: 3.5rem;
    font-weight: 900;
    text-shadow: 0 0 10px rgba(50,205,50,0.5);
    margin-bottom: 0.5rem;
}

/* Card Styling */
.enrollment-card {
    background-color: #1a1a1a;
    padding: 35px;
    border-radius: 15px;
    margin: 30px auto;
    max-width: 800px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.7);
    border-left: 5px solid #32cd32; /* Green highlight */
}

/* Success Button (Payment/Action) */
.primary-action-button button {
    background: linear-gradient(135deg, #32cd32, #008000);
    color: white;
    font-size: 20px;
    font-weight: 700;
    padding: 15px 40px;
    border-radius: 15px;
    border: none;
    box-shadow: 0 10px 30px rgba(50,205,50,0.5);
    width: 100%;
    transition: all 0.3s ease;
}

.primary-action-button button:hover {
    transform: translateY(-2px);
    box-shadow: 0 15px 45px rgba(50,205,50,0.7);
}
</style>
""", unsafe_allow_html=True)


# --- Page Content ---
st.markdown("<h1>🎓 Professional Certification Enrollment</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center; font-size:18px; color:#aaa;'> "
    "Validate your expertise in **AI-Driven Career Strategy**."
    "</p>", 
    unsafe_allow_html=True
)

st.markdown("<div class='enrollment-card'>", unsafe_allow_html=True)

st.subheader("Certificate Program Details")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### **Course:** Advanced AI Match Strategy")
    st.markdown("**Duration:** 4 Weeks (Self-Paced)")
    st.markdown("**Modules:** 12 Core Modules & Final Assessment")
    st.markdown("**Format:** Video Lectures, Interactive Quizzes, Capstone Project.")
    st.markdown("---")
    st.metric(label="Total Price (Limited Offer)", value="USD 149", delta="-50% Discount")

with col2:
    st.subheader("Key Takeaways:")
    st.markdown("""
    * **Master AI Tools:** Learn to use generative AI for resume tailoring.
    * **NLP Keyword Optimization:** Deep dive into how ATS systems score resumes.
    * **Strategic Interview Prep:** Develop advanced behavioral and technical response frameworks.
    * **Lifetime Access:** Access to all course materials and future updates.
    """)

st.markdown("<br>", unsafe_allow_html=True)

st.header("Enrollment Form")
with st.form(key='enrollment_form'):
    full_name = st.text_input("Full Name (as it should appear on certificate)", key="cert_name")
    email = st.text_input("Email Address", key="cert_email")
    st.checkbox("I agree to the Terms and Conditions.", key="cert_terms")
    
    # Use a standard Streamlit button inside a container for styling
    submitted = st.form_submit_button(
        label="Complete Enrollment & Pay Now",
        use_container_width=True,
        type="primary"
    )

    if submitted:
        if full_name and email:
            st.success(f"Thank you, {full_name}! Redirecting you to the secure payment gateway...")
            # In a real app, this would redirect to a payment URL
        else:
            st.error("Please fill in your name and email address.")

st.markdown("</div>", unsafe_allow_html=True)

# Link back to the main app (assuming your main app is named 'app.py' or similar)
st.markdown("<br>", unsafe_allow_html=True)
st.page_link("app.py", label="⬅️ Return to AI Matcher", icon="🏠")