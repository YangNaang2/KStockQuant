import pandas as pd
import yfinance as yf
import datetime
import matplotlib.pyplot as plt
# 시작 및 종료 날짜 설정
start = datetime.datetime(2014, 1, 1)
end = datetime.datetime(2016, 3, 6)

# 주식 코드에 대한 데이터 가져오기
gs = yf.download("078930.KS", start=start, end=end)

#공휴일, 주말에 장 안열리는거 생각
new_gs = gs[gs['Volume'] != 0]
ma5 = new_gs['Close'].rolling(window=5).mean()
ma20 = new_gs['Close'].rolling(window=20).mean()
ma60 = new_gs['Close'].rolling(window=60).mean()
ma120 = new_gs['Close'].rolling(window=120).mean()


new_gs.insert(len(new_gs.columns), "MA5", ma5)
new_gs.insert(len(new_gs.columns), "MA20", ma20)
new_gs.insert(len(new_gs.columns), "MA60", ma60)
new_gs.insert(len(new_gs.columns), "MA120", ma120)

plt.plot(new_gs.index, new_gs['Close'], label="Close")
plt.plot(new_gs.index, new_gs['MA5'], label ="MA5")
plt.plot(new_gs.index, new_gs['MA20'], label ="MA20")
plt.plot(new_gs.index, new_gs['MA60'], label ="MA60")
plt.plot(new_gs.index, new_gs['MA120'], label ="MA120")
plt.legend(loc='best')
plt.grid()
plt.show()
