import requests
from typing import Optional
class Brewery:
    def __init__(self, id: str, name:str, type: str, street: Optional[str], city: str, state: Optional[str], country: str, website: Optional[str]):
        self.id=id
        self.name=name
        self.type=type
        self.street=street
        self.city=city
        self.country=country
        self.state=state
        self.website=website

    def __str__(self):
        return (f"Brewery:{self.name}\n"
                f"Type:{self.type}\n"
                f"Street:{self.street}\n"
                f"City:{self.city}\n"
                f"Country:{self.country}\n"
                f"State:{self.state}\n"
                f"Website:{self.website}"






                )
