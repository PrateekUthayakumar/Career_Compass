import streamlit as st
import time
# Assuming ai_matcher and pdf_utils are correctly implemented and available
# from ai_matcher import analyze_job_resume
# from pdf_utils import read_pdf

# --- Mock functions for demonstration (Replace with your actual imports) ---
def read_pdf(file):
    """Mock function to simulate reading a PDF."""
    st.info(f"Successfully processed: {file.name}")
    return "Python, Machine Learning, Deep Learning, Data Analysis, SQL, Communication, Agile, Project Management, Azure"

def analyze_job_resume(job_desc, resume_text):
    """Mock function to simulate AI analysis."""
    # Score logic tied to skills
    score = 8.8  # Higher score for presentation
    matched = ["Python", "Machine Learning", "Data Analysis", "SQL", "Project Management", "Agile"]
    missing = ["GoLang", "Kubernetes", "Microservices Architecture"]
    
    # Simple Keyword Extraction for the new feature
    keywords = ["Python", "Machine Learning", "Azure", "Deep Learning", "SQL", "Agile"]
    
    tip = (
        "**Elite Match Status Confirmed!** You are highly competitive. Your next step should be **Targeted Storytelling**. "
        "During interviews, use the STAR method to describe projects where you utilized your matched skills (Python, ML) "
        "and subtly mention efforts toward the missing skills (e.g., 'We decided against Kubernetes for MVP but I prototyped a setup...')."
    )
    return score, matched, missing, tip, keywords
# --------------------------------------------------------------------------


# -------------------------------------------------
# Page Configuration
# ---------------------------------
st.set_page_config(
    page_title="🚀 AI Career Catalyst",
    page_icon="✨",
    layout="wide"
)

