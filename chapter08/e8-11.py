def show_magic(magics):
    for magic in magics:
        print(magic)

def make_great(magics):
    copy_magics=magics[:]
    for magic in copy_magics:
        magic="The Great "+magic

    print(magics) 
    print(copy_magics)

magics=["xiyunfei","zhangwenyuan","xiyucheng"]

make_great(magics)
