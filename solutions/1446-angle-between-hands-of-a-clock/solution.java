class Solution {
    public double angleClock(int hour, int minutes) {
        double d=Math.abs(30*hour+0.5*minutes-6*minutes);
        return Math.min(d,360-d);
    }
}
