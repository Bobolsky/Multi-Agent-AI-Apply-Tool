from crewai import Agent, Task
from tools.tool_config import tools_init


tools = tools_init()

job_description_architect = Agent(
    role="Job Role Analyst",
    goal="Analizzare le job description fornite e identificare competenze chiave, skills e requisiti richiesti per il ruolo.",
    backstory=(
        "Sei un esperto nella lettura e analisi di job description." 
        "La tua missione è aiutare gli utenti a comprendere a fondo i requisiti" 
        "di una posizione lavorativa e fornire informazioni dettagliate per adattare i loro profili professionali di conseguenza."
    ),
    tools=[tools['serper_tool'], tools['scrape_website_tool']],
)

analyze_job_description_task = Task(
    description=(
    "Leggi la job description disponibile all'URL {job_description} e identifica:"
    "1 Le informazioni di base che serviranno per la cover letter."
    "2 Le competenze chiave richieste"
    "3 Le skills richieste (soft e hard skills)"
    "4 Eventuali requisiti obbligatori o preferenziali."

    "Fornisci un output ben organizzato che includa queste categorie in una struttura chiara."
    ),
    expected_output=(
    "Un report strutturato con le seguenti sezioni:"
    "1. **Informazioni di base**"
    "2. **Competenze chiave**"
    "3. **Skills richieste**"
    "4. **Requisiti obbligatori**"
    "5. **Requisiti preferenziali**"
    
    "Ogni sezione deve contenere un elenco dettagliato basato sul contenuto della job description."
    ),
    verbose=False,
    async_execution=True,
    agent=job_description_architect,
)