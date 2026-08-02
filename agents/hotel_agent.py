from tools.rag_pipeline import retrieve_information


def hotel_agent(state):

    destination = state.get(
        "destination",
        ""
    )


    hotels = retrieve_information(
        destination,
        "hotels"
    )


    return hotels