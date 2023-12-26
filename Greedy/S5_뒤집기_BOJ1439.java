import java.io.*;
import java.util.*;

class Node{
    long cost;
    long distanceToNext;

    public Node(int cost, int distanceToNext) {
        this.cost = cost;
        this.distanceToNext = distanceToNext;
    }
}
public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st = new StringTokenizer("");
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        String inputStr = br.readLine();

        String[] splittedByOne = inputStr.split("1");

        long onePartCount = 0;
        long zeroPartCount = 0;
        for(int i=0; i<splittedByOne.length; i++){
            if(!splittedByOne[i].equals("") && splittedByOne[i] != null ){
                zeroPartCount += 1;
            }
        }

        String[] splittedByZero= inputStr.split("0");
        for(int i=0; i<splittedByZero.length; i++){
            if(!splittedByZero[i].equals("") && splittedByZero[i] != null ){
                onePartCount += 1;
            }
        }

        System.out.print(Math.min(zeroPartCount, onePartCount));
    }
}
