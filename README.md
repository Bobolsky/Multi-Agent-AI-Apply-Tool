
# **AI Apply Tool** 🧠📄  

AI Apply Tool is an intelligent multi-agent system designed to craft the perfect resume and cover letter tailored to your target job. It also guides you through technical interview preparation with a structured to-do list.
Simply upload your resume, provide a job description URL, and let AI take care of the rest! 🚀

---

## **📌 Features**
✅ **Smart Job Description Analysis**  
- Extracts key job requirements and identifies critical skills, experience, and qualifications needed for the role.  

✅ **AI-Powered Resume Generation**  
- Dynamically tailors your resume to match the job description.  
- Selects only the most relevant experiences and projects to fit on a single page (ATS-friendly format).

✅ **Personalized Cover Letter Generation**  
- Crafts a compelling, tailored cover letter that highlights your strengths.  
- Ensures no placeholders or irrelevant information—only real, impactful content.

✅ **AI-Driven Interview Preparation**  
- Generates a structured list of key topics and concepts you should master.  
- Focuses on technical interview questions related to the job role.

✅ **Live Preview, Edit & Download**  
- Instantly preview your Resume, Cover Letter, and Interview Guide in a tabbed UI.  
- Edit directly from the interface before downloading your final application documents.

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
- **Role**: Creates the candidate’s resume based on the job description and his profile.  
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

```bash
pip install crewai[tools]
```

## **Demo**



https://github.com/user-attachments/assets/cd1f4fb7-e784-4a46-aaa0-ce55e272b4e8






## 🎯 **Roadmap**
- [ ] PDF Output Generation
- [ ] Custom Resume Templates
- [ ] API Integration for job platforms (Linkedin, Indeed, etc)
