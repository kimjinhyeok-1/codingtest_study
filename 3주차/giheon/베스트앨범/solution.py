from collections import defaultdict

def solution(genres, plays):
    answer = []
    song_dic = defaultdict(list)
    genres_dict = {}
    
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        
        if genre not in genres_dict:
            genres_dict[genre] = 0
        
        genres_dict[genre] += play
        song_dic[genre].append((play, i))
    
    sorted_gen = sorted(genres_dict, key=lambda x: genres_dict[x], reverse=True)
    print("[INFO] - sorted_gen is", sorted_gen)
    
    for sg in sorted_gen:
        sorted_song = sorted(song_dic[sg], key=lambda x: (-x[0], x[1]))
        print("[INFO] - sorted_song is", sorted_song)
        for song, i in sorted_song[:2]:
            answer.append(i)
    
    return answer