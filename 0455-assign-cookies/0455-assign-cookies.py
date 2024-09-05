class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Sort both greed factors and cookie sizes
        g.sort()
        s.sort()
        
        # Initialize pointers for g (children) and s (cookies)
        i = 0  # pointer for children
        j = 0  # pointer for cookies
        content_children = 0
        
        # Try to satisfy as many children as possible
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:  # if the cookie can satisfy the child
                content_children += 1
                i += 1  # move to the next child
            j += 1  # move to the next cookie regardless
        
        return content_children
