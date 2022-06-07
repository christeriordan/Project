from enum import Enum


class PriceModel(Enum):
    Regular = 0  # zero % discount
    HappyHour = 0.5  # 50%
    BlackFriday = (100, 500)  # x kr discount if price is above y
