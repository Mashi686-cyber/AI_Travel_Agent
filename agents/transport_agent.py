from tools.rag_pipeline import retrieve_information


def transport_agent(state):

    destination = state.get(
        "destination",
        ""
    )


    transport = retrieve_information(
        destination,
        "transport"
    )


    return transport