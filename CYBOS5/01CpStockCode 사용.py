import win32com.client
instCpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")
stockNum = instCpStockCode.GetCount()

print(instCpStockCode.GetCount()) #주식시장 항목 수 확인

print('\n')

print(instCpStockCode.GetData(0,0)) #0번 위치의 종목코드
print(instCpStockCode.GetData(1,0)) #0번 위치의 종목명
print(instCpStockCode.GetData(2,0)) #0번 위치의 full code

print('\n')

for i in range(0, 10): #0~9인덱스 해당 종목명 출력
    print(instCpStockCode.GetData(1,i))

print('\n')

for i in range(stockNum): #for문 돌면서 naver 찾기
    if instCpStockCode.GetData(1, i) == 'NAVER':
        print(instCpStockCode.GetData(0,i))
        print(instCpStockCode.GetData(1,i))
        print(i)

print('\n')

naverCode = instCpStockCode.NameToCode('NAVER')
naverIndex = instCpStockCode.CodeToIndex(naverCode)
print(naverCode)
print(naverIndex)
