import re
import sys
import os
import cgi
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
		'CITAT': 'blockquote',
		'KOD': 'code',
		'RUTA': 'div',
		'HTML': 'html-code'
	}
	
	# Base html template
	template = Template('''
		<!doctype html>
		<html>
		<head>
			<meta charset="utf8"/>
			<title>{{ title }}</title>
			{{ head }}
			
			
			{% for style in styles %}
				<link rel="stylesheet" type="text/css" href="{{ style }}" />
			{% endfor %}
		</head>
		<body>
			{{ content }}
	
			{% for script in javascripts %}
				<script src="{{ script }}"></script>
			{% endfor %}
		</body>
		</html>
	''')
	
	def compile(self, filename):
		"""Compile file into html"""
		
		# Check that file exist
		if os.path.exists(filename) is False:
			print('File {0} does not exist'.format(filename))
			exit()
			
		# Check that file is not a directory
		if os.path.isfile(filename) is False:
			print('File {0} is not a file'.format(filename))
			exit()
			
		# Check if file is readable
		if os.access(filename, os.R_OK) is False:
			print('File {0} is not readable'.format(filename))
			exit()
		
		# Open file and read lines
		file = open(filename)
		lines = file.readlines()
		file.close()
		
		# Remove comments
		lines = self.removeMultilineComments(lines)
		lines = self.removeSinglelineComments(lines)
		
		# Remove empty lines
		lines = self.removeEmptyLines(lines)
		
		# Search for includes
		includes = self.addIncludes(lines)
		
		# Remove includes lines
		lines = self.removeIncludes(lines)
		
		# Create root tags
		tags = self.findTags(0, lines)
		content = ''
		for tagInfo in tags:

			tag = self.createTag(tagInfo['tagLine'], tagInfo['contentLines'])
		
		
			content += str(tag)
			
		# Compile html
		html = self.template.render({
			'title': 'Min webbsida',
			'content': content,
			'styles': includes['styles'],
			'javascripts': includes['javascripts']
		})
		
		return html
	
	def isTag(self, line):
		"""Checks if line is a tag start"""
	
		return re.match('^\s*(LÄNK|BILD|RUBRIK|STYCKE|LISTA|NUMMER|CITAT|TEXT|HTML|KOD|RUTA)', line)
		
	def getTagName(self, line):
		"""Get HTML tag name from Swedish capitalized"""
		tagname = re.match('^\s*(LÄNK|BILD|RUBRIK|STYCKE|LISTA|NUMMER|CITAT|TEXT|HTML|KOD|RUTA)', line)
	
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
		linkMatch = re.search('till\s(BILD|SIDA)?\s?\'([a-zåäö\.\/\-\_]+)\'', tagLine)
	
		# If link is found
		if linkMatch:
			
			# Modifier can be BILD or SIDA
			modifier = linkMatch.group(1)
			href = linkMatch.group(2)
		
			# If image
			if modifier == 'BILD':
				href = 'bilder/'+href
				
			elif modifier == 'SIDA':
				href = 'sidor/'+href
			
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
		classMatch = re.findall('\.([a-zåäö\-]+)', tagLine)
	
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
		
		text = self.convertInlineTags(text)
	
		return text
		
	def convertInlineTags(self, text):
		"""Expands inline tags like NY-RAD"""
		
		for match in re.finditer('(NY[\s\-]RAD)', text):
			
			# Replace newline
			if re.match('(NY[\s\-]RAD)', match.group(1)):
				text = re.sub('(NY[\s\-]RAD)', '<br>', text)
			
		return text
		
	def createTag(self, tagLine, contentLines):
		"""Create a tag from information in tagLine and contentLines)"""

		# If this line does not contain a tag, then use as text
		if not self.isTag(tagLine):
			return self.formatText(tagLine)

		indentation = self.getIndentation(tagLine)
	
		# Remove indentation
		tagLine.strip()
	
		tagName = self.getTagName(tagLine)
		attributes = self.findAttributes(tagName, tagLine)
	
		content = ''
	
		# If tag is image
		if tagName in ['img']:
			content = None
	
		# If list
		elif tagName in['ul', 'ol']:
			for line in contentLines:
				lineMatch = re.match('^\s*(\-|\d+\.?)\s?', line)
			
				# Create list item
				if lineMatch:
					tag =  html.Tag('li', line[lineMatch.end():], attributes)
					content += str(tag)	
					
		# If html
		elif tagName == 'html-code':
			return ''.join(contentLines)
			
		elif tagName == 'code':
			content = '<pre>'+cgi.escape(''.join(contentLines))+'</pre>'

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
		
			# If line has same indentation
			if self.hasIndentation(indentation, line):
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
		
	def addIncludes(self, lines):
		"""Searches for includes and adds them to document, cleans the line afterwards"""
		
		styles = []
		javascripts = []
		
		for line in lines:
			includeMatch = re.match('^\+(STIL|TEMA|JAVASCRIPT)\s\'([a-zåäö\-\_\.\/]+)\'', line)
			
			if includeMatch:
				
				# Find url
				url = includeMatch.group(2)
				
				if includeMatch.group(1) == 'STIL':
					if url[-4:] != '.css':
						url += '.css'
				
					styles.append('stilar/'+url)
					
				elif includeMatch.group(1) == 'TEMA':
					if url[-4:] != '.css':
						url += '.css'
						
					styles.append('stilar/teman/'+url)
					
				else:
					if url[-3:] != '.js':
						url += '.js'
				
					javascripts.append('js/'+url)
			
		return {
			'styles': styles,
			'javascripts': javascripts
		}		
				
	
	def removeIncludes(self, lines):
		"""Searches for includes and clear matching lines"""
		
		for index, line in enumerate(lines):
			
			if re.match('^\+(STIL|TEMA|JAVASCRIPT)', line):
				lines[index] = ''
					
		return lines
		
	
