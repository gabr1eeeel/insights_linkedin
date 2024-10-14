from langchain import hub
from langchain_ollama import ChatOllama
from langchain.agents import (create_react_agent, AgentExecutor)
from langchain_core.tools import Tool
from langchain_core.prompts import PromptTemplate
from tools.tools import get_profile_url_tavily

def lookup(name: str, mock: bool = False) -> str:

    linked_profile_url = None
    
    if mock:
        linked_profile_url = "https://linkedin.com/in/gabr1eeeel"
    else:
        llm = ChatOllama(
            temperature=0,
            model="tinyllama")
        
        template = """
        Given the full name {name_of_person}.
        I want you to get it me a link to their Linkedin profile page.
        Your answer should contain only a unique URL
        """

        prompt_template = PromptTemplate(
            template=template, input_variables=["name_of_person"]
        )
        tools_for_agent = [
            Tool(
                name="Crawl Google for linkedin profile page",
                func=get_profile_url_tavily,
                description="useful for when you need get the Linkedin Page URL",
            )
        ]

        react_prompt = hub.pull("hwchase17/react")
        agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
        agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

        result = agent_executor.invoke(
            input={"input": prompt_template.format_prompt(name_of_person=name)}
        )

        linked_profile_url = result["output"]
    
    return linked_profile_url