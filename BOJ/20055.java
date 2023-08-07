import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[] durability = new int[n * 2];
        boolean[] robot = new boolean[n];
        Arrays.fill(robot, false);

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n * 2; i++) {
            durability[i] = Integer.parseInt(st.nextToken());
        }

        int time = 0;
        while (k > checkDurability(n, durability)) {
            moveBeltWithRobot(n, durability, robot);
            moveRobot(n, durability, robot);
            loadRobot(durability, robot);
            time++;
        }
        System.out.println(time);
    }

    private static int checkDurability(int n, int[] durability) {
        int cntUnavailableBelt = 0;
        for (int i = 0; i < n * 2; i++) {
            cntUnavailableBelt += durability[i] == 0 ? 1 : 0;
        }
        return cntUnavailableBelt;
    }

    private static void loadRobot(int[] durability, boolean[] robot) {
        if (durability[0] != 0 && !robot[0]) {
            durability[0]--;
            robot[0] = true;
        }
    }

    private static void moveRobot(int n, int[] durability, boolean[] robot) {
        for (int i = n - 2; i >= 0; i--) {
            if (robot[i] && canMove(i + 1, durability, robot)) {
                robot[i + 1] = true;
                robot[i] = false;
                durability[i + 1]--;
            }
        }
        robot[n - 1] = false;
    }

    private static boolean canMove(int i, int[] durability, boolean[] robot) {
        if (robot[i]) {
            return false;
        }
        if (durability[i] == 0) {
            return false;
        }
        return true;
    }

    private static void moveBeltWithRobot(int n, int[] durability, boolean[] robot) {
        int tmp = durability[2 * n - 1];
        for (int i = 2 * n - 1; i > 0; i--) {
            durability[i] = durability[i - 1];
        }
        durability[0] = tmp;
        for (int i = n - 1; i > 0; i--) {
            robot[i] = robot[i - 1];
        }
        robot[0] = false;
        robot[n - 1] = false;
    }
}

