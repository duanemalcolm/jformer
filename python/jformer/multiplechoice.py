#class JFormComponentMultipleChoice extends JFormComponent:
#    self.multipleChoiceType = 'checkbox' # radio, checkbox
#    self.multipleChoiceClass = 'choice'
#    self.multipleChoiceLabelClass = 'choiceLabel'
#    self.multipleChoiceArray = {}
#    self.showMultipleChoiceTipIcons = True
#
#    /**
#     * Constructor
#     */
#    def __construct(id, label, multipleChoiceArray, optionArray = {}):
#        # General settings
#        self.id = id
#        self.name = self.id
#        self.class = 'jFormComponentMultipleChoice'
#        self.label = label
#        self.multipleChoiceArray = multipleChoiceArray
#
#        # Initialize the abstract FormComponent object
#        self.initialize(optionArray)
#    }
#
#    def hasInstanceValues():
#        if(self.multipleChoiceType == 'radio' ){
#            return is_array(self.value)
#        } else:
#            if(!empty(self.value)){
#                return is_array(self.value[0])
#            }
#        }
#        return False
#    }
#
#     /**
#     * MultipleChoice Specific Instance Handling for validation
#     *
#     */
#     def validateComponent():
#        self.passedValidation = True
#        self.errorMessageArray = {}
#
#        if(is_array(self.value[0])){
#            foreach(self.value as value){
#                self.errorMessageArray[] = self.validate(value)
#            }
#        }
#        else:
#            self.errorMessageArray = self.validate(self.value)
#        }
#    }
#
#    def getOptions():
#        options = parent::getOptions()
#
#        # Make sure you have an options array to manipulate
#        if(!isset(options['options'])):
#            options['options']  = {}
#        }
#
#        # Set the multiple choice type
#        options['options']['multipleChoiceType'] = self.multipleChoiceType
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
#        if(sizeof(self.multipleChoiceArray) > 1):
#            div = parent::generateComponentDiv()
#        }
#        else:
#            div = parent::generateComponentDiv(False)
#        }
#        
#        # Case
#        # array(array('value':'option1', 'label':'Option 1', 'checked':'checked', 'tip':'This is a tip'))
#        multipleChoiceCount = 0
#        foreach(self.multipleChoiceArray as multipleChoice):
#            
#            multipleChoiceValue = isset(multipleChoice['value']) ? multipleChoice['value'] : ''
#            multipleChoiceLabel =  isset(multipleChoice['label']) ? multipleChoice['label'] : ''
#            multipleChoiceChecked =  isset(multipleChoice['checked']) ? multipleChoice['checked'] : False
#            multipleChoiceTip =  isset(multipleChoice['tip']) ? multipleChoice['tip'] : ''
#            multipleChoiceDisabled =  isset(multipleChoice['disabled']) ? multipleChoice['disabled'] : ''
#            multipleChoiceInputHidden =  isset(multipleChoice['inputHidden']) ? multipleChoice['inputHidden'] : ''
#
#            multipleChoiceCount++
#
#            div.insert(self.getMultipleChoiceWrapper(multipleChoiceValue, multipleChoiceLabel, multipleChoiceChecked, multipleChoiceTip, multipleChoiceDisabled, multipleChoiceInputHidden, multipleChoiceCount))
#        }
#
#        # Add any description (optional)
#        div = self.insertComponentDescription(div)
#
#        # Add a tip (optional)
#        div = self.insertComponentTip(div, self.id.'-div')
#
#        return div.__toString()
#    }
#    
#    #def to insert tips onto the wrappers
#
#    def getMultipleChoiceWrapper(multipleChoiceValue, multipleChoiceLabel, multipleChoiceChecked, multipleChoiceTip, multipleChoiceDisabled, multipleChoiceInputHidden, multipleChoiceCount):
#        # Make a wrapper div for the input and label
#        multipleChoiceWrapperDiv = new JFormElement('div', array(
#            'id':self.id.'-choice'.multipleChoiceCount.'-wrapper',
#            'class':self.multipleChoiceClass.'Wrapper',
#        ))
#
#        # Input tag
#        input = new JFormElement('input', array(
#            'type':self.multipleChoiceType,
#            'id':self.id.'-choice'.multipleChoiceCount,
#            'name':self.name,
#            'value':multipleChoiceValue,
#            'class':self.multipleChoiceClass,
#            'style':'display: inline',
#        ))
#        if(multipleChoiceChecked == 'checked'):
#            input.setAttribute('checked', 'checked')
#        }
#        if(multipleChoiceDisabled):
#            input.setAttribute('disabled', 'disabled')
#        }
#        if(multipleChoiceInputHidden):
#            input.setAttribute('style', 'display: none')
#        }
#        multipleChoiceWrapperDiv.insert(input)
#
#        # Multiple choice label
#        multipleChoiceLabelElement = new JFormElement('label', array(
#            'for':self.id.'-choice'.multipleChoiceCount,
#            'class':self.multipleChoiceLabelClass,
#            'style':'display: inline',
#        ))
#        # Add an image to the label if there is a tip
#        if(!empty(multipleChoiceTip) && self.showMultipleChoiceTipIcons):
#            multipleChoiceLabelElement.update(multipleChoiceLabel.' <span class="jFormComponentMultipleChoiceTipIcon">&nbsp</span>')
#        }
#        else:
#            multipleChoiceLabelElement.update(multipleChoiceLabel)
#        }
#        # Add a required star if there is only one multiple choice option and it is required
#        if(sizeof(self.multipleChoiceArray) == 1):
#            # Add the required star to the label
#            if(in_array('required', self.validationOptions)):
#                labelRequiredStarSpan = new JFormElement('span', array(
#                    'class':self.labelRequiredStarClass
#                ))
#                labelRequiredStarSpan.update(' *')
#                multipleChoiceLabelElement.insert(labelRequiredStarSpan)
#            }
#        }
#        multipleChoiceWrapperDiv.insert(multipleChoiceLabelElement)
#
#        # Multiple choice tip
#        if(!empty(multipleChoiceTip)):
#            multipleChoiceTipDiv = new JFormElement('div', array(
#                'id':self.id.'-'.multipleChoiceValue.'-tip',
#                'style':'display: none',
#                'class':'jFormComponentMultipleChoiceTip'
#            ))
#            multipleChoiceTipDiv.update(multipleChoiceTip)
#            multipleChoiceWrapperDiv.insert(multipleChoiceTipDiv)
#        }
#
#        return multipleChoiceWrapperDiv
#    }
#
#
#    # Validations
#    def required(options):
#        errorMessageArray = array('Required.')
#        return  sizeof(options['value']) > 0 ? 'success' : errorMessageArray
#    }
#    def minOptions(options):
#        errorMessageArray = array('You must select more than '. options['minOptions'] .' options')
#        return sizeof(options['value']) == 0 || sizeof(options['value']) > options['minOptions'] ? 'success' : errorMessageArray
#    }
#    def maxOptions(options):
#        errorMessageArray = array('You may select up to '. options['maxOptions'] .' options. You have selected '. sizeof(options['value']) . '.')
#        return sizeof(options['value']) == 0 || sizeof(options['value']) <= options['maxOptions'] ? 'success' : errorMessageArray
#    }
#}
#
#?>
#
