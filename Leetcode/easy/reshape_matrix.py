class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        flatten_mat = [ item for subitems in mat for item in subitems ]
        if r*c != len(flatten_mat):
            return mat
        
        op = []
        idx = 0
        while r > 0:
            local_lst = []

            for i in range(c):
                local_lst.append(flatten_mat[idx])
                idx += 1
            op.append(local_lst)

            r -= 1

        return op 