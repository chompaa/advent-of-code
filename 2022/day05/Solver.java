import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Stack;

class Solver {
	public static void main(String[] args) throws Exception {
		ArrayList<String> lines = new ArrayList<>();

		Files.readAllLines(Path.of("example.txt")).forEach(line -> {
			lines.add(line);
		});

		// part 1
	
		ArrayList<Stack<Character>> stacks = getStacks(lines);

		for (String line : lines) {
			if (!line.contains("move")) {
				continue;
			}

			String[] instruction = line.split(" ");
			int move = Integer.parseInt(instruction[1]);
			int from = Integer.parseInt(instruction[3]) - 1;
			int to = Integer.parseInt(instruction[5]) - 1;

			for (int j = 0; j < move; j++) {
				stacks.get(to).add(stacks.get(from).pop());
			}
		}

		stacks.forEach(s -> System.out.print(s.peek()));
		System.out.println();

		// part 2

		stacks = getStacks(lines);

		for (String line : lines) {
			if (!line.contains("move")) {
				continue;
			}

			String[] instruction = line.split(" ");
			int move = Integer.parseInt(instruction[1]);
			int from = Integer.parseInt(instruction[3]) - 1;
			int to = Integer.parseInt(instruction[5]) - 1;

			Stack<Character> buffer = new Stack<>();

			for (int j = 0; j < move; j++) {
				buffer.add(stacks.get(from).pop());
			}

			for (int j = 0; j < move; j++) {
				stacks.get(to).add(buffer.pop());
			}
		}

		stacks.forEach(s -> System.out.print(s.peek()));
		System.out.println();
	}

	public static ArrayList<Stack<Character>> getStacks(ArrayList<String> lines) {
		int numberOfStacks = (int) Math.ceil(lines.get(0).length() / 4.0);
		ArrayList<Stack<Character>> stacks = new ArrayList<Stack<Character>>();	

		// popualte ArrayList
		for (int i = 0; i < numberOfStacks; i++) {
			stacks.add(new Stack<Character>());
		}

		for (String line : lines) {
			// have we passed the crates?
			if (line.contains("1")) {
				break;
			}

			for (int col = 0; col < numberOfStacks; col++) {
				Stack<Character> stack = stacks.get(col);

				int charIndex = (col + 1) + (col * 3);
				char letter = line.charAt(charIndex);

				if (letter != ' ') {
					stack.push(line.charAt(charIndex));
				}
			}
		}

		// stacks are currently in reverse order
		for (Stack<Character> stack : stacks) {
			Collections.reverse(stack);
		}

		return stacks;
	}
}
