import streamlit as st
from PIL import Image
import base64

from graph import travel_graph


# ================= PAGE CONFIG =================

st.set_page_config(
    page_title="Ceylon AI Travel Assistant",
    page_icon="🇱🇰",
    layout="wide"
)


# ================= BACKGROUND =================

def get_base64(path):

    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


background = get_base64(
    "assets/background.jpg"
)


# ================= CSS LOAD =================

with open("style.css") as f:
    css = f.read()


css = css.replace(
    "assets/background.jpg",
    f"data:image/jpg;base64,{background}"
)


st.markdown(
    f"<style>{css}</style>",
    unsafe_allow_html=True
)



# ================= HEADER =================


st.markdown(
"""
<div class="header">

<div class="title">
🇱🇰 Ceylon AI Travel Assistant
</div>

<div class="subtitle">
Explore Sri Lanka Smarter with Artificial Intelligence
</div>

</div>
""",
unsafe_allow_html=True
)



# ================= HERO =================


st.markdown(
"""
<div class="card">

<h2>
🌴 Discover the Wonders of Sri Lanka
</h2>

<p>
Plan your journey with AI.
Discover hotels, restaurants,
foods, activities and transport
based on your travel style.
</p>

</div>
""",
unsafe_allow_html=True
)



# ================= AI PLANNER =================


st.markdown(
"""
<div class="card">

<h2>
✈️ AI Trip Planner
</h2>

<p>
Create your personalized Sri Lanka journey.
</p>

</div>
""",
unsafe_allow_html=True
)



# ================= DESTINATIONS =================


destinations = [

"Sigiriya 🏛️",

"Ella 🌿",

"Kandy 🛕",

"Galle Fort 🏰",

"Yala National Park 🐘",

"Mirissa Beach 🏖️",

"Unawatuna Beach 🏖️",

"Bentota Beach 🌊",

"Hikkaduwa Beach 🌊",

"Arugam Bay 🏄",

"Trincomalee 🌊",

"Pasikuda 🌊",

"Tangalle 🏝️",

"Nuwara Eliya 🍃",

"Horton Plains 🌿",

"Knuckles Mountain Range ⛰️",

"Anuradhapura 🏛️",

"Polonnaruwa 🏛️",

"Udawalawe National Park 🐘",

"Colombo 🌆",

"Negombo 🌊",

"Jaffna 🌴"

]



# ================= SEARCH DESTINATION =================


search_col, dest_col = st.columns([2,3])


with search_col:

    search = st.text_input(
        "🔍 Search Destination",
        placeholder="Type Ella, Galle, Mirissa..."
    )


with dest_col:


    if search:


        filtered = [
            x for x in destinations
            if search.lower() in x.lower()
        ]


        if filtered:

            destination = st.selectbox(
                "📍 Destination",
                filtered
            )

        else:

            st.warning(
                "⚠️ Destination not found. Please select a valid destination."
            )

            destination = destinations[0]


    else:


        destination = st.selectbox(
            "📍 Destination",
            destinations
        )



# ================= TRAVEL DETAILS =================


st.markdown(
"""
<div class="card">

<h2>
👤 Travel Preferences
</h2>

</div>
""",
unsafe_allow_html=True
)



row1 = st.columns(5)



with row1[0]:

    travelers = st.number_input(
        "👥 Travelers",
        1,
        20,
        2
    )



with row1[1]:

    days = st.number_input(
        "📅 Days",
        1,
        30,
        7
    )



with row1[2]:

    currency = st.selectbox(
        "💰 Currency",
        [
            "USD ($)",
            "LKR (Rs)"
        ]
    )



with row1[3]:

    budget = st.number_input(
        "💵 Budget",
        100,
        1000000,
        1500
    )



with row1[4]:

    travel_type = st.selectbox(
        "🧳 Travel Type",
        [
            "Solo",
            "Couple",
            "Family",
            "Friends"
        ]
    )



# ================= SECOND ROW =================


row2 = st.columns(4)


with row2[0]:

    hotel = st.selectbox(
        "🏨 Hotel Preference",
        [
            "Budget",
            "Mid Range",
            "Luxury"
        ]
    )



with row2[1]:

    transport = st.selectbox(
        "🚆 Transport",
        [
            "Train",
            "Bus",
            "Taxi",
            "Rental Car"
        ]
    )



with row2[2]:

    food = st.multiselect(
        "🍛 Food Interests",
        [
            "Sri Lankan Food",
            "Seafood",
            "Indian Food",
            "Thai Food",
            "Korean Food",
            "Chinese Food",
            "Italian Food",
            "Coffee & Desserts"
        ]
    )

    # ================= EXPERIENCE MAPPING =================


