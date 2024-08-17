class CalculateMoney:
    def sum_price_count(self, price: float, count: int, discount: int = None):
        result = round(count * price, 2)

        if discount:
            result = round(result * (1 - (discount/100)), 2)

        return result


    def sum_price(self, prices: list, discount: int = None):
        result = round(sum(prices), 2)
        if discount:
            result = round(result * (1 - (discount/100)), 2)
        return result

def sum_price_count(price: float, count: int, discount: int = None):
    return CalculateMoney().sum_price_count(price=price, count=count, discount=discount)