<h1>카카오톡 단어 분석 to JSON (2024.07)</h1>

<pre><code>"name": "박종범",
    "data": {
        "사진": 4440,
        "나": 2837,
        "이모티콘": 2736,
        "내": 1843,
        "너": 1670,
        "난": 1512,</code></pre>
<h1>사용법</h1>


<h1>사용한것</h1>
<h2>한국어 명사분류(Konlpy)</h2>
https://konlpy.org/ko/latest/morph/ </p>
한국어 Konlpy의 nouns 메소드를 통해 명사를 추출하였다.</p>
<pre><code>$ python3 -m pip install konlpy </code></pre>
<pre><code>import konlpy
from konlpy.tag import Okt</code></pre>




<h2>JSON</h2>
JSON 파일을 만들기 위해 JSON 모듈을 사용하였다.
<pre><code>import json</code></pre>



