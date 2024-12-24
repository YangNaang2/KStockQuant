import win32com.client
instStockChart = win32com.client.Dispatch("CpSysDib.StockChart")

# 0은 종목 코드, 뒤는 종목 코드 값
instStockChart.SetInputValue(0, "A003540")
# 기간으로 요청시 '1', 개수로 요청시 '2'
instStockChart.SetInputValue(1, ord('2'))
# 최근 거래일로부터 10일 치에 해당하는 데이터
instStockChart.SetInputValue(4, 10)
# 5는 종가 값
#instStockChart.SetInputValue(5, 5)
# 일자별로 시가, 고가, 저가, 종가, 거래량 구하기
instStockChart.SetInputValue(5, (0, 2, 3, 4, 5, 8))
#'D' 일 단위의 데이터
instStockChart.SetInputValue(6, ord('D'))
# 수정 주가의 반영 여부
instStockChart.SetInputValue(9, ord('1'))

instStockChart.BlockRequest()

numData = instStockChart.GetHeaderValue(3)
numField = instStockChart.GetHeaderValue(1)

for i in range(numData):
    for j in range(numField):
        print(instStockChart.GetDataValue(j, i), end=" ")
    print("")

#조회 날짜 설정시
instStockChart.SetInputValue(1, ord('1'))
instStockChart.SetInputValue(2, 20161031)
instStockChart.SetInputValue(3, 20161020)