// Don't place your source in a package
import java.util.*;
import java.lang.*;
import java.io.*;

// Please name your class Main
class Main {
	public static void main (String[] args) throws java.lang.Exception {
	    Scanner in = new Scanner(System.in);
		int a = in.nextInt();
		int b = in.nextInt();
		if (a>b){
		    int diff = a-b;
		    int d = b;
		    if (diff > b){
		        d = b;
		    }
		    else if (diff < b){
		        d = diff;
		    }
		    else {
		        d = b;
		    }
		    while (true){
		        if (a%d == 0 & b%d == 0) {
		        System.out.print(d);
		        break;
		        }
		        else{
		        d--;
		        }
		    }
		}
		else if (b>a){
		    int diff = b-a;
		    int d = a;
		    if (diff > b) {
		        d = a;
		    }
		    else if (a > diff) {
		        d = diff;
		    }
		    else {
		        d = a;
		    }
		    while (true){
		    if (a%d == 0 & b%d == 0) {
		        System.out.print(d);
		        break;
		    }
		    else{
		        d--;
		    }
		}
		} 
		else{
		    System.out.print(b);
		}
		
		
	}
}