class Solution {
    List<Integer>[] adjArr;
    int N ;
    int p = 1_000_000_007;

    public int assignEdgeWeights(int[][] edges) {
        N = edges.length + 1;

        // 1. Construct adJList representation graph (0-indexed representation)
        adjArr = (List<Integer>[]) new List[N];
        for(int i=0; i<N; i++)
            adjArr[i] = new ArrayList<>();
        
        for(int[] edge : edges) {
            int u = edge[0] - 1; //(0-indexed representation)
            int v = edge[1] - 1;
            (adjArr[u]).add(v);
            (adjArr[v]).add(u);
        }

        // 2. use DFS to find max Depth
        int maxD = depth(0, new boolean[N]) - 1; // rooted at node 1 (0 for 0-indexed representation)

        // 3. Permutations of placing 1-2-1-2-1 ... 1 so that sum = odd 
        //                    at post 1 2 3 4 5 ... d 
        // for d-1 positions we have two options 1/2 but to make sum odd, one of d positions must be 1
        // so ans = 2*2*2*2....2(d-1 times)*1
        // so ans = 2^(d-1)*1
        long x = 2l;
        long n = maxD-1L;
        return (int) powerMod(x, n, p);
    }
    
    // MEMORIZE this : save in notes
    public long powerMod(long x, long n, long p) { 
		long result = 1; 
		x = x % p; 
		while (n > 0) { 
			if ((n & 1) == 1) { // Checks if n is odd 
				result = (result * x) % p; 
			} 
			x = (x * x) % p; 
			n >>= 1; // Divides n by 2 using right shift 
		} 
		return result; 
	} 

    int depth(int node, boolean[] visited) {
        visited[node] = true;
        int depthSoFar = 0; 
        for(int neighbour : adjArr[node] ) {
            if(!visited[neighbour]) {
                depthSoFar = Math.max(depthSoFar, depth(neighbour, visited));
            }
        }
        return depthSoFar + 1; 
    }
}
