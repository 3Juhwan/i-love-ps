import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        while(true) {

            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            
            int a = Integer.valueOf(st.nextToken());
            int b = Integer.valueOf(st.nextToken());
            int c = Integer.valueOf(st.nextToken());

            if(a==0) {
                break;
            }
            
            if(a >= b+c || b >= a+c || c >= a+b) {
                System.out.println("Invalid");
            }
            else if(a==b && b==c) {
                System.out.println("Equilateral");
            }
            else if(a==b || b==c || c==a) {
                System.out.println("Isosceles");
            }
            else {
                System.out.println("Scalene");
            }
        }
    }
}