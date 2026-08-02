import streamlit as st
import base64
import os

from agents.profile_agent import profile_agent
from graph import travel_graph



st.set_page_config(
    page_title="Ceylon AI Travel Assistant",
    page_icon="🇱🇰",
    layout="wide"
)



# ================= BACKGROUND =================

def get_base64(path):

    with open(path, "rb") as f:
        return base64.b64encode(
            f.read()
        ).decode()



if os.path.exists("assets/background.jpg"):

    bg = get_base64(
        "assets/background.jpg"
    )

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image:
            linear-gradient(
            rgba(0,0,0,0.65),
            rgba(0,0,0,0.65)
            ),
            url("data:image/jpg;base64,{bg}");

            background-size:cover;
            background-position:center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )




# ================= TITLE =================

st.markdown(
"""
<h1 style="text-align:center">
🇱🇰 Ceylon AI Travel Assistant
</h1>

<p style="text-align:center">
AI Powered Sri Lanka Travel Planner 🌴
</p>

""",
unsafe_allow_html=True
)



st.divider()



# ================= INPUT =================


st.subheader(
"✈️ Create Your Travel Plan"
)



destination = st.selectbox(

"📍 Destination",

[
"Colombo",
"Ella",
"Kandy",
"Sigiriya",
"Galle",
"Yala",
"Mirissa",
"Nuwara Eliya",
"Bentota",
"Arugam Bay",
"Trincomalee",
"Jaffna",
"Anuradhapura",
"Horton Plains",
"Knuckles",
"Polonnaruwa",
"Dambulla"
]

)



days = st.number_input(

"📅 Number of Days",

1,

30,

3

)



currency = st.selectbox(

"💱 Currency",

[
"LKR",
"USD"
]

)



budget = st.number_input(

"💰 Budget",

1000,

5000000,

50000

)



travel_type = st.selectbox(

"👥 Travel Type",

[
"Solo",
"Couple",
"Family",
"Friends"
]

)



travelers = st.number_input(

"👤 Number of Travelers",

1,

20,

1

)



interest = st.multiselect(

"🎯 Interests",

[
"History",
"Culture",
"Beach",
"Adventure",
"Nature",
"Food",
"Hiking",
"Wildlife"
],

default=["Culture"]

)



transport = st.selectbox(

"🚆 Transport Preference",

[
"Train",
"Bus",
"Taxi",
"Tuk Tuk"
]

)




# ================= VALIDATION =================


def validate():


    if travel_type == "Solo" and travelers != 1:

        return "Solo travel requires 1 person."



    if travel_type == "Couple" and travelers != 2:

        return "Couple travel requires 2 people."



    historical_places = [

        "Sigiriya",
        "Anuradhapura",
        "Polonnaruwa",
        "Dambulla"

    ]


    if destination in historical_places and "Beach" in interest:

        return "This destination is mainly historical."



    nature_places = [

        "Yala",
        "Horton Plains",
        "Knuckles"

    ]


    if destination in nature_places and "Beach" in interest:

        return "This destination is mainly nature/wildlife."



    return None





# ================= BUDGET =================


def budget_check():


    minimum = days * travelers * 20000



    if budget < minimum:


        return f"""

⚠️ Budget Warning


Selected Budget:

{currency} {budget:,}



Recommended Minimum:

{currency} {minimum:,}



Includes:

✓ Accommodation

✓ Food

✓ Transport

✓ Activities


Some options may be limited.

"""


    return """

✅ Budget is suitable for this trip.

"""





# ================= GENERATE =================



if st.button(
"🚀 Create Travel Plan"
):


    error = validate()



    if error:

        st.error(error)



    else:


        with st.spinner(
            "AI creating travel plan..."
        ):


            request = f"""

Destination:
{destination}


Duration:
{days} days


Budget:
{currency} {budget}


Travel Type:
{travel_type}


Travelers:
{travelers}


Interests:
{", ".join(interest)}


Transport:
{transport}

"""



            profile = profile_agent(
                request
            )



            result = travel_graph.invoke(

{
    "profile": profile["profile"],

    "destination": destination,

    "transport_preference": transport,

    "destination_info": "",

    "hotels": "",

    "activities": "",

    "transport": "",

    "final_plan": ""
}

)




        st.success(
            "Travel Plan Created!"
        )



        st.subheader(
            "💰 Budget Advice"
        )


        st.info(
            budget_check()
        )



        st.subheader(
            "👤 Traveller Profile"
        )


        st.write(
            profile["profile"]
        )



        st.divider()



        st.subheader(
            "🇱🇰 Final Travel Plan"
        )



        st.markdown(

            result.get(

                "final_plan",

                "No plan generated"

            )

        )






# ================= IMAGES =================

st.divider()

st.subheader(
    "🌴 Popular Sri Lanka Destinations"
)


places = {

    "Ella":
    "assets/ella.jpg",

    "Kandy":
    "assets/kandy.jpg",

    "Yala":
    "assets/yala.jpg",

    "Galle":
    "assets/galle.jpg"

}



# Image Styling

st.markdown(
"""
<style>

.destination-card img {

    width: 100%;
    height: 250px;
    object-fit: cover;
    border-radius: 15px;

}


.destination-title {

    text-align: center;
    font-size: 18px;
    font-weight: bold;
    margin-top: 10px;

}

</style>
""",
unsafe_allow_html=True
)



cols = st.columns(4)



for i, (name, img) in enumerate(places.items()):


    with cols[i]:


        if os.path.exists(img):


            st.markdown(
                '<div class="destination-card">',
                unsafe_allow_html=True
            )


            st.image(
                img,
                use_container_width=True
            )


            st.markdown(
                f"""
                <p class="destination-title">
                {name}
                </p>
                """,
                unsafe_allow_html=True
            )


            st.markdown(
                "</div>",
                unsafe_allow_html=True
            )
