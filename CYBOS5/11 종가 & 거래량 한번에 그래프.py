import yfinance as yf
import matplotlib.pyplot as plt

# yfinance로 데이터 가져오기
sk_hynix = yf.download("000660.KS")

# 그래프 크기 설정
fig = plt.figure(figsize=(12, 8))

# 위쪽 그래프 (조정 종가)
top_axes = plt.subplot2grid((4, 4), (0, 0), rowspan=3, colspan=4)
top_axes.plot(sk_hynix.index, sk_hynix['Adj Close'], label='Adjusted Close', color='blue')
top_axes.set_title("SK Hynix Adjusted Close Price")
top_axes.legend()

# 아래쪽 그래프 (거래량)
bottom_axes = plt.subplot2grid((4, 4), (3, 0), rowspan=1, colspan=4)
bottom_axes.plot(sk_hynix.index, sk_hynix['Volume'], label='Volume', color='green')
bottom_axes.set_title("SK Hynix Volume")
bottom_axes.get_yaxis().get_major_formatter().set_scientific(False)  # 과학적 표기 비활성화
bottom_axes.legend()

# 레이아웃 조정 및 그래프 출력
plt.tight_layout()
plt.show()
