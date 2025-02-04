from crewai import Agent, Task
from tools.tool_config import tools_init
import modules.job_description_architect as jda
import modules.profiler as pr

tools = tools_init()

# Definizione dell'agente
cover_letter_specialist = Agent(
    role="Cover Letter Specialist",
    goal=(
        "Creare una cover letter personalizzata analizzando una job description, "
        "il percorso accademico e le esperienze dell'utente, evidenziando le competenze rilevanti."
    ),
    backstory=(
        "Un esperto nella scrittura di lettere di presentazione efficaci e persuasive. "
        "Specializzato nel collegare esperienze professionali e accademiche alle esigenze delle aziende."
    ),
    tools=[tools['semantic_search_resume']],  
)


generate_cover_letter_task = Task(
    name="Cover Letter Generator",
    description=(
        "Utilizza la job description fornita e il riassunto delle informazioni del candidato ottenute dai task precedenti "
        "per creare una cover letter personalizzata. "
        "La lettera deve mettere in evidenza come le esperienze e le competenze dell'utente siano allineate con i requisiti del ruolo. "
        "Se un'informazione non è disponibile, OMETTILA DEL TUTTO invece di inserire un placeholder. "
        "Non scrivere segnaposti come [Address], [City, State, Zip Code] o altri placeholder generici. "
        "Assicurati che la cover letter sia pronta per essere inviata, con le informazioni reali disponibili. "
        "Se il nome del candidato non è specificato, inizia direttamente con 'Dear Hiring Manager,'. "
    ),
    expected_output=(
        "Una cover letter persuasiva in formato markdown, pronta per essere inviata. "
        "Include solo informazioni disponibili e reali. "
        "NON inserire placeholder o segnaposti di alcun tipo."
    ),
    context=[jda.analyze_job_description_task, pr.profile_task],
    agent=cover_letter_specialist,
)

