from crewai import Crew, Process, LLM
from modules.job_description_architect import job_description_architect, analyze_job_description_task
from modules.resume_strategist import resume_strategist, resume_strategy_task
from modules.profiler import profiler, profile_task
from modules.cover_letter_specialist import cover_letter_specialist, generate_cover_letter_task
from modules.interview_prep import interview_preparer, interview_preparation_task
import os
from tools.tool_config import tools_init


tools = tools_init()
# Configura la crew
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
    
# Avvio del processo
inputs = {
    "job_description": "https://www.linkedin.com/jobs/view/4061517631/?alternateChannel=search&refId=yl83RmbaTBbTiJtd3z1PQg%3D%3D&trackingId=fZGdceiz2xKcZiWLFlMNew%3D%3D",
    "experiences": "fake_experiences.md",
}
result = crew.kickoff(inputs=inputs)

print(result)
