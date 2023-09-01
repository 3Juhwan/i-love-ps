import java.io.*;
import java.util.*;

public class Main {

    private final static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private final static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private final static Board board = new Board();
    private static Piece[] pieces = new Piece[4];
    private static int[] arr = new int[10];
    private static int answer = 0;

    public static void main(String args[]) throws IOException {
        input();
        init();
        solve(0, 0);
        System.out.println(answer);
    }

    private static void input() throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < 10; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
    }

    public static void init() {
        Point startPoint = board.getStartPoint();
        for (int i = 0; i < 4; i++) {
            pieces[i] = new Piece(startPoint);
        }
    }

    private static void solve(int sequence, int score) {
        if (sequence == 10) {
            answer = Math.max(answer, score);
            return;
        }

        for (Piece piece : pieces) {
            if (piece.position.bluePoint != null) {
                if (canMove(piece.position.bluePoint, arr[sequence] - 1)) {
                    piece.move(false);
                    for (int i = 0; i < arr[sequence] - 1; i++) {
                        piece.move(true);
                    }
                    solve(sequence + 1, score + piece.position.score);
                    for (int i = 0; i < arr[sequence]; i++) {
                        piece.undo();
                    }
                }
            } else {
                if (canMove(piece.position.redPoint, arr[sequence] - 1)) {
                    for (int i = 0; i < arr[sequence]; i++) {
                        piece.move(true);
                    }
                    solve(sequence + 1, score + piece.position.score);
                    for (int i = 0; i < arr[sequence]; i++) {
                        piece.undo();
                    }
                }
            }
        }
    }

    private static boolean canMove(Point point, int step) {
        if (point == board.getEndPoint()) {
            return true;
        }
        if (step == 0) {
            return point.occupied == 0;
        }
        return canMove(point.redPoint, step - 1);
    }
}

class Piece {
    Point position;
    List<Point> visited;

    Piece(Point point) {
        this.position = point;
        this.visited = new ArrayList<>();
        this.visited.add(point);
    }

    public Point getPosition() {
        return position;
    }

    public boolean move(boolean isRed) {
        Point nextPoint = isRed ? position.redPoint : position.bluePoint;
        if (nextPoint == null) {
            return false;
        }
        position.occupied--;
        position = nextPoint;
        position.occupied++;
        visited.add(position);
        return true;
    }

    public void undo() {
        if (visited.isEmpty()) {
            throw new NoSuchElementException();
        }
        position.occupied--;
        visited.remove(visited.size() - 1);
        position = visited.get(visited.size() - 1);
        position.occupied++;
    }
}

class Point {
    int score;
    Point redPoint, bluePoint;
    int occupied;

    Point() {
        this.occupied = 0;
    }

    Point(int score) {
        this();
        this.score = score;
    }

    Point(int score, boolean self) {
        this();
        this.score = score;
        this.redPoint = this;
    }

    private void addPoint(Point point, boolean isRed) {
        if (isRed) {
            this.redPoint = point;
        } else {
            this.bluePoint = point;
        }
    }

    public boolean isOccupied() {
        return this.occupied > 0;
    }
}

class Board {
    private final Point startPoint = new Point(0);
    private final Point endPoint = new Point(0, true);
    private final Point point10 = new Point(10);
    private final Point point20 = new Point(20);
    private final Point point25 = new Point(25);
    private final Point point30 = new Point(30);
    private final Point point40 = new Point(40);


    Board() {
        makeBoard();
    }

    private void makeBoard() {
        makeLine(this.startPoint, point10, 2, 4, 2, true);
        makeLine(point10, point25, 13, 3, 3, false);
        makeLine(point10, point20, 12, 4, 2, true);
        makeLine(point20, point25, 22, 2, 2, false);
        makeLine(point25, point40, 30, 2, 5, true);
        makeLine(point20, point30, 22, 4, 2, true);
        makeLine(point30, point25, 28, 3, -1, false);
        makeLine(point30, point40, 32, 4, 2, true);
        makeLine(point40, this.endPoint);
    }

    private void makeLine(Point startPoint, Point endPoint) {
        startPoint.redPoint = endPoint;
    }

    private void makeLine(Point startPoint, Point endPoint, int startScore, int repeat, int digit, boolean startRed) {
        int currScore = startScore;
        Point currPoint = new Point(startScore);
        if (startRed) {
            startPoint.redPoint = currPoint;
        } else {
            startPoint.bluePoint = currPoint;
        }
        for (int i = 0; i < repeat - 1; i++) {
            currScore += digit;
            Point nextPoint = new Point(currScore);
            currPoint.redPoint = nextPoint;
            currPoint = nextPoint;
        }
        currPoint.redPoint = endPoint;
    }

    public Point getStartPoint() {
        return this.startPoint;
    }

    public Point getEndPoint() {
        return this.endPoint;
    }

}