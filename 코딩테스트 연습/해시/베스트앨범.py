def solution(genres, plays):
    answer = []
    album = {}
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        album[genre] = album.get(genre, []) + [(idx, play)]
        album[genre].sort(key=lambda x : x[1], reverse=True)
    else:
        for genre, songs in sorted(album.items(), key=lambda x : sum(p for _, p in x[1]), reverse=True):
            answer.extend([idx for idx, _ in songs[:2]])
    return answer
