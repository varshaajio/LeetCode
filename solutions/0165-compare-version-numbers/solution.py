class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        # Split the version strings into revision parts
        v1_parts = version1.split('.')
        v2_parts = version2.split('.')

        # Determine the maximum length to normalize both lists
        max_len = max(len(v1_parts), len(v2_parts))

        # Pad the shorter list with '0's
        v1_parts += ['0'] * (max_len - len(v1_parts))
        v2_parts += ['0'] * (max_len - len(v2_parts))

        # Compare each revision part
        for i in range(max_len):
            num1 = int(v1_parts[i])
            num2 = int(v2_parts[i])
            if num1 < num2:
                return -1
            elif num1 > num2:
                return 1

        # All revisions are equal
        return 0

        
