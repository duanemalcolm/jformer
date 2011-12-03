class Element():
    unaryTagArray = ['input', 'img', 'hr', 'br', 'meta', 'link']
    
    def __init__(self, tag, *args, **kwargs):
        '''
        A Element object describe html tags with attributes and content.
        
        >>> img = Element('IMG', _src='profile.jpg', _class='profile')
        >>> print img
        <img src="profile.jpg" class="profile" />
        >>> img.addClassName('left')
        >>> print img
        <img src="profile.jpg" class="profile left" />
        
        >>> div = Element('Div', 'Joe', img, _id='mydiv')
        >>> print div
        <div id="mydiv">Joe<img src="profile.jpg" class="profile left" /></div>
        
        @param <type> tag
        @param <type> innerHtml
        @param <type> attributes
        '''
        self.tag = tag.lower()
        self.attributeArray =:}
        self.innerHtml = []
        
        for arg in args:
            self.innerHtml.append(arg)
        
        for key in kwargs:
            self.setAttribute(key, kwargs[key])
    
    
    def getAttribute(self, attribute):
        '''
        Set an array, can pass an array or a key, value combination
        
        >>> div = Element('Div', 'Joe', _id='mydiv')
        >>> print div.getAttribute('id')
        mydiv
        
        @param <type> attribute
        @param <type> value
        '''
        return self.attributeArray[attribute]
    
    
    def setAttribute(self, attribute, value=''):
        if attribute[0]=='_':
            attribute = attribute[1:]
        self.attributeArray[attribute] = value
    
    
    def addToAttribute(self, attribute, value=''):
        if attribute in self.attributeArray.keys():
            currentValue = self.attributeArray[attribute]
        else:
            currentValue = ''
        self.setAttribute(attribute, currentValue + value)
        

    def addClassName(self, className) :
        currentClasses = self.getAttribute('class')

        # Check to see if the class is already added
        if className not in currentClasses:
            newClasses = currentClasses+' '+className
            self.setAttribute('class', newClasses)
        
    
    def append(self, obj):
        '''
        Appends an element into the current element
        
        @param <type> obj
        '''
        # DM: Unsure?
        #~ if(@get_class(object) == __class__) :
            #~ self.innerHtml .= object.build()
        #~ 
        #~ else :
            #~ self.innerHtml .= object
        self.innerHtml.append(obj)
        
    
    def update(self, **kwargs):
        '''
        Updates attributes
        
        @param <type> object
        @return <type>
        '''
        for key in kwargs:
            self.setAttribute(key, kwargs[key])
        
        
    def build(self):
        '''
        Builds the element
        
        @return <type>
        '''
        # Start the tag
        element = '<'+self.tag

        # Add attributes
        for key, value in self.attributeArray.iteritems():
            element += ' '+key+'="'+value+'"'
        
        # Close the element
        if self.tag in self.unaryTagArray:
            element += ' />'
        else:
            element += '>'
            for obj in self.innerHtml:
                if isinstance(obj, str):
                    element += obj
                else:
                    element += obj.build()
            element += '</'+self.tag+'>'
        

        # Don't format the XML string, saves time
        #return self.formatXmlString(element)
        return element
    
    
    def __str__(self):
        '''
        Echoes out the element
        
        @return <type>
        '''
        return self.build()
        
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()
