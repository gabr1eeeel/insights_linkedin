import os
from typing import Tuple
from output_parsers import Summary
from chains.custom_chains import get_summary_chain
from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from dotenv import load_dotenv

load_dotenv()

def insights_linkedin(name: str) -> Tuple[Summary, str]:
    mock = os.environ.get("MOCK")
    linkedin_url = linkedin_lookup_agent(name=name, mock=mock)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_url, mock=mock)

    summary_chain = get_summary_chain()
    summary_and_facts: Summary = summary_chain.invoke(
        input={"information": linkedin_data},
    )

    profile_pic_url = linkedin_data.get('main', {}).get('aboutImage') if mock else linkedin_data.get("profile_pic_url")

    return (
        summary_and_facts,  profile_pic_url
    )