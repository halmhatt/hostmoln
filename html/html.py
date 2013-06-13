
class Tag():
	"""Simple tag class to hold a html tag"""

	tagname = 'div'
	attributes = []
	content = ''
	
	def __init__(self, tagname='div', content='', attributes={}):
	
		self.tagname = tagname
		self.content = content
		self.attributes = attributes
	
	def __str__(self):
		"""Convert to string"""
	
		# If closing itself
		if(self.content is None):
			return '<{0} {1}/>'.format(self.tagname, self.formatAttributes())
	
		return '<{0} {1}>{2}</{0}>'.format(self.tagname, self.formatAttributes(), self.content)
			
	def formatAttributes(self):
		"""Ouput all attributes"""
		
		attributes = []
		
		# Format each attribute
		for key in self.attributes:
			attributes.append(key + '="' + self.attributes[key] + '"')
	
		return ' '.join(attributes)
