from dotenv import load_dotenv
import os
import openai
import json
import pandas as pd

load_dotenv()
api_key = os.getenv("openai_key")
openai.api_key = api_key

def extract_financial_data(text):
    prompt = get_prompt_financial() + text

    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{'role':'user','content':prompt}]

    )

    content = response.choice[0]['message']['content']

    try:
        data = json.loads(content)
        return pd.DataFrame(data.items(),columns=['Measure','Value'])
    except(json.JSONDecodeError,IndexError):
        pass

    return pd.DataFrame({
        "Measure": ["Company Name", "Stock Symbol", "Revenue", "Net Income", "EPS"],
        "Value": ["", "", "", "", ""]
    })


def get_prompt_financial():
    pass