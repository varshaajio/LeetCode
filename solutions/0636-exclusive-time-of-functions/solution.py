from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []
        prev_time = 0
        
        for log in logs:
            fn_id_str, typ, ts_str = log.split(':')
            fn_id = int(fn_id_str)
            ts = int(ts_str)
            
            if typ == 'start':
                if stack:
                    # Add time to the function currently on top of the stack
                    res[stack[-1]] += ts - prev_time
                stack.append(fn_id)
                prev_time = ts
            else:  # 'end'
                # Pop the function and add its execution time
                res[stack.pop()] += ts - prev_time + 1
                prev_time = ts + 1  # next interval starts after this timestamp
        
        return res

