
from crewai import Agent, Task
from tools.tool_config import tools_init
from modules.job_description_architect import analyze_job_description_task

tools = tools_init()

interview_preparer = Agent(
    role="Engineering Interview Preparer",
    goal="Create interview questions and talking points "
         "based on the resume and job requirements",
    tools = [tools['serper_tool'], tools['scrape_website_tool'],tools['semantic_search_resume']],
    verbose=True,
    backstory=(
        "Your role is crucial in anticipating the dynamics of "
        "interviews. With your ability to formulate key questions "
        "and talking points, you prepare candidates for success, "
        "ensuring they can confidently address all aspects of the "
        "job they are applying for." 
    ),
    #llm=tools['llm'],
)

interview_preparation_task = Task(
    name="Interview Preparation",
    description=(
        "Crea un insieme di argomenti chiave su cui il candidato sarà interrogato durante il colloquio tecnico."
        "Cerca di includere una piccola to do list delle cose su cui saper parlare in modo da essere preparato."
        "Siccome il candidato avrà poco tempo a disposizione, concentrati sulle competenze e le esperienze più rilevanti."
        "Ad esempio se la posizione richiede esperienza con AWS, chiedi al candidato di preparare un esempio di progetto in cui ha utilizzato AWS e a cosa è servito."
    ),
    expected_output=(
        "Un documento contenente una to do list su cui il candidato sarà interrogato durante il colloquio tecnico."
    ),
    output_file="results/interview_materials.md",
    context=[analyze_job_description_task],
    async_execution=True,
    agent=interview_preparer
)
