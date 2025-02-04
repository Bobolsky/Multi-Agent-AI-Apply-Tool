from crewai import Agent, Task
from tools.tool_config import tools_init
import modules.job_description_architect as jda
import modules.profiler as pr

tools = tools_init()

# 🔹 Definizione dell'agente Resume Strategist
resume_strategist = Agent(
    role="Resume Strategist for Engineers",
    goal=(
        "Optimize and tailor a candidate’s resume to perfectly match a specific job posting, "
        "ensuring it stands out by emphasizing the most relevant skills and experiences."
    ),
    verbose=True,
    backstory=(
        "As an expert in resume optimization, you specialize in strategically refining resumes "
        "to ensure they align with job requirements. You have a deep understanding of industry trends, "
        "applicant tracking systems (ATS), and what hiring managers look for in a candidate's profile."
    ),
    tools=[tools['read_resume']],  # Aggiunto un tool utile per selezionare i migliori progetti/esperienze
)

# 🔹 Task per generare un resume perfettamente adattato alla Job Description
resume_strategy_task = Task(
    name="Resume Optimization",
    description=(
        "Using the candidate’s profile obtained from the Profiler Agent and the job requirements analyzed earlier, "
        "generate a **one-page resume** that highlights the most relevant aspects of the candidate’s experience. "
        "The resume must be structured and formatted professionally, ensuring that it is tailored to the job posting."
        
        "✅ **Key Guidelines:**\n"
        "- Only use **real information** from the candidate's profile; do **not** invent details.\n"
        "- **No placeholders** should be included (e.g., avoid '[Company Name]' or '[Job Title]').\n"
        "- Prioritize and **select only the most relevant experiences and projects** that align with the job.\n"
        "- Ensure the **resume fits within one page** while maintaining readability and clarity.\n"
        "- Highlight skills that are explicitly mentioned in the **job description** and are present in the candidate’s profile.\n"
        
        "✅ **Resume Sections (in this order):**\n"
        "1️⃣ **Professional Summary** (1-2 sentences summarizing key strengths and experience)\n"
        "2️⃣ **Experience** (only the most relevant positions, focusing on achievements related to the job post)\n"
        "3️⃣ **Projects** (highlight projects that demonstrate the required skills for the role)\n"
        "4️⃣ **Education** (list degrees/certifications, prioritize those relevant to the job post)\n"
        "5️⃣ **Skills** (focus on hard skills and tools relevant to the position)"
        
        "⚠️ **Rules:**\n"
        "- **Do NOT fabricate information**—only use existing details.\n"
        "- **Ensure ATS optimization** by using keywords from the job description.\n"
        "- **Keep the format concise and professional**—avoid unnecessary details."
    ),
    expected_output=(
        "A **professionally formatted one-page resume** (Markdown format) that:\n"
        "- Contains **only the most relevant details** for the job post.\n"
        "- Has **no placeholders or fabricated data**.\n"
        "- Follows a clear and structured format.\n"
    ),
    context=[jda.analyze_job_description_task, pr.profile_task],
    agent=resume_strategist,
)
