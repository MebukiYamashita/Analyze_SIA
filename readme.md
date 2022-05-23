# Starbucks Influence Area(SIA)

## - Introduce
인터넷 기사에서 흔히 볼 수 있는 표현인 스세권(SIA)!
스타벅스라는 단일 브랜드가 해당 지역의 인구 밀집 또는 번화가로서 기능하는 것 뿐만 아니라
해당 지역의 부동산 가격과도 연결될만큼 스타벅스라는 브랜드는 인구 밀집 지역에서 꽤 중요한 브랜드로 인식되고 있다.
여기서 우리는 3가지 가설을 세울 수 있다.

### 가설 1 → 인구가 많은 지역에는 스타벅스의 수가 많다?
### 가설 2 → 스타벅스가 많은 지역과 부동산 가격의 상관관계
### 가설 3 → 해외에서도 스세권이라는 개념이 성립하는가?


해당 가설의 경우 세계적으로 유명한 주제며
솔직히 사회인들의 입장에서, 당연히 해당 가설이 성립하겠지? 라고 생각하는게 사회통념적인 인식이다.

그러나 최근 기사와 논문을 참고해보자.

https://biz.chosun.com/distribution/food/2021/12/28/XTKICN5WJZBCRM23GR64BUFYIM/  
위의 기사에서는 DT 매장의 확대로 스타벅스가 더 이상 번화가의 상징으로 기능하지 않는다고 한다.

DOI : 10.22905/kaopqj.2020.54.1.77  
논문에 의하면 16년도 기준으로 스타벅스의 입지 상승효과는 불분명하다는 결론이 있다.


## 진행 순서
### 1번 가설의 경우
    1. 스타벅스 공식 홈페이지에서 지역 검색을 통해 지역 내 매장 위치 데이터를 얻는다.
    2. 각 지역별 인구 데이터를 얻는다.
    3. 받은 데이터를 정제하고 인구 수와 매장 수의 상관관계를 분석한다.

### 2번 가설의 경우
    1. 1번 가설에서 가져온 스타벅스의 지역 데이터를 활용한다.
    2. 국토교통부에서 제공하는 집값이 가장 비싼 지역의 데이터를 사용한다.
    3. 두 데이터의 상관관계를 분석한다.

### 3번 가설의 경우
    1. 스타벅스 일본 홈페이지에서 매장 별 데이터를 받는다.
    - Q: 스타벅스는 매장 데이터의 좌표가 없는데 어떻게 해야할까?
    2. 1번 가설이 성립하는지 분석한다.

## - 사전 준비
    1. Data Crawling
    - 사용 라이브러리: BeautifulSoup, Selenium
    2. Data Pre-processing 
    - 사용 라이브러리: ggplot
    3. Data Analyze
    - 사용 라이브러리: Matplotlib, Folium, pandas

