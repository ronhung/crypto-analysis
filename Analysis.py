class Analysis():
    def __init__(self, datas):
        self.profits = []
        self.accumulatedValue = []

        bookValue = high = low = 8000
        win = self.MMD = 0
        totalProfit = totalLoss = 0

        for data in datas:
            if data["fillPnl"] != '0':
                profit = float(data["fillPnl"]) + float(data["fee"])
                bookValue += profit
                # collect data
                self.profits.append(profit)
                self.accumulatedValue.append(bookValue)

                # winRate / profit factor
                if profit > 0:
                    win += 1
                    totalProfit += profit
                else:
                    totalLoss -= profit
                # MMD
                if bookValue > high:
                    if high-low > self.MMD:
                        self.MMD = high-low
                    high = bookValue
                elif bookValue < low:
                    low = bookValue
                    if high-low > self.MMD:
                        self.MMD = high-low
        self.MMD = self.MMD/8000 * 100
        number = len(self.profits)

        # ROI
        self.ROI = (bookValue-8000)/8000 * 100
        # winRate
        self.winRate = win/number * 100
        # profit factor
        self.profitFactor = totalProfit/totalLoss * 100
        # sharpe ratio
        self.mean = (self.profits[0]/8000) * (1/number)
        for i in range(1, number):
            self.mean += (self.profits[i]/self.accumulatedValue[i-1]) * (1/number)
        var = ((self.profits[0]/8000) - self.mean)**2 * (1/number)
        for i in range(1, number):
            var += (self.profits[i]/self.accumulatedValue[i-1]-self.mean)**2 * (1/number)
        self.SD = var ** (0.5)

    def getROI(self):
        return f"{round(self.ROI, 4)}%"
    
    def getWinRate(self):
        return f"{round(self.winRate, 4)}%"
    
    def getMMD(self):
        return f"{round(self.MMD, 4)}%"
    
    def getProfitFactor(self):
        return f"{round(self.profitFactor, 4)}%"
    
    def getSharpeRatio(self, riskFreeRate=0):
        return round((self.ROI/100-riskFreeRate)/self.SD, 4)

    def getProfits(self):
        return [round(p, 4) for p in self.profits]
    
    def getAccumulatedValue(self):
        return [round(v, 4) for v in self.accumulatedValue]
