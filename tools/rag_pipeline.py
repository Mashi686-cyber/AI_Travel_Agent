import os


BASE_PATH = "data/travel_documents"



# ==================================================
# Extract ## Destination Section
# ==================================================

def extract_destination_section(text, destination):

    lines = text.splitlines()

    result = []

    capture = False


    for line in lines:

        clean = line.strip()


        # Start destination section
        if destination.lower() in clean.lower() and clean.startswith("##"):
             capture = True
             continue

             capture = True
             continue


        # Stop when next destination starts
        elif capture and clean.startswith("##"):

            break


        if capture:

            result.append(line)



    return "\n".join(result)





# ==================================================
# Extract General Destination File
# (ella.txt, yala.txt etc.)
# ==================================================

def read_destination_file(destination):

    file_path = os.path.join(

        BASE_PATH,

        f"{destination.lower().replace(' ','_')}.txt"

    )


    if not os.path.exists(file_path):

        return "Information not available."



    with open(

        file_path,

        "r",

        encoding="utf-8"

    ) as file:


        return file.read()





# ==================================================
# Main RAG Retrieval Function
# ==================================================

def retrieve_information(destination, category=None):


    if not destination:

        return "Information not available."



    destination = destination.strip()



    # ==================================================
    # Category Based Files
    # ==================================================

    if category:


        category_files = {

            "activities": "Activity.txt",

            "hotels": "hotels.txt",

            "restaurants": "restaurants.txt",

            "transport": "transport.txt",

            "knowledge": "sri_lanka_knowledge.txt"

        }



        file_name = category_files.get(category)



        if not file_name:

            return "Information not available."



        file_path = os.path.join(

            BASE_PATH,

            file_name

        )



        if not os.path.exists(file_path):

            return "Information not available."



        with open(

            file_path,

            "r",

            encoding="utf-8"

        ) as file:


            data = file.read()





        # -----------------------------
        # Activities
        # Hotels
        # Restaurants
        # Transport
        # -----------------------------
    
                # -----------------------------
        # Activities / Hotels / Restaurants
        # -----------------------------

        if category in [
            "activities",
            "hotels",
            "restaurants"
        ]:

            result = extract_destination_section(
                data,
                destination
            )

            if result.strip():
                return result


        # -----------------------------
        # Transport
        # -----------------------------

        if category == "transport":

            blocks = data.split(
                "--------------------------------------------------"
            )

            results = []

            for block in blocks:

                if destination.lower() in block.lower():
                    results.append(block)

            if results:
                return "\n\n".join(results)

            return "Information not available."


        # Knowledge database

        if category == "knowledge":

            return data





    # ==================================================
    # Destination Information
    # ==================================================

    else:


        data = read_destination_file(

            destination

        )


        if data:

            return data





    return "Information not available."