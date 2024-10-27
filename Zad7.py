import requests

class Brewery:
    def __init__(self, id, name, brewery_type, street, city, state, postal_code, country, phone, website_url):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.street = street
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country
        self.phone = phone
        self.website_url = website_url

    def __str__(self):
        return f"Brewery {self.name} located at {self.street}, {self.city}, {self.state}, {self.country}. Type: {self.brewery_type}, Website: {self.website_url}"

def fetch_breweries():
    response = requests.get("https://api.openbrewerydb.org/breweries?per_page=20")
    if response.status_code == 200:
        return response.json()
    else:
        return []

def main():
    breweries_data = fetch_breweries()
    breweries = []

    for data in breweries_data:
        brewery = Brewery(
            id=data.get("id"),
            name=data.get("name"),
            brewery_type=data.get("brewery_type"),
            street=data.get("street"),
            city=data.get("city"),
            state=data.get("state"),
            postal_code=data.get("postal_code"),
            country=data.get("country"),
            phone=data.get("phone"),
            website_url=data.get("website_url")
        )
        breweries.append(brewery)

    for brewery in breweries:
        print(brewery)

if __name__ == "__main__":
    main()
