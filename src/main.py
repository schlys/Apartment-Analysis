from models.zillow import Zillow
from utils.send_email import send_warning_email

sources = [
    Zillow(),
]

def validate_listings(listings: list, source_name: str) -> bool:
    if not listings:
        print(f"No listings found for {source_name}, did the URL change?")
        send_warning_email(
            subject=f"Warning: No listings found for {source_name}",
            body=f"Please check the {source_name} source, it may have changed its structure or URL."
        )
        return False
    return True


def fetch_all_listings() -> set:
    listings = set()

    for source in sources:
        source_listings = source.fetch_listings()
        if validate_listings(source_listings, source.name):
            listings.update(source_listings)
    
    return listings


if __name__ == "__main__":
    # listings = fetch_all_listings()
    validate_listings([], "Zillow")