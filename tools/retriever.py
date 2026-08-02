import os


BASE_PATH = "data"



def retrieve_information(destination):


    destination = destination.lower().strip()


    file_path = os.path.join(
        BASE_PATH,
        f"{destination}.txt"
    )


    if not os.path.exists(file_path):

        print("RAG FILE NOT FOUND:", destination)

        return "Information not available."



    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        data = file.read()



    print(
        "RAG LOADED:",
        destination + ".txt"
    )


    return data