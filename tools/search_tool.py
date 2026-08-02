from langchain_community.tools import DuckDuckGoSearchRun
import time


search = DuckDuckGoSearchRun()


def web_search(query):

    try:

        result = search.run(query)

        return result


    except Exception as e:

        print("Web search failed:", e)

        return """
        Sri Lanka activity information:

        - Sigiriya rock climbing
        - Ella hiking
        - Nine Arch Bridge visit
        - Tea plantation tours
        - Wildlife safaris
        - Beach activities
        - Cultural sightseeing
        - Temple visits
        """
