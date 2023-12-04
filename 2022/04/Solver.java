import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;

class Solver {
	public static void main(String[] args) throws Exception {
		ArrayList<int[]> pairs = new ArrayList<>();

		Files.readAllLines(Path.of("example.txt")).forEach(line -> {
			String[] sep = line.split(",");

			int[] pair = new int[] {
				Integer.parseInt(sep[0].split("-")[0]),
				Integer.parseInt(sep[0].split("-")[1]),
				Integer.parseInt(sep[1].split("-")[0]),
				Integer.parseInt(sep[1].split("-")[1])
			};

			pairs.add(pair);
		});

		// part 1

		int containsAll = 0;

		for (int[] pair : pairs) {
			int leftLow = pair[0];
			int leftUpp = pair[1];
			int rightLow = pair[2];
			int rightUpp = pair[3];

			if (leftLow >= rightLow && leftUpp <= rightUpp) {
				containsAll++;
			} else if (rightLow >= leftLow && rightUpp <= leftUpp) {
				containsAll++;
			}
		}

		System.out.println(containsAll);

		// part 2

		int containsAny = 0;

		for (int[] pair : pairs) {
			int leftLow = pair[0];
			int leftUpp = pair[1];
			int rightLow = pair[2];
			int rightUpp = pair[3];

			if ((leftLow >= rightLow && leftLow <= rightUpp)
					|| (leftUpp >= rightLow && leftUpp <= rightUpp)
					|| (rightLow >= leftLow && rightLow <= leftUpp)
					|| (rightUpp >= leftLow && rightUpp <= leftUpp)) {
				containsAny++;
			}
		}

		System.out.println(containsAny);
	}
}
