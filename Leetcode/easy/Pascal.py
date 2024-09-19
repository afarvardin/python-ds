class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        tri = [[1],[1,1]]
        if rowIndex == 0 or rowIndex == 1:
            return tri[rowIndex]
            # return tri[:rowIndex]

        row_i = 2
        while row_i <= rowIndex:
            local_lst = [1,1]
            insert_idx = 1
            
            idx = 0 
            prev_lst = tri[-1]
            while idx < len(prev_lst):
                local_lst.insert(idx+1, prev_lst[idx] + prev_lst[idx+1])
                idx += 1
                if prev_lst[idx] == 1:
                    break
                
            tri.append(local_lst)
            row_i += 1
        
        return tri[-1]
    
    
cls = Solution()
print(cls.getRow(6))