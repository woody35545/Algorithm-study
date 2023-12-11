import java.io.*;
import java.util.*;

class Person{
    String name;
    int birthYear;
    int birthMonth;
    int birthDay;

    public Person(String name, int birthYear, int birthMonth, int birthDay) {
        this.name = name;
        this.birthYear = birthYear;
        this.birthMonth = birthMonth;
        this.birthDay = birthDay;
    }
}

class PersonComparator implements Comparator<Person> {
    @Override
    public int compare(Person a, Person b) {
        if (a.birthYear != b.birthYear) {
            return Integer.compare(a.birthYear, b.birthYear);
        }

        if (a.birthMonth != b.birthMonth) {
            return Integer.compare(a.birthMonth, b.birthMonth);
        }

        return Integer.compare(a.birthDay, b.birthDay);
    }
}

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        ArrayList<Person> personList = new ArrayList<>();

        int N = Integer.parseInt(br.readLine());

        for(int i=0; i<N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            String name = st.nextToken();
            int birthDay = Integer.parseInt(st.nextToken());
            int birthMonth = Integer.parseInt(st.nextToken());
            int birthYear  = Integer.parseInt(st.nextToken());

            Person tmp = new Person(name, birthYear, birthMonth, birthDay);
            personList.add(tmp);
        }
        personList.sort(new PersonComparator());


        StringBuilder sb = new StringBuilder();
        sb.append(personList.get(personList.size()-1).name).append("\n");
        sb.append(personList.get(0).name).append("\n");

        System.out.print(sb);
    }


}


