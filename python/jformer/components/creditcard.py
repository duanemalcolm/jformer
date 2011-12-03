#class JFormComponentCreditCard extends JFormComponent:
#    self.emptyValues = None # cardNumber, securityCode
#    self.showSublabels = True
#    self.showCardType = True
#    self.showSecurityCode = True
#    self.creditCardProviders = array('visa':'Visa', 'masterCard':'MasterCard', 'americanExpress':'American Express', 'discover':'Discover')
#    self.showMonthName = True
#    self.showLongYear = True
#
#    /*
#     * Constructor
#     */
#    def __construct(id, label, optionArray = {}):
#        # Class variables
#        self.id = id
#        self.name = self.id
#        self.label = label
#        self.class = 'jFormComponentCreditCard'
#        
#        # Initialize the abstract FormComponent object
#        self.initialize(optionArray)
#
#        # Set the empty values with a boolean
#        if(self.emptyValues === True):
#            self.emptyValues = array('cardNumber':'Card Number', 'securityCode':'CSC/CVV')
#        }
#    }
#
#    def getOption(optionValue, optionLabel, optionSelected, optionDisabled):
#        option = new JFormElement('option', array('value':optionValue))
#        option.update(optionLabel)
#
#        if(optionSelected):
#            option.setAttribute('selected', 'selected')
#        }
#
#        if(optionDisabled):
#            option.setAttribute('disabled', 'disabled')
#        }
#
#        return option
#    }
#
#    def getOptions():
#        options = parent::getOptions()
#
#        if(!empty(self.emptyValues)):
#            options['options']['emptyValues'] = self.emptyValues
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
#        componentDiv = self.generateComponentDiv()
#
#         # Add the card type select tag
#        if(self.showCardType):
#            cardTypeDiv = new JFormElement('div', array(
#                'class':'cardTypeDiv',
#            ))
#            cardType = new JFormElement('select', array(
#                'id':self.id.'-cardType',
#                'name':self.name.'-cardType',
#                'class':'cardType',
#            ))
#            # Have a default value the drop down list if there isn't a sublabel
#            if(self.showSublabels == False){
#                cardType.insert(self.getOption('', 'Card Type', True, True))
#            }
#            # Add the card types
#            foreach(self.creditCardProviders as key:value):
#                cardType.insert(self.getOption(key, value, False, False))
#            }
#            cardTypeDiv.insert(cardType)
#        }
#
#        # Add the card number input tag
#        cardNumberDiv = new JFormElement('div', array(
#            'class':'cardNumberDiv',
#        ))
#        cardNumber = new JFormElement('input', array(
#            'type':'text',
#            'id':self.id.'-cardNumber',
#            'name':self.name.'-cardNumber',
#            'class':'cardNumber',
#            'maxlength':'16',
#        ))
#        cardNumberDiv.insert(cardNumber)
#
#        # Add the expiration month select tag
#        expirationDateDiv = new JFormElement('div', array(
#            'class':'expirationDateDiv',
#        ))
#        expirationMonth = new JFormElement('select', array(
#            'id':self.id.'-expirationMonth',
#            'name':self.name.'-expirationMonth',
#            'class':'expirationMonth',
#        ))
#        # Have a default value the drop down list if there isn't a sublabel
#        if(self.showSublabels == False){
#            expirationMonth.insert(self.getOption('', 'Month', True, True))
#        }
#        # Add the months
#        foreach(JFormComponentDropDown::getMonthArray() as dropDownOption):
#            optionValue = isset(dropDownOption['value']) ? dropDownOption['value'] : ''
#            optionLabel = isset(dropDownOption['label']) ? dropDownOption['label'] : ''
#            optionSelected = isset(dropDownOption['selected']) ? dropDownOption['selected'] : False
#            optionDisabled = isset(dropDownOption['disabled']) ? dropDownOption['disabled'] : False
#            optionOptGroup = isset(dropDownOption['optGroup']) ? dropDownOption['optGroup'] : ''
#
#            if(self.showMonthName):
#                expirationMonth.insert(self.getOption(optionValue, optionValue.' - '.optionLabel, optionSelected, optionDisabled))
#                expirationMonth.addClassName('long')
#            }
#            else:
#                expirationMonth.insert(self.getOption(optionValue, optionValue, optionSelected, optionDisabled))
#            }
#        }
#        expirationDateDiv.insert(expirationMonth)
#        # Add the expiration year select tag
#        expirationYear = new JFormElement('select', array(
#            'id':self.id.'-expirationYear',
#            'name':self.name.'-expirationYear',
#            'class':'expirationYear',
#        ))
#        # Add years
#        if(self.showLongYear):
#            startYear = Date('Y')
#            expirationYear.addClassName('long')
#        }
#        else:
#            startYear = Date('y')
#            if(!self.showMonthName):
#                expirationDateDiv.insert('<span class="expirationDateSeparator">/</span>')
#            }
#        }
#        if(self.showSublabels == False){
#            expirationYear.insert(self.getOption('', 'Year', True, True))
#        }
#        foreach(range(startYear, startYear+6) as year):
#            expirationYear.insert(self.getOption(year, year, False, False))
#        }
#        expirationDateDiv.insert(expirationYear)
#
#        # Add the security code input tag
#        securityCodeDiv = new JFormElement('div', array(
#            'class':'securityCodeDiv',
#        ))
#        securityCode = new JFormElement('input', array(
#            'type':'text',
#            'id':self.id.'-securityCode',
#            'name':self.name.'-securityCode',
#            'class':'securityCode',
#            'maxlength':'4',
#        ))
#        securityCodeDiv.insert(securityCode)
#
#        # Set the empty values if they are enabled
#        if(!empty(self.emptyValues)):
#            foreach(self.emptyValues as emptyValueKey:emptyValue):
#                if(emptyValueKey == 'cardNumber'):
#                    cardNumber.setAttribute('value', emptyValue)
#                    cardNumber.addClassName('defaultValue')
#                }
#                if(emptyValueKey == 'securityCode'):
#                    securityCode.setAttribute('value', emptyValue)
#                    securityCode.addClassName('defaultValue')
#                }
#            }
#        }
#
#        # Put the sublabels in if the option allows for it
#        if(self.showSublabels):
#            if(self.showCardType):
#                cardTypeDiv.insert('<div class="jFormComponentSublabel"><p>Card Type</p></div>')
#            }
#            cardNumberDiv.insert('<div class="jFormComponentSublabel"><p>Card Number</p></div>')
#            expirationDateDiv.insert('<div class="jFormComponentSublabel"><p>Expiration Date</p></div>')
#            if(self.showSecurityCode):
#                securityCodeDiv.insert('<div class="jFormComponentSublabel"><p>Security Code</p></div>')
#            }
#        }
#
#        # Insert the components
#        if(self.showCardType):
#            componentDiv.insert(cardTypeDiv)
#        }
#        componentDiv.insert(cardNumberDiv)
#        componentDiv.insert(expirationDateDiv)
#        if(self.showSecurityCode):
#            componentDiv.insert(securityCodeDiv)
#        }
#        
#        # Add any description (optional)
#        componentDiv = self.insertComponentDescription(componentDiv)
#
#        # Add a tip (optional)
#        componentDiv = self.insertComponentTip(componentDiv)
#
#        return componentDiv.__toString()
#    }
#
#    # Credit card validations
#    def required(options):
#        errorMessageArray = {}
#        if(self.showCardType && empty(options['value'].cardType)):
#            array_push(errorMessageArray, array('Card type is required.'))
#        }
#        if(empty(options['value'].cardNumber)):
#            array_push(errorMessageArray, array('Card number is required.'))
#        }
#        else:
#            if(preg_match('/[^\d]/', options['value'].cardNumber)):
#                array_push(errorMessageArray, array('Card number may only contain numbers.'))
#            }
#            if(strlen(options['value'].cardNumber) > 16 || strlen(options['value'].cardNumber) < 13):
#                array_push(errorMessageArray, array('Card number must contain 13 to 16 digits.'))
#            }
#        }
#        if(empty(options['value'].expirationMonth)):
#            array_push(errorMessageArray, array('Expiration month is required.'))
#        }
#        if(empty(options['value'].expirationYear)):
#            array_push(errorMessageArray, array('Expiration year is required.'))
#        }
#        if(self.showSecurityCode && empty(options['value'].securityCode)):
#            array_push(errorMessageArray, array('Security code is required.'))
#        }
#        else if(self.showSecurityCode):
#            if(preg_match('/[^\d]/', options['value'].securityCode)):
#                array_push(errorMessageArray, array('Security code may only contain numbers.'))
#            }
#            if(strlen(options['value'].securityCode) > 4 || strlen(options['value'].securityCode) < 3):
#                array_push(errorMessageArray, array('Security code must contain 3 or 4 digits.'))
#            }
#        }
#        return sizeof(errorMessageArray) < 1 ? 'success' : errorMessageArray
#    }
#}
#
#?>
#
