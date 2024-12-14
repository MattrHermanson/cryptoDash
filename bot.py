from main import CryptoAPITrading
import time
from trade import Trade

class Bot:

    #TODO add min time interval between api requests
    def __init__(self, coin: str, client: CryptoAPITrading, pathToLog: str):
        print("bot created")
        self.coin = coin
        self.client = client
        self.pathToLog = pathToLog
        self.tradeList = []

        self.positionQ = 0
        self.positionP = 0
        self.profit = 0

    #TODO type hint runTime, decide default value too
    def run(self, mode: int):
        #Mode 0: observe/track profits and losses
        #Mode 1: give buy and sell recomendations
        #Mode 2: auto trade

        if (mode == 0): 
            print("Running Mode 0\n")
            #get orders, store current # of orders
            currentOrderNum = self.client.get_orders()
            currentOrderNum = len(currentOrderNum['results'])

            #every 5min look for new orders, keep track of order updates,
            #and look for buy sell pairs
            #note most recent order is at [0] and order [i] becomes [i+1] when there is a new order
            while (True):

                getOrderRequest = self.client.get_orders()
                getOrderRequest = getOrderRequest['results']

                #check for new orders
                if (len(getOrderRequest) > currentOrderNum):
                        
                    self.logOrder(self.tradeList, getOrderRequest[0])
                    
                self.updateOrders(self.tradeList, getOrderRequest)
                self.printInfo()
                #wait 1 minute
                time.sleep(60)
        elif (mode == 1):
            pass 
        elif (mode == 2):
            pass

    #Log new orders into the list of open orders
    def logOrder(self, openOrders: list, newOrder: dict):
        newTrade = Trade(newOrder['client_order_id'], 0, 0, newOrder['side'], newOrder['state'])
        openOrders.append(newTrade)
   
    #update all open orders with new info from most recent request
    def updateOrders(self, openOrders: list, currentOrders: list):
        #TODO figure out better way to cross check order updates 

        #for every open trade, look for a corresponding trade, then update info
        for trade in openOrders:
            for curTrade in currentOrders:
                if (trade['client_order_id'] == curTrade['client_order_id']):

                    trade.updateTrade(curTrade['executions'][0]['effective_price'], curTrade['executions'][0]['quantity'], curTrade['state'])
                    if (trade['state'] == 'filled'):
                        #close out order if its been filled
                        self.closeOrder(openOrders, openOrders.index(trade))

    def closeOrder(self, openOrders:list, index: int):
        
        match openOrders[index]['state']:
            case 'buy':
                #average the new and old purchase price
                price1 = self.positionP * self.positionQ
                price2 = openOrders[index]['executions'][0]['effective_priceprice'] * openOrders[index]['executions'][0]['quantity']
                self.positionQ += openOrders[index]['executions'][0]['quantity']
                self.positionP = (price1 + price2)/(self.positionQ)
                print(f"Buy order Q: {openOrders[index]['executions'][0]['quanity']} P: {openOrders[index]['executions'][0]['effective_price']}")
                openOrders.pop(index)

            case 'sell':
                
                #calculate profits
                originalCost = self.positionP * self.positionQ
                profit = (openOrders[index]['executions'][0]['effective_priceprice'] * openOrders[index]['executions'][0]['quantity']) - originalCost
                
                #subtract quantity
                self.positionQ -= openOrders[index]['executions'][0]['quantity']

                print(f"Sell order Q: {openOrders[index]['executions'][0]['quanity']} P: {openOrders[index]['executions'][0]['effective_price']}")
                #pop openOrder
                openOrders.pop(index)

    def printInfo(self):
        print(f"Position Quantity: {self.positionQ}")
        print(f"Position Price: {self.positionP}")
        print(f"Profit: {self.profit}")
        print("")

