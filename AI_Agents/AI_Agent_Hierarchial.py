from crewai import Agent, Task, Crew, Process
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from crewai_tools import SerperDevTool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI


load_dotenv()

# Agents 

# Article writing => Planner, Researcher, Writer, Editor, Proof Reader, Publisher

# Agents => role, goal, backstory 

os.environ["GROQ_API_KEY"] = "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"

os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')


os.environ["GOOGLE_API_KEY"] = "AIzaSyC5ARfKTC8apwldp8pBg8a7FT1ZGo5Tbx4"

os.environ["SERPER_API_KEY"] = "2c2d3fec0ce86b07646fac264273f7135d24036a"

llm = ChatOpenAI(model="gpt-4o-mini")

# llm = ChatGoogleGenerativeAI(model="gemini/gemini-1.5-pro")

# llm = ChatGroq(model="groq/llama3-8b-8192")

planner = Agent(
    role = "Content Planner", 
    goal = "Plan engaging and factually accurate content on {topic}",
    backstory="You are an expert content planner and you are working on planning a blog article",
    verbose = True,
    allow_delegation = True,
    llm = llm,
    max_rpm = 5 
)

researcher = Agent(
    role = "Content Researcher", 
    goal = "Research engaging and factually accurate content on {topic}",
    backstory="You are an expert content researcher and you are working on researching a blog article on the given topic",
    verbose = True,
    allow_delegation = True,
    llm = llm,
    max_rpm = 5,
    tools=[SerperDevTool()]
)

writer = Agent(
    role = "Content writer",
    goal = "Write engaging blog post the given topic {topic}",
    backstory = "You are an expert content writer and you are working on writing a blog article",
    verbose = True,
    allow_delegation=True,
    llm = llm,
    max_rpm = 5
)

editor = Agent(
    role = "Content editor",
    goal = "Edit the content that you recieve from the writer to form a gramatically correct, easy to understand content",
    backstory = "You are an expert content edtor and you are working on editing a blog article",
    verbose = True,
    allow_delegation=True,
    llm = llm,
    max_rpm = 5
)

plan = Task(
    description = "Prioritize the latest trends, key players, noteworthy news on {topic}",
    expected_output = "A comprehensive content plan document",
    agent = planner
)

research = Task(
    description = "Prioritize the latest trends, key players, noteworthy news on {topic}",
    expected_output = "A comprehensive researcher content from the interent",
    agent = researcher,
    # context = [plan]
)


write = Task(
    description = "Prioritize the latest trends, key players, noteworthy news on {topic} while writing engaging article",
    expected_output = "A comprehensive content document which can be understood from the layman point of view",
    agent = writer,
    # context = [research]
)

edit = Task(
    description = "Edit the content recieved from the write task and make it easy to understand",
    expected_output = "A comprehensive content document which does not contain any language jargons, is easy to understand and organised in a proper manner",
    agent = editor,
    # context = [write]
)


crew = Crew(
    agents = [planner, researcher, writer, editor],
    tasks = [plan, research, write, edit],
    verbose = True,
    manager_llm = llm,
    process = Process.hierarchical
)

result = crew.kickoff(inputs = {'topic' : "Rise of Generative AI"})