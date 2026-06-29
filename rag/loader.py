from langchain_community.document_loaders import RecursiveUrlLoader
from bs4 import BeautifulSoup

from config import WEBSITE_URL


def extractor(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")

    # Remove unwanted tags
    for tag in soup(["script", "style", "noscript", "svg"]):
        tag.decompose()

    return soup.get_text(
        separator=" ",
        strip=True
    )


def load_website():

    loader = RecursiveUrlLoader(
        url=WEBSITE_URL,
        max_depth=2,
        extractor=extractor
    )

    documents = loader.load()

    print(f"Loaded {len(documents)} pages")

    return documents