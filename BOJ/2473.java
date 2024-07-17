import java.io.*;
import java.util.*;

public class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader((System.in)));

    private static String[] inputs;
    private static int MAX = 5050;

    private static int n;
    private static long[] arr = new long[MAX];
    private static long ans;
    private static int[] ansIdx = new int[3];

    static {
        ans = 3000000001L;
    }

    public static void main(String[] args) throws IOException {
        read();
        n = Integer.parseInt(inputs[0]);

        read();
        for(int i=0; i<n; i++) {
            arr[i] = Integer.parseInt(inputs[i]);
        }
        Arrays.sort(arr, 0, n);

        for(int i=0; i<n; i++) {
            int lo = i+1, hi = n-1;
            while(lo < hi) {
                long sum = arr[i] + arr[lo] + arr[hi];
                long absSum = (sum > 0) ? sum : -sum;
                if(absSum < ans) {
                    ans = absSum;
                    ansIdx[0] = i;
                    ansIdx[1] = lo;
                    ansIdx[2] = hi;
                }
                if(sum > 0) {
                    hi -= 1;
                }
                else {
                    lo += 1;
                }
            }
        }

        System.out.println(arr[ansIdx[0]] + " " + arr[ansIdx[1]] + " " + arr[ansIdx[2]]);
    }

    private static void read() throws IOException {
        inputs = br.readLine().split(" ");
    }
}
