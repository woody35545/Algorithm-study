import java.io.*;
import java.util.Stack;

/**
 * 처음에 커서위치를 나타내는 pointer 변수를 선언하고, 
 * StringBuilder.insert로 pointer가 현재 가리키는 위치에 삽입하는 방식으로 풀었으나 시간초과가 발생했다.
 * StringBuilder.insert를 사용하여 구현하는 경우 시간이 초과됨을 깨닫고 
 * 커서 기준 왼쪽에 위치하는 문자들과 오른쪽에 위치하는 문자들을 저장하는 스택을 사용하여 해결하였다.
 */

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();

    // 현재 커서를 기준으로 왼쪽 문자들과 오른쪽 문자들로 분리

    // 현재 커서 기준 왼쪽 문자들을 저장하는 스택
    static Stack<String> leftStack = new Stack<>();
    // 현재 커서 기준 오른쪽 문자들을 저장하는 스택
    static Stack<String> rightStack = new Stack<>();

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(br.readLine());
        for(int t=0; t<T; t++){

            /* tokens ~> { "h", "e", "l", "l", "o" } */
            String[] tokens = br.readLine().split("");

            /* str ~> [ "h" -> "e" ... ] */
            for(String str : tokens){
                switch(str){
                    case "<":
                        // 커서를 왼쪽으로 한칸 이동해야하므로 leftStack top을 꺼내서 rightStack에 push
                        if(!leftStack.isEmpty()){
                            rightStack.push(leftStack.pop());
                        }
                        break;
                    case ">":
                        // 커서를 오른쪽으로 한칸 이동해야하므로 rightStack의 top을 꺼내서 leftStack에 push
                        if(!rightStack.isEmpty()){
                            leftStack.push(rightStack.pop());
                        }
                        break;
                    case "-":
                        // 커서 기준 왼쪽 문자를 하나 삭제해야하므로, leftStack에서 pop
                        if(!leftStack.isEmpty()){
                            leftStack.pop();
                        }
                        break;

                    default:
                        // 이외의 경우 leftStack에 삽입
                        leftStack.push(str);
                }

            }

            while(!leftStack.isEmpty()){
                rightStack.push(leftStack.pop());
            }

            while(!rightStack.isEmpty()){
                sb.append(rightStack.pop());
            }
            sb.append("\n");
        }

        System.out.print(sb);
    }

}
