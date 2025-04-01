import random as rt

board=["-","-","-","-"]

def comp_guess():
    li=["-","-","-","-"]
    guess=rt.randint(1000,9999)
    print(guess)
    for i in range(3,-1,-1):
        r=guess%10
        li[i]=str(r)
        guess//=10
    return li

guess=comp_guess()

play=True
while play:
    # print(board)
    num=int(input("Enter any 4 digit number: "))

    for i in range (3,-1,-1):
        r=num%10
        board[i]=str(r)
        num//=10

    comp_board=guess
    boo=["-","-","-","-"]
    for i in range(4):
        if comp_board[i]==board[i]:
            boo[i]=board[i]
    print("Board ->",boo)
    if boo==board:
        break
