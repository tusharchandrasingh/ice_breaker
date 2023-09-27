# todo: review the tweets stub is for Harrison Chase and
# todo: refactor removing the debug code sections 

from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from agents.twitter_lookup_agent import lookup as twitter_lookup_agent

from third_parties.linkedin import scrape_linkedin_profile
from third_parties.twitter import scrape_user_tweets

name = "Harrison Chase"
if __name__ == "__main__":
    print("Hello LangChain!")

    # LinkedIn processing
    print("log: looking for linkedin url for ", name)
    linkedin_profile_url = linkedin_lookup_agent(name=name)

    print("log: scraping linkedin url", linkedin_profile_url, "for information ")
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url)
    print("log: scraping linkedin complete, linkedin data retrieved is \n", linkedin_data)

    # Twitter processing
    print("log: looking for twitter username for ", name)
    # twitter_username = twitter_lookup_agent(name=name)
    # debug
    twitter_username = 'hwchase17'

    print("log: scraping twitter for tweets for username", twitter_username)
    tweets = scrape_user_tweets(username=twitter_username, num_tweets = 5)
    print("log: scraping twitter complete, tweets retrieved is \n", tweets)

    # Summarize using LLM
    summary_template = """
         given a person's Linkedin information {linkedin_information} and some tweets {twitter_information} on him/her, I want you to create:
         1. A short summary
         2. Two interesting facts about them
         3. A topic that may interest them
         4. 2 creative Ice breakers to open a conversation with them
     """
    summary_prompt_template = PromptTemplate(
        input_variables=["linkedin_information", "twitter_information"],
        template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    print("log: running llm")
    print(chain.run(linkedin_information=linkedin_data, twitter_information=tweets))
