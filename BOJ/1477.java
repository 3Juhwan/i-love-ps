import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    private static String[] inputs;
    private static int MAX = 1010;

    private static int n, m, l; 
    private static int[] arr = new int[MAX];

    public static void main(String[] args) throws IOException {
        Arrays.fill(arr, MAX);
        
        inputs = br.readLine().split(" ");
        n = Integer.parseInt(inputs[0]);
        m = Integer.parseInt(inputs[1]);
        l = Integer.parseInt(inputs[2]);
        inputs = br.readLine().split(" ");
        for(int i=0; i<n; i++) {
            arr[i] = Integer.parseInt(inputs[i]);
        }
        arr[n] = 0; arr[n+1] = l;
        n += 2;
        Arrays.sort(arr);

        int ans = 0;

        int start = 1, end = arr[n-1];
        while(start <= end) {
            int mid = (start + end) / 2;
            if(fun1(mid)) {
                ans = mid;
                end = mid - 1;
            }
            else {
                start = mid + 1;
            }
        }

        System.out.println(ans);
    }

    private static boolean fun1(int x) {
        int cnt = 0;
        for(int i=0; i<n-1; i++) {
            int curr = arr[i], next = arr[i+1];
            cnt += (next-curr-1) / x;
        }
        if(cnt <= m) {
            return true;
        }
        return false;
    }
}