destination_experiences = {

    "Ella 🌿": [
        "Nature",
        "Adventure",
        "Culture"
    ],

    "Sigiriya 🏛️": [
        "Culture",
        "Adventure",
        "History"
    ],

    "Mirissa Beach 🏖️": [
        "Beach",
        "Wildlife",
        "Adventure"
    ],

    "Yala National Park 🐘": [
        "Wildlife",
        "Nature",
        "Adventure"
    ],

    "Kandy 🛕": [
        "Culture",
        "Nature",
        "History"
    ],

    "Galle Fort 🏰": [
        "Culture",
        "History",
        "Beach"
    ],

    "Nuwara Eliya 🍃": [
        "Nature",
        "Adventure",
        "Culture"
    ],

    "Arugam Bay 🏄": [
        "Beach",
        "Adventure",
        "Surfing"
    ],

    "Trincomalee 🌊": [
        "Beach",
        "Wildlife",
        "Adventure"
    ],

    "Anuradhapura 🏛️": [
        "Culture",
        "History"
    ],

    "Colombo 🌆": [
        "Culture",
        "Shopping",
        "Food"
    ]

}



with row2[3]:


    available_experiences = destination_experiences.get(

        destination,

        [
            "Nature",
            "Culture",
            "Adventure",
            "Beach",
            "Wildlife"
        ]

    )


    experience = st.selectbox(

        "🌴 Experience",

        available_experiences

    )



# ================= GENERATE BUTTON =================


if st.button(
    "🚀 Generate AI Travel Plan"
):


    with st.spinner(
        "🤖 AI Agents are creating your travel plan..."
    ):



        user_input = {


            "profile": {


                "traveler_request": f"""

Create a complete Sri Lanka travel plan.


Destination:

{destination}


Number of Travelers:

{travelers}


Travel Days:

{days}


Currency:

{currency}


Budget:

{budget} {currency}


Travel Type:

{travel_type}


Hotel Preference:

{hotel}


Transport:

{transport}


Food Interests:

{food}


Experience:

{experience}



Need details about:

- Trip summary
- Day by day itinerary
- Real hotels
- Real restaurants
- Cafes
- Sri Lankan foods
- International foods
- Activities
- Transport
- Budget
- Travel tips


"""

            }

        }



        try:


            result = travel_graph.invoke(
                user_input
            )


            st.session_state.final_plan = result["final_plan"]



        except Exception as e:


            st.error(
                "⚠️ AI agents are temporarily unavailable. Please try again."
            )


            st.write(e)



# ================= RESULT =================


st.markdown(
"""
<div class="card">

<h2>
🗺️ AI Generated Sri Lanka Travel Plan
</h2>

</div>
""",
unsafe_allow_html=True
)



if "final_plan" in st.session_state:


    st.markdown(
        st.session_state.final_plan
    )



# ================= INFORMATION CARDS =================


c1, c2 = st.columns(2)



with c1:


    st.markdown(
    """
    <div class="card">

    <h2>
    🏨 Hotel Recommendations
    </h2>

    <p>

    AI recommends hotels according to:

    <br><br>

    • Destination<br>
    • Budget<br>
    • Travel style<br>
    • Comfort level

    </p>

    </div>
    """,
    unsafe_allow_html=True
    )



    st.markdown(
    """
    <div class="card">

    <h2>
    🍛 Food Experience
    </h2>

    <p>

    Try Sri Lankan foods:

    <br><br>

    🍚 Rice & Curry<br>
    🍜 Kottu Roti<br>
    🥞 Hoppers<br>
    🦐 Seafood<br>
    ☕ Ceylon Tea<br>
    🍰 Desserts

    </p>

    </div>
    """,
    unsafe_allow_html=True
    )





with c2:


    st.markdown(
    """
    <div class="card">

    <h2>
    🚆 Transport Plan
    </h2>

    <p>

    AI suggests:

    <br><br>

    🚆 Scenic trains<br>
    🚌 Buses<br>
    🚕 Taxi<br>
    🚗 Rental vehicles

    </p>

    </div>
    """,
    unsafe_allow_html=True
    )



    st.markdown(
    """
    <div class="card">

    <h2>
    🎯 Activities
    </h2>

    <p>

    Discover:

    <br><br>

    🏖 Beaches<br>
    🌿 Nature<br>
    🐘 Wildlife<br>
    🏛 Culture<br>
    🏄 Adventure

    </p>

    </div>
    """,
    unsafe_allow_html=True
    )



# ================= DESTINATION SHOWCASE =================


st.markdown(
"""
<div class="card">

<h2>
🌍 Popular Sri Lanka Destinations
</h2>

</div>
""",
unsafe_allow_html=True
)



places = [

("Sigiriya","assets/sigiriya.jpg"),

("Ella","assets/ella.jpg"),

("Kandy","assets/kandy.jpg"),

("Galle","assets/galle.jpg"),

("Yala","assets/yala.jpg")

]



cols = st.columns(5)



for col, item in zip(cols, places):


    with col:


        img = Image.open(item[1])


        st.image(
            img,
            use_container_width=True
        )


        st.markdown(

        f"""

        <div style="
        text-align:center;
        color:white;
        font-size:18px;
        font-weight:700;
        margin-top:10px;
        ">

        {item[0]}

        </div>

        """,

        unsafe_allow_html=True

        )