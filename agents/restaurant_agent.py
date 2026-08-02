from tools.rag_pipeline import retrieve_information



def restaurant_agent(state):


    destination = state.get(
        "destination",
        ""
    )


    restaurants = retrieve_information(

        destination,

        "restaurants"

    )


    if not restaurants:

        return "Information not available."


    return restaurants