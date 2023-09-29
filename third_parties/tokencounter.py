import tiktoken


def num_tokens_from_string(string: str, encoding_name="gpt-3.5-turbo") -> int:
    encoding = tiktoken.encoding_for_model(encoding_name)
    token_count = len(encoding.encode(string))
    return token_count


# # Debug
# if __name__ == "__main__":
#     text = "This is an example sentence to count tokens."
#     print(f"The text contains {num_tokens_from_string(text)} tokens.")
