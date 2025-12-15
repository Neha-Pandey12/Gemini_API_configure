import os
from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv()
gemini_API_KEY=os.getenv("Gemini_API_key")
genai.configure(api_key=gemini_API_KEY)
gemini_model=genai.GenerativeModel("gemini-2.5-flash")
gemini_response=gemini_model.generate_content("Example 1:English:\"hello\" Nepali:\"Namaste\" Example 2: English:\"Good Morning\" Nepali:\"Subha Prabhat\" Now transalte this: English:\"Book\" Nepali:\"")  
print("Gemini Output:- \n",gemini_response.text)
# kena xi Prinnce Push vel ki nai
print("hello Ranjan")