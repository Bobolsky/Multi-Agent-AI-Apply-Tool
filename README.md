# Multi-Agent-AI-Apply-Tool
Tailor your job application with AI. Upload your resume, provide a job description, and let AI optimize your resume, create a cover letter to perfectly match the role and guide you through a technical interview.
# **AI Apply Tool** 🧠📄  
### 🚀 AI-powered Resume & Cover Letter Generator  

**AI Apply Tool** is an intelligent multi-agent system that optimize your resume, creates a cover letter to perfectly match the role and guides you through a technical interview.  
Simply **upload your resume**, **provide a job description URL**, and let AI handle the rest.  

---

## **📌 Features**
✅ **Job Description Analysis** → Extracts key job requirements to optimize your resume.  
✅ **Resume Optimization** → Highlights the most relevant experience and skills.  
✅ **Cover Letter Generation** → Creates a tailored, ATS-friendly cover letter.  
✅ **Interview Preparation** → Generates AI-driven interview tips based on the job description.  
✅ **Quality Assurance (QA) Check** → Ensures there are **no placeholders** or missing details.  
✅ **Modern Streamlit UI** → **Dark mode, gold accents, smooth animations**.  
✅ **Live Preview & Download** → View and download your documents directly from the UI.  

---

## **🛠 AI Agents Overview**
The **AI Apply Tool** is powered by **CrewAI**, a multi-agent system where each agent is specialized in a specific task.

### **1️⃣ Job Description Architect 🏗️**
- **Role**: Extracts key information from the job description.  
- **Goal**: Identify the most important **skills, experience, and qualifications** required for the job.  
- **Output**: A structured job summary with essential insights for resume optimization.

### **2️⃣ Profiler Agent 🔍**
- **Role**: Analyzes the candidate's resume to create a **detailed profile**.  
- **Goal**: Extract work experience, education, projects, and key skills.  
- **Output**: A structured **profile document** used for resume tailoring.

### **3️⃣ Resume Strategist 📝**
- **Role**: Optimizes the candidate’s resume based on the job description.  
- **Goal**: Highlight only the **most relevant** experience, skills, and projects.  
- **Rules**:
  - **No placeholders** or fake information.  
  - Must fit **on a single page** (ATS-friendly).  
  - Uses **real data** from the candidate profile.  
- **Output**: A **one-page, structured resume** in **Markdown format**.

### **4️⃣ Cover Letter Specialist ✉️**
- **Role**: Generates a personalized cover letter.  
- **Goal**: Align the candidate’s experience with job requirements.  
- **Rules**:
  - **No placeholders** (e.g., `[Company Name]`, `[Address]`).  
  - Uses **only real** candidate information.  
  - Must be **clear, concise, and impactful**.  
- **Output**: A **professionally structured cover letter** in **Markdown format**.

### **5️⃣ Interview Preparation Agent 🎤**
- **Role**: Creates a **custom interview guide** based on the job description.  
- **Goal**: Identify key **questions**, **expected responses**, and **talking points**.  
- **Output**: An **interview prep document** with AI-generated tips.

---

## **How to Run**
First you will have to install al the dependencies for the CrewAI Tool by running 

## **Demo**


https://github.com/user-attachments/assets/954ef50f-cf8f-4a7d-8354-b5dab3637cd4



## **Roadmap**
- [] PDF Output Generation
- [] Custom Resume Templates
- [] API Integration for job platforms (Linkedin, Indeed, etc)
