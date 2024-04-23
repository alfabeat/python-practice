import pandas as pd

class stock:
    def __init__(self, name, stockpershare, total):
        self.name = name
        self.stockpershare = stockpershare
        self.total = total
        
    

def myfunc(flink):
    {

    }
simpsons = pd.read_html('https://markets.ft.com/data/equities/tearsheet/summary?s=GAW:LSE')

len(simpsons)
print(simpsons)
a = ' '.join(str(e) for e in simpsons)
f = open("stock.txt", "a")
f.write(a)
f.close