#최근 60일치 거래량을 volumes라는 리스트에 저장
import win32com.client

instStockChart = win32com.client.Dispatch("CpSysDib.StockChart")

instStockChart.SetInputValue(0, "A003540")
instStockChart.SetInputValue(1, ord('2'))
instStockChart.SetInputValue(4, 60)
instStockChart.SetInputValue(5, 8)
instStockChart.SetInputValue(6, ord('D'))
instStockChart.SetInputValue(9, ord('1'))

instStockChart.BlockRequest()

volumes = []
numData = instStockChart.GetHeaderValue(3)
for i in range(numData):
    volume = instStockChart.GetDataValue(0, i)
    volumes.append(volume)
print(volumes)

#거래량이 1000% 급증했는지 확인하는 코드
#평균 거래량 계산. volumes[0]은 최근 거래일 거래량이니까 제외하고 59개의 평균 계산
averageVolume = (sum(volumes) - volumes[0]) / (len(volumes) -1)

if (volumes[0] > averageVolume * 10):
    print("대박 주")
else:
    print("일반 주", volumes[0] / averageVolume)
