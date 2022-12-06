import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solver {
	public static void main(String[] args) throws Exception {
		List<Character> game = Arrays.asList('A', 'C', 'B');
		ArrayList<Character> oppMoves = new ArrayList<>();
		ArrayList<Character> elfMoves = new ArrayList<>();

		Files.readAllLines(Path.of("example.txt")).forEach(line -> {
			oppMoves.add(line.charAt(0));
			elfMoves.add(line.charAt(2));
		});

		// part 1
	
		int score = 0;

		for (int move = 0; move < elfMoves.size(); move++) {
			char elfMove = (char) ((int) elfMoves.get(move) - ('X' - 'A'));
			char oppMove = oppMoves.get(move);

			score += elfMove - 'A' + 1;

			if (elfMove == oppMove) {
				score += 3;
			} else if (game.get(Math.floorMod(game.indexOf(elfMove) + 1, 3)) == oppMove) {
				score += 6;
			}
		}

		System.out.println(score);

		// part 2
		
		score = 0;
		
		for (int move = 0; move < oppMoves.size(); move++) {
			char elfMove = elfMoves.get(move);
			char oppMove = oppMoves.get(move);

			switch (elfMove) {
				case 'X':
					int loseIndex = Math.floorMod(game.indexOf(oppMove) + 1, 3);
					score += game.get(loseIndex) - 'A' + 1;
					break;
				case 'Y':
					score += (oppMove - 'A' + 1) + 3;
					break;
				case 'Z':
					int winIndex = Math.floorMod(game.indexOf(oppMove) - 1, 3);
					score += (game.get(winIndex) - 'A' + 1) + 6;
					break;
			}
		}

		System.out.println(score);
	}
}
