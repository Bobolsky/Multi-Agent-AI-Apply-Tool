import streamlit as st
import os
from crewai import Crew, Process
from langchain_openai import ChatOpenAI
from modules.job_description_architect import job_description_architect, analyze_job_description_task
from modules.resume_strategist import resume_strategist, resume_strategy_task
from modules.profiler import profiler, profile_task
from modules.cover_letter_specialist import cover_letter_specialist, generate_cover_letter_task
from modules.interview_prep import interview_preparer, interview_preparation_task

# Configura CrewAI
crew = Crew(
    agents=[
        job_description_architect,
        profiler,
        resume_strategist,
        cover_letter_specialist,
        interview_preparer,
    ],
    tasks=[
        analyze_job_description_task,
        profile_task,
        resume_strategy_task,
        generate_cover_letter_task,
        interview_preparation_task,
    ],
    verbose=True,
    memory=True,
    process=Process.sequential,
    #manager_llm=ChatOpenAI(model="gpt-4o-mini", temperature=0.7),
    full_output=True,
)

# 🌟 Configurazione generale di Streamlit con tema scuro
st.set_page_config(page_title="AI Apply Tool", layout="wide")
# Inizializziamo lo stato della sessione se non esiste
if "resume_strategy_output" not in st.session_state:
    st.session_state.resume_strategy_output = None
if "cover_letter_output" not in st.session_state:
    st.session_state.cover_letter_output = None
if "interview_prep_output" not in st.session_state:
    st.session_state.interview_prep_output = None
# 🌟 Stile CSS personalizzato per i colori e l'animazione
st.markdown(
    """
    <style>
        .stApp {
            background-color: #121212;
            color: white;
        }
        .container {
            background-color: #1E1E1E;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0px 4px 10px rgba(255, 215, 0, 0.2);
            margin-bottom: 20px;
        }
        .stTabs [data-baseweb="tab-list"] {
            display: flex;
            justify-content: center;
            gap: 10px;
        }
        .stTextInput, .stFileUploader, .stButton {
            background-color: #222;
            color: white;
            border-radius: 8px;
        }
        .stButton > button {
            background-color: gold !important;
            color: black !important;
            border-radius: 8px;
            font-weight: bold;
        }
        .stDownloadButton > button {
            background-color: #FFD700 !important;
            color: black !important;
            border-radius: 8px;
        }
        .loading-animation {
            text-align: center;
            font-size: 24px;
            color: #FFD700;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# 🌟 Titolo stilizzato con colori migliorati
st.markdown(
    """
    <h1 style='text-align: center; color: gold; font-size: 42px;'>📄 AI Apply Tool</h1>
    <p style='text-align: center; font-size: 18px; color: white;'>Upload your experiences and provide the job description link to generate optimized outputs.</p>
    """,
    unsafe_allow_html=True,
)

# 🌟 Layout della finestra contenitore
st.markdown("<div class='container'>", unsafe_allow_html=True)
col1, col2 = st.columns(2, gap="large")

# 🔹 **Colonna 1: Input**
with col1:
    st.header("🔍 Input")
    job_link = st.text_input("📌 Job Description Link", placeholder="Paste the job link here...")
    uploaded_file = st.file_uploader("📂 Upload your experiences file (Markdown)", type=["md"])
    generate_button = st.button("🚀 Generate", help="Click to process your resume and generate outputs.")

# 🔹 **Colonna 2: Output**
with col2:
    st.header("📄 Generated Outputs")

    if generate_button:
        if not job_link or not uploaded_file:
            st.error("⚠ Please provide both the job description link and the experiences file.")
        else:
            # Legge il file Markdown
            file_content = uploaded_file.read().decode("utf-8")

            # Input per CrewAI
            inputs = {
                "job_description": job_link,
                "experiences": file_content,
            }

            # Avvio CrewAI con animazione di caricamento
            loading_message = st.empty()  # Creiamo un placeholder per il messaggio

            # Mostriamo il messaggio di caricamento
            loading_message.markdown("<div class='loading-animation'>⏳ Generating files... Please wait.</div>", unsafe_allow_html=True)

            # Esegui CrewAI
            result = crew.kickoff(inputs=inputs)

            # Rimuoviamo il messaggio al termine dell'elaborazione
            loading_message.empty()

            # 📌 Estrazione dei risultati
            for task in result.tasks_output:
                if task.name:
                    if "cover letter generator" == task.name.lower():
                        st.session_state.cover_letter_output = task.raw  
                    elif "interview preparation" in task.name.lower():
                        st.session_state.interview_prep_output = task.raw  
                    elif "resume optimization" in task.name.lower():
                        st.session_state.resume_strategy_output = task.raw

            # 📂 **Tabs con stile migliorato**
            tabs = st.tabs(["📄 Resume", "✉️ Cover Letter", "🎤 Interview Prep"])

            # 📌 Estrazione dei risultati
            cover_letter_output = None
            interview_prep_output = None
            resume_strategy_output = None

            for task in result.tasks_output:
                if task.name:
                    if "cover letter generator" == task.name.lower():
                        cover_letter_output = task.raw  
                    elif "interview preparation" in task.name.lower():
                        interview_prep_output = task.raw  
                    elif "resume optimization" in task.name.lower():
                        resume_strategy_output = task.raw  

            # 🔹 Funzione per adattare l'altezza del text_area al contenuto
            def auto_height(content):
                min_height = 100
                max_height = 400
                lines = content.count("\n") + 1
                height = min(max(min_height, lines * 20), max_height)
                return height

            # 🔹 Tab Resume
            with tabs[0]:
                if st.session_state.resume_strategy_output:
                    st.text_area("📄 Resume Content", st.session_state.resume_strategy_output, height=auto_height(st.session_state.resume_strategy_output))
                    st.download_button("⬇ Download Resume", st.session_state.resume_strategy_output, "resume.md")

            # 🔹 Tab Cover Letter
            with tabs[1]:
                if st.session_state.cover_letter_output:
                    st.text_area("✉️ Cover Letter Content", st.session_state.cover_letter_output, height=auto_height(st.session_state.cover_letter_output))
                    st.download_button("⬇ Download Cover Letter", st.session_state.cover_letter_output, "cover_letter.md")

            # 🔹 Tab Interview Prep
            with tabs[2]:
                if st.session_state.interview_prep_output:
                    st.text_area("🎤 Interview Prep", st.session_state.interview_prep_output, height=auto_height(st.session_state.interview_prep_output))
                    st.download_button("⬇ Download Interview Guide", st.session_state.interview_prep_output, "interview_prep.md")

st.markdown("</div>", unsafe_allow_html=True)
