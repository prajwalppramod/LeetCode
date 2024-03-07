class Solution:
    def calPoints(self, operations: List[str]) -> int:
        points = []
        top =0
        for i in operations:
            if i.isdigit() or (i[0] == '-' and i[1:].isdigit()):
                points.append(int(i))
                top+=1
            elif i=='C':
                points.pop()
                top-=1
            elif i=='D':
                points.append(points[top-1]*2)
                top+=1
            elif i=='+':
                points.append(points[top-1]+points[top-2])
                top+=1
        return sum(points)
                