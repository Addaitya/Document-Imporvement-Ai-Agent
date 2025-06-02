import os
from bs4 import BeautifulSoup
from selenium.webdriver import Remote
from selenium.webdriver.firefox.options import Options
from html_to_markdown import convert_to_markdown
BROWSER_URL = os.getenv("BROWSER_URL")

class WebScrapper:
    def __init__(self):
        if not BROWSER_URL:
            raise ValueError("Enviornment variable BROWSER_URL is None")
        options = Options()  
        options.add_argument("--no-sandbox")
        self.driver = Remote(BROWSER_URL, options=options)
    
    def get_page(self, url: str) -> BeautifulSoup:
        """
        Fetch the article html content.
        """
        try:

            self.driver.get(url)
            html = self.driver.page_source
            page_soup = BeautifulSoup(html, 'html.parser')
            # driver.close()
            return page_soup
        except Exception as e:
            print(f"Error occured in fetch web content: \n{e}")
    




class Page:
    def __init__(self, page_soup: BeautifulSoup):
        self.page_soup = page_soup
    def toc(self) -> str:
        """
        Fetch table of content from the page.
        """
        def get_level(classes: list[str]):
            # lt-toc--item-h1 = subheading level 1
            # lt-toc--item-h2 = subheading level 2
            for cls in classes:
                if "lt-toc--item-h" in cls:
                    st = len("lt-toc--item-h")
                    level = int(cls[st:])
                    return level
            return -1

        try:
            toc = self.page_soup.find("ul", {"class": "lt-toc--list"})

            table_of_content = ""

            # take out each heading and indent based on subheading level
            for child in toc.children:
                if child.name != "li":
                    continue
                level = get_level(child['class'])
                text = child.get_text().strip()
                heading = "\t"*(level-1) + "- " + text + "\n"
                table_of_content += heading
            return table_of_content
        except Exception as e:
            print(f"Exception in fetching table of context: \n{e}")
    
    def plain_text(self)->str:
        '''
        Return article in plain text.
        '''
        return self.page_soup.get_text()
    
    def markdown(self)->str:
        '''
        Return article in markdown format
        '''
        md = convert_to_markdown(self.page_soup, heading_style="atx")
        return md
    
    def title(self) -> str:
        '''
        Return title of article
        '''
        article_title = self.page_soup.find("header", {"class":"article-header"})
        return article_title
    
    def article_path(self) -> str:
        '''
        Returns article path
        '''
        breadcrumbs = self.page_soup.find("ol", {"class": "breadcrumbs"})
        breadcrumbs = [child.get_text().strip() for child in breadcrumbs.children if child.name == "li"]
        path = " > ".join(breadcrumbs)
        return path

    
