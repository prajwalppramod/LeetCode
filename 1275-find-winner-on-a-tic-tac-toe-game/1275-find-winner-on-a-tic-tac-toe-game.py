class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        AXplays = []
        BOplays = []
        wins = [{(0,0), (1,1), (2,2)}, 
                {(0,2), (1,1), (2,0)}, 
                {(0,0), (0,1), (0,2)}, 
                {(1,0), (1,1), (1,2)}, 
                {(2,0), (2,1), (2,2)}, 
                {(0,0), (1,0), (2,0)}, 
                {(0,1), (1,1), (2,1)}, 
                {(0,2), (1,2), (2,2)}]
        
        for i in range(len(moves)):
            if i % 2 == 0:
                AXplays.append(tuple(moves[i]))  # Convert list to tuple
            else:
                BOplays.append(tuple(moves[i]))  # Convert list to tuple
                
        for win_combo in wins:
            if win_combo <= set(AXplays):
                return "A"
            if win_combo <= set(BOplays):
                return "B"
        
        if len(moves) == 9:
            return "Draw"
        else:
            return "Pending"
