import os
import requests


def scrape_linkedin_profile(linkedin_profile_url: str):
    """scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile"""

    # # scrape Linkedin using PROXYCURL
    # api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    # header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}
    #
    # response = requests.get(
    #     api_endpoint, params={"url": linkedin_profile_url}, headers=header_dic
    # )

    # skip looking up actual url and instead respond using a static json
    harrison_chase_json = "https://gist.githubusercontent.com/tusharchandrasingh/7996787bde67cc24b66f6f34d5c24300/raw/5c6e04f2aac13da3b02c7a9065bdd3cffa2845a8/harrison_chase.json"
    response = requests.get(harrison_chase_json)
    print("log: avoiding PROXYCURL for look up", linkedin_profile_url, "and instead return data from", harrison_chase_json)

    # reduce token size by clean up the json
    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data
