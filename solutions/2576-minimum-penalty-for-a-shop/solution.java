class Solution {
    public int bestClosingTime(String customers) {
        int n = customers.length();
        int penalty = 0;

        // Step 1: count total 'Y'
        for (int i = 0; i < n; i++) {
            if (customers.charAt(i) == 'Y') {
                penalty++;
            }
        }

        int minPenalty = penalty;
        int bestHour = 0;

        // Step 2: sweep closing hour
        for (int i = 0; i < n; i++) {
            if (customers.charAt(i) == 'Y') {
                penalty--;   // Y moves from closed → open
            } else {
                penalty++;   // N causes open penalty
            }

            if (penalty < minPenalty) {
                minPenalty = penalty;
                bestHour = i + 1;
            }
        }

        return bestHour;
    }
}

