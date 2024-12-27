import win32com.client

#객체 생성
instMarketEye = win32com.client.Dispatch("CpSysDib.MarketEye")

#SetInputValue 메서드
# type 0에 요청하고자 하는 필드 값 설정. 4, 67, 70, 111 -> 현재가, PER, EPS, 최근분기년월
instMarketEye.SetInputValue(0, (4, 67, 70, 111))
# type 1에 조회할 종목에 대한 종목 코드
instMarketEye.SetInputValue(1, 'A003540')

#BlockRequest
instMarketEye.BlockRequest()

#GetDataValue(a,b) a: 필드에 대한 인덱스 b: 종목의 인덱스
print("현재가: ", instMarketEye.GetDataValue(0,0))
print("PER: ", instMarketEye.GetDataValue(1,0))
print("EPS: ", instMarketEye.GetDataValue(2,0))
print("최근분기년월: ", instMarketEye.GetDataValue(3,0))
