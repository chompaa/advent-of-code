import java.nio.file.Files;
import java.nio.file.Path;
import java.util.LinkedList;
import java.util.List;
import java.util.Collections;

class Solver {
	public static void main(String[] args) throws Exception {
		LinkedList<Integer> calorieCounts = new LinkedList<>(List.of(0));

		Files.readAllLines(Path.of("example.txt")).forEach(line -> {
			if (line.isBlank()) {
				calorieCounts.add(0);
			} else {
				calorieCounts.add(calorieCounts.removeLast() + Integer.parseInt(line));
			}
		});

		// part 1

		System.out.println(Collections.max(calorieCounts));

		// part 2
		
		Collections.sort(calorieCounts, Collections.reverseOrder());
		
		System.out.println(calorieCounts.stream().limit(3).mapToInt(i -> i).sum());

	}
}
