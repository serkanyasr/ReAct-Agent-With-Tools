from langchain.agents import AgentExecutor, create_react_agent, load_tools
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.chat_models import ChatAnthropic
from langchain import hub
from langchain_community.callbacks import StreamlitCallbackHandler
from langchain_community.tools.tavily_search import TavilySearchResults
import streamlit as st
import os
from tools import *
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve API keys from environment variables
my_key_openai = os.getenv("OPENAI_API_KEY")
my_key_google = os.getenv("GOOGLE_AI_API_KEY")
my_key_anthropic = os.getenv("ANTHROPIC_API_KEY")
os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")

# Initialize different LLM models
llm_gemini = ChatGoogleGenerativeAI(google_api_key=my_key_google, model="gemini-2.0-flash")
llm_gpt = ChatOpenAI(api_key=my_key_openai, model="gpt-4-0125-preview", temperature=0, streaming=True)
llm_claude = ChatAnthropic(anthropic_api_key=my_key_anthropic, model_name="claude-2.1")

# Load the prompt template for ReAct agent
agent_prompt = hub.pull("hwchase17/react")

# Function to configure the agent based on user selections
def configure_agent(selected_llm, selected_search_engine, selected_image_generator):
    
    # Select the appropriate LLM model
    if selected_llm == "GPT-4":
        llm = llm_gpt
    elif selected_llm == "Gemini Pro":
        llm = llm_gemini
    elif selected_llm == "Claude":
        llm = llm_claude

    # Get tools for image generation and web scraping
    image_generator_tool = get_tool(selected_image_generator=selected_image_generator)
    web_scraping_tool = get_web_tool()
    
    # Select the search engine tool
    if selected_search_engine == "DuckDuckGo":
        tools = load_tools(["ddg-search"])
        tools.extend([image_generator_tool, web_scraping_tool])
    elif selected_search_engine == "Tavily":
        tools = [TavilySearchResults(max_results=1), image_generator_tool, web_scraping_tool]

    # Create the ReAct agent and executor
    agent = create_react_agent(llm=llm, tools=tools, prompt=agent_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    return agent_executor

# Configure the Streamlit page
st.set_page_config(page_title="ReAct (Reason-Action) Agent")

# Display the banner image and title
st.image(image="img/ai_agent_banner.png")
st.title("ReAct (Reason-Action) Agent")
st.divider()

# Sidebar configuration options
st.sidebar.header("Agent Configuration")
st.sidebar.divider()
selected_llm = st.sidebar.radio(label="Select Language Model", options=["GPT-4", "Gemini Pro", "Claude"])
st.sidebar.divider()
selected_search_engine = st.sidebar.radio(label="Select Search Engine", options=["DuckDuckGo", "Tavily"], index=1)
st.sidebar.divider()
selected_image_generator = st.sidebar.radio(label="Select Image Production Model", options=["Stable Diffusion XL","DALL-E 3"])
st.sidebar.divider()
selected_web_scraper = st.sidebar.radio(label="Select Web Scraping Tool", options=["BeautifulSoup"])
st.sidebar.divider()

# Button to reset chat history
reset_chat_btn = st.sidebar.button(label="Reset Chat History")

# Initialize chat messages session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle user input
if prompt := st.chat_input(placeholder="Write your message"):
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({"role":"user", "content": prompt + " please answer with Turkish"})
    
    with st.chat_message("assistant"):
        st.info("🧠 Chain of Thought in Action...")

        st_callback = StreamlitCallbackHandler(st.container())

        # Configure and execute the agent
        executor = configure_agent(selected_llm=selected_llm, selected_search_engine=selected_search_engine, selected_image_generator=selected_image_generator)
        AI_Response = executor.invoke(
            {"input": st.session_state.messages}, {"callbacks": [st_callback]},
            handle_parsing_errors=True
        )

        # Display AI response
        st.markdown(AI_Response["output"], unsafe_allow_html=True)
        st.session_state.messages.append({"role":"assistant", "content": AI_Response["output"]})

# Handle chat reset
if reset_chat_btn:
    st.session_state.messages = []
    st.toast("Chat history reset!")