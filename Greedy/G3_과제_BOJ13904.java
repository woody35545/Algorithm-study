import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.sql.PseudoColumnUsage;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

class Task{
    int endDate;
    int score;

    public Task(int endDate, int score) {
        this.endDate = endDate;
        this.score = score;
    }
}
public class Main {

    /**
     * 과제 점수가 높을수록 무조건 수행할 수 있도록 우선 선택한다.
     * 해당 과제의 수행일은 과제의 마감일에 수행하거나 최대한 마감일과 가깝게 스케줄링한다.
     * 그래야 점수는 상대적으로 낮지만 마감일이 더 짧은 과제들을 수행할 수 있
     */
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


    public static void main(String[] args) throws IOException {

        // 과제 수
        int N = Integer.parseInt(br.readLine());

        // 과제 정보
        Task[] tasks = new Task[N];

        // 날짜별로 수행한 과제의 점수
        int[] schedules = new int[1001];

        // -1은 아직 아무 과제도 해당 날짜에 배치되지 않은 상태를 의미
        Arrays.fill(schedules, 0);


        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            // 마감일
            int endDate = Integer.parseInt(st.nextToken());
            // 점수
            int score = Integer.parseInt(st.nextToken());

            tasks[i] = new Task(endDate, score);
        }

        // task를 점수가 높은 순서대로 정렬
        Arrays.sort(tasks, new Comparator<Task>() {
            @Override
            public int compare(Task t1, Task t2) {
                return -(t1.score - t2.score);
            }
        });

        // 과제를 각 날짜에 배치
        // 최대한 해당 과제의 마감일에 가깝게 배치
        for(int i=0; i<tasks.length; i++){
            int endDate = tasks[i].endDate;

            // schedule[0]은 사용하지 않음
            for(int j=endDate; j>0; j--){
                if(schedules[j] == 0){
                    schedules[j] = tasks[i].score;
                    break;
                }
            }
        }

        long totalScore = 0;
        for(int score : schedules){
            totalScore += score;
        }

        System.out.print(totalScore);

    }
}
