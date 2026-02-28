from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime


# Save ddgo and wiki to file
def save_to_txt(data: str, filename: str = "data/research_output.txt"):
    timestamp = datetime().now().strftime("%Y-%m-%d %H:%M:%S")
    f_text = f"---Research Output---\nTimeStamp:{ timestamp}\n\n{data}\n\n"
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f_text)

    return f"Successfully wrote file {filename}"

save_tool = Tool(
    name="save_text_to_file",
    func=save_to_txt,
    description="Saves unstructured research data to file."
)

search_tool = DuckDuckGoSearchRun(name="search")
api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)


