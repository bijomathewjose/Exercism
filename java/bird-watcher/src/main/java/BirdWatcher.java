
class BirdWatcher {
    private final int[] birdsPerDay;

    public BirdWatcher(int[] birdsPerDay) {
        this.birdsPerDay = birdsPerDay.clone();
    }
    public int[] getLastWeek() {
        return this.birdsPerDay;
    }

    public int getToday() {
        if(this.birdsPerDay.length==0) return 0;
        return this.birdsPerDay[birdsPerDay.length-1];
    }

    public void incrementTodaysCount() {
        this.birdsPerDay[birdsPerDay.length-1]++;
    }

    public boolean hasDayWithoutBirds() {
        for(int count:this.birdsPerDay){
            if(count==0)
                return true;
        }
        return false;
    }

    public int getCountForFirstDays(int numberOfDays) {
        int sum=0;
        for(int i=0;i<numberOfDays && i<7;i++){
            sum+=this.birdsPerDay[i];
        }
        return sum;
    }

    public int getBusyDays() {
        int count=0;
         for(int i:this.birdsPerDay){
             if(i>=5) count++;
         }
        return count;
    }
}
