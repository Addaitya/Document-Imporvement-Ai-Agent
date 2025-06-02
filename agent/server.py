import time
import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse

## TODO: Remove with production
###########################3
# from dotenv import load_dotenv
# load_dotenv()
############################

from agent.web_scraping.main import WebScrapper, Page
from agent.main import graph

scrapper = WebScrapper()

# @asynccontextmanager
# async def lifespan(app: FastAPI):

#     # Make connection with remote broswer
#     scrapper = WebScrapper()
#     yield
#     scrapper.close()


# app = FastAPI(lifespan=lifespan)

app = FastAPI()

@app.get("/health")
async def health():
    return "Healthy"

@app.get("/suggestion")
async def get_suggestions(url: str = Query(...)):
    if "https://help.moengage.com/hc/en-us/articles" not in url:
        raise HTTPException(status_code=400, detail="Invalid URL")

    try:
        page_soup = scrapper.get_page(url)

        page = Page(page_soup)
        logging.info("Page fetch successfully: \n{page_soup}")

        criteria = ["readability", "structure", "completeness", "style_guide"]
        input_payload = {
            "article_title": page.title(),
            "article_path": page.article_path(),
            "article": page.markdown(),
            "table_of_content": page.toc(),
            "article_plain_text": page.plain_text()
        }


        result = {}
        for criterion in criteria:
            input_payload["criterion"] = criterion
            response = await graph.ainvoke(input_payload)
            result[criterion] = response["final_review"]
            logging.info(f"response for {criteria}: \n{response['final_review']}")
            time.sleep(10)
        return result
    except Exception as e:
        logging.error(f"Error in get_suggestion: {e}")
        return JSONResponse(
            status_code=500,
            content= {
                "error": str(e)
            }
        )

@app.get('/')
def p(url: str= Query(...)):
    # url = "https://help.moengage.com/hc/en-us/articles/360000347066-Tracking-Users-in-Flows%23h_01HV6692KWH361Q3RPX3SQ1RHN"
    page_soup = scrapper.get_page(url)

    page = Page(page_soup)
    
    return page.markdown()