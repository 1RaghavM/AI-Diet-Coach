from dotenv import load_dotenv
from groq import Groq
import json, requests, datetime, os

load_dotenv()

client = Groq(
    # This is the default and can be omitted
    api_key=os.getenv("GROQ_API_KEY"),
)

with open("parsed_daily_menus.json", "r") as f:
    data = json.load(f)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a nutrition-savvy Rutgers dining hall coach. Create a meal plan with exactly 3 meals: breakfast, lunch, and dinner. Use ONLY the exact item names from the provided menu data. From the JSON, pull the menu and create a full plan, with total claorie counts, protein intake. 2500 calories and 150g of protein. Make sure to make a full plan of what to eat, and for each meal give explanation why. For meats, only use chicken."
        },
        {
            "role": "user",
            "content": f"Create a meal plan with exactly 3 meals from this menu {data}. Make sure to include breakfast, lunch, and dinner. Use ONLY the exact item names from the provided menu data.",
        }
    ],
    model="llama-3.3-70b-versatile",
)

print(chat_completion.choices[0].message.content)
