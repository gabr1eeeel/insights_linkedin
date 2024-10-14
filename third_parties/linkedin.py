import os
import requests

def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """
    Scrape informations from LinkedIn profiles,
    manually scrape the information from LinkedIn profile.
    """
    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/gabr1eeeel/23c30ef7fd8ddd87cfe86763d082bcae/raw/17b1d165f35cbe013eba840bd232d1223c003c31/cv_data.json"
        response = requests.get(linkedin_profile_url,timeout=10)

    else:
        api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
        header_dictionary = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}
        response = requests.get(
            api_endpoint,
            params={"url", linkedin_profile_url},
            headers=header_dictionary,
            timeout=10
        )

    data = response.json()

    return data