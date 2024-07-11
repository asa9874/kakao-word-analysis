import konlpy
from konlpy.tag import Okt
import json

okt = Okt()
kor_dics ={}
human=[]

# 파일 경로 설정
file_path = './kakao.txt'

# 파일 열기 (읽기 모드로)
with open(file_path, 'r', encoding='utf-8') as file:
    # 파일의 각 줄에 대해 반복
    cnt=0
    for line in file:
        #앞의 날짜,이름,텍스트 부분 분리, 단어형태소분리
        try:
            name,txt=line.split(", ", 1)[1].split(" : ")
            kor_list=okt.nouns(txt.strip())
        except:
            print(cnt+"줄 오류")
            continue
        
        #등록되지않은 사용자 추가
        if(name not in human):
            kor_dics[name]={}
            human.append(name)
        

        #단어 추가
        for voca in kor_list:
            try:
                kor_dics[name][voca]+=1
            except:
                kor_dics[name][voca]=1


        #몇번째 줄인지 출력
        cnt+=1
        #if(cnt==100000):break #줄수 제한할때사용
        print(cnt)


#JSON 파일 만들어서 출력하기
for human_name in human:
    file_path = human_name+'.json'
    with open(file_path, 'w', encoding='utf-8') as f:
        sorted_items = sorted(kor_dics[human_name].items(), key=lambda x: x[1], reverse=True)
        data = {
            "name": human_name,
            "data": {name: value for name, value in sorted_items}
        }
        json.dump(data, f, ensure_ascii=False, indent=4)