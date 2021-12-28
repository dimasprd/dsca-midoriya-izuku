import random
import string

def generate_password(n_token=3):
    """Generate password from words.txt

    Args:
        n_token (int): number of token to be included
            in password. Default is 3.

    Returns:
        str: password
    """
    filename = "words.txt"
    with open(filename, "r") as f:
        word_list = f.read()
    separator = random.sample(string.punctuation, k=n_token)
    tokens = random.sample(word_list, k=n_token)
    tokens = [separator[i] + tokens[i] for i in range(n_token)]
    return "".join(tokens)