class Solution {
    public int maxIceCream(int[] costs, int coins) {
        Arrays.sort(costs);
        int sum=0,count=0;
        for(int coin:costs){
            if(coin>coins) return 0;
            sum+=coin; count++;
            if(sum==coins) return count;
            if(sum>coins) return count-1;
        }
        return count;
    }
}
