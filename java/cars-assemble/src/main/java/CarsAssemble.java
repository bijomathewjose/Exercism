public class CarsAssemble {

    public double productionRatePerHour(int speed) {
        int produced=speed*221;
        if(speed<5){
            return produced;
        }
        else if(speed<9){
            return produced*0.9;
        }
        else if(speed<10){
            return produced*0.8;
        }
        return produced*0.77;
    }

    public int workingItemsPerMinute(int speed) {
        int produced=(int)productionRatePerHour(speed)/60;
        return produced;
    }
}
