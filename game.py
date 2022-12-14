
def sum(a,b,c):
    return a+b+c


def board(xState, zState):
    zero = 'X' if xState[0] else ('O' if zState[0] else 0)
    one = 'X' if xState[1] else ('O' if zState[1] else 1)
    two = 'X' if xState[2] else ('O' if zState[2] else 2)
    three = 'X' if xState[3] else ('O' if zState[3] else 3)
    four = 'X' if xState[4] else ('O' if zState[4] else 4)
    five = 'X' if xState[5] else ('O' if zState[5] else 5)
    six = 'X' if xState[6] else ('O' if zState[6] else 6)
    seven = 'X' if xState[7] else ('O' if zState[7] else 7)
    eight = 'X' if xState[8] else ('O' if zState[8] else 8)
    
    
    #Structure of Tic Tac Toe board
    print("\n")
    print(f"{zero} | {one} | {two} ")
    print(f"--|---|---")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight} ") 
    
    
def checkWinner(xState, zState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]#row diagonal or column entirely one symbol X or O
    for win in wins:
        if(sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
            print("X Won the match \U0001F973\U0001F973\n")
            return 1
        if(sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3):
            print("O Won the match  \U0001F973\U0001F973\n")
            return 0
    return -1 #if no one has won
         



if __name__=="__main__":
    xState=[0,0,0,0,0,0,0,0,0] #0,1,2,3,4,5,6,7,8 for 9 boxes and all initialized to 0 for both x and z users
    zState=[0,0,0,0,0,0,0,0,0]
    turn=1 #1 for X and 0 for O
    print("\n\n\U0001f600   Let's Play Tic Tac Toe !!   \U0001f600\n")
    
    
    while(True):
        board(xState,zState)
        if (turn==1):
            print("\n-----------X's chance now-----------\n")
            value=int(input("Enter value : "))
            xState[value]=1
            
        else:
            print("\n-----------Z's chance-----------\n")
            value=int(input("\nEnter value : "))#value is the box to be marked
            zState[value]=1
            
            
        board(xState, zState)
        
        winner=checkWinner(xState,zState)
        
        if (winner!=-1):
            print("\n\n========== Game Over ==========\n")
            break
            
        turn=1-turn
