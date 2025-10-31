# application - internally it will have multiple agents
#Eg: summarize and recommend the stocks of nvidia
# how a chatbot should interact when i put this question
# chatbot will go and contact agents
#1st agent - autonomous ai agent which is doing all the interaction to get the details of the stock
#2nd Agents - try to get some info from the news (web search)
#once we combine all them- all those info interact with the llm and come to the conclusion
#that what are all the recommendations for that stock

from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools

#phi data has lot of integrations with various tools
#Eg: yfinance, news api, web search,youtube, zoom etc
#i can call those tools inside the agent
#i can give parameters like analyse recommendations and more

# web search tool
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.googlesearch import GoogleSearch
from dotenv import load_dotenv
load_dotenv()
import os

os.environ["GROQL_API_KEY"] = os.getenv("GROQ_API_KEY")  # Set GROQ API key from environment variable


#agent first it will hit the Google search tool to get the info from the web
#use the infomation with LLm with the prompt given and it will give the output


#google search tool
search_agent = Agent(
    tools=[GoogleSearch()], # many tools can be added
    model=Groq(id="meta-llama/llama-4-scout-17b-16e-instruct"),#for every agent the backbone is the LLM
    #LLm will be provided some data from the tools that we are using
    description="You are a news agent that helps users find the latest news.",
    instructions=[
        "Given a topic by the user, respond with 4 latest news items about that topic.",
        "Search for 10 news items and select the top 4 unique items."
    ],
    show_tool_calls=True,
    debug_mode=True,
)

##FINANCE agent
finance_agent=Agent(
    name="Finance Agent",
    role="Analyze stock data and provide recommendations",
    model=Groq(id="meta-llama/llama-4-scout-17b-16e-instruct"),
    instructions=[
        "use tables to display the data"],
    show_tool_calls=True,
    markdown=True,debug_mode=True
)


#two independent agents are created
#whenerver we define a workflow, if i combine both of these
#it becomes multimodel agents

multi_ai_agent=Agent(
    team=[search_agent,finance_agent],
    model=Groq(id="meta-llama/llama-4-scout-17b-16e-instruct"),#for every agent the backbone is the LLM
    instructions=["Always include sources for web search",
                  "Use tables to display the data",
                ],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True
)

#activate the multi agent
multi_ai_agent.print_response("summarize analyst recommendations and share the latest news of AAPL",stream=True) 