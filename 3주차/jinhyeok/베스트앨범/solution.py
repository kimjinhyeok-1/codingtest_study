from collections import defaultdict

def solution(genres, plays):
    answer = []
    # 1. 장르를 정렬하기: 많이 재생된 순으로
    # 2. 장르 안에서 정렬하기: 많이 재생된 노래 순으로
    # 총합이 많은 첫번째 dic의 key값을 순회하면서 두개씩 꺼내기
    
    # 1. 총합이 저장된 dic 만들기
    genre_total = defaultdict(int)
    # 2. 해당 장르 안에 (재생수, 고유 번호) 들어간 list dict 만들기
    genre_music = defaultdict(list)
    
    for i in range(len(genres)):
        genre = genres[i]
        genre_total[genre] += plays[i]
        genre_music[genre].append((plays[i], i))
    
    # 총합 기준으로 정렬
    genre_total = sorted(genre_total.items(), key = lambda x: x[1], reverse = True)
    
    for genre, _ in genre_total:
        songs = genre_music[genre]
        songs.sort(key = lambda x: (-x[0], x[1]))
        
        # 개별 음악 정렬
        for g, idx in songs[:2]:
            answer.append(idx)

    return answer