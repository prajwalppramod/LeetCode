class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x0 = 0
        y0 = 0
        x1 = 0
        y1 = 0
        for i in moves:
            if i=='U':
                y1+=1
            elif i=='D':
                y1-=1
            elif i=='L':
                x1-=1
            elif i=='R':
                x1+=1
        if x0==x1 and y0==y1:
            return True
        else:
            return False