### API(응용프로그램인터페이스)

- 주소로 요청을 보내면 문서로 응답해준다

```python
import requests
order_currency='BTC'
payment_currency='KRW'
URL=f'주소{order_currency}{payment_currency}'
response=requests.get(URL)
print(response,type(response) )
```

- http요청 헤더에 클라이언트 아이디와 클라이언트 시크릿을 추가해야합니다.(호출횟수제한)

```python
import request
URL='https:apiagify.io'
params={
    'name':'hyunjung'
}
response= requests.get(URL, params).json()
print(response)
```





```python
import requests
BASE_URL=주소
path='/movie/popular'
params={
    'api_key':값
    'language':'KO-KR'
}
response=requests.get(BASE_URL+path, params).json()
print(response)

```

