import java.io.*;
import java.util.*;

class Person{
    int age;
    String name;

    public Person(int age, String name) {
        this.age = age;
        this.name = name;
    }
}
public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st = new StringTokenizer("");
    static StringBuilder sb = new StringBuilder();


    public static void main(String[] args) throws IOException{
        int N = Integer.parseInt(br.readLine());
        Person[] persons = new Person[N];
        for(int i=0; i<N; i++){
            st = new StringTokenizer(br.readLine());
            persons[i] = new Person(Integer.parseInt(st.nextToken()), st.nextToken());
        }

        Arrays.sort(persons, new Comparator<>() {
            @Override
            public int compare(Person a, Person b) {
                if (a.age != b.age) {
                    return a.age - b.age;
                } else {
                    // 나이가 같으면 먼저온 사람이 우선이므로 우선순위를 유지하도록 0 리턴
                    return 0;
                }
            }
        });

        for(var elem : persons){
            sb.append(elem.age).append(" ").append(elem.name).append("\n");
        }

        System.out.print(sb);
    }
}
