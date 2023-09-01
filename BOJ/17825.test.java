import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;

class Tests {

    private final Board board = new Board();
    private final Main main = new Main();

    @Test
    void 라인_시작_10_25_40_도착까지의_포인트_검증() {
        // given
        int[] line1 = new int[]{2, 4, 6, 8, 10};
        int[] line2 = new int[]{16, 19, 25, 30, 35, 40, 0};
        Point currPoint = board.getStartPoint();

        // when
        for (int score : line1) {
            currPoint = currPoint.redPoint;    // when
            assertThat(currPoint.score).isEqualTo(score);   // then
        }

        currPoint = currPoint.bluePoint;    // when
        assertThat(currPoint.score).isEqualTo(13);  // then

        // when
        for (int score : line2) {
            currPoint = currPoint.redPoint;    // when
            assertThat(currPoint.score).isEqualTo(score);   // then
        }

        assertThat(currPoint).isEqualTo(board.getEndPoint());   // then
    }

    @Test
    void 라인_시작_10_20_30_40_도착_까지의_포인트_검증() {
        // given
        int[] line1 = new int[]{2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 0};
        Point startPoint = board.getStartPoint(), endPoint = board.getEndPoint();

        // when
        Point currPoint = startPoint;
        for (int score : line1) {
            currPoint = currPoint.redPoint;
            assertThat(currPoint.score).isEqualTo(score);   // then
        }

        assertThat(currPoint).isEqualTo(board.getEndPoint());   // then
    }

    @Test
    void 라인_시작_10_20_30_25_40_도착_까지의_포인트_검증() {
        // given
        int[] line1 = new int[]{2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30};
        int[] line2 = new int[]{27, 26, 25, 30, 35, 40, 0};
        Point currPoint = board.getStartPoint();

        // when
        for (int score : line1) {
            currPoint = currPoint.redPoint;    // when
            assertThat(currPoint.score).isEqualTo(score);   // then
        }

        currPoint = currPoint.bluePoint;    // when
        assertThat(currPoint.score).isEqualTo(28);  // then

        // when
        for (int score : line2) {
            currPoint = currPoint.redPoint;    // when
            assertThat(currPoint.score).isEqualTo(score);   // then
        }

        assertThat(currPoint).isEqualTo(board.getEndPoint());   // then
    }

}
