import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Stack;

class Animation {
	public static final String ANSI_RESET = "\u001B[0m";
	public static final String ANSI_GREEN = "\u001B[32m";

	public static void main(String[] args) throws Exception {
		ArrayList<String> lines = new ArrayList<>();

		Files.readAllLines(Path.of("input.txt")).forEach(line -> {
			lines.add(line);
		});

		// part 1
	
		ArrayList<Stack<Character>> stacks = getStacks(lines);
		
		displayStacks(stacks);

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
				displayStacks(stacks);
				Thread.sleep(50);
			}
		}


	}

	public static void clearConsole() {
		final String os = System.getProperty("os.name");  

		try {
			if (os.contains("Windows")) {
				Runtime.getRuntime().exec("cls");
			} else {
				Runtime.getRuntime().exec("clear");
			}
		} catch (final Exception e) {  
			e.printStackTrace();  
		}

		System.out.print("\033[H\033[2J");  
		System.out.flush();
	}

	public static void displayStacks(ArrayList<Stack<Character>> stacks) {
		clearConsole();

		ArrayList<String> lines = new ArrayList<>();
		StringBuilder colNumbers = new StringBuilder();

		for (int i = 1; i <= stacks.size(); i++) {
			colNumbers.append(String.format("  %d ", i));
		}

		lines.add(colNumbers.toString());
		int maxStack = 0;

		for (Stack<Character> stack : stacks) {
			if (stack.size() > maxStack) {
				maxStack = stack.size();
			}
		}

		for (int i = 0; i < maxStack; i++) {
			StringBuilder crateLine = new StringBuilder();

			for (Stack<Character> stack : stacks) {
				if (i < stack.size() - 1) {
					crateLine.append(String.format(" [%s]", String.valueOf(stack.get(i))));
				} else if (i == stack.size() - 1) {
					crateLine.append(String.format(
								"%s [%s]%s", 
								ANSI_GREEN,
								String.valueOf(stack.get(i)),
								ANSI_RESET
								)
							);
				} else {
					crateLine.append("    ");
				}
			}

			lines.add(crateLine.toString());
		}
		
		Collections.reverse(lines);
		lines.forEach(System.out::println);
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
