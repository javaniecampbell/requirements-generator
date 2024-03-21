import datetime
import httpx
import csv
import json
from markdown import markdown
from selectolax.parser import HTMLParser
from urllib.parse import urljoin
from dataclasses import dataclass
from itertools import islice


@dataclass
class Item:
    name: str | None
    item_no: str | None
    brand: str | None
    price: str | None
    rating: float | None


def extract_text(html: HTMLParser, selector: str):
    try:
        return html.css_first(selector).text()
    except AttributeError as err:
        return None


def extract_textV2(node, default=None):
    return node.text(strip=True) if node else default


def scrape(url, **kwargs):
    """
    This function takes a URL as an argument and performs a web scraping operation.
    It returns the HTML content of the page.
    """

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0"
    }

    if kwargs.get("page"):
        response = httpx.get(
            url + str(kwargs.get("page")), headers=headers, follow_redirects=True
        )
    else:
        response = httpx.get(url, headers=headers, follow_redirects=True)
    # handling errors
    try:
        response.raise_for_status()
    except httpx.HTTPStatusError as ex:
        print(
            f"Error response {ex.response.status_code} while requesting {ex.request.url!r}."
        )
        return False
    html = HTMLParser(response.text)
    return html


def output(results):
    """
    This function takes the parsed data as an argument and outputs it.
    """
    if results is None:
        return
    # write_json()(results)
    for result in results:
        if result is None:
            continue
        print(result)


def write_csv(rows, headers, filename):
    """
    Responsible for taking the results, creating a new file if the file
    does not exist and updating exisitng file with a timestamp for that day.
    Return True when successful otherwise return false.
    """
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        for row in rows:
            writer.writerow(row)


def write_json(results, filename):
    """
    Responsible for taking the results, creating a new file if the file
    does not exist and updating exisitng file with a timestamp for that day.
    Return True when successful otherwise return false.
    """
    if results is None:
        return None
    with open(filename, "w") as jsonfile:
        json.dump([obj.__dict__ for obj in results], jsonfile)


def read_file(filename):
    """
    Responsible for reading the file and returning the data as a list.
    """
    content = ""
    with open(filename, "r") as file:
        content = file.read()
        file.close()
    return content


def write_to_md(file_path, text):
    with open(file_path, "a") as f:
        f.write(markdown.markdown(text) + "\n")
