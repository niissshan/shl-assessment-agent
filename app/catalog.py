import requests
from bs4 import BeautifulSoup
import json
import time

BASE_URL = "https://www.shl.com/solutions/products/product-catalog/"


headers = {
    "User-Agent": "Mozilla/5.0"
}


def scrape_shl_catalog():

    response = requests.get(BASE_URL, headers=headers)

    print("Status Code:", response.status_code)

    soup = BeautifulSoup(response.text, "html.parser")

    assessments = []

    links = soup.find_all("a")

    seen = set()

    for link in links:

        href = link.get("href")
        text = link.get_text(strip=True)

        if href and "/products/product-catalog/view/" in href:

            full_url = "https://www.shl.com" + href

            if full_url in seen:
                continue

            seen.add(full_url)

            print("Scraping:", text)

            try:

                detail_response = requests.get(full_url, headers=headers)

                detail_soup = BeautifulSoup(detail_response.text, "html.parser")

                description = detail_soup.get_text(" ", strip=True)

                assessments.append({
                    "name": text,
                    "url": full_url,
                    "description": description[:3000]
                })

                time.sleep(1)

            except Exception as e:

                print("Error scraping:", full_url)
                print(e)

    with open("../data/catalog.json", "w", encoding="utf-8") as f:

        json.dump(assessments, f, indent=4)

    print(f"\nSaved {len(assessments)} assessments")


if __name__ == "__main__":
    scrape_shl_catalog()