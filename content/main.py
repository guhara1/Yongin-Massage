# 메인 페이지 — 허브 역할. 모든 키워드를 밀어 넣지 않고 상세 페이지로 연결한다.
from .site import BASE_URL, BRAND, PHONE, PHONE_DISPLAY
from .pricing import PRICING

_JSONLD = f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "HealthAndBeautyBusiness",
  "name": "{BRAND}",
  "telephone": "{PHONE}",
  "url": "{BASE_URL}/",
  "image": "{BASE_URL}/assets/og-image.png",
  "description": "용인 전지역 방문 출장마사지·홈타이 예약 안내",
  "areaServed": {{
    "@type": "AdministrativeArea",
    "name": "경기도 용인시"
  }},
  "openingHours": "Mo-Su 00:00-24:00",
  "priceRange": "₩90,000 - ₩180,000"
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "용인 전지역 방문이 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "예약 시간, 정확한 위치, 배정 상황에 따라 가능 여부가 달라집니다. 지역별 안내 페이지에서 처인구, 기흥구, 수지구 기준으로 확인할 수 있습니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "기흥역이나 수지구청역 근처도 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "주요 역세권은 역 상세 페이지에서 주변 생활권과 함께 안내합니다. 정확한 가능 여부는 예약 시 위치를 기준으로 확인합니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "죽전1동과 죽전2동은 왜 따로 없나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "죽전1동부터 죽전3동까지는 죽전동 대표 페이지에서 통합 안내하여 중복 페이지 위험을 줄입니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "당일 예약도 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "가능할 수 있지만 저녁 시간대와 주말은 문의가 많을 수 있어 사전 예약을 권장합니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "테마별 관리는 어디에서 확인하나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "스웨디시, 타이마사지, 홈케어 등 테마별 안내 페이지에서 특징과 추천 대상을 확인할 수 있습니다."
      }}
    }}
  ]
}}
</script>
"""

_HERO = f"""<section class="hero">
  <div class="hero-inner">
    <p class="hero-badge">Premium Visiting Spa · 용인 전지역</p>
    <h1>용인 출장마사지·홈타이<br>예약 안내</h1>
    <p class="hero-lead">샵까지 갈 필요 없이, 계신 곳에서 받는 프리미엄 방문 관리.<br>자택·오피스텔·숙소 어디든 전화 한 통이면 예약이 끝납니다.</p>
    <div class="hero-actions">
      <a class="hero-btn primary" href="tel:{PHONE}">📞 {PHONE_DISPLAY}</a>
      <a class="hero-btn" href="/courses/">코스 안내 보기</a>
    </div>
    <ul class="hero-stats">
      <li><strong>30곳</strong><span>대표 지역</span></li>
      <li><strong>24곳</strong><span>역세권 안내</span></li>
      <li><strong>14개</strong><span>관리 테마</span></li>
      <li><strong>24시간</strong><span>예약 상담</span></li>
    </ul>
  </div>
</section>
"""

_BODY = f"""
<section id="service">
<h2>용인 출장마사지·홈타이 서비스 안내</h2>
<p>용인에서 방문 마사지와 홈타이 예약을 찾는 분들을 위해 가능 지역, 예약 절차, 코스 선택 기준, 이용 전 확인사항을 한곳에 정리했습니다. 이 페이지는 용인 전체 구조를 설명하는 허브 역할을 하며, 더 자세한 내용은 지역별·지하철역별·테마별 안내 페이지에서 확인하실 수 있습니다.</p>
</section>

<section id="coverage">
<h2>용인 전지역 방문 가능 안내</h2>
<p>용인은 처인구, 기흥구, 수지구로 생활권이 넓게 나뉘며, 같은 시각이라도 지역에 따라 이동 시간과 배정 가능 여부가 달라질 수 있습니다. 예약 전에는 정확한 위치, 희망 시간, 코스 정보를 기준으로 방문 가능 여부를 확인하는 것이 좋습니다.</p>
</section>

