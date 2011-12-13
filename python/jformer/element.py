class Element():
    
    def __init__(self, tag, attributeArray = {}):
        '''
        Init
        
        >>> e = Element('Div')
        >>> print e.tag
        div
        
        '''
        self.unaryTagArray = ['input', 'img', 'hr', 'br', 'meta', 'link']
        
        self.tag = tag.lower()
        self.attributeArray = {}
        self.innerHtml = []
        
        for attribute, value in attributeArray.iteritems():
            self.setAttribute(attribute, value)
    
    def getAttribute(self, attribute):
        if attribute in self.attributeArray.keys():
            return self.attributeArray[attribute]
        return None
    
    def setAttribute(self, attribute, value = ''):
        if not isinstance(attribute, dict):
            self.attributeArray[attribute] = value
        else:
            self.attributeArray.update(attribute)
        
    def addToAttribute(self, attribute, value = ''):
        if self.attributeArray.has_key(attribute):
            currentValue = self.attributeArray[attribute] + ' '
        else:
            currentValue = ''
        
        self.attributeArray[attribute] = currentValue + value

    def addClassName(self, className):
        if 'class' in self.attributeArray.keys():
            currentClasses = self.getAttribute('class').split()
        else:
            currentClasses = []
        
        # Check to see if the class is already added
        if className not in currentClasses:
            currentClasses.append(className)
            self.setAttribute('class', ' '.join(currentClasses))
        
    def insert(self, obj):
        '''
        Insert an element object or html string into the current
        element.
        '''
        self.innerHtml.append(obj)
        
    def update(self, obj):
        '''
        Set the innerHtml of an element
        
        *** DM:
        Not sure if this is the correct function, it replaces the
        entire innerHtml array with a element object.
        ***
        
        '''
        #~ self.innerHtml = obj # was this
        self.innerHtml = [obj]
        
    def build(self):
        '''
        Builds the html string for the element object.
        '''
        # Start the tag
        element = '<'+self.tag

        # Add attributes
        for key, value in self.attributeArray.iteritems():
                element += ' '+key+'="'+value+'"'

        # Add innerHtml and close the element
        if self.tag in self.unaryTagArray:
            element += ' />'
        else:
            element += '>'
            for obj in self.innerHtml:
                if isinstance(obj, str):
                    element += obj
                else:
                    element += obj.__str__()
            element += '</'+self.tag+'>'
            
        # Don't format the XML string, saves time
        # return self.formatXmlString(element)
        return element
    
    def __str__(self):
        return self.build()
 
