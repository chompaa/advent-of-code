import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.HashMap;

class Directory {
	public static HashMap<String, Integer> directorySizes = new HashMap<>();

	private Directory parent;
	private String name;
	private ArrayList<Integer> files;
	private ArrayList<Directory> children;


	public Directory(Directory parent, String name) {
		this.parent = parent;
		this.name = name;
		this.files = new ArrayList<>();
		this.children = new ArrayList<>();

		directorySizes.put(this.name, 0);
	}

	public Directory(String name) {
		this.name = name;	
		this.files = new ArrayList<>();
		this.children = new ArrayList<>();

		directorySizes.put(this.name, 0);
	}

	public static void setDirectorySizes(Directory root) {
		for (int file : root.files) {
			Directory traverse = root;

			while (traverse != null) {
				directorySizes.put(traverse.name, directorySizes.get(traverse.name) + file);
				traverse = traverse.parent;
			}
		}

		for (Directory child : root.getChildren()) {
			setDirectorySizes(child);
		}
	}

	public static HashMap<String, Integer> getDirectorySizes() {
		return directorySizes;
	}

	public Directory getParent() {
		return this.parent;
	}

	public String getName() {
		return this.name.split("-")[0];
	}

	public ArrayList<Directory> getChildren() {
		return this.children;
	}

	public Directory getDirectory(String name) {
		for (Directory child : this.getChildren()) {
			if (child.getName().equals(name)) {
				return child;
			}
		}

		return null;
	}

	public void addFile(Integer file) {
		files.add(file);
	}

	public void addChild(Directory child){
		children.add(child);
	}
}

class Solver {
	public static void main(String[] args) throws Exception {
		ArrayList<String> lines = new ArrayList<>();

		Files.readAllLines(Path.of("example.txt")).forEach(line -> {
			lines.add(line);
		});

		Directory root = new Directory("/");
		Directory cwd = root;
		lines.remove(0);

		for (String line : lines) {
			String[] tokens = line.split(" ");

			if (tokens[1].equals("cd")) {
				String directory = tokens[2];

				if (directory.equals("..")) {
					cwd = cwd.getParent();
				} else {
					cwd = cwd.getDirectory(directory);
				}
			} else if (tokens[1].equals("ls")) {
				continue;
			} else if (tokens[0].equals("dir")) {
				// directories can have same name, append line index for uniqueness
				cwd.addChild(new Directory(cwd, tokens[1] + "-" + lines.indexOf(line)));
			} else {
				cwd.addFile(Integer.parseInt(tokens[0]));
			}
		}

		Directory.setDirectorySizes(root);
		HashMap<String, Integer> sizes = Directory.getDirectorySizes();

		// part 1

		int sizeSum = 0;

		for (int size : sizes.values()) {
			if (size <= 100000) {
				sizeSum += size;
			}
		}

		System.out.println(sizeSum);

		// part 2

		int unused = 70000000 - sizes.get("/");
		int minSpace = Integer.MAX_VALUE;

		for (int size : sizes.values()) {
			if (unused + size >= 30000000) {
				minSpace = Math.min(minSpace, size);
			}
		}

		System.out.println(minSpace);
	}
}
