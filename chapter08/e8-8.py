def make_album(singer,album,numbers=100):
    albums={'singerName':singer,'albumName':album}
    if numbers:
        albums['account']=numbers

    return albums

while True:
    singerName=input("输入歌手的名字:")
    if singerName=='q':
        break

    albumName=input("输入专辑的名字:")
    if albumName=='q':
        break

    numbers=input("输入专辑数量:")
    if numbers=='q':
        break

    print(make_album(singerName,albumName,int(numbers)))
