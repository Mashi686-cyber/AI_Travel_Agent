def supervisor_agent(state):

    profile = state.get(
        "profile",
        ""
    )


    # Supervisor decides workflow

    return {

        "profile": profile,

        "next_agents": [

            "destination",

            "hotel",

            "restaurant",

            "activity",

            "transport",

            "planner"

        ]

    }