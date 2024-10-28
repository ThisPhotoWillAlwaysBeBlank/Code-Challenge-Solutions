// Don't place your source in a package
import java.util.*;
import java.lang.*;
import java.io.*;
// Please name your class Main
class Main {
	public static void main (String[] args) throws java.lang.Exception {
	    Scanner scan = new Scanner(System.in);
		int numberOfSubstances = scan.nextInt();
		int[] temperatureRangeLow = new int[numberOfSubstances];
		int[] temperatureRangeHigh = new int[numberOfSubstances];
		int temperatureLow = 100;
		int temperatureHigh = -100;
		int[][] temperaturePairs = new int[numberOfSubstances][2];
		boolean failure = false;
		for (int i=0; i < numberOfSubstances; i++) {
		        scan.nextLine();
		        temperatureRangeLow[i] = scan.nextInt();
		        temperatureRangeHigh[i] = scan.nextInt();
		        temperaturePairs[i][0] = temperatureRangeLow[i];
		        temperaturePairs[i][1] = temperatureRangeHigh[i];
	    	}
	    if (numberOfSubstances == 0){
	        System.out.print(-100 + " " + -100);
	    }
	    else if (numberOfSubstances == 1){
	        System.out.print(temperatureRangeLow[0] + " " + temperatureRangeLow[0]);
	    }
	    else{
	    	// This sort method is borrowed from chatGPT
            Arrays.sort(temperaturePairs, (a , b) -> Integer.compare(a[0], b[0]));
            int[][] lowSort = new int[numberOfSubstances][2];
            for (int i = 0; i<numberOfSubstances;i++){
                lowSort[i][0] = temperaturePairs[i][0];
                lowSort[i][1] = temperaturePairs[i][1];
            }
            Arrays.sort(temperaturePairs, (a , b) -> Integer.compare(a[1], b[1]));
            int fridgeOne = lowSort[0][0];
            int fridgeTwo = lowSort[numberOfSubstances-1][0];
            for (int i=1; i<numberOfSubstances;i++){
                if(lowSort[i][0]>fridgeOne){
                    if(lowSort[i][1]<fridgeTwo){
                        fridgeOne = lowSort[i][0];
                    }
                    
                }
            }
            if (fridgeOne > temperaturePairs[0][1]){
                failure = true;
            }
		    if (!failure){
		        System.out.print(fridgeOne + " " + fridgeTwo);
		    }else {
		        System.out.print(-1);
		    }
	    }
	}

}