import requests
from bs4 import BeautifulSoup
import pandas as pd
import os


class DataMiner:
    def __init__(self, urls, output_format='csv', output_file='data_output'):

        self.urls = urls
        self.output_format = output_format.lower()
        self.output_file = output_file

    def fetch_content(self, url):
        try:
            response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None

    def parse_content(self, html, target_tags):


        soup = BeautifulSoup(html, 'html.parser')
        extracted_data = []

        for tag, attributes in target_tags.items():
            elements = soup.find_all(tag, attributes)
            extracted_data.extend([element.get_text(strip=True) for element in elements])

        return extracted_data

    def save_data(self, data):

        if self.output_format == 'csv':
            df = pd.DataFrame(data, columns=["Extracted Data"])
            file_name = f"{self.output_file}.csv"
            df.to_csv(file_name, index=False)
            print(f"Data saved to {file_name}")
        else:
            print("Unsupported format! csv is only supported.")

    def run(self, target_tags):

        all_data = []

        for url in self.urls:
            print(f"Scraping the {url}...")
            html_content = self.fetch_content(url)

            if html_content:
                extracted_data = self.parse_content(html_content, target_tags)
                all_data.extend([[data] for data in extracted_data])

        if all_data:
            self.save_data(all_data)
        else:
            print("No data extracted.")


if __name__ == "__main__":
    # Example usage
    target_urls = ["https://wikipedia.com"]
    tags_to_extract = {
        "h1": {},  # Extract all <h1> tags
        "h2": {},
        "p": {},  # Extract all <p> tags
        "a": {"href": True}  # Extract all <a> tags with an href attribute
    }

    miner = DataMiner(target_urls, output_format='csv', output_file='scraped_data')
    miner.run(tags_to_extract)