# -------------------------------------------------
# Attractive but Not Too Much (Deep Blue/Cyan Contrast)
# ---------------------------------
st.markdown("""
<style>
/* 1. Base Streamlit Overrides (Deep Blue Dark Mode) */
.stApp {
    background: #111827; /* Deep Slate Blue background */
    color: #e5e7eb; /* Light Gray text */
    font-family: 'Montserrat', sans-serif; /* Attractive Modern Font */
    font-size: 16px; /* Slightly larger base font */
}

/* Subtle Animated Background */
.stApp::before {
    content: '';
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: radial-gradient(circle, rgba(59,130,246,0.03) 1px, transparent 1px); /* Subtle blue glow particles */
    background-size: 30px 30px;
    animation: moveBG 100s linear infinite;
    z-index: -1;
}

@keyframes moveBG {
    0% { background-position: 0 0; }
    100% { background-position: 1000px 1000px; }
}

/* 2. Header/Title (Clean & Prominent) */
h1 {
    color: #3b82f6; /* Medium Blue */
    text-align: center;
    font-size: 3rem; /* Slightly smaller than previous */
    font-weight: 800;
    font-family: 'Montserrat', sans-serif;
    text-shadow: 0 0 5px rgba(59, 130, 246, 0.4); /* Subtle shadow */
    margin-bottom: 1rem;
}

/* Subtitle/Section Titles (Cyan/Teal) */
.section-subtitle {
    font-size: 22px;
    font-weight: 600;
    color: #22d3ee; /* Bright Cyan/Teal */
    margin-top: 25px;
    margin-bottom: 15px;
    border-bottom: 2px solid #374151; /* Subtle divider */
    padding-bottom: 5px;
    font-family: 'Montserrat', sans-serif;
}

/* 3. Primary Content Card */
.stContainer {
    background-color: #1f2937; /* Slightly lighter slate */
    padding: 25px;
    border-radius: 8px;
    margin-top: 10px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.4); /* Clean, standard shadow */
    border: 1px solid #374151;
    transition: all 0.2s ease;
}

.stContainer:hover {
    border-color: #3b82f6; /* Blue highlight on hover */
    box-shadow: 0 6px 15px rgba(0,0,0,0.6);
}

/* 4. Sidebar Revert (Default Left) */
[data-testid="stSidebar"] {
    position: sticky; 
    right: auto;
    left: 0;
    background-color: #1f2937;
    border-right: 1px solid #374151;
}
[data-testid="stAppViewBlockContainer"] {
    margin-right: auto !important; 
}

/* 5. Skill Badges (Clean look with primary color) */
.skill-badge {
    background: #3b82f6; /* Solid Blue */
    color: #ffffff;
    padding: 6px 14px;
    border-radius: 20px;
    margin: 5px;
    font-weight: 600;
    box-shadow: none;
    font-size: 14px;
}

.skill-badge-missing {
    background: #ef4444; /* Soft Red */
    color: #ffffff;
}

/* 6. Tabs Styling */
.stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p{
    color: #e5e7eb; 
    font-weight: 600;
}

.stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {
    border-top: 3px solid #22d3ee !important; /* Cyan active border */
    background-color: #1f2937 !important;
}

/* 7. Action Buttons (Clean Blue Primary) */
.stButton>button {
    background: #3b82f6; /* Solid Blue */
    color: white !important;
    font-size: 16px;
    font-weight: 700;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.4);
}
.stButton>button:hover {
    background: #2563eb; 
    transform: translateY(-1px);
}

/* Score Gauge (Cyan Highlight) */
.score-value {
    color: #22d3ee;
    text-shadow: none;
    font-size: 3.5rem;
    font-weight: 800;
}

/* Plans Button (Removed, CSS placeholder cleanup) */
.plans-link { display: none; }

/* Input Overhaul Styling for Human Look */
.human-subheader {
    font-size: 1.3rem;
    color: #22d3ee;
    font-weight: 700;
    margin-bottom: 5px;
    border-left: 4px solid #3b82f6;
    padding-left: 10px;
    margin-top: 10px;
}
.human-description {
    color: #a1a1aa;
    font-size: 0.95rem;
    margin-bottom: 15px;
}

/* Certification Enrollment UI (New Clean Look) */
.cert-card {
    background-color: #1f2937;
    border: 1px solid #3b82f6;
    border-radius: 8px;
    padding: 15px;
    margin-top: 10px;
    text-align: center;
    box-shadow: 0 4px 8px rgba(0,0,0,0.4);
}
.cert-header {
    color: #22d3ee;
    font-size: 1.2rem;
    font-weight: 700;
    margin-bottom: 10px;
}
.cert-button button {
    background: #10b981 !important; /* Attractive Green/Teal for enrollment */
    color: white !important;
    font-size: 16px;
    font-weight: 700;
    width: 100%;
    margin-top: 15px;
    padding: 10px 0;
    border: none;
    border-radius: 6px;
    transition: background 0.2s ease;
}
.cert-button button:hover {
    background: #059669 !important;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# Application Logic
# -------------------------------------------------

# NOTE: The 'Plans' button section has been removed entirely here.

# Header Section
st.markdown("<h1>AI Career Match Analyzer</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center; font-size:17px; color:#9ca3af; margin-bottom: 25px;'> "
    "Unlocking your profile's optimal placement potential through analytical matching."
    "</p>", 
    unsafe_allow_html=True
)


# ---------------------------------------------
# STEP 1: INPUTS (Order Swapped and Enhanced Text)
# ---------------------------------------------
st.markdown("<div class='section-subtitle'>1. Profile Matcher: Data Input</div>", unsafe_allow_html=True)

col_resume, col_jd = st.columns(2)

# Resume/Profile Input (Left)
resume_text = ""
with col_resume:
    with st.container(border=True):
        st.markdown("<h3 class='human-subheader'>📥 Your Resume/Profile (Source Data)</h3>", unsafe_allow_html=True)
        st.markdown("<p class='human-description'>Provide the comprehensive data representing your skills, experience, and achievements.</p>", unsafe_allow_html=True)
        
        resume_file = st.file_uploader("Upload Resume (PDF Recommended)", type=["pdf"], key="file_uploader")
        
        if resume_file is not None:
            resume_text = read_pdf(resume_file)
            st.info("✅ Profile data successfully processed.")
            st.text_area("Profile Data Preview (Read-Only)", value=resume_text[:400] + "...", height=150, key="resume_preview", disabled=True)
        else:
            resume_text = st.text_area("Or input raw profile text manually", height=200, key="resume_text_input")

# Job Description Input (Right)
with col_jd:
    with st.container(border=True):
        st.markdown("<h3 class='human-subheader'>🎯 Target Job Description (Objective)</h3>", unsafe_allow_html=True)
        st.markdown("<p class='human-description'>Paste the *full* job description here. The AI must ingest all requirements for accurate calibration.</p>", unsafe_allow_html=True)
        job_desc = st.text_area("Paste the Full Job Description here", height=300, key="job_desc_input")


st.markdown("<br>", unsafe_allow_html=True)

# ---------------------------------------------
# STEP 2: ACTION BUTTON
# ---------------------------------------------
if st.button("Run Comprehensive AI Analysis", use_container_width=True):
    if job_desc.strip() == "" or resume_text.strip() == "":
        st.error("❗ **Data Required:** Please input both the Job Description and Profile Data to run the analysis.")
    else:
        with st.status("Analyzing Match Data...", expanded=True) as status:
            st.write("Extracting key entities and job requirements...")
            time.sleep(0.5)
            st.write("Performing Semantic NLP comparison...")
            time.sleep(0.5)
            st.write("Calculating match score and generating recommendations...")
            
            score, matched, missing, tip, keywords = analyze_job_resume(job_desc, resume_text)
            
            status.update(label="✅ Analysis Complete: Report Generated!", state="complete", expanded=False)

        # ---------------------------------------------
        # STEP 3: RESULTS
        # ---------------------------------------------
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<div class='section-subtitle'>2. AI Analysis & Strategy Report</div>", unsafe_allow_html=True)
        
        with st.container(border=True):
            
            col_score, col_status_tip = st.columns([1, 2])
            
            with col_score:
                st.markdown("<div class='score-gauge-container'>", unsafe_allow_html=True)
                st.markdown("<h4 style='color:#3b82f6;'>🎯 Match Confidence Score</h4>", unsafe_allow_html=True)
                st.markdown(f"<div class='score-value'>{score:.1f} / 10</div>", unsafe_allow_html=True)
                st.progress(int(score * 10))
                st.markdown("</div>", unsafe_allow_html=True)
            
            with col_status_tip:
                st.markdown("<h4 style='color:#3b82f6;'>🔥 Current Match Status</h4>", unsafe_allow_html=True)
                if score >= 8.0:
                    st.success(f"**Level: Elite Match** - Exceptional profile alignment. Prepare for interview deployment!")
                elif score >= 6.0:
                    st.warning(f"**Level: Strong Contender** - High potential. Integrate missing keywords to achieve Elite status.")
                else:
                    st.error(f"**Level: Needs Review** - Critical skill gaps detected. Focus on bridging gaps before applying.")
                    
                st.markdown("<h4 style='color:#3b82f6;'>💡 AI Recommendation Strategy</h4>", unsafe_allow_html=True)
                st.info(f"*{tip}*")

            st.markdown("<hr style='border-color:#374151; margin: 25px 0;'>", unsafe_allow_html=True)

            # --- Skill Comparison Map ---
            st.markdown("<h4 style='color:#22d3ee;'>📊 Skill Comparison Map (Keyword Alignment)</h4>", unsafe_allow_html=True)
            
            col_matched, col_missing, col_keywords = st.columns(3)
            
            with col_matched:
                st.subheader("✅ Synced Skills")
                with st.container(height=200, border=True):
                    if matched:
                        for skill in matched:
                            st.markdown(f"<span class='skill-badge'>{skill}</span>", unsafe_allow_html=True)
                    else:
                        st.markdown("*No significant matched key skills found.*", unsafe_allow_html=True)
            
            with col_missing:
                st.subheader("❌ Potential Gaps")
                with st.container(height=200, border=True):
                    if missing:
                        for skill in missing:
                            st.markdown(f"<span class='skill-badge skill-badge-missing'>{skill}</span>", unsafe_allow_html=True)
                    else:
                        st.success("🎉 No critical gaps detected! Full compliance.")
                        
            with col_keywords:
                st.subheader("🔍 Profile Keywords Detected")
                with st.container(height=200, border=True):
                    st.caption("What the AI engine sees in your resume:")
                    if keywords:
                        for keyword in keywords:
                            st.markdown(f"<span class='skill-badge' style='background: #6b7280;'>{keyword}</span>", unsafe_allow_html=True)
                    else:
                        st.warning("Could not extract primary keywords.")


# ---------------------------------------------
# STEP 3: INDUSTRY INSIGHTS & CERTIFICATION CENTER (New Step 3)
# ---------------------------------------------
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<div class='section-subtitle'>3. 🌟 Industry Insights & Certification Center</div>", unsafe_allow_html=True)

col_needs, col_pie, col_studies, col_cert = st.columns(4)

with col_needs:
    st.subheader("Current Industry Needs")
    st.markdown(
        """
        * **Cloud Native:** Expertise in deployment and scaling.
        * **Prompt Engineering:** Optimizing AI/LLM interactions.
        * **Data Governance:** Ethical and secure data management.
        * **Agile/Scrum:** Methodology for fast, iterative development.
        """
    )

with col_pie:
    st.subheader("Required Skill Distribution")
    st.info("A balanced profile is key. Focus on a 60:40 split between technical capability and soft skills.")
    st.markdown(
        """
        * **Hard Skills (60%):** Coding, tools, frameworks, and domain knowledge.
        * **Soft Skills (40%):** Communication, Problem-Solving, Teamwork, and Leadership.
        """
    )
    # --- Diagram Trigger for Skill Distribution Pie Chart ---
    st.markdown("", unsafe_allow_html=True)

with col_studies:
    st.subheader("Trendy Studies for Students")
    st.markdown(
        """
        * **Quantum Computing Basics:** Gaining foundational knowledge.
        * **FinTech & Blockchain:** Understanding decentralized ledger technology.
        * **Bioinformatics:** Applying data science to biological problems.
        * **Serverless Architecture:** Developing apps without managing servers.
        """
    )

with col_cert:
    st.subheader("Boost Your Profile")
    st.markdown("Validate your expertise with a recognized professional certificate.")
    
    # Custom Enrollment Card UI
    st.markdown("""
        <div class="cert-card">
            <div class="cert-header">Validate Your Skills</div>
            <p style='color: #a1a1aa; font-size: 0.9em; margin-bottom: 10px;'>
                Certification is a powerful signal to recruiters for roles with missing skills.
            </p>
            <div class="cert-button">
                <a href="" target="_blank">
                    <button>
                        Explore Official Certifications ↗️
                    </button>
                </a>
            </div>
        </div>
    """, unsafe_allow_html=True)


# ---------------------------------------------
# STEP 4: PLACEMENT STRATEGY HUB (New Step 4)
# ---------------------------------------------
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<div class='section-subtitle'>4. 🌐 Placement Strategy Hub: Market & Skill Deep Dive</div>", unsafe_allow_html=True)

tab_market, tab_interview, tab_resume = st.tabs(["🔥 Trending Market Skills", "🤝 Interview Tactics", "📝 Resume Visual Guide"])

with tab_market:
    st.subheader("Top 5 High-Demand Tech Studies for 2026")
    st.markdown("Unlock skills that recruiters are actively seeking, complete with learning paths.")

    col_data, col_cloud = st.columns(2)

    with col_data:
        st.markdown("##### 1. Modern Data Science Stack")
        st.info("Focus on scalability: Python, PySpark, MLOps, and real-time data streaming.")
        st.markdown("Visualize the MLOps Lifecycle:")
        # --- Diagram Trigger for MLOps Lifecycle ---
        st.markdown("", unsafe_allow_html=True)

    with col_cloud:
        st.markdown("##### 2. Cloud and DevOps Mastery")
        st.info("Master one cloud provider (AWS/Azure/GCP) and container orchestration tools.")
        st.markdown("Essential tools required:")
        # --- Diagram Trigger for Container Orchestration Tools ---
        st.markdown("", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("##### 3. Cybersecurity & AI Integration")
    st.info("Understanding AI-driven threat detection and vulnerability assessment is crucial.")
    
with tab_interview:
    st.subheader("Crack the Interview: Tactical Flowcharts")
    
    col_tech, col_behavioral = st.columns(2)
    
    with col_tech:
        st.markdown("##### Technical Interview (Coding/System Design)")
        st.markdown("Follow this step-by-step method to approach technical problems and ensure clarity.")
        # --- Diagram Trigger for System Design Process ---
        st.markdown("", unsafe_allow_html=True)
        
        
    with col_behavioral:
        st.markdown("##### Behavioral Interview (STAR Method)")
        st.markdown("Use the proven STAR method (Situation, Task, Action, Result) to structure all your answers.")
        # --- Diagram Trigger for STAR Method ---
        st.markdown("", unsafe_allow_html=True)
        

with tab_resume:
    st.subheader("Resume Structure: The 6-Second Rule")
    st.warning("Recruiters spend less than 6 seconds on the first pass. Your structure must be perfect.")
    
    st.markdown("##### Key Structural Elements")
    st.markdown(
        """
        * **Headline/Summary:** 3-4 lines targeted directly at the job description.
        * **Core Competencies:** A visual bullet list of 8-12 hard skills (what the AI matcher checks!).
        * **Experience (Reverse Chronological):** Use quantified achievement bullets (e.g., "Increased X by 20%").
        """
    )
    # --- Diagram Trigger for Resume Structure ---
    st.markdown("", unsafe_allow_html=True)