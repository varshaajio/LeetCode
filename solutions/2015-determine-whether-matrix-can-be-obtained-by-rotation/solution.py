class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target: return True 
        def rotate_matrix(mat):
            output = [[] for i in range(len(mat))]
            for i in reversed(range(len(mat))): 
                pointer = 0
                for val in mat[i]: 
                    output[pointer].append(val)
                    pointer += 1 
            return output 

        for i in range(3): 
            mat = rotate_matrix(mat)
            if mat == target: return True 

        return False 
