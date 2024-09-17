<h1>[Python]카카오톡 대화 분석 프로그램</h1>
<h3>카카오톡 대화 내용을 분석하여 가장 많이 사용된 단어를 추출하고, 시간대별로 카톡 기록을 분석하여 표로 볼수있고 , JSON 파일로 확인할수있다.</h3>

![kakao_screenshot1720682479991](https://github.com/asa9874/Kakao_Word_Analysis/assets/84450816/496f1976-0484-45b1-bfc7-8e8e78198077)

=>

![image](https://github.com/user-attachments/assets/9962751c-587d-4e0d-ab59-461fccb00aa9)

<pre><code>"name": "단호한 포돌이",
    "data": {
        "사진": 4440,
        "나": 2837,
        "이모티콘": 2736,
        "내": 1843,
        "너": 1670,
        "난": 1512,</code></pre>

        
<h1>1.사용법</h1>
<h2>1-1.카카오톡 대화기록준비</h2>
<h3>1-1-1.카카오톡 대화방에서 대화내용 내보내기로 카카오톡 내화내용.txt를 얻는다.</h3>

![image](https://github.com/asa9874/Kakao_Word_Analysis/assets/84450816/cc0c5ad5-6082-4c17-961a-c1c70bc59461)

![image](https://github.com/asa9874/Kakao_Word_Analysis/assets/84450816/c3d043a5-2ee1-403b-ab96-fcd2b75ecfe7)

<h3>1-1-2.txt파일 이름을 kakao.txt로 바꿔준다.</h3>

![image](https://github.com/asa9874/Kakao_Word_Analysis/assets/84450816/408cf5d3-8d21-4f64-97cf-ce1e6acf093d)


<h2>1-2.사용하기</h2>
<h3>1-2-1.git clone으로 레포지터리를 복사한다.</h3>
<pre><code>$ git clone https://github.com/asa9874/Kakao_Word_Analysis</code></pre>

<h3>1-2-2.한국어 명사분류(Konlpy)</h2>
<h3>pip으로 konlpy,matplotlib를 설치한다.</h3>
<pre><code>$ python3 -m pip install konlpy 
$ python3 -m pip install matplotlib</code></pre>


<h3>1-2-3.내보내기한 kakao파일을 다음처럼 main.py와 같은 폴더안에 구성한다.</h3>

![image](https://github.com/asa9874/Kakao_Word_Analysis/assets/84450816/5b4d30dc-1d95-4158-a7f4-2e3e0b1021ca)

<h3>1-2-3.파이썬 프로그램을 실행해준다.</h3>

![image](https://github.com/asa9874/Kakao_Word_Analysis/assets/84450816/b7c9cecd-e942-4fd1-8b8e-6e46dea230a9)




