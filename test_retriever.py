from tools.retriever import retrieve_information


print("\n===== HOTELS =====")

hotels = retrieve_information(
    "real Sri Lanka hotels"
)

print(hotels)



print("\n===== RESTAURANTS =====")

restaurants = retrieve_information(
    "real Sri Lanka restaurants food"
)

print(restaurants)



print("\n===== CAFES =====")

cafes = retrieve_information(
    "real Sri Lanka cafes coffee shops"
)

print(cafes)