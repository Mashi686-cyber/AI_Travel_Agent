from typing import TypedDict

from langgraph.graph import StateGraph, END

from agents.restaurant_agent import restaurant_agent
from agents.destination_agent import destination_agent
from agents.hotel_agent import hotel_agent
from agents.activity_agent import activity_agent
from agents.transport_agent import transport_agent
from agents.planner_agent import planner_agent


# =========================
# STATE
# =========================

class TravelState(TypedDict):

    profile: str

    destination: str

    transport_preference: str

    destination_info: str

    hotels: str

    restaurants: str

    activities: str

    transport: str

    final_plan: str



# =========================
# NODES
# =========================


def destination_node(state):

    print("DESTINATION NODE")


    return {

        "destination_info":

        destination_agent(state)

    }




def hotel_node(state):

    print("HOTEL NODE")


    return {

        "hotels":

        hotel_agent(state)

    }

def restaurant_node(state):

    print("RESTAURANT NODE")

    return {

        "restaurants":

        restaurant_agent(state)

    }




def activity_node(state):

    print("ACTIVITY NODE")


    return {

        "activities":

        activity_agent(state)

    }

def restaurant_node(state):

    print("RESTAURANT NODE")

    return {

        "restaurants":

        restaurant_agent(state)

    }




def transport_node(state):

    print("TRANSPORT NODE")


    return {

        "transport":

        transport_agent(state)

    }





def planner_node(state):

    print("PLANNER NODE")


    information = {

    "destination":
    state["destination_info"],

    "hotels":
    state["hotels"],

    "restaurants":
    state["restaurants"],

    "activities":
    state["activities"],

    "transport":
    state["transport"]

}



    result = planner_agent(

        state["profile"],

        information

    )



    return {


        "final_plan":

        result["final_plan"]

    }




# =========================
# BUILD GRAPH
# =========================


workflow = StateGraph(
    TravelState
)



workflow.add_node(
    "destination",
    destination_node
)



workflow.add_node(
    "hotel",
    hotel_node
)


workflow.add_node(
    "restaurant",
    restaurant_node
)



workflow.add_node(
    "activity",
    activity_node
)



workflow.add_node(
    "transport",
    transport_node
)



workflow.add_node(
    "planner",
    planner_node
)




workflow.set_entry_point(
    "destination"
)




workflow.add_edge(
    "destination",
    "hotel"
)



workflow.add_edge(
    "hotel",
    "restaurant"
)


workflow.add_edge(
    "restaurant",
    "activity"
)


workflow.add_edge(
    "activity",
    "transport"
)



workflow.add_edge(
    "transport",
    "planner"
)



workflow.add_edge(
    "planner",
    END
)




travel_graph = workflow.compile()