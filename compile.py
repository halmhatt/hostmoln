import sys
import html.compiler as html

if __name__ == '__main__':

	Compiler = html.Compiler()

	if len(sys.argv) < 2:
		print('Usage: compile.py filename.sm')
		exit() 

	# Get filename
	filename = sys.argv[1]

	# Load file
	html = Compiler.compile(filename)
	
	if len(sys.argv) == 3:
		output = open(sys.argv[2], 'w')
		output.write(html)
		output.close()
	else:
		print(html)
