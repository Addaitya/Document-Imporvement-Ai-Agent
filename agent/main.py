import operator
import logging
import re
from typing import Annotated, TypedDict, Literal
from langgraph.graph import START, END, StateGraph
from agent.utils import get_llm
from langgraph.constants import Send
from langchain_text_splitters import MarkdownHeaderTextSplitter
from langchain_core.documents.base import Document
from langchain_core.prompts.chat import ChatPromptTemplate
import textstat

from agent.utils import get_prompt_template


class State(TypedDict):
    criterion: Literal["readability", "structure", "completeness", "style_guide"]
    article_title: str
    table_of_content: str
    article_path: str
    article: str
    article_sections: list[Document]
    final_review: str
    reviews: Annotated[list, operator.add]
    readability_score: float
    article_plain_text: str

class ReviewState(TypedDict):
    criterion: Literal["readability", "structure", "completeness", "style_guide"]
    article_path: str
    article_title: str
    article_section: str
    curr_heading: str
    table_of_content: str


headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
]

markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on)

def _word_count(text: str):
    return len(re.findall(r"/w+", text))

def split_article(state: State):
    """
    Split the article into section using headings.
    """

    if "article" not in state or not state["article"]:
        raise ValueError("Article in state of agent is absent.")

    markdown = state["article"]
    logging.info(f"Article word count: {_word_count(markdown)}")
    md_header_splits = markdown_splitter.split_text(markdown)
    return {"article_sections": md_header_splits}


def map_reviews(state: State):
    """
    Distribute sections to generate_review node
    """
    return [
        Send(
            "generate_reviews",
            {
                "criterion": state["criterion"],
                "article_path": state["article_path"],
                "article_title": state["article_title"],
                "table_of_content": state["table_of_content"],
                "article_section": section.page_content,
                "curr_heading": " > ".join(section.metadata.values())
            },
        )
        for section in state["article_sections"]
    ]


async def generate_review(state: ReviewState):
    '''
    This node generates review for a section of article 
    '''
    llm = get_llm()
    prompts = get_prompt_template(state["criterion"])
    prompt = prompts.get("generate_review_prompt", "")
    prompt = ChatPromptTemplate.from_messages([("human", prompt)])

    prompt = prompt.invoke(state)
    response = await llm.ainvoke(prompt)

    return {"reviews": [response.content]}


def get_readability_score(state: State) -> float:
    """
    Returns Flesch-Kincaid readabilty score
    """
    score = textstat.flesch_reading_ease(state["article_plain_text"])
    score = round(score, 2)
    return {"readability_score": score}


async def generate_final_review(state: State):
    """
    This node generates final review
    """
    llm = get_llm()
    prompts = get_prompt_template(state['criterion'])
    prompt = prompts.get("final_review_prompt", "")
    prompt = ChatPromptTemplate.from_messages([("human", prompt)])

    prompt = prompt.invoke(state)
    response = await llm.ainvoke(prompt)

    return {"final_review": response.content}


workflow = StateGraph(State)

workflow.add_node("split_article", split_article)
workflow.add_node("generate_reviews", generate_review)
workflow.add_node("get_readability_score", get_readability_score)
workflow.add_node("generate_final_review", generate_final_review)

workflow.add_edge(START, "split_article")
workflow.add_conditional_edges("split_article", map_reviews, ["generate_reviews"])
workflow.add_edge("generate_reviews", "get_readability_score")
workflow.add_edge("get_readability_score", "generate_final_review")
workflow.add_edge("generate_final_review", END)

graph = workflow.compile()

if __name__=="__main__":
    # Get agent visulisation
    png_data = graph.get_graph().draw_mermaid_png()

    # Save it to a PNG file
    with open("graph.png", "wb") as f:
        f.write(png_data)
