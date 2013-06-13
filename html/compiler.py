import re
import sys
import html.html as html
from jinja2 import Template, FileSystemLoader

class Compiler():

	# Mapping between Swedish tag names and html tag names
	elementDefinition = {
		'LÄNK': 'a',
		'BILD': 'img',
		'TEXT': 'p',
		'STYCKE': 'p',
		'RUBRIK': 'h1',
		'LISTA': 'ul',
		'NUMMER': 'ol',
		'CITAT': 'blockquote'
	}
	
	# Base html template
	template = Template('''
		<!doctype html>
		<html>
		<head>
			<title>{{ title }}</title>
			{{ head }}
			{{ style }}
		</head>
		<body>
			{{ content }}
	
			{{ javascript }}
		</body>
		</html>
	''')
	
	def compile(self, filename):
		"""Compile file into html"""
		
		# Open file and read lines
		file = open(filename)
		lines = file.readlines()
		file.close()
		
		# Remove comments
		lines = self.removeMultilineComments(lines)
		lines = self.removeSinglelineComments(lines)
		
		# Remove empty lines
		lines = self.removeEmptyLines(lines)
		
		# Create root tags
		tags = self.findTags(0, lines)
		content = ''
		for tagInfo in tags:

			tag = self.createTag(tagInfo['tagLine'], tagInfo['contentLines'])
		
		
			content += str(tag)
			
		# Compile html
		html = self.template.render({
			'title': 'Min webbsida',
			'content': content
		})
		
		return html
	
	def isTag(self, line):
		"""Checks if line is a tag start"""
	
		return re.match('^\s*(LÄNK|BILD|RUBRIK|STYCKE|LISTA|NUMMER|CITAT|TEXT)', line)
		
	def getTagName(self, line):
		"""Get HTML tag name from Swedish capitalized"""
		tagname = re.match('^\s*(LÄNK|BILD|RUBRIK|STYCKE|LISTA|NUMMER|CITAT|TEXT)', line)
	
		return self.elementDefinition[tagname.group(1)]
		
	def getIndentation(self, line):
		"""Returns indentation of line"""
	
		nonSpace = re.search('\S', line)
	
		if nonSpace is None:
			return 0
	
		return nonSpace.start()
		
	def hasIndentation(self, indentation, line):
		"""Returns true if line has same indentation"""
	
		return indentation == self.getIndentation(line)
		
	def findAttributes(self, tagName, tagLine):
		"""Find attributes in tag-line"""
	
		attributes = {}
		
		# Try to find links
		linkMatch = re.search('till\s(BILD)?\s?\'([a-zåäö\.\/\-\_]+)\'', tagLine)
	
		# If link is found
		if linkMatch:
			
			# Modifier can be BILD or SIDA
			modifier = linkMatch.group(1)
			href = linkMatch.group(2)
		
			# If image
			if modifier == 'BILD':
				href = 'bilder/'+href
			
			# Remove href part from tagName
			tagLine = tagLine[:linkMatch.start()] + tagLine[linkMatch.end():]
			
			# Set link attribute
			attributes['href'] = href
		
		# If image, set src
		if tagName == 'img':
			srcMatch = re.search('\'([a-zåäö\.\/\-\_]+)\'', tagLine)
		
			if srcMatch:
				src = 'bilder/'+srcMatch.group(1)
			
				# Remove href part from tagName
				tagLine = tagLine[:srcMatch.start()] + tagLine[srcMatch.end():]
			
			attributes['src'] = src
		
		# Find classes
		classMatch = re.findall('\.([a-zåäö]+)', tagLine)
	
		if classMatch:
	
			attributes['class'] = ' '.join(classMatch)
	
		return attributes
		
	def formatLines(self, contentLines):
		"""Format all lines as text"""
	
		return self.formatText('\n'.join(contentLines))
		
	def formatText(self, text):
		"""Format text with bold and italics"""
	
		# Bold
		text = re.sub(r'\-\-([^\-]+)\-\-', r'<strong>\1</strong>', text)
	
		# Italic
		text = re.sub(r'\-([^\-]+)\-', r'<em>\1</em>', text)
	
		return text
		
	def createTag(self, tagLine, contentLines):
		"""Create a tag from information in tagLine and contentLines)"""

		indentation = self.getIndentation(tagLine)
	
		# Remove indentation
		tagLine.strip()
	
		tagName = self.getTagName(tagLine)
		attributes = self.findAttributes(tagName, tagLine)
	
		content = ''
	
		if tagName in ['img']:
			content = None
	
		# This tag can have content
		else:
			# Find tags in content
			if len(contentLines) > 0:
	
				contentTags = self.findTags(indentation+1, contentLines)
		
				if len(contentTags) > 0:

					# Expand each found tag
					for tagInfo in contentTags:
						tag = self.createTag(tagInfo['tagLine'], tagInfo['contentLines'])
						content += str(tag)
				
				# Just text content
				else:
					content += self.formatLines(contentLines)
			
		return html.Tag(tagName, content, attributes)
		
	def findTags(self, indentation, lines):
		"""Find all tags that has the right indentation"""
	
		tagIndexes = []
		tags = []
	
		# Loop over lines
		for lineNumber, line in enumerate(lines):
		
			# If tag is found with the right indentation
			if self.hasIndentation(indentation, line) and self.isTag(line):
				tagIndexes.append(lineNumber)
		
		# Loop over tag indexes and extract tags 	
		for index, lineNumber in enumerate(tagIndexes):
		
			tagStart = tagIndexes[index]
			start = tagStart+1
		
			# If this is the last tag, all next lines should be added
			if index == len(tagIndexes) - 1:
				end = len(lines)
			else:
				end = tagIndexes[index+1]
		
			# Tag with tag line and content lines as tupple
			tag = {
				'tagLine': lines[tagStart], 
				'contentLines': lines[start:end]
			}
		
			tags.append(tag)
		
		return tags
		
	def removeMultilineComments(self, lines):
		"""Removes multiline comments"""
	
		inComment = False
		for index, line in enumerate(lines):
		
			if inComment is True:
				# End is found, remove start
				if re.search('\.\.\.§', line) is not None:
					lines[index] = re.sub('^(.*\.\.\.§)', '', line)
					inComment = False
				else:
					# Remove whole line
					lines[index] = ''
			
			elif re.search('§\.\.\.', line):
			
				# Remove rest of comment on this line
				lines[index] = re.sub('§.*$', '', line)
				inComment = True
				
		return lines
		
	def removeSinglelineComments(self, lines):
		"""Removes single line comments"""
		
		for index, line in enumerate(lines):
			lines[index] = re.sub('§.*$', '', line)
			
		return lines
		
	def removeEmptyLines(self, lines):
		"""Removes all lines that are empty or whitespace"""

		noneEmptyLines = []
		for line in lines:
			if line.strip() != '':
				noneEmptyLines.append(line)
			
		return noneEmptyLines
	
		
	
