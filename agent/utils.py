import os
from functools import lru_cache
import yaml
from langchain_groq import ChatGroq
from langchain_core.rate_limiters import InMemoryRateLimiter


# TODO: Remove this dotenv
#####   
# from dotenv import load_dotenv
# load_dotenv()
###############
LLM_API_KEY = os.getenv("LLM_API_KEY")
LLM_MODEL = os.getenv("LLM_MODEL")

##TODO: Add rate limiter to avoid hitting api limits


@lru_cache()
def get_llm(temperature: float = 0.6) -> ChatGroq:
    '''
    Return llm chat object
    '''
    if not LLM_API_KEY or not LLM_MODEL:
        raise ValueError("Problem in LLM api key or model name env.")

    rate_limiter = InMemoryRateLimiter(
        requests_per_second=0.25, check_every_n_seconds=1, max_bucket_size=1
    )
    llm = ChatGroq(
        model=LLM_MODEL,
        temperature=0.6,
        max_retries=3,
        api_key=LLM_API_KEY,
        rate_limiter=rate_limiter,
    )
    return llm




@lru_cache()
def get_prompt_template(criterion: str) -> dict:
    """
    Extract prompt from yaml file.
    """
    prompt_dir = "agent/prompts"
    path = {
        "readability": f"{prompt_dir}/readability.yaml",
        "structure": f"{prompt_dir}/structure.yaml",
        "completeness": f"{prompt_dir}/completeness.yaml",
        "style_guide": f"{prompt_dir}/style_guide.yaml",
    }
    with open(path[criterion], "r") as f:
        prompt_template = yaml.safe_load(f)
        return prompt_template
