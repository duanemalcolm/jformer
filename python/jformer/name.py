#class JFormComponentName extends JFormComponent:
#    self.middleInitialHidden = False
#    self.emptyValues = None
#    self.showSublabels = True
#
#    /*
#     * Constructor
#     */
#    def __construct(id, label, optionArray = {}):
#        # Class variables
#        self.id = id
#        self.name = self.id
#        self.label = label
#        self.class = 'jFormComponentName'
#
#        # Input options
#        self.initialValues = array('firstName':'', 'middleInitial':'', 'lastName':'')
#
#        if(self.emptyValues === True):
#            self.emptyValues = array('firstName':'First Name', 'middleInitial':'M' ,'lastName':'Last Name')
#        }
#        #self.mask = ''
#
#        # Initialize the abstract FormComponent object
#        self.initialize(optionArray)
#    }
#
#    def hasInstanceValues():
#        return is_array(self.value)
#    }
#
#    def getOptions():
#        options = parent::getOptions()
#
#        if(!empty(self.emptyValues)):
#            options['options']['emptyValue'] = self.emptyValues
#        }
#
#        if(empty(options['options'])):
#            unset(options['options'])
#        }
#
#        return options
#    }
#
#    /**
#     *
#     * @return string
#     */
#    def __toString():
#        # Generate the component div
#        div = self.generateComponentDiv()
#
#
#        firstNameDiv = new JFormElement('div', array(
#            'class':'firstNameDiv',
#        ))
#        # Add the first name input tag
#        firstName = new JFormElement('input', array(
#            'type':'text',
#            'id':self.id.'-firstName',
#            'name':self.name.'-firstName',
#            'class':'firstName singleLineText',
#            'value':self.initialValues['firstName'],
#        ))
#        firstNameDiv.insert(firstName)
#
#        # Add the middle initial input tag
#        middleInitialDiv = new JFormElement('div', array(
#            'class':'middleInitialDiv',
#        ))
#        middleInitial = new JFormElement('input', array(
#            'type':'text',
#            'id':self.id.'-middleInitial',
#            'name':self.name.'-middleInitial',
#            'class':'middleInitial singleLineText',
#            'maxlength':'1',
#            'value':self.initialValues['middleInitial'],
#        ))
#        if(self.middleInitialHidden):
#            middleInitial.setAttribute('style', 'display: none')
#            middleInitialDiv.setAttribute('style', 'display: none')
#        }
#        middleInitialDiv.insert(middleInitial)
#        
#
#        # Add the last name input tag
#        lastNameDiv = new JFormElement('div', array(
#            'class':'lastNameDiv',
#        ))
#        lastName = new JFormElement('input', array(
#            'type':'text',
#            'id':self.id.'-lastName',
#            'name':self.name.'-lastName',
#            'class':'lastName singleLineText',
#            'value':self.initialValues['lastName'],
#        ))
#        lastNameDiv.insert(lastName)
#
#        if(!empty(self.emptyValues)){
#            self.emptyValues = array('firstName':'First Name', 'middleInitial':'M' ,'lastName':'Last Name')
#            foreach(self.emptyValues as key:value):
#            if(key == 'firstName'):
#                firstName.setAttribute('value', value)
#                firstName.addClassName('defaultValue')
#            }
#            if(key == 'middleInitial'):
#                middleInitial.setAttribute('value', value)
#                middleInitial.addClassName('defaultValue')
#            }
#            if(key == 'lastName'):
#                lastName.setAttribute('value', value)
#                lastName.addClassName('defaultValue')
#            }
#        }
#            
#        }
#
#        if(self.showSublabels):
#            firstNameDiv.insert('<div class="jFormComponentSublabel"><p>First Name</p></div>')
#            middleInitialDiv.insert('<div class="jFormComponentSublabel"><p>MI</p></div>')
#            lastNameDiv.insert('<div class="jFormComponentSublabel"><p>Last Name</p></div>')
#        }
#        
#        div.insert(firstNameDiv)
#        div.insert(middleInitialDiv)
#        div.insert(lastNameDiv)
#
#        # Add any description (optional)
#        div = self.insertComponentDescription(div)
#
#        # Add a tip (optional)
#        div = self.insertComponentTip(div)
#
#        return div.__toString()
#    }
#
#    def required(options):
#        errorMessageArray = {}
#        if(options['value'].firstName == ''):
#            array_push(errorMessageArray, array('First name is required.'))
#        }
#        if(options['value'].lastName == ''):
#            array_push(errorMessageArray, array('Last name is required.'))
#        }
#        return sizeof(errorMessageArray) == 0 ? 'success' : errorMessageArray
#    }
#}
#
#?>
#
