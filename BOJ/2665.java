import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static List<Pair<Integer, Integer>> dir = Arrays.asList(new Pair<>(1, 0), new Pair<>(0, 1), new Pair<>(-1, 0), new Pair<>(0, -1));

    static int n;
    static int[][] arr;
    static int[][] visited;

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());

        arr = new int[n][n];
        visited = new int[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                visited[i][j] = Integer.MAX_VALUE;
            }
        }

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            String s = st.nextToken();
            for (int j = 0; j < n; j++) {
                arr[i][j] = s.charAt(j) - '0';
            }
        }

        System.out.println(bfs());
    }

    private static int bfs() {
        LinkedList<Triple<Integer, Integer, Integer>> queue = new LinkedList<>();
        if (arr[0][0] == 1) {
            visited[0][0] = 0;
            queue.add(new Triple<>(0, 0, 0));
        } else {
            visited[0][0] = 1;
            queue.add(new Triple<>(1, 0, 0));
        }

        while (!queue.isEmpty()) {
            Triple<Integer, Integer, Integer> dequeued = queue.removeFirst();
            int w = dequeued.weight, x = dequeued.first, y = dequeued.second;
            if (visited[x][y] < w) {
                continue;
            }

            for (Pair<Integer, Integer> p : dir) {
                int nx = x + p.first, ny = y + p.second;
                if (nx < 0 || nx >= n || ny < 0 || ny >= n) {
                    continue;
                }
                if (visited[nx][ny] <= w) {
                    continue;
                }
                if (arr[nx][ny] == 1) {
                    visited[nx][ny] = w;
                    queue.addFirst(new Triple<>(w, nx, ny));
                } else {
                    visited[nx][ny] = w + 1;
                    queue.add(new Triple<>(w + 1, nx, ny));
                }
            }
        }

        return visited[n - 1][n - 1];
    }
}


class Pair<F, S> {

    final public F first;
    final public S second;

    Pair(F first, S second) {
        this.first = first;
        this.second = second;
    }

}

class Triple<W, F, S> {
    final public W weight;
    final public F first;
    final public S second;

    Triple(W weight, F first, S second) {
        this.weight = weight;
        this.first = first;
        this.second = second;
    }

}
