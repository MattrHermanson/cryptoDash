from main import CryptoAPITrading
import time

class Bot:

    #TODO add time interval that governs API requests
    def __init__(self, coin: str, client: CryptoAPITrading, pathToLog: str): 
        self.coin = coin
        self.client = client
        self.pathToLog = pathToLog 

    #TODO type hint runTime, decide default value too
    def run(mode: int = 0, runTime, budget: float = 0):
        #Mode 0: observe/track profits and losses
        #Mode 1: give buy and sell recomendations
        #Mode 2: auto trade

        switch(mode):
            case 0:
                #get orders, store current # of orders
                curOrderNum = len(client.get_orders['results'])

                #every 5min look for new orders, keep track of order updates,
                #and look for buy sell pairs
                #note most recent order is at [0] and order [i] becomes [i+1] when there is a new order
                while (true):

                    if (len(client.get_orders['results']) > curOrderNum):
                        
                        #log new order
                    
                    time.sleep(300)


                #maybe make Trade class 

                #calculate profit/loss and log it

                break

            case 1:

                break

            case 2:

                break
        

    
