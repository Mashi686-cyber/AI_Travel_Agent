from tools.rag_pipeline import retrieve_information


def activity_agent(state):

    destination = state.get(
        "destination",
        ""
    )


    activities = retrieve_information(
        destination,
        "activities"
    )


    return activities