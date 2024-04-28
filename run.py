import json
from Analysis import *
with open("trades.json") as f:
    raw = json.load(f)

datas = raw["data"]

result = Analysis(datas)

print(result.getROI())
print(result.getWinRate())
print(result.getMMD())
print(result.getProfitFactor())
print(result.getSharpeRatio())
print(result.getAccumulatedValue())



