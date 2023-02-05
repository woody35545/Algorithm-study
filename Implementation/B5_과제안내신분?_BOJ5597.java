import java.util.*;

public class Main {
    public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    boolean [] summit = new boolean[33];
    for (int i=0; i<28; i++) {
        int input_int = sc.nextInt();
        summit[input_int] = true;
    }
        for (int i=1; i<31; i++){
            if (!summit[i]) System.out.println(i);
        }

    }
}
