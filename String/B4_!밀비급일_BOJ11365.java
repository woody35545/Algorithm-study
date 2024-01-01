import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    static String reverseString(String str){
        Stack<Character> stack = new Stack<>();
        for(int i=0; i<str.length(); i++){
            stack.push(str.charAt(i));
        }

        StringBuilder sb = new StringBuilder();

        while(!stack.isEmpty()){
            sb.append(stack.pop());
        }

        return sb.toString();
    }

    public static void main(String[] args) throws IOException{
        StringBuilder sb = new StringBuilder();
        while(true){
            String inputStr = br.readLine();
            if(inputStr.equals("END")) break;

            sb.append(reverseString(inputStr)).append("\n");
        }

        System.out.print(sb);
    }
}
