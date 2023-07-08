import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int H = Integer.valueOf(st.nextToken()) - 1;
        int W = Integer.valueOf(st.nextToken()) - 1;
        int N = Integer.valueOf(st.nextToken()) + 1;
        int M = Integer.valueOf(st.nextToken()) + 1;
        
        int height = H/N;
        int width = W/M;  

        System.out.print((height+1) * (width+1));
    }
}
