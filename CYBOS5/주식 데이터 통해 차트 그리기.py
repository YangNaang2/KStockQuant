import pandas as pd
import yfinance as yf
import datetime
import matplotlib.pyplot as plt
# 시작 및 종료 날짜 설정
start = datetime.datetime(2016, 2, 19)
end = datetime.datetime(2016, 3, 4)

# 주식 코드에 대한 데이터 가져오기
gs = yf.download("078930.KQ", start=start, end=end)
gs.to_csv("temp.csv")
df = pd.read_csv("temp.csv")

plt.figure(figsize=(10, 6))
plt.plot(gs.index, gs['Close'], label="Close")
plt.title("Close Price of 078930.KQ")
plt.xlabel("Date")
plt.ylabel("Price")
plt.grid(True)
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