<section id="gu">
<h2>구별 지역 안내</h2>
<ul class="card-grid">
<li><a href="/yongin-si/cheoin-gu/">처인구</a></li>
<li><a href="/yongin-si/giheung-gu/">기흥구</a></li>
<li><a href="/yongin-si/suji-gu/">수지구</a></li>
</ul>
<p>구별 안내는 용인 전체 구조를 이해하기 쉽게 나누는 허브 역할을 합니다. 처인구는 읍·면과 시청 원도심 생활권, 기흥구는 수인분당선 역세권과 택지지구 생활권, 수지구는 신분당선과 아파트 밀집 생활권 중심으로 구성했습니다. <a href="/yongin-si/">용인 전체 안내</a>에서 한눈에 보실 수도 있습니다.</p>
</section>

<section id="areas">
<h2>읍·면·대표 동 안내</h2>
<p>지역별 안내는 구와 대표 지역 30곳 기준으로 구성됩니다. 유림1·2동, 영덕1·2동, 동백1~3동, 풍덕천1·2동, 죽전1~3동, 상현1~3동처럼 숫자로 나뉜 행정동은 별도 페이지를 만들지 않고 대표 지역 페이지에서 통합 안내하여 중복 페이지 위험을 줄입니다.</p>
<p>처인구 — <a href="/yongin-si/cheoin-gu/pogok-eup/">포곡읍</a> · <a href="/yongin-si/cheoin-gu/mohyeon-eup/">모현읍</a> · <a href="/yongin-si/cheoin-gu/idong-eup/">이동읍</a> · <a href="/yongin-si/cheoin-gu/namsa-eup/">남사읍</a> · <a href="/yongin-si/cheoin-gu/yangji-eup/">양지읍</a> · <a href="/yongin-si/cheoin-gu/wonsam-myeon/">원삼면</a> · <a href="/yongin-si/cheoin-gu/baegam-myeon/">백암면</a> · <a href="/yongin-si/cheoin-gu/jungang-dong/">중앙동</a> · <a href="/yongin-si/cheoin-gu/yeokbuk-dong/">역북동</a> · <a href="/yongin-si/cheoin-gu/samga-dong/">삼가동</a> · <a href="/yongin-si/cheoin-gu/yurim-dong/">유림동</a> · <a href="/yongin-si/cheoin-gu/dongbu-dong/">동부동</a></p>
<p>기흥구 — <a href="/yongin-si/giheung-gu/singal-dong/">신갈동</a> · <a href="/yongin-si/giheung-gu/yeongdeok-dong/">영덕동</a> · <a href="/yongin-si/giheung-gu/gugal-dong/">구갈동</a> · <a href="/yongin-si/giheung-gu/sanggal-dong/">상갈동</a> · <a href="/yongin-si/giheung-gu/bora-dong/">보라동</a> · <a href="/yongin-si/giheung-gu/giheung-dong/">기흥동</a> · <a href="/yongin-si/giheung-gu/seonong-dong/">서농동</a> · <a href="/yongin-si/giheung-gu/guseong-dong/">구성동</a> · <a href="/yongin-si/giheung-gu/mabuk-dong/">마북동</a> · <a href="/yongin-si/giheung-gu/dongbaek-dong/">동백동</a> · <a href="/yongin-si/giheung-gu/sangha-dong/">상하동</a> · <a href="/yongin-si/giheung-gu/bojeong-dong/">보정동</a></p>
<p>수지구 — <a href="/yongin-si/suji-gu/pungdeokcheon-dong/">풍덕천동</a> · <a href="/yongin-si/suji-gu/sinbong-dong/">신봉동</a> · <a href="/yongin-si/suji-gu/jukjeon-dong/">죽전동</a> · <a href="/yongin-si/suji-gu/dongcheon-dong/">동천동</a> · <a href="/yongin-si/suji-gu/sanghyeon-dong/">상현동</a> · <a href="/yongin-si/suji-gu/seongbok-dong/">성복동</a></p>
</section>

