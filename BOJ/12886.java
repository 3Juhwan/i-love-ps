import java.io.*;
import java.util.*;

public class Main {
    static final int MAX = 2000;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static boolean visited[][] = new boolean[MAX][MAX];
    static int arr[] = new int[3];

    public static void main(String[] arg) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < 3; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        if (Arrays.stream(arr).sum() % 3 != 0) {
            System.out.println(0);
            return;
        }

        Queue<Pair> queue = new LinkedList<>();
        queue.add(new Pair(arr[0], arr[1], arr[2]));

        visited[arr[0]][arr[1]] = true;

        while (!queue.isEmpty()) {
            Pair dequeued = queue.poll();
            int a = dequeued.a, b = dequeued.b, c = dequeued.c;

            solve(queue, a, b, c);
            solve(queue, a, c, b);
            solve(queue, b, c, a);
        }

        int avg = Arrays.stream(arr).sum() / 3;
        System.out.println(visited[avg][avg] ? 1 : 0);
    }

    private static void solve(Queue<Pair> q, int x, int y, int z) {
        if (y < x) {
            int tmp = x;
            x = y;
            y = tmp;
        }

        if (x * 2 >= MAX) {
            return;
        }

        if (visited[x * 2][y - x]) {
            return;
        }

        q.add(new Pair(x * 2, y - x, z));
        visited[x * 2][y - x] = true;
    }


    private static class Pair {
        int a, b, c;

        Pair(int a, int b, int c) {
            this.a = a;
            this.b = b;
            this.c = c;
        }
    }
}