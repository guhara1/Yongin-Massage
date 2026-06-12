# 지역별 안내 — 용인시 허브 1개 + 구 허브 3개 + 대표 지역 30곳.
# 숫자 행정동(유림1동, 동백2동, 죽전3동 등) 개별 페이지는 만들지 않는다.
# 구별 페이지 본문은 areas_cheoin / areas_giheung / areas_suji 모듈에 나눠 작성한다.
from .site import PHONE, PHONE_DISPLAY
from .pricing import PRICING
from .areas_cheoin import PAGES as CHEOIN_PAGES
from .areas_giheung import PAGES as GIHEUNG_PAGES
from .areas_suji import PAGES as SUJI_PAGES

_CTA = f"""
<section class="cta">
<h2>예약문의</h2>
<p>계신 곳 위치와 원하시는 시간을 말씀해 주시면 배정 가능 여부를 곧바로 확인해 드립니다.</p>
<a class="cta-phone" href="tel:{PHONE}">{PHONE_DISPLAY}</a>
</section>
"""

_HUB_BODY = """
<p class="lead">용인 방문 관리는 처인구·기흥구·수지구 세 개 구와 대표 지역 서른 곳을 기준으로 안내합니다. 숫자가 붙은 행정동에 거주하셔도 아래 대표 지역 페이지에서 필요한 정보를 모두 확인하실 수 있습니다.</p>

<section>
<h2>용인 지역 안내 구성</h2>
<p>용인시는 면적이 서울보다 넓은 도시라, 같은 용인이라도 생활권에 따라 동네 분위기와 이동 시간이 크게 다릅니다. 동쪽 처인구는 시청과 원도심, 그리고 포곡읍·백암면 같은 읍·면 지역이 함께 있는 도농복합 생활권이고, 서쪽 기흥구는 수인분당선 역세권을 따라 택지지구와 산업단지가 이어지는 지역이며, 북서쪽 수지구는 신분당선을 축으로 아파트 단지가 밀집한 주거 중심 생활권입니다. 행정 구역으로는 읍 5곳, 면 2곳에 행정동이 30개 가까이 되지만, 이 사이트는 생활권이 같은 곳을 묶어 구 허브 3곳과 대표 지역 30곳으로 안내합니다. 같은 동네를 잘게 쪼개 비슷한 설명을 반복하면 정작 필요한 정보를 찾기 어렵고, 방문 가능 여부도 행정동 경계가 아니라 실제 주소와 예약 시간으로 판단하기 때문입니다.</p>
</section>

<section>
<h2>구별 안내 세 곳</h2>
<ul class="card-grid">
<li><a href="/yongin-si/cheoin-gu/">처인구</a></li>
<li><a href="/yongin-si/giheung-gu/">기흥구</a></li>
<li><a href="/yongin-si/suji-gu/">수지구</a></li>
</ul>
<p>처인구는 용인시청과 용인중앙시장이 있는 원도심부터 에버라인 연선의 읍·면까지 범위가 가장 넓은 구입니다. 기흥구는 기흥역과 구성역을 비롯한 역세권, 동백·흥덕 같은 택지지구가 모여 있어 문의가 가장 고르게 들어오는 지역이고, 수지구는 수지구청역과 죽전·상현 일대의 대단지 아파트가 중심입니다. 구 허브 페이지에서는 각 구의 생활권 구분과 대표 지역 목록, 구별 이동 시간 특징을 정리해 두었습니다.</p>
</section>

<section>
<h2>대표 지역 서른 곳</h2>
<p>처인구 — <a href="/yongin-si/cheoin-gu/pogok-eup/">포곡읍</a>, <a href="/yongin-si/cheoin-gu/mohyeon-eup/">모현읍</a>, <a href="/yongin-si/cheoin-gu/idong-eup/">이동읍</a>, <a href="/yongin-si/cheoin-gu/namsa-eup/">남사읍</a>, <a href="/yongin-si/cheoin-gu/yangji-eup/">양지읍</a>, <a href="/yongin-si/cheoin-gu/wonsam-myeon/">원삼면</a>, <a href="/yongin-si/cheoin-gu/baegam-myeon/">백암면</a>, <a href="/yongin-si/cheoin-gu/jungang-dong/">중앙동</a>, <a href="/yongin-si/cheoin-gu/yeokbuk-dong/">역북동</a>, <a href="/yongin-si/cheoin-gu/samga-dong/">삼가동</a>, <a href="/yongin-si/cheoin-gu/yurim-dong/">유림동</a>, <a href="/yongin-si/cheoin-gu/dongbu-dong/">동부동</a></p>
<p>기흥구 — <a href="/yongin-si/giheung-gu/singal-dong/">신갈동</a>, <a href="/yongin-si/giheung-gu/yeongdeok-dong/">영덕동</a>, <a href="/yongin-si/giheung-gu/gugal-dong/">구갈동</a>, <a href="/yongin-si/giheung-gu/sanggal-dong/">상갈동</a>, <a href="/yongin-si/giheung-gu/bora-dong/">보라동</a>, <a href="/yongin-si/giheung-gu/giheung-dong/">기흥동</a>, <a href="/yongin-si/giheung-gu/seonong-dong/">서농동</a>, <a href="/yongin-si/giheung-gu/guseong-dong/">구성동</a>, <a href="/yongin-si/giheung-gu/mabuk-dong/">마북동</a>, <a href="/yongin-si/giheung-gu/dongbaek-dong/">동백동</a>, <a href="/yongin-si/giheung-gu/sangha-dong/">상하동</a>, <a href="/yongin-si/giheung-gu/bojeong-dong/">보정동</a></p>
<p>수지구 — <a href="/yongin-si/suji-gu/pungdeokcheon-dong/">풍덕천동</a>, <a href="/yongin-si/suji-gu/sinbong-dong/">신봉동</a>, <a href="/yongin-si/suji-gu/jukjeon-dong/">죽전동</a>, <a href="/yongin-si/suji-gu/dongcheon-dong/">동천동</a>, <a href="/yongin-si/suji-gu/sanghyeon-dong/">상현동</a>, <a href="/yongin-si/suji-gu/seongbok-dong/">성복동</a></p>
</section>

<section>
<h2>행정동 통합 기준</h2>
<p>숫자로 나뉜 행정동은 대표 지역 한 곳으로 통합해 안내합니다. 처인구 유림1동·유림2동은 유림동 페이지에서, 기흥구 영덕1동·영덕2동은 영덕동 페이지에서, 동백1동부터 동백3동까지는 동백동 페이지에서 함께 다룹니다. 수지구도 마찬가지로 풍덕천1동·풍덕천2동은 풍덕천동, 죽전1동부터 죽전3동까지는 죽전동, 상현1동부터 상현3동까지는 상현동 페이지로 통합됩니다. 숫자 동 단위의 개별 페이지는 만들지 않습니다. 또한 행정동과 법정동 이름이 다른 경우도 많습니다. 예를 들어 중앙동 주소에는 김량장동이, 동부동에는 마평동이, 동백동에는 중동이 포함될 수 있습니다. 어느 경우든 예약 시 도로명 주소만 알려주시면 같은 기준으로 안내해 드립니다.</p>
</section>

<section>
<h2>지역과 역세권을 함께 확인하세요</h2>
<p>용인은 수인분당선, 신분당선, 용인 에버라인 세 노선이 지나는 도시라 동 이름보다 역 이름이 익숙한 분들도 많습니다. 기흥역, 죽전역, 수지구청역처럼 역 인근에서 예약하실 때는 <a href="/yongin-si/stations/">지하철역별 안내</a>를 함께 보시면 위치 설명이 쉬워집니다. 역 페이지는 해당 역세권의 분위기와 인접 대표 지역을 연결해 설명하며, 역과 지역과 테마를 조합한 별도 페이지는 운영하지 않습니다. 원하시는 관리 유형은 <a href="/themes/">테마별 안내</a>에서 따로 고르시면 되고, 어느 페이지를 보시든 예약 기준은 동일합니다.</p>
</section>

<section>
<h2>예약 전 참고사항</h2>
<p>서른 개 지역 모두 예약 절차는 같습니다. 위치와 시간, 코스와 인원을 확인한 뒤 배정 가능 여부를 안내받고 확정하는 순서이며, 용인은 생활권이 넓어 같은 시각이라도 수지구와 처인구 읍·면 지역의 도착 시간이 다를 수 있습니다. 저녁과 주말은 문의가 몰리므로 미리 연락 주시는 편이 좋고, 아파트는 동·호수와 공동현관 출입 방법을, 호텔과 오피스텔은 건물 출입 안내를 함께 알려주시면 방문이 매끄럽습니다. 수원, 성남, 화성, 광주 등 인접 도시와 맞닿은 경계 주소도 위치에 따라 가능할 수 있으니 전화로 확인해 주세요.</p>
</section>

<section>
<h2>자주 묻는 질문</h2>
<div class="faq-item">
<h3>우리 동네 행정동 이름이 목록에 없어요.</h3>
<p>숫자가 붙은 행정동은 대표 지역 페이지에 통합되어 있습니다. 죽전2동은 죽전동 페이지, 동백3동은 동백동 페이지를 보시면 됩니다. 김량장동이나 중동처럼 법정동 주소도 각각 중앙동·동백동 페이지에서 다룹니다.</p>
</div>
<div class="faq-item">
<h3>구 경계나 시 경계에 가까운 위치는 어떻게 하나요?</h3>
<p>경계 지역은 어느 쪽 페이지를 보셔도 괜찮습니다. 실제 방문은 행정 구역이 아닌 주소 기준으로 진행되므로, 예약 전화에서 건물 주소만 정확히 알려주시면 됩니다.</p>
</div>
</section>
""" + PRICING + _CTA

HUB = {
    "path": "yongin-si/",
    "title": "용인 지역별 출장마사지·홈타이 안내 | 처인구·기흥구·수지구",
    "desc": "용인 방문 마사지 지역별 안내입니다. 처인구·기흥구·수지구와 대표 지역 30곳의 생활권 특징, 방문 조건을 확인하세요.",
    "h1": "용인 지역별 방문 관리 안내",
    "body": _HUB_BODY,
    "breadcrumb": [("지역별 안내", None)],
}

PAGES = [HUB] + CHEOIN_PAGES + GIHEUNG_PAGES + SUJI_PAGES
