import sys
import html.compiler as html

if __name__ == '__main__':

	# Check that atleast 1 argument exists
	if len(sys.argv) < 2:
		print('Usage: compile.py filename.ssm [output-filename.html]')
		exit() 
		
	Compiler = html.Compiler()

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
