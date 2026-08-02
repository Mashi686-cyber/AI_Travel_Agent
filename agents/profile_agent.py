from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os


load_dotenv()



llm = ChatGroq(

    model="llama-3.1-8b-instant",

    temperature=0.2,

    api_key=os.getenv("GROQ_API_KEY")

)



def profile_agent(request):


    prompt = f"""

Create traveller profile.

Use ONLY given information.


USER INPUT:

{request}


Rules:

- Keep destination exactly.
- Keep travel type exactly.
- Keep interests exactly.
- Keep transport exactly.
- Do not add information.


Format:


Destination:

Duration:

Budget:

Travel Type:

Number of Travelers:

Interests:

Transport Preference:

"""


    response = llm.invoke(
        prompt
    )


    return {

        "profile":
        response.content.strip()

    }