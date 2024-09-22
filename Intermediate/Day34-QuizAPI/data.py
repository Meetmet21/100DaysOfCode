import requests


def get_random_questions(amount):
    """
    Get N randorm questions from TRIVIA DB, setting a session to avoid same question to get drawn.

    :param amount: number of question to be retrieved.
    :return: A dictionary containing random questions
    """
    # API URL
    URL = "https://opentdb.com/api.php"
    # Params
    params = {
        "amount": amount,
        "type": "boolean",
    }
    # Send request to TRIVIA db
    response = requests.get(url=URL, params=params)
    response.raise_for_status()
    # Fetch data
    data = response.json()

    # Check response status
    if data["response_code"] == 0:
        return data["results"]
    else:
        raise Exception(f"The non-zero response status {data["response_code"]} was return from API request.")

# DB
question_data = get_random_questions(10)