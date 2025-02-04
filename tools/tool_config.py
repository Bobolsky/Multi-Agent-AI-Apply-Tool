from crewai import Agent, Task, Crew,Process, LLM
from crewai_tools import (
    DirectoryReadTool,
    FileReadTool,
    SerperDevTool,
    WebsiteSearchTool,
    ScrapeWebsiteTool,
    JSONSearchTool,
    MDXSearchTool

)
from crewai_tools.tools.pdf_search_tool.pdf_search_tool import PDFSearchTool
from langchain_ollama import OllamaEmbeddings
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")
from huggingface_hub import HfApi


# Configura strumenti
serper_tool = SerperDevTool()
scrape_website_tool = ScrapeWebsiteTool()
semantic_search_resume = MDXSearchTool()
read_resume = FileReadTool()


def tools_init():
    tools = {
        "serper_tool": serper_tool,
        "scrape_website_tool": scrape_website_tool,
        "semantic_search_resume": semantic_search_resume,
        "read_resume": read_resume
    }
    return tools