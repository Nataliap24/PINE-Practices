from pathlib import Path
FILENAME = "U5.txt"
text = Path(FILENAME).read_text()
lines = text.split("\n")
print (lines[0])