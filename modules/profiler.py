from crewai import Agent, Task
from tools.tool_config import tools_init

tools = tools_init()

profiler = Agent(
    role="Personal Profiler for Engineers",
    goal="Do increditble research on job applicants "
         "to help them stand out in the job market",
    tools = [tools['semantic_search_resume']],
    verbose=False,
    backstory=(
        "Equipped with analytical prowess, you dissect "
        "and synthesize information "
        "from diverse sources to craft comprehensive "
        "personal and professional profiles, laying the "
        "groundwork for personalized resume enhancements."
    ),
    #llm=tools['llm'],
)

profile_task = Task(
    description=(
        "Compile a detailed personal and professional profile "
        "using the file ({experiences}) containing the past experiences "
        "of the candidate. Utilize tools to extract and "
        "describe all the experiences, projects, skills and achievements. Also includes information such as name, mail, phone number. That will be used later on together with the job description to create a tailored resume."
    ),
    expected_output=(
        "A comprehensive profile document that includes personal information, skills, work experiences, "
        "project experiences, contributions, interests, and "
        "communication style. "
    ),
    agent=profiler,
    async_execution=True
)