import java.io.*;
import java.util.*;

public class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader((System.in)));

    private static String[] inputs;

    private static int n = 5;
    private static int ans = 0;
    private static char[][] arr = new char[5][5];
    private static List<Integer> bucket = new ArrayList<>();
    private static List<List<Integer>> comb = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        for(int i=0; i<n; i++) {
            read();
            arr[i] = inputs[0].toCharArray();
        }

        combination(-1);

        for(List<Integer> com : comb) {
            solve1(com);
        }

        System.out.println(ans);
    }

    private static void solve1(List<Integer> com) {
        if(!isAdjacent(com)) {
            return;
        }
        if(!isOverHalf(com)) {
            return;
        }
        ans += 1;
    }

    private static boolean isAdjacent(List<Integer> com) {
        int cnt = 1;
        int[] visited = new int[25];
        Deque<Integer> q = new ArrayDeque<>();
        visited[com.get(0)] = 1;
        q.add(com.get(0));
        
        while(!q.isEmpty()) {
            Integer value = q.pollFirst();
            int x = value/5, y = value%5;
            for(int[] dxdy : List.of(new int[]{0, -1}, new int[]{0, 1}, new int[]{-1, 0}, new int[]{1, 0})) {
                int nx = x+dxdy[0], ny = y+dxdy[1];
                if(nx < 0 || nx >= 5 || ny < 0 || ny >= 5) {
                    continue;
                }
                int tmp = nx*5 + ny;
                if(visited[tmp] != 0) {
                    continue;
                }
                if(com.contains(tmp)) {
                    cnt += 1;
                    visited[tmp] = 1;
                    q.add(tmp);
                }
            }
        }

        return cnt == 7;
    }

    private static boolean isOverHalf(List<Integer> com) {
        int cnt = 0;
        for(Integer i : com) {
            int x = i/5, y = i%5;
            cnt += arr[x][y] == 'S' ? 1 : 0;
        }
        return cnt >= 4;
    }

    private static void combination(int x) {
        if(x >= 25) {
            return;
        }
        if(bucket.size() == 7) {
            comb.add(new ArrayList(bucket));
            return;
        }

        for(int i=x+1; i<25; i++) {
            bucket.add(i);
            combination(i);
            bucket.remove(bucket.size()-1);
        }
    }

    private static void read() throws IOException {
        inputs = br.readLine().split(" ");
    }
}
