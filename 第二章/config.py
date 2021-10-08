# work

# 1 生成一副扑克牌（自己设计扑克牌的结构，小王和大王可以分别用14、15表示 ）

poker_color = ["Spade", 'Heart', 'Diamond', 'Club']
poker_num = ['A', 'J', 'Q', 'K']
poker_num.extend(list(range(2, 11, 1)))
poker = []


# 生成扑克
def creat_poke(poker):
    for i in poker_color:
        for j in poker_num:
            item = i + str(j)
            poker.append(item)
    poker.extend(['joker', 'JOKER'])
    return poker

# 发牌







if __name__ == '__main__':
    creat_poke(poker)





# 2,