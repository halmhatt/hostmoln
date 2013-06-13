
class Tag():

	tagname = 'div'
	attributes = []
	content = ''
	
	def __init__(self, tagname='div', content='', attributes={}):
		self.tagname = tagname
		self.content = content
		self.attributes = attributes
	
	def __str__(self):
	
		# If closing itself
		if(self.content is None):
			return '<{0} {1}/>'.format(self.tagname, self.attr())
	
		return '<{0} {1}>{2}</{0}>'.format(self.tagname, self.attr(), self.content)
			
	def attr(self):
		attributes = []
		
		for key in self.attributes:
			attributes.append(key + '="' + self.attributes[key] + '"')
	
		return ' '.join(attributes)
