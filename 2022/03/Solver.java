import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Set;
import java.util.Map.Entry;
import java.util.HashSet;

class Solver {
	public static void main(String[] args) throws Exception {
		ArrayList<String> rucksacks = new ArrayList<>();

		Files.readAllLines(Path.of("example.txt")).forEach(line -> {
			rucksacks.add(line);
		});

		// part 1

		int sum = 0;

		for (String rucksack : rucksacks) {
			String leftCompartment = rucksack.substring(0, (rucksack.length() / 2));
			String rightCompartment = rucksack.substring((rucksack.length() / 2));

			for (char left : leftCompartment.toCharArray()) {
				if (rightCompartment.contains(String.valueOf(left))) {
					if (left > 'Z') {
						sum += 1 + (left - 'a');
					} else {
						sum += 27 + (left - 'A');
					}
					break;
				}
			}
		}

		System.out.println(sum);

		// part 2

		sum = 0;
		HashMap<Character, Integer> counts = new HashMap<>();

		for (int i = 0; i < rucksacks.size() + 1; i++) {
			if (i % 3 == 0) {
				for (Entry<Character, Integer> entry : counts.entrySet()) {
					if (entry.getValue() == 3) {
						char priority = entry.getKey();

						if (priority > 'Z') {
							sum += 1 + (priority - 'a');
						} else {
							sum += 27 + (priority - 'A');
						}

						break;
					}
				}

				counts.clear();
			}

			if (i == rucksacks.size() - 1) {
				break;
			}

			String rucksack = rucksacks.get(i);
			Set<Character> uniqueChars = new HashSet<>();

			for (char ch : rucksack.toCharArray()) {
				if (uniqueChars.add(ch)) {
					counts.put(ch, counts.getOrDefault(ch, 0) + 1);
				}
			}

		}

		System.out.println(sum);
	}
}
