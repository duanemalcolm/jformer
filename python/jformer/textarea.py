from component import _Component

class TextArea(_Component):
    
    def __init__(self, id, label, optionArray = {}):
        _Component.__init__(self)
        
        # Class variables
        self.id = id
        self.name = self.id
        self.label = label
        self._class = 'jFormComponentTextArea'
        self.inputClass = 'textArea'
        self.widthArray = {'shortest':'5em', 'short':'10em', 'medium':'20em', 'long':'30em', 'longest':'40em'}
        self.heightArray = {'short':'6em', 'medium':'12em', 'tall':'18em'}

        # Input options
        self.initialValue = ''
        self.disabled = False
        self.readOnly = False
        self.wrap = '' # hard, off
        self.width = ''
        self.height = ''
        self.style = ''
        self.allowTabbing = False
        self.emptyValue = ''
        self.autoGrow = False

        # Initialize the abstract FormComponent object
        #~ self.initialize(optionArray)
#
#    def hasInstanceValues():
#        return is_array(self.value)
#    }
#
#    def getOptions():
#        options = parent::getOptions()
#
#        # Tabbing
#        if(self.allowTabbing):
#            options['options']['allowTabbing'] = True
#        }
#
#        # Empty value
#        if(!empty(self.emptyValue)):
#            options['options']['emptyValue'] = self.emptyValue
#        }
#
#        # Auto grow
#        if(self.autoGrow):
#            options['options']['autoGrow'] = self.autoGrow
#        }
#
#        return options

    #~ def __str__():
        #~ # Generate the component div
        #~ div = self.generateComponentDiv()
#~ 
        #~ # Add the input tag
        #~ textArea = new JFormElement('textarea', array(
            #~ 'id':self.id,
            #~ 'name':self.name,
            #~ 'class':self.inputClass,
        #~ ))
        #~ if(!empty(self.width)):
            #~ if(array_key_exists(self.width, self.widthArray)):
                #~ textArea.setAttribute('style', 'width: '.self.widthArray[self.width].'')
            #~ }
            #~ else:
                #~ textArea.setAttribute('style', 'width: '.self.width.'')
            #~ }
        #~ }
        #~ if(!empty(self.height)):
            #~ if(array_key_exists(self.height, self.heightArray)):
                #~ textArea.addToAttribute('style', 'height: '.self.heightArray[self.height].'')
            #~ }
            #~ else:
                #~ textArea.addToAttribute('style', 'height: '.self.height.'')
            #~ }
        #~ }
        #~ if(!empty(self.style)):
            #~ textArea.addToAttribute('style', self.style)
        #~ }
        #~ if(self.disabled):
            #~ textArea.setAttribute('disabled', 'disabled')
        #~ }
        #~ if(self.readOnly):
            #~ textArea.setAttribute('readonly', 'readonly')
        #~ }
        #~ if(self.wrap):
            #~ textArea.setAttribute('wrap', self.wrap)
        #~ }
        #~ if(!empty(self.initialValue)):
            #~ textArea.update(self.initialValue)
        #~ }
        #~ div.insert(textArea)
#~ 
        #~ # Add any description (optional)
        #~ div = self.insertComponentDescription(div)
#~ 
        #~ # Add a tip (optional)
        #~ div = self.insertComponentTip(div)
#~ 
        #~ return div.__str__()
       
