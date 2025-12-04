class Solution:
    def countCollisions(self, directions: str) -> int:
        n = len(directions)
        left = 0
        right = n - 1
        
        # 1. Skip cars at the start moving left (they drive away safely)
        while left < n and directions[left] == 'L':
            left += 1
            
        # 2. Skip cars at the end moving right (they drive away safely)
        while right >= 0 and directions[right] == 'R':
            right -= 1
            
        # 3. Count moving cars in the remaining "danger zone"
        # Any car between 'left' and 'right' that is moving (L or R) 
        # will eventually collide with something.
        collision_count = 0
        for i in range(left, right + 1):
            if directions[i] != 'S':
                collision_count += 1
                
        return collision_count
