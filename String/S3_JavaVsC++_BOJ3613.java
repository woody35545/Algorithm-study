import java.io.*;
import java.util.*;

public class Main {

        static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        public static boolean isSnakeCase(String str){
            boolean result = true;

            if(str.charAt(0) == '_' || str.charAt(str.length()-1) == '_'){
                return false;
            }
            int cnt = 0;
            for(int i=0; i<str.length(); i++){
                char currentChar = str.charAt(i);

                if(currentChar == '_'){
                    cnt++;
                }
                else{
                    cnt = 0;
                    if(Character.isUpperCase(currentChar)){
                        return false;
                    }
                }

                if(cnt > 1){
                    return false;
                }
            }

            return result;
        }

        public static boolean isCamelCase(String str){

            if(str.contains("_") || Character.isUpperCase(str.charAt(0))) {
                return false;
            }
            return true;
        }
        public static String covertToCamelCase(String str){
            // str ~> long_and_mnemonic_identifier

            StringBuilder sb = new StringBuilder();

            // tokens ~> { "long", "and", ... , "identifier" }
            String[] tokens = str.split("_");


            for(int i=0; i<tokens.length; i++){
                String currentToken = tokens[i];
                if(i != 0){
                    // 두번째 토큰부터 첫문자를 대문자로 변경
                    sb.append(currentToken.substring(0, 1).toUpperCase())
                            .append(currentToken.substring(1, currentToken.length()));
                }
                else {
                    sb.append(currentToken);
                }
            }
            return sb.toString();
        }

        public static String convertToSnakeCase(String str){
            // str ~> longAndMnemonicIdentifier

            StringBuilder sb = new StringBuilder();

            ArrayList<String> tokens = new ArrayList<>();
            // 문자열을 대문자 단위로 분리
            for(int i=0; i<str.length(); i++){
                if(!Character.isUpperCase(str.charAt(i))){
                    sb.append(str.charAt(i));
                }
                else{
                    // 이전 단어 뒤에 "_" 붙이고 tokens 리스트에 추가
                    sb.append("_");
                    tokens.add(sb.toString());

                    // sb 초기화 및 새로운 단어 소문자로 변환하여 입력
                    sb = new StringBuilder();
                    sb.append(Character.toLowerCase(str.charAt(i)));
                }
            }
            if(sb.length() != 0){
                tokens.add(sb.toString());
            }
            sb = new StringBuilder();

            for(int i=0; i<tokens.size(); i++){
                sb.append(tokens.get(i));
            }

            return sb.toString();
        }
        public static void main(String[] args) throws IOException{
            String inputStr = br.readLine();
            StringBuilder sb = new StringBuilder();
            if(isSnakeCase(inputStr)){
                sb.append(covertToCamelCase(inputStr));
            }
            else if(isCamelCase(inputStr)){
                sb.append(convertToSnakeCase(inputStr));
            }
            else{
                sb.append("Error!");
            }

            System.out.print(sb);
        }
    }
    
/**
 * 유의해야할 반례
 * //맨 뒤 문자가 '_' 이면 에러
 * asd_
 * Error! 
 *
 * //맨 앞 문자가 '_' 이면 에러
 * _asd
 * Error!
 *
 * //'_' 연속 두개면 에러
 * as__asd
 * Error!
 *
 * //맨 앞 문자가 대문자면 에러
 * Aasd
 * Error!
 *
 * //대문자와 '_'가 혼종이면 에러
 * asdAasd_asd
 * Error!
 *
 * //소문자만 입력 될 경우 정상
 * fadfadfadsf
 * fadfadfadsf
 *
 * // 대문자 연속일 경우 정상
 * asdasdASDASD
 * asdasd_a_s_d_a_s_d
 */
