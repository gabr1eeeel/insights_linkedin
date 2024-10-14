from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_ollama import ChatOllama
from output_parsers import summary_parser

llm = ChatOllama(temperature=0, model="gemma2:2b")


def get_summary_chain() -> RunnableSequence:
    summary_template = """
        Given the information about a person from LinkedIn: {information}, please create a response that includes:
        1. A brief summary of the person's experience and skills.
        2. Two interesting facts about the person.
        
        Please return the response in Brazilian Portuguese strictly in the following JSON format:
        {{
            "summary": "<Your summary here>",
            "facts": [
                "<Fact 1 here>",
                "<Fact 2 here>"
            ]
        }}
        
        {format_instructions}
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables={
            "format_instructions": summary_parser.get_format_instructions()
        },
    )

    return summary_prompt_template | llm | summary_parser