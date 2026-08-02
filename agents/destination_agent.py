from tools.rag_pipeline import retrieve_information



def destination_agent(state):


    destination = state.get(
        "destination",
        ""
    )


    info = retrieve_information(
        destination
    )


    if not info:

        return "Information not available."


    return info