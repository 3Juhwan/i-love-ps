import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    private static final BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) {
        try {
            solve();
        } catch (IOException ignored) {
        }
    }

    private static void solve() throws IOException {
        int numberOfSubject = Integer.parseInt(reader.readLine());
        String[] scores = reader.readLine().split(" ");
        
        int korean = 0, math = 0, english = 0, inquiry = 0, foreign = 0;
        if (numberOfSubject > 0) {
            korean = Integer.parseInt(scores[0]);
        }
        if (numberOfSubject > 1) {
            math = Integer.parseInt(scores[1]);
        }
        if (numberOfSubject > 2) {
            english = Integer.parseInt(scores[2]);
        }
        if (numberOfSubject > 3) {
            inquiry = Integer.parseInt(scores[3]);
        }
        if (numberOfSubject > 4) {
            foreign = Integer.parseInt(scores[4]);
        }

        int score = 0;

        if (korean > english) {
            score += (korean - english) * 508;
        } else {
            score += (english - korean) * 108;
        }

        if (math > inquiry) {
            score += (math - inquiry) * 212;
        } else {
            score += (inquiry - math) * 305;
        }

        score += foreign * 707;

        score *= 4763;

        System.out.println(score);
    }
}

