import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
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
		ArrayList<Character> chars = new ArrayList<>();
		int end = 0;

		for (int i = 0; i < buffer.length(); i++) {
			if (i > length - 1) {
				chars.set(0, buffer.charAt(i));
				// [a, b, c, d] -> [b, c, d, a]
				Collections.rotate(chars, -1);

				Set<Character> uniqueChars = new HashSet<>(chars);

				if (uniqueChars.size() == length) {
					end = i + 1;
					break;
				}
			} else {
				chars.add(buffer.charAt(i));
			}
		}

		return end;
	}
}
