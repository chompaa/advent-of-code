import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;

class Solver {
	public static void main(String[] args) throws Exception {
		ArrayList<String> lines = new ArrayList<>();

		Files.readAllLines(Path.of("input.txt")).forEach(line -> {
			lines.add(line);
		});

		ArrayList<ArrayList<Character>> grid = new ArrayList<>(99);
		for (int i = 0; i < grid.size(); i++) {
			ArrayList<Character> row = new ArrayList<>();
			for (int j = 0; j < row.size(); j++) {
				row.add('.');
			}
		}

		HashMap<ArrayList<Integer>, Integer> visited = new HashMap<>();

		int[] headPos = new int[2];
		int[] tailPos = new int[2];

		for (String line : lines) {
			char direction = line.split(" ")[0].charAt(0);
			int amount = Integer.parseInt(line.split(" ")[1]);

			for (int i = 0; i < amount; i++) {
				// move head	
				switch (direction) {
					case 'U':
						headPos[1] += 1;
						break;
					case 'D':
						headPos[1] -= 1;
						break;
					case 'R':
						headPos[0] += 1;
						break;
					case 'L':
						headPos[0] -= 1;
						break;
				}

				ArrayList<Integer> pos = new ArrayList<>(
						Arrays.asList(
							tailPos[0],
							tailPos[1]
						)
				);

				visited.put(pos, visited.getOrDefault(pos, 0) + 1);

				ArrayList<int[]> neighbours = getNeighbours(headPos);

				boolean valid = false;

				for (int[] neighbour : neighbours) {
					if (neighbour[0] == tailPos[0] && neighbour[1] == tailPos[1]) {
						valid = true;
					}
				}

				if (valid) continue;

				int xDir = headPos[0] < tailPos[0] ? -1 : 1;
				int yDir = headPos[1] < tailPos[1] ? -1 : 1;

				// y directions are equal
				if (headPos[1] == tailPos[1]) {
					tailPos[0] += 1 * xDir;
					continue;
				}

				// x directions are equal
				if (headPos[0] == tailPos[0]) {
					tailPos[1] += 1 * yDir;
					continue;
				}
		
				// move diagonal otherwise
				tailPos[0] += 1 * xDir;
				tailPos[1] += 1 * yDir;

			}
		}

		System.out.println(visited.size());
	}


	public static ArrayList<int[]> getNeighbours(int[] position) {
		return new ArrayList<int[]>(
				Arrays.asList(
					new int[] {position[0] + 1, position[1] + 1},
					new int[] {position[0] - 1, position[1] + 1},
					new int[] {position[0] + 1, position[1] - 1},
					new int[] {position[0] - 1, position[1] - 1},
					new int[] {position[0] + 1, position[1]},
					new int[] {position[0] - 1, position[1]},
					new int[] {position[0], position[1] + 1},
					new int[] {position[0], position[1] - 1},
					new int[] {position[0], position[1]}
				)
		);
	}
}
