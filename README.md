Perfect — thanks, that gives me a clear picture. Here’s a **simple but polished README** draft for your repo:

---

# AI Diet Coach

AI Diet Coach is a personalized nutrition assistant that generates meal plans based on Rutgers University’s daily dining hall menu. It extracts the menu data from **Nutrislice**, parses it into JSON, and uses **Groq’s API with Llama 3.3-70B Versatile** to recommend what to eat for breakfast, lunch, and dinner. The output includes a **full calorie, protein breakdown, and serving sizes** for the day.

---

## Features

* 🍽 **Daily Rutgers Dining Menu Parsing** – pulls menu data from Nutrislice.
* 🤖 **AI-Powered Recommendations** – uses Llama 3.3-70B (via Groq API) for meal plan generation.
* 🔢 **Nutritional Insights** – calculates total calories, protein, and macro breakdown.
* 🥗 **Personalized Suggestions** – provides specific breakfast, lunch, and dinner recommendations.

---

## Tech Stack

* **Python** – backend and parsing logic
* **Groq API** – large language model inference
* **Llama 3.3-70B Versatile** – core reasoning engine
* **JSON** – structured menu data format

---

## Installation

1. Clone the repo:

   ```bash
   git clone https://github.com/1RaghavM/AI-Diet-Coach.git
   cd AI-Diet-Coach
   ```

2. Create a virtual environment (recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Mac/Linux
   .venv\Scripts\activate      # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:

   * `GROQ_API_KEY` = your Groq API key

---

## Usage

Run the script to fetch the daily Rutgers dining hall menu, parse it, and generate an AI-powered meal plan:

```bash
python main.py
```

Example output:

```
**Breakfast**

* 2 BELGIAN WAFFLES (258 calories, 6g protein)
* 2 HARD BOILED EGGS (152 calories, 14g protein)

Total Calories: 410
Total Protein: 20g

**Lunch**

* 6 oz TURKEY BREAST (228 calories, 42g protein)
* 4 oz RED BLISS HOME FRIES (238 calories, 3g protein)
* 2 oz BROCCOLI (38 calories, 4g protein)

Total Calories: 504
Total Protein: 49g

**Dinner**

* 3 oz TURKEY BREAST (228 calories, 42g protein)
* 6 oz OATMEAL (438 calories, 15g protein)
* 2 oz BABY SPINACH (14 calories, 2g protein)

Total Calories: 680
Total Protein: 59g

Total Daily Calories: 2502
Total Daily Protein: 151g
```

---

## Roadmap

* [ ] Fine-tune a model to act more as a specialized Diet Coach instead of using a LLM
* [ ] Allow for User's preferences to be changeable based on their goals of cutting or bulking/find their calorie count and protein intake based on height and weight
* [ ] Add fat and carb breakdown
* [ ] Support multiple universities via Nutrislice
* [ ] Export plans as PDF/CSV
* [ ] Build a simple web UI

---

## License

MIT License – feel free to use and modify.

---