<section id="stations">
<h2>지하철역 인근 안내</h2>
<p>지하철역별 안내는 수인분당선, 신분당선, 용인 에버라인 기준으로 구성합니다. 각 역 페이지에서는 인근 생활권과 대표 지역, 방문 전 준비사항을 설명하며, 출구별 페이지나 역과 테마를 조합한 페이지는 만들지 않습니다.</p>
<ul class="card-grid">
<li><a href="/yongin-si/stations/giheung-station/">기흥역</a></li>
<li><a href="/yongin-si/stations/jukjeon-station/">죽전역</a></li>
<li><a href="/yongin-si/stations/bojeong-station/">보정역</a></li>
<li><a href="/yongin-si/stations/guseong-station/">구성역</a></li>
<li><a href="/yongin-si/stations/singal-station/">신갈역</a></li>
<li><a href="/yongin-si/stations/sanggal-station/">상갈역</a></li>
<li><a href="/yongin-si/stations/dongcheon-station/">동천역</a></li>
<li><a href="/yongin-si/stations/suji-gu-office-station/">수지구청역</a></li>
<li><a href="/yongin-si/stations/seongbok-station/">성복역</a></li>
<li><a href="/yongin-si/stations/sanghyeon-station/">상현역</a></li>
<li><a href="/yongin-si/stations/dongbaek-station/">동백역</a></li>
<li><a href="/yongin-si/stations/cityhall-yongin-univ-station/">시청·용인대역</a></li>
<li><a href="/yongin-si/stations/myongji-univ-station/">명지대역</a></li>
<li><a href="/yongin-si/stations/gimnyangjang-station/">김량장역</a></li>
<li><a href="/yongin-si/stations/jeondae-everland-station/">전대·에버랜드역</a></li>
</ul>
<p>전체 24개 역 목록은 <a href="/yongin-si/stations/">지하철역별 안내</a>에서 확인하실 수 있습니다.</p>
</section>

<section id="themes">
<h2>테마별 관리 안내</h2>
<p>테마별 안내에서는 관리 유형별 특징, 추천 대상, 예약 전 확인사항을 설명합니다. 테마는 각각 독립 페이지로 운영하고, 지역·역 페이지에서는 관련 테마로 연결만 해 드립니다. 원하시는 관리 유형을 먼저 고른 뒤 예약 시 위치를 알려주시면 됩니다.</p>
<ul class="card-grid">
<li><a href="/themes/swedish/">스웨디시</a></li>
<li><a href="/themes/lomilomi/">로미로미</a></li>
<li><a href="/themes/thai/">타이마사지</a></li>
<li><a href="/themes/chinese/">중국마사지</a></li>
<li><a href="/themes/aroma/">아로마테라피</a></li>
<li><a href="/themes/homecare/">홈케어</a></li>
<li><a href="/themes/hotel-style/">호텔식마사지</a></li>
<li><a href="/themes/foot/">발마사지</a></li>
<li><a href="/themes/sports/">스포츠·경락</a></li>
<li><a href="/themes/skincare/">스킨케어</a></li>
<li><a href="/themes/waxing/">왁싱</a></li>
<li><a href="/themes/couple/">커플 관리</a></li>
<li><a href="/themes/24hours/">24시간</a></li>
<li><a href="/themes/overnight/">수면 가능</a></li>
</ul>
</section>

<section id="course">
<h2>코스 선택 안내</h2>
<p>코스는 이용 목적과 그날의 컨디션에 따라 선택하시는 것이 좋습니다. 누적된 피로를 풀고 싶은 분, 편안한 휴식이 필요한 분, 운동 후 근육 이완이 필요한 분, 숙소로 방문을 원하시는 분, 커플이 함께 받고 싶은 분 등 상황에 맞는 선택 기준을 <a href="/courses/">코스안내</a> 페이지에서 자세히 다룹니다.</p>
</section>

