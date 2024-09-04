class SubscribedGameUpdatedData:
    def __init__(self, product_type, city, condition, details, price, link):
        self.product_type = product_type
        self.city = city
        self.condition = condition
        self.details = details
        self.price = price
        self.link = link

    def to_dict(self):
        return {
            "product_type": self.product_type,
            "city": self.city,
            "condition": self.condition,
            "details": self.details,
            "price": self.price,
            "link": self.link,
        }
