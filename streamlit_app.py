import streamlit as st

from graph import travel_graph


st.set_page_config(
    page_title="Sri Lanka AI Travel Planner",
    page_icon="🌴"
)


st.title("🌴 Sri Lanka AI Travel Assistant")


request = st.text_area(
    "Travel Request",
    "Create a 7 day Sri Lanka trip"
)


days = st.number_input(
    "Number of Days",
    min_value=1,
    value=7
)


budget = st.number_input(
    "Budget (USD)",
    value=1000
)


if st.button("Generate Trip Plan"):

    profile = {

        "traveler_request": request,

        "days": days,

        "budget": budget

    }


    with st.spinner("Creating your Sri Lanka trip plan..."):

        result = travel_graph.invoke(
            {
                "profile": profile,
                "destinations": "",
                "hotels": "",
                "restaurants": "",
                "activities": "",
                "transport": "",
                "knowledge": "",
                "final_plan": ""
            }
        )


    st.success("Trip Plan Generated")

    st.markdown(
        result["final_plan"]
    )