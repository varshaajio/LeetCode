class Solution {
    public int longestCommonPrefix(int[] arr1, int[] arr2) {
        int cpl = 0;
        HashSet<Integer> p = new HashSet<>();
        for (int num : arr1) {
            while (num > 0) {
                p.add(num);
                num /= 10;
            }
        }
        for (int num : arr2) {
            while (num > 0) {
                if (p.contains(num)) {
                    int pl = String.valueOf(num).length();
                    if(pl > cpl) {
                        cpl = pl;
                    }
                    break;
                }
                num /= 10;
            }
        }
        return cpl;
    }
}
