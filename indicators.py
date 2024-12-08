import time

def rsi(lastPrices: [float]) -> float:
    #calculate n periods of change
    #change = close[t] - close[t-1]
 
    changeList = [lastPrices[i] - lastPrices[i-1] for i in range(1, len(lastPrices))]

    #calculate up moves and down moves
    #up moves equal change if pos or 0 if neg; down moves equal abs(change) if change is neg or 0 if pos
    upMoves = []
    downMoves = []

    for x in changeList:
        if x > 0:
            upMoves.append(x)
            downMoves.append(0)
        elif x < 0:
            upMoves.append(0)
            downMoves.append(abs(x))
        else:
            upMoves.append(0)
            downMoves.append(0)

    #RSI = 100 - 100/(1+RS), RS = AvgU/AvgD
    rs = (sum(upMoves)/len(upMoves))/(sum(downMoves)/len(downMoves))
    return 100 - (100/(1+rs))

def sma(lastPrices: [float]) -> float:
    sum = 0 

    for x in range(1, len(lastPrices)):
        sum += lastPrices[x]
    
    return sum/(len(lastPrices)-1)

def ema(close: float, lastEma: float, period: int) -> float:
    weightFactor = 2/(period + 1)

    return (((close - lastEma) * weightFactor) + lastEma)

def macd(shortEma: float, longEma: float, signal: float) -> float:
    return (shortEma - longEma) - signal