<section id="how">
<h2>예약 진행 방식</h2>
<p>예약은 다섯 단계로 진행됩니다. 먼저 희망 지역 또는 역 인근 위치를 확인하고, 희망 시간을 확인한 뒤, 코스와 인원을 정하고, 방문 가능 여부를 안내받은 다음, 예약을 확정합니다. 용인은 생활권이 넓어 처인구·기흥구·수지구에 따라 이동 가능 시간이 달라질 수 있습니다. 자세한 절차는 <a href="/reservation/">예약안내</a>에서 확인하세요.</p>
</section>

<section id="check">
<h2>이용 전 확인사항</h2>
<p>원활한 방문 관리를 위해 정확한 주소, 공동현관 출입 방법, 주차 가능 여부, 조용한 공간 확보 여부를 미리 확인해 주시면 좋습니다. 숙소나 오피스텔로 방문을 요청하실 때는 건물 출입 안내와 예약 시간대 연락 가능 여부를 함께 알려주세요. 준비사항 전체는 <a href="/guide/">이용가이드</a>에 정리되어 있습니다.</p>
</section>

<section id="safety">
<h2>위생 및 안전 안내</h2>
<p>건전하고 안전한 방문 관리를 위해 위생 기준, 예약 정보 확인, 개인정보 보호, 금지행위 안내를 명확히 제공합니다. 이용 전 서비스 범위와 유의사항을 확인해 주시고, 불법적이거나 무리한 요청은 어떤 경우에도 진행하지 않는다는 기준을 분명히 안내드립니다.</p>
</section>

<section id="faq">
<h2>자주 묻는 질문</h2>
<div class="faq-item">
<h3>용인 전지역 방문이 가능한가요?</h3>
<p>예약 시간, 정확한 위치, 배정 상황에 따라 가능 여부가 달라집니다. 지역별 안내 페이지에서 처인구, 기흥구, 수지구 기준으로 확인할 수 있습니다.</p>
</div>
<div class="faq-item">
<h3>기흥역이나 수지구청역 근처도 가능한가요?</h3>
<p>주요 역세권은 역 상세 페이지에서 주변 생활권과 함께 안내합니다. 정확한 가능 여부는 예약 시 위치를 기준으로 확인합니다.</p>
</div>
<div class="faq-item">
<h3>죽전1동과 죽전2동은 왜 따로 없나요?</h3>
<p>죽전1동부터 죽전3동까지는 죽전동 대표 페이지에서 통합 안내하여 중복 페이지 위험을 줄입니다.</p>
</div>
<div class="faq-item">
<h3>당일 예약도 가능한가요?</h3>
<p>가능할 수 있지만 저녁 시간대와 주말은 문의가 많을 수 있어 사전 예약을 권장합니다.</p>
</div>
<div class="faq-item">
<h3>테마별 관리는 어디에서 확인하나요?</h3>
<p>스웨디시, 타이마사지, 홈케어 등 테마별 안내 페이지에서 특징과 추천 대상을 확인할 수 있습니다.</p>
</div>
</section>

{PRICING}
<section id="contact" class="cta">
<h2>예약문의</h2>
<p>용인 방문 관리 예약과 상담은 전화로 가장 빠르게 진행됩니다. 위치와 희망 시간을 알려주시면 가능 여부를 바로 확인해 드립니다.</p>
<a class="cta-phone" href="tel:{PHONE}">{PHONE_DISPLAY}</a>
</section>
"""

PAGE = {
    "path": "",
    "title": "용인 출장마사지·홈타이 | 용인 전지역 방문 마사지 예약 안내",
    "desc": "용인 출장마사지·홈타이 안내입니다. 처인구·기흥구·수지구와 주요 역세권, 테마별 관리, 예약 전 확인사항을 확인해보세요.",
    "h1": "용인 출장마사지·홈타이 예약 안내",
    "body": _BODY,
    "extra_head": '<meta name="naver-site-verification" content="44ff55e324e1184de4c32682d74719bb4507fbb2" />\n' + _JSONLD,
    "breadcrumb": [],
    "hero": _HERO,
}
