from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os


load_dotenv()


llm = ChatGroq(

    model="llama-3.1-8b-instant",

    temperature=0.2,

    api_key=os.getenv(
        "GROQ_API_KEY"
    )

)



def planner_agent(profile, destination_info):


    prompt = f"""

You are a professional Sri Lanka travel planner.


Create a travel plan using ONLY the provided information.



TRAVELLER PROFILE:

{profile}



AVAILABLE TRAVEL INFORMATION:

{destination_info}



STRICT RULES:


- Follow exact travel duration from traveller profile.
- If duration is 2 days create ONLY Day 1 and Day 2.
- If duration is 3 days create ONLY Day 1, Day 2 and Day 3.
- Never create extra days.

- Keep exact destination.
- Keep exact travel type.
- Keep exact transport preference.

- Never add other destinations.
- Never use activities from other destinations.

- Never invent hotels.
- Never invent activities.
- Never invent transport routes.
- Never invent prices.

- Use only provided database information.

- If information is missing write:
Information not available.

- Do not create cafe section.
- Do not create current weather details.



FORMAT:



# 🇱🇰 Sri Lanka Travel Plan



## 📌 Trip Summary


Destination:

Duration:

Budget:

Travel Type:

Number of Travelers:

Interests:

Transport:



## 🗓️ Day by Day Itinerary



Create only required days.



Day 1

Morning activity:

Afternoon activity:

Evening activity:



Day 2

Morning activity:

Afternoon activity:

Evening activity:



Day 3

Morning activity:

Afternoon activity:

Evening activity:



## 🏨 Recommended Hotels


Use only provided hotel information.



If unavailable:

Information not available.



## 🍽️ Food & Restaurants


Use only provided restaurant information.



If unavailable:

Information not available.



Local Foods To Try:

- Rice and Curry
- Kottu Roti
- Hoppers
- Seafood



## 🎯 Activities


Use only provided activity information.



## 🚆 Transport Plan


Use only provided transport information.



Starting Point:

Route:

Transport Type:

Travel Time:

Local Transport Options:



## 🌦️ Weather & Best Time To Visit


Climate:

Best Season:

Recommendation:



## 💡 Travel Tips



## ☎️ Emergency Contacts


Police: 119

Ambulance: 1990

Tourist Police: 1912


## 💰 Budget Summary


Selected Budget:
Use the traveller selected budget.


Recommended Minimum Budget:
Use only the budget information available in database.


Budget Status:
Compare selected budget with recommended minimum budget.


Recommendation:
Provide a short recommendation based on the available budget information.


Do not calculate prices.

"""



    response = llm.invoke(
        prompt
    )


    return {

        "final_plan":

        response.content.strip()

    }