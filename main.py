import konlpy
from konlpy.tag import Okt
import json
from draw import * 

okt = Okt()

#사람:{단어:수}
kor_dics ={}
#사람리스트
human=[]
#사람:{0:1,... }시간톡개수
human_talktime={}

# 파일 경로 설정
file_path = './kakao.txt'


#줄 분리 함수 (시간,이름,텍스트 부분 분리, 단어형태소분리)
def split_line(line):
    talkday,talk_main=line.split(", ", 1)
    ampm,talk_time=talkday.split("일 ",1)[1].split(" ",1)
    talk_time=int(talk_time.split(":")[0])
    if((ampm=="오후" and talk_time!=12) or (ampm=="오전" and talk_time==12)):talk_time+=12
    name,txt=talk_main.split(" : ")
    return talk_time,name,txt


#통계치에 추가함수
def add_statistics(talk_time,name,kor_list):
    #등록되지않은 사용자 추가
    if(name not in human):
        kor_dics[name]={}
        human.append(name)
        human_talktime[name]={i:0 for i in range(1,25)}
    
    #시간 추가
    human_talktime[name][talk_time]+=1
    #단어 추가
    for voca in kor_list:
        try:
            kor_dics[name][voca]+=1
        except:
            kor_dics[name][voca]=1



# 파일 열기 (읽기 모드로)
with open(file_path, 'r', encoding='utf-8') as file:
    # 파일의 각 줄에 대해 반복
    cnt=0
    for line in file:
        cnt+=1
        try:
            #라인분리,형태소분리,통계추가
            talk_time,name,txt=split_line(line)
            if(len(txt)>=2000):continue
            kor_list=okt.nouns(txt.strip())
            add_statistics(talk_time,name,kor_list)
        except:
            print(str(cnt)+"줄 오류")
            continue

        #if(cnt==50000):break #줄수 제한할때사용
        print(cnt)          #몇번째 줄인지 출력
        









#JSON 파일 만들어서 출력하기
for human_name in human:
    file_path = human_name+'.json'
    with open(file_path, 'w', encoding='utf-8') as f:
        sorted_items_voca = sorted(kor_dics[human_name].items(), key=lambda x: x[1], reverse=True)
        sorted_items_time = sorted(human_talktime[human_name].items(), key=lambda x: x[1], reverse=True)
        data = {
            "name": human_name,
            "data": {name: value for name, value in sorted_items_voca},
            "data2": {name: value for name, value in sorted_items_time}
        }
        json.dump(data, f, ensure_ascii=False, indent=4)
data={}
for human_name in human:
    data[human_name]={name: value for name, value in human_talktime[human_name].items()}

print(data)
drawgraph(human,data)
drawgraph2(human,data)