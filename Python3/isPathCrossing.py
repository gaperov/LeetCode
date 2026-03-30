class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        visited = set([(x,y)])

        for step in path:
            if step == 'N':
                dx, dy = 0, 1
            elif step == 'S':
                dx, dy = 0, -1
            elif step == 'E':
                dx, dy = 1, 0
            else:
                dx, dy = -1, 0

            x += dx
            y += dy

            if (x, y) in visited:
                return True
            
            visited.add((x, y))
            
        return False
