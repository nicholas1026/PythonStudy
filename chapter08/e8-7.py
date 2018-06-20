def make_album(singer,album,numbers=10):
    albums = {'singerName':singer,'albumName':album}

    if numbers :
        albums['account'] = numbers

    return albums

print(make_album("刘德华","忘情水"))
print(make_album("张学友","恶狼传说",23))
print(make_album("郭富城","亚洲舞王",15))
