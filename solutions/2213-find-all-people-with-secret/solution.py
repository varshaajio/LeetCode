from typing import List
from collections import defaultdict

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # parent array for Union-Find
        parent = list(range(n))
        
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                # Always union towards 0 if possible to keep logic simple
                if root_i == find(0):
                    parent[root_j] = root_i
                else:
                    parent[root_i] = root_j

        # Initial secret sharing at time 0
        union(0, firstPerson)

        # Sort meetings by time
        meetings.sort(key=lambda x: x[2])

        i = 0
        m = len(meetings)
        while i < m:
            curr_time = meetings[i][2]
            pool = set()
            
            # Find all meetings happening at the same time
            j = i
            while j < m and meetings[j][2] == curr_time:
                u, v, t = meetings[j]
                union(u, v)
                pool.add(u)
                pool.add(v)
                j += 1
            
            # After processing this time block, reset anyone not connected to 0
            # because the secret only spreads if someone already had it.
            root_zero = find(0)
            for person in pool:
                if find(person) != root_zero:
                    parent[person] = person
            
            i = j

        # Collect everyone who is in the same component as 0
        result = []
        root_zero = find(0)
        for i in range(n):
            if find(i) == root_zero:
                result.append(i)
        
        return result
