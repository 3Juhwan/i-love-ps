import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {
    private static final Map<Integer, String> NUMERIC_MAP = new HashMap<>();

    static {
        NUMERIC_MAP.put(0, "0000\n0  0\n0  0\n0  0\n0000\n");
        NUMERIC_MAP.put(1, "   1\n   1\n   1\n   1\n   1\n");
        NUMERIC_MAP.put(2, "2222\n   2\n2222\n2\n2222\n");
        NUMERIC_MAP.put(3, "3333\n   3\n3333\n   3\n3333\n");
        NUMERIC_MAP.put(4, "4  4\n4  4\n4444\n   4\n   4\n");
        NUMERIC_MAP.put(5, "5555\n5\n5555\n   5\n5555\n");
        NUMERIC_MAP.put(6, "6666\n6\n6666\n6  6\n6666\n");
        NUMERIC_MAP.put(7, "7777\n   7\n   7\n   7\n   7\n");
        NUMERIC_MAP.put(8, "8888\n8  8\n8888\n8  8\n8888\n");
        NUMERIC_MAP.put(9, "9999\n9  9\n9999\n   9\n   9\n");
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String n = sc.next();
        for (char x : n.toCharArray()) {
            System.out.println(NUMERIC_MAP.get(Integer.parseInt(String.valueOf(x))));
        }
    }
}

