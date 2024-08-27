import streamlit as st
import os
from dotenv import load_dotenv

# load enviornment variables
load_dotenv()

st.title("Check_pass")

# st.write(st.secrets["API"])
# st.write(os.getenv("API_v"))


# def pass_urls():
#     WEBHOOK_URL = st.secrets.get("WEBHOOK_URL") if "WEBHOOK_URL" in st.secrets else os.getenv("WEBHOOK_URL")
#     W_URL = st.secrets.get("W_URL") if "W_URL" in st.secrets else os.getenv("W_URL")
#     WORK_URL = st.secrets.get("WORK_URL") if "WORK_URL" in st.secrets else os.getenv("WORK_URL")
#     SKILL_URL = st.secrets.get("SKILL_URL") if "SKILL_URL" in st.secrets else os.getenv("SKILL_URL")
#     COMEDY_URL = st.secrets.get("COMEDY_URL") if "COMEDY_URL" in st.secrets else os.getenv("COMEDY_URL")
#     PREDICTION_URL = st.secrets.get("PREDICTION_URL") if "PREDICTION_URL" in st.secrets else os.getenv("PREDICTION_URL")

#     return {
#         "WEBHOOK_URL": WEBHOOK_URL,
#         "W_URL": W_URL,
#         "WORK_URL": WORK_URL,
#         "SKILL_URL": SKILL_URL,
#         "COMEDY_URL": COMEDY_URL,
#         "PREDICTION_URL": PREDICTION_URL
#     }


def API_CALL():
    API = os.getenv("API_L")
    if API is None:
        API = st.secrets["API"]
    return API

def api_call():
    API_1 = os.getenv("URL_1_v") or st.secrets["URL_1"]
    API_2 = os.getenv("URL_2_v") or st.secrets["URL_2"]
    call = {"API_1": API_1, "API_2": API_2}

    return call

call = api_call()

api_1 = call["API_1"]
api_2 = call["API_2"]

st.write(api_1)
st.write(api_2)