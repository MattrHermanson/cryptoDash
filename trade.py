

class Trade:
    
    def __init__(id: str, openPrice: float, quantity: float, tradeType: str, state: str):
        self.id = id
        self.price = openPrice
        self.quantity = quantity
        self.tradeType = tradeType
        self.state = state

    def updateTrade(newPrice: float, newQuantity: float, newState: str):
        price = newPrice
        quantity = newQuantity
        state = newState
