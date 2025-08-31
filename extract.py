import requests
import json
import datetime

date = datetime.date.today().strftime("%Y/%m/%d")
print(date)
api_url = f"https://rutgers.api.nutrislice.com/menu/api/weeks/school/busch-dining-hall/menu-type/breakfast/{date}/"

response = requests.get(api_url)
data = response.json()

menus_by_day = {}

for day in data.get("days", []):
    date = day.get("date")
    items = day.get("menu_items", [])
    categories = []
    current_category = None
    
    for item in items:
        if item.get("is_section_title") or item.get("is_station_header"):
            current_category = {
                "category": item.get("text", "Uncategorized"),
                "foods": []
            }
            categories.append(current_category)
        elif item.get("food"):
            food = item["food"]
            food_entry = {
                "name": food.get("name"),
                "description": food.get("description", ""),
                "nutrition": food.get("rounded_nutrition_info", {}),
                "serving_size": food.get("serving_size_info", {}),
            }
            if current_category is None:
                current_category = {"category": "Uncategorized", "foods": []}
                categories.append(current_category)
            current_category["foods"].append(food_entry)
    
    menus_by_day[date] = categories


with open("parsed_daily_menus.json", "w") as f:
    json.dump(menus_by_day, f, indent=2)