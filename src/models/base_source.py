from abc import ABC, abstractmethod
from typing import List, Dict

class Source(ABC):
    def __init__(self, base_url: str=None):
        pass

    @abstractmethod
    def fetch_listings(self) -> List[Dict]:
        """
        Logic to open the browser and get raw HTML/JSON.
        Should return a list of dictionaries with 'id', 'url', 'price', and 'title'.
        """
        pass

    @abstractmethod
    def parse_listing(self, data) -> Dict:
        """
        Logic to extract specific details from a single listing.
        """
        pass