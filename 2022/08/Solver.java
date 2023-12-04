import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Arrays;

class Solver {
	public static void main(String[] args) throws Exception {
		ArrayList<ArrayList<Integer>> treeMap = new ArrayList<>();

		Files.readAllLines(Path.of("example.txt")).forEach(line -> {
			ArrayList<Integer> row = new ArrayList<>();

			for (char number : line.toCharArray()) {
				row.add(Integer.parseInt(String.valueOf(number)));
			}

			treeMap.add(row);
		});

		int numOfCols = treeMap.get(0).size();
		int numOfRows = treeMap.size(); 
		int visible = 0;
		int score = 0;

		for (int row = 0; row < numOfRows; row++) {
			for (int col = 0; col < numOfCols; col++) {
				if (row == 0 || col == 0 || row == numOfRows - 1 || col == numOfCols - 1) {
					visible += 1;
					continue;
				}

				int[] scores = new int[4];
				boolean[] notVisible = new boolean[4];
				int height = treeMap.get(row).get(col);

				for (int i = row + 1; i < numOfRows; i++) {
					scores[0]++;
					if (treeMap.get(i).get(col) >= height) {
						notVisible[0] = true;
						break;
					}
				}

				for (int i = row - 1; i >= 0; i--) {
					scores[1]++;
					if (treeMap.get(i).get(col) >= height) {
						notVisible[1] = true;
						break;
					}
				}

				for (int i = col + 1; i < numOfCols; i++) {
					scores[2]++;
					if (treeMap.get(row).get(i) >= height) {
						notVisible[2] = true;
						break;
					}
				}

				for (int i = col - 1; i >= 0; i--) {
					scores[3]++;
					if (treeMap.get(row).get(i) >= height) {
						notVisible[3] = true;
						break;
					}
				}

				if (Arrays.asList(notVisible).contains(false)) {
					visible += 1;
				}

				score = Math.max(score, scores[0] * scores[1] * scores[2] * scores[3]);
			}
		}

		// part 1

		System.out.println(visible);

		// part 2

		System.out.println(score);
	}
}
