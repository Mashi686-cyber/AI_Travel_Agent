from agents.profile_agent import profile_agent
from graph import travel_graph



print("=" * 50)
print("🇱🇰 AI Sri Lanka Travel Assistant")
print("=" * 50)



print("\nEnter your travel request.")
print("Type your request and press ENTER twice to finish.")
print("-" * 50)



lines = []

while True:

    line = input()

    if line == "":

        break

    lines.append(line)



user_request = "\n".join(lines)



if not user_request:

    print("No travel request entered.")

    exit()



# ================= PROFILE AGENT =================


profile = profile_agent(
    user_request
)



print("\nPROFILE")
print("=" * 50)


print(
    profile.get(
        "profile",
        "Information not available."
    )
)



# ================= EXTRACT VALUES =================


profile_text = profile.get(
    "profile",
    ""
)



destination = ""


transport = ""



for line in profile_text.splitlines():


    if line.startswith("Destination:"):

        destination = line.split(":")[1].strip()



    if line.startswith("Transport Preference:"):

        transport = line.split(":")[1].strip()




# ================= LANGGRAPH =================


result = travel_graph.invoke(

    {

        "profile": profile_text,

        "destination": destination,

        "transport_preference": transport,

        "destination_info": "",

        "hotels": "",

        "activities": "",

        "transport": "",

        "final_plan": ""

    }

)




print("\n")

print("=" * 60)

print("🇱🇰 FINAL TRAVEL PLAN")

print("=" * 60)



print(

    result.get(

        "final_plan",

        "No plan generated."

    )

)