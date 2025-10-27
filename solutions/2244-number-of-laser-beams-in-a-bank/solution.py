class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        total = 0
        prev = 0  # number of devices in the last non-empty row

        for row in bank:
            cnt = row.count('1')
            if cnt:
                # beams form between this row and the last non-empty row
                total += prev * cnt
                prev = cnt  # update last non-empty row count

        return total

