# 지하철역별 안내 — 허브 1개 + 역 24곳 (수인분당선 6 + 신분당선 4 + 에버라인 14).
# 기흥역은 수인분당선·에버라인 환승역이지만 URL은 하나만 사용한다.
# 출구별 페이지, 역+테마 조합 페이지는 만들지 않는다.
from .site import PHONE, PHONE_DISPLAY
from .pricing import PRICING
from .stations_bundang import PAGES as BUNDANG_PAGES
from .stations_everline import PAGES as EVERLINE_PAGES

_CTA = f"""
<section class="cta">
<h2>예약문의</h2>
<p>가까운 역과 건물 주소를 말씀해 주시면 배정 가능 여부를 곧바로 확인해 드립니다.</p>
<a class="cta-phone" href="tel:{PHONE}">{PHONE_DISPLAY}</a>
</section>
"""

_HUB_BODY = """
<p class="lead">용인을 지나는 수인분당선, 신분당선, 용인 에버라인의 주요 역 스물네 곳을 역세권 기준으로 안내합니다. 환승역도 페이지는 하나만 운영하며, 출구별 안내 페이지는 만들지 않습니다.</p>

<section>
<h2>용인 지하철 노선 구성</h2>
<p>용인의 철도 교통은 세 노선이 분담합니다. 수인분당선은 죽전역부터 상갈역까지 수지구와 기흥구를 남북으로 가로지르며 분당과 수원을 잇는 가장 오래된 축입니다. 신분당선은 동천역부터 상현역까지 수지구를 관통해 강남까지 한 번에 닿는 노선이라 출퇴근 수요가 가장 많습니다. 용인 에버라인은 기흥역에서 전대·에버랜드역까지 기흥구 동백 지구와 처인구 원도심, 포곡읍을 잇는 경전철로, 시청과 에버랜드 방면 생활권을 책임집니다. 역 이름이 익숙하다면 동 이름 대신 역 기준으로 위치를 알려주셔도 예약 안내는 동일하게 진행됩니다.</p>
</section>

<section>
<h2>수인분당선 용인권</h2>
<ul class="card-grid">
<li><a href="/yongin-si/stations/jukjeon-station/">죽전역</a></li>
<li><a href="/yongin-si/stations/bojeong-station/">보정역</a></li>
<li><a href="/yongin-si/stations/guseong-station/">구성역</a></li>
<li><a href="/yongin-si/stations/singal-station/">신갈역</a></li>
<li><a href="/yongin-si/stations/giheung-station/">기흥역</a></li>
<li><a href="/yongin-si/stations/sanggal-station/">상갈역</a></li>
</ul>
<p>죽전역 일대는 백화점과 대학가가 함께 있는 수지구 동쪽 관문이고, 보정역과 구성역은 카페거리와 신규 개발 예정지가 섞인 주거 역세권입니다. 신갈역과 기흥역, 상갈역은 기흥구 남부 생활권의 중심으로, 오래된 시가지와 새 아파트가 함께 있어 방문 형태도 다양합니다.</p>
</section>

<section>
<h2>신분당선 용인권</h2>
<ul class="card-grid">
<li><a href="/yongin-si/stations/dongcheon-station/">동천역</a></li>
<li><a href="/yongin-si/stations/suji-gu-office-station/">수지구청역</a></li>
<li><a href="/yongin-si/stations/seongbok-station/">성복역</a></li>
<li><a href="/yongin-si/stations/sanghyeon-station/">상현역</a></li>
</ul>
<p>네 역 모두 수지구의 아파트 밀집 지역을 지나며, 강남 방면 출퇴근 인구가 많아 평일 저녁 문의가 집중되는 권역입니다. 수지구청역은 수지 상권의 중심, 성복역은 대형 쇼핑몰과 고급 주거지가 모인 곳, 동천역과 상현역은 각각 성남·수원 경계와 맞닿은 생활권입니다.</p>
</section>

<section>
<h2>용인 에버라인</h2>
<ul class="card-grid">
<li><a href="/yongin-si/stations/giheung-station/">기흥역</a></li>
<li><a href="/yongin-si/stations/gangnam-univ-station/">강남대역</a></li>
<li><a href="/yongin-si/stations/jiseok-station/">지석역</a></li>
<li><a href="/yongin-si/stations/eojung-station/">어정역</a></li>
<li><a href="/yongin-si/stations/dongbaek-station/">동백역</a></li>
<li><a href="/yongin-si/stations/chodang-station/">초당역</a></li>
<li><a href="/yongin-si/stations/samga-station/">삼가역</a></li>
<li><a href="/yongin-si/stations/cityhall-yongin-univ-station/">시청·용인대역</a></li>
<li><a href="/yongin-si/stations/myongji-univ-station/">명지대역</a></li>
<li><a href="/yongin-si/stations/gimnyangjang-station/">김량장역</a></li>
<li><a href="/yongin-si/stations/stadium-songdam-station/">운동장·송담대역</a></li>
<li><a href="/yongin-si/stations/gojin-station/">고진역</a></li>
<li><a href="/yongin-si/stations/bopyeong-station/">보평역</a></li>
<li><a href="/yongin-si/stations/dunjeon-station/">둔전역</a></li>
<li><a href="/yongin-si/stations/jeondae-everland-station/">전대·에버랜드역</a></li>
</ul>
<p>에버라인은 기흥구 동백 지구를 지나 처인구 원도심과 포곡읍까지 이어지는 노선입니다. 동백역·어정역·초당역은 동백 생활권, 시청·용인대역부터 김량장역까지는 처인구 행정·시장 중심지, 둔전역과 전대·에버랜드역은 포곡읍과 에버랜드 방면을 담당합니다.</p>
</section>

<section>
<h2>환승역과 단일 페이지 원칙</h2>
<p>기흥역은 수인분당선과 에버라인이 만나는 용인의 대표 환승역이지만, 안내 페이지는 하나만 운영합니다. 노선이 두 개라고 같은 역을 두 페이지로 나누면 내용이 중복될 뿐 이용자에게 도움이 되지 않기 때문입니다. 같은 이유로 출구 번호별 페이지, 특정 역과 관리 테마를 조합한 페이지도 만들지 않습니다. 역 페이지에서는 역세권 분위기, 인접 대표 지역, 예약이 몰리는 시간대, 방문 전 준비사항을 다루고, 관리 유형이 궁금하시면 <a href="/themes/">테마별 안내</a>에서 따로 확인하시면 됩니다.</p>
</section>

<section>
<h2>역 페이지 활용법</h2>
<p>역 페이지는 위치 설명이 쉬운 분들을 위한 입구일 뿐, 실제 방문 가능 여부는 건물 주소와 예약 시간으로 판단합니다. 역에서 멀리 떨어진 곳이라면 <a href="/yongin-si/">지역별 안내</a>의 대표 지역 페이지가 더 정확하고, 모현읍이나 백암면처럼 철도가 지나지 않는 곳도 차량 이동 기준으로 안내해 드립니다. 예약 전화에서는 가까운 역 이름과 함께 도로명 주소를 알려주시면 확인이 가장 빠릅니다. 특히 신분당선과 수인분당선이 모두 가까운 죽전·보정 일대, 에버라인과 분당선이 겹치는 기흥역 일대는 어느 역 페이지를 보셔도 같은 기준으로 안내되니 익숙한 역을 고르시면 됩니다.</p>
</section>

<section>
<h2>예약이 몰리는 시간대</h2>
<p>노선별로 문의가 몰리는 시간대가 조금씩 다릅니다. 신분당선 연선은 강남 방면 출퇴근 인구가 많아 평일 밤 9시 이후 자택 예약이 집중되고, 수인분당선 연선은 주말 낮과 저녁 문의가 고르게 들어옵니다. 에버라인 연선은 에버랜드 방문객의 숙소 예약과 처인구 원도심의 당일 예약이 섞여 주말 비중이 높은 편입니다. 원하는 시간대가 분명하다면 한두 시간 여유를 두고 미리 연락 주시는 편이 배정에 유리합니다.</p>
</section>

<section>
<h2>자주 묻는 질문</h2>
<div class="faq-item">
<h3>기흥역은 분당선 페이지와 에버라인 페이지가 따로 있나요?</h3>
<p>아니요. 환승역도 페이지는 하나입니다. 기흥역 페이지에서 두 노선 이용자 모두에게 필요한 내용을 함께 안내합니다.</p>
</div>
<div class="faq-item">
<h3>역에서 먼 동네는 어디를 보면 되나요?</h3>
<p>철도가 지나지 않는 모현읍, 이동읍, 남사읍, 양지읍, 원삼면, 백암면은 지역별 안내의 각 대표 지역 페이지에서 차량 이동 기준으로 안내합니다.</p>
</div>
</section>
""" + PRICING + _CTA

HUB = {
    "path": "yongin-si/stations/",
    "title": "용인 지하철역별 출장마사지·홈타이 안내 | 역세권 방문 관리",
    "desc": "수인분당선·신분당선·용인 에버라인 24개 역 기준 방문 관리 안내입니다. 역세권 특징과 예약 방법을 확인하세요.",
    "h1": "용인 지하철역별 방문 관리 안내",
    "body": _HUB_BODY,
    "breadcrumb": [("지하철역별 안내", None)],
}

PAGES = [HUB] + BUNDANG_PAGES + EVERLINE_PAGES
