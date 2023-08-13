import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static List<Pair<Integer, Integer>> dir = Arrays.asList(new Pair<>(1, 0), new Pair<>(0, 1), new Pair<>(-1, 0), new Pair<>(0, -1));
    static List<Pair<Integer, Integer>> virus = new ArrayList<>();
    static List<Integer> bucket = new ArrayList<>();
    static int[][] arr;
    static int[][] visited;
    static int ans = 3000;
    static int targetCnt = 0;
    static int n, m;

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        arr = new int[n][n];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
                if (arr[i][j] == 2) {
                    virus.add(new Pair<>(i, j));
                }
                if (arr[i][j] == 0) {
                    targetCnt++;
                }
            }
        }

        // 1. combination
        solve(0, m);

        if (ans == 3000) {
            ans = 0;
        }
        System.out.println(ans - 1);
    }

    private static void init() {
        visited = new int[n][n];
    }

    private static void bfs() {
        Queue<Pair<Integer, Integer>> queue = new LinkedList<>();
        for (Integer index : bucket) {
            Pair<Integer, Integer> virusPos = virus.get(index);
            queue.add(virus.get(index));
            visited[virusPos.first][virusPos.second] = 1;
        }

        int target = targetCnt;
        int time = 1;

        while (!queue.isEmpty()) {
            Pair<Integer, Integer> dequeued = queue.poll();
            int x = dequeued.first, y = dequeued.second;
            for (Pair<Integer, Integer> p : dir) {
                int nx = x + p.first, ny = y + p.second;
                if (nx < 0 || nx >= n || ny < 0 || ny >= n) {
                    continue;
                }
                if (visited[nx][ny] > 0) {
                    continue;
                }
                if (arr[nx][ny] == 1) {
                    continue;
                }
                visited[nx][ny] = visited[x][y] + 1;
                queue.add(new Pair<>(nx, ny));
                if (arr[nx][ny] == 0) {
                    target--;
                    time = Math.max(time, visited[nx][ny]);
                }
            }
        }

        if (target == 0) {
            ans = Math.min(ans, time);
        }
    }

    private static void solve(int start, int remain) {
        if (remain == 0) {
            init();
            bfs();
            return;
        }
        if (start >= virus.size()) {
            return;
        }

        for (int i = start; i < virus.size(); i++) {
            bucket.add(i);
            solve(i + 1, remain - 1);
            bucket.remove(bucket.size() - 1);
        }
    }

    public static class Pair<F, S> {

        final public F first;
        final public S second;

        Pair(F first, S second) {
            this.first = first;
            this.second = second;
        }
    }
}

