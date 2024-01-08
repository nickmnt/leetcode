class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        s = [(sr,sc)]
        orig_c = image[sr][sc]
        if color == orig_c:
            return image
        m = len(image)
        n = len(image[0])
        while len(s) > 0:
            x, y = s.pop()
            image[x][y] = color
            if x > 0 and image[x-1][y] == orig_c:
                image[x-1][y] = color
                s.append((x-1,y))
            if y > 0 and image[x][y-1] == orig_c:
                image[x][y-1] = color
                s.append((x,y-1)) 
            if x+1 < m and image[x+1][y] == orig_c:
                image[x+1][y] = color
                s.append((x+1,y))
            if y+1 < n and image[x][y+1] == orig_c:
                image[x][y+1] = color
                s.append((x,y+1))
        return image
        