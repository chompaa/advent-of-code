import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Set;

class Solver {
	public static void main(String[] args) throws Exception {
		ArrayList<String> lines = new ArrayList<>();

		Files.readAllLines(Path.of("example.txt")).forEach(line -> {
			lines.add(line);
		});

		String buffer = lines.get(0);

		// part 1

		System.out.println(getMarkerEnd(buffer, 4));

		// part 2

		System.out.println(getMarkerEnd(buffer, 14));
	}

	public static int getMarkerEnd(String buffer, int length) {
		Queue<Character> queue = new LinkedList<>();
		int end = 0;

		for (int i = 0; i < buffer.length(); i++) {
			if (i > length - 1) {
				queue.remove();
				queue.add(buffer.charAt(i));

				Set<Character> uniqueChars = new HashSet<>(queue);
				if (uniqueChars.size() == length) {
					end = i + 1;
					break;
				}
			} else {
				queue.add(buffer.charAt(i));
			}
		}
		
		return end;
	}
}
