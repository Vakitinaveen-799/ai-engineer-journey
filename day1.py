import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

raw_data = """
ravi traders hyd, gst 36AAAAA0000A1Z5, phone 9999999999
SRI LAKSHMI steel - vizag - gst: 37BBBBB1111B1Z6
abc enterprises,chennai,no gst
"""

prompt = f"""Convert these messy vendor rows into a JSON list.
Fields: name (Title Case), city, gst_number (null if missing), phone (null if missing).
Return only JSON.

{raw_data}"""

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=prompt,
)
print(response.text)