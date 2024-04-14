class SubscribedGameUpdatedData:
    def __init__(self, city, condition, details, price, link):
        self.city = city
        self.condition = condition
        self.details = details
        self.price = price
        self.link = link

    def to_dict(self):
        return {
            "city": self.city,
            "condition": self.condition,
            "details": self.details,
            "price": self.price,
            "link": self.link,
        }
