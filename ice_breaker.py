
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from agents.twitter_lookup_agent import lookup as twitter_lookup_agent

from third_parties.linkedin import scrape_linkedin_profile
from third_parties.twitter import scrape_user_tweets

from third_parties.tokencounter import num_tokens_from_string

name = "Harrison Chase"
if __name__ == "__main__":
    print("Hello LangChain!")

    # LinkedIn processing
    print("log: looking for linkedin url for ", name)
    linkedin_profile_url = linkedin_lookup_agent(name=name)

    print("log: scraping linkedin url", linkedin_profile_url, "for information ")
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url)
    print("log: scraping linkedin complete")

    # Twitter processing
    print("log: looking for twitter username for ", name)
    # twitter_username = twitter_lookup_agent(name=name)
    # debug
    print(
        "log: Skipping google search for twitter handle, and instead using a hwchase17"
    )
    twitter_username = "hwchase17"

    print("log: scraping twitter for tweets for username", twitter_username)
    tweets = scrape_user_tweets(username=twitter_username, num_tweets=5)
    print(
        "log: using saved tweets instead of using Twitter API; Scraping twitter complete"
    )

    # Summarize using LLM
    summary_template = """
         given Harrison Chase's Linkedin information {linkedin_information} and some tweets {twitter_information} on Harrison Chase, I want you to create:
         1. A short summary with his/her name
         2. Two interesting facts about them
         3. A topic that may interest them
         4. 2 creative Ice breakers to open a conversation with them
     """

    summary_prompt_template = PromptTemplate(
        input_variables=["linkedin_information", "twitter_information"],
        template=summary_template,
    )

    # calculate the number of tokens in the summary template
    # print("log: Summary prompt template is ")
    prompt_summary = summary_prompt_template.format(
        linkedin_information=linkedin_data, twitter_information=tweets
    )
    prompt_token_count = num_tokens_from_string(prompt_summary)
    print(f"Summary prompt template is {prompt_token_count} tokens")

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    print("log: running llm")
    result = chain.run(linkedin_information=linkedin_data, twitter_information=tweets)
    print(result)
    print(f"\nlog: LLM output contains {num_tokens_from_string(result)} tokens")
