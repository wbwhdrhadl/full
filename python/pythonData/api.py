import requests
import json

# 사용할 인증키와 요청할 URL 설정
api_key = "여기에_인증키_입력"
url = f"http://openapi.seoul.go.kr:8088/6f56774f4d6461653130355164414e79/json/citydata/1/5/광화문·덕수궁"

try:
    # API에 GET 요청 보내기
    response = requests.get(url)

    # 요청이 성공하면 상태코드 200을 반환함
    if response.status_code == 200:
        # XML 형식으로 반환된 데이터를 파싱하여 사용
        data = json.loads(response.text)
        print(data)  # 받은 데이터 출력
        print("위치", data["RTE_CONGEST_1"])  # "John" 출력
        print("혼잡도", data["RTE_SECT"])  # 30 출력
    else:
        # 상태코드가 200이 아니면 요청 실패 메시지 출력
        print(f"API 요청 실패 - 상태코드: {response.status_code}")

except requests.exceptions.RequestException as e:
    # 요청 중 예외 발생 시 에러 메시지 출력
    print(f"API 요청 중 오류 발생: {e}")
