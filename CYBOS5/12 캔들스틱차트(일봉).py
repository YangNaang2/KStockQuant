import yfinance as yf
import matplotlib.pyplot as plt
import mplfinance as mpf
import matplotlib.ticker as ticker

# 1. 데이터 가져오기
start_date = "2016-03-01"
end_date = "2016-03-31"
ticker_symbol = "000660.KS"  # SK 하이닉스 (KOSPI)

# yfinance로 데이터 다운로드
skhynix = yf.download(ticker_symbol, start=start_date, end=end_date)

# 2. 열 이름 재설정
# MultiIndex를 단순한 Index로 변환
skhynix.columns = [col[0] for col in skhynix.columns]

# 3. 데이터 전처리: NaN 값 제거 및 거래량이 0인 날 제외
skhynix.dropna(inplace=True)  # NaN 값이 있는 행 제거
skhynix = skhynix[skhynix['Volume'] > 0]  # 거래량이 0인 날 제외

# 4. x축 레이블 설정
day_list = []
name_list = []
for i, day in enumerate(skhynix.index):
    if day.dayofweek == 0:  # 월요일만 선택
        day_list.append(i)
        name_list.append(day.strftime('%Y-%m-%d') + '(Mon)')

# 5. 캔들스틱 차트 그리기
fig, ax = plt.subplots(figsize=(12, 8))

# mplfinance로 캔들스틱 차트 추가
mpf.plot(
    skhynix,
    type='candle',
    ax=ax,
    style='charles',
    show_nontrading=False
)

# x축 레이블 커스터마이징
ax.xaxis.set_major_locator(ticker.FixedLocator(day_list))
ax.xaxis.set_major_formatter(ticker.FixedFormatter(name_list))

# 차트 꾸미기
plt.grid()
plt.title(f"{ticker_symbol} Candlestick Chart")
plt.show()
