#class JFormComponentAddress extends JFormComponent:
#    self.selectedCountry = None
#    self.selectedState = None
#    self.stateDropDown = False
#    self.emptyValues = None
#    self.showSublabels = True
#    self.unitedStatesOnly = False
#    self.addressLine2Hidden = False
#
#    /*
#     * Constructor
#     */
#    def __construct(id, label, optionArray = {}):
#        # Class variables
#        self.id = id
#        self.name = self.id
#        self.label = label
#        self.class = 'jFormComponentAddress'
#        
#        # Initialize the abstract FormComponent object
#        self.initialize(optionArray)
#
#        # Set the empty values with a boolean
#        if(self.emptyValues === True):
#            self.emptyValues = array('addressLine1':'Street Address', 'addressLine2':'Address Line 2', 'city':'City', 'state':'State / Province / Region', 'zip':'Postal / Zip Code')
#        }
#
#        # United States only switch
#        if(self.unitedStatesOnly):
#            self.stateDropDown = True
#            self.selectedCountry = 'US'
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
#            options['options']['emptyValue'] = self.emptyValues
#        }
#
#        if(self.stateDropDown){
#            options['options']['stateDropDown'] = True
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
#        # Add the Address Line 1 input tag
#        addressLine1Div = new JFormElement('div', array(
#            'class':'addressLine1Div',
#        ))
#        addressLine1 = new JFormElement('input', array(
#            'type':'text',
#            'id':self.id.'-addressLine1',
#            'name':self.name.'-addressLine1',
#            'class':'addressLine1',
#        ))
#        addressLine1Div.insert(addressLine1)
#
#        # Add the Address Line 2 input tag
#        addressLine2Div = new JFormElement('div', array(
#            'class':'addressLine2Div',
#        ))
#        addressLine2 = new JFormElement('input', array(
#            'type':'text',
#            'id':self.id.'-addressLine2',
#            'name':self.name.'-addressLine2',
#            'class':'addressLine2',
#        ))
#        addressLine2Div.insert(addressLine2)
#
#        # Add the city input tag
#        cityDiv = new JFormElement('div', array(
#            'class':'cityDiv',
#        ))
#        city = new JFormElement('input', array(
#            'type':'text',
#            'id':self.id.'-city',
#            'name':self.name.'-city',
#            'class':'city',
#            'maxlength':'15',
#        ))
#        cityDiv.insert(city)
#
#        # Add the State input tag
#        stateDiv = new JFormElement('div', array(
#            'class':'stateDiv',
#        ))
#        if(self.stateDropDown){
#            state = new JFormElement('select', array(
#                'id':self.id.'-state',
#                'name':self.name.'-state',
#                'class':'state',
#            ))
#
#            # Add any options that are not in an opt group to the select
#            foreach(JFormComponentDropDown::getStateArray(self.selectedState) as dropDownOption):
#                optionValue = isset(dropDownOption['value']) ? dropDownOption['value'] : ''
#                optionLabel = isset(dropDownOption['label']) ? dropDownOption['label'] : ''
#                optionSelected = isset(dropDownOption['selected']) ? dropDownOption['selected'] : False
#                optionDisabled = isset(dropDownOption['disabled']) ? dropDownOption['disabled'] : False
#                optionOptGroup = isset(dropDownOption['optGroup']) ? dropDownOption['optGroup'] : ''
#
#                state.insert(self.getOption(optionValue, optionLabel, optionSelected, optionDisabled))
#            }
#        }
#        else:
#            state = new JFormElement('input', array(
#                'type':'text',
#                'id':self.id.'-state',
#                'name':self.name.'-state',
#                'class':'state',
#            ))
#        }
#        stateDiv.insert(state)
#
#        # Add the Zip input tag
#        zipDiv = new JFormElement('div', array(
#            'class':'zipDiv',
#        ))
#        zip = new JFormElement('input', array(
#            'type':'text',
#            'id':self.id.'-zip',
#            'name':self.name.'-zip',
#            'class':'zip',
#            'maxlength':'5',
#        ))
#        zipDiv.insert(zip)
#
#        # Add the country input tag
#        countryDiv = new JFormElement('div', array(
#            'class':'countryDiv',
#        ))
#        # Don't built a select list if you are United States only
#        if(self.unitedStatesOnly):
#            country = new JFormElement('input', array(
#                'type':'hidden',
#                'id':self.id.'-country',
#                'name':self.name.'-country',
#                'class':'country',
#                'value':'US',
#                'style':'display: none',
#            ))
#        }
#        else:
#            country = new JFormElement('select', array(
#                'id':self.id.'-country',
#                'name':self.name.'-country',
#                'class':'country',
#            ))
#            # Add any options that are not in an opt group to the select
#            foreach(JFormComponentDropDown::getCountryArray(self.selectedCountry) as dropDownOption):
#                optionValue = isset(dropDownOption['value']) ? dropDownOption['value'] : ''
#                optionLabel =  isset(dropDownOption['label']) ? dropDownOption['label'] : ''
#                optionSelected = isset(dropDownOption['selected']) ? dropDownOption['selected'] : False
#                optionDisabled = isset(dropDownOption['disabled']) ? dropDownOption['disabled'] : False
#                optionOptGroup = isset(dropDownOption['optGroup']) ? dropDownOption['optGroup'] : ''
#
#                country.insert(self.getOption(optionValue, optionLabel, optionSelected, optionDisabled))
#            }
#        }
#        countryDiv.insert(country)
#
#        # Set the empty values if they are enabled
#        if(!empty(self.emptyValues)):
#            foreach(self.emptyValues as empyValueKey:emptyValue):
#                if(empyValueKey == 'addressLine1'):
#                    addressLine1.setAttribute('value', emptyValue)
#                    addressLine1.addClassName('defaultValue')
#                }
#                if(empyValueKey == 'addressLine2'):
#                    addressLine2.setAttribute('value', emptyValue)
#                    addressLine2.addClassName('defaultValue')
#                }
#                if(empyValueKey == 'city'):
#                    city.setAttribute('value', emptyValue)
#                    city.addClassName('defaultValue')
#                }
#                if(empyValueKey == 'state' && !self.stateDropDown):
#                    state.setAttribute('value', emptyValue)
#                    state.addClassName('defaultValue')
#                }
#                if(empyValueKey == 'zip'):
#                    zip.setAttribute('value', emptyValue)
#                    zip.addClassName('defaultValue')
#                }
#            }
#        }
#
#
#        # Put the sublabels in if the option allows for it
#        if(self.showSublabels):
#            addressLine1Div.insert('<div class="jFormComponentSublabel"><p>Street Address</p></div>')
#            addressLine2Div.insert('<div class="jFormComponentSublabel"><p>Address Line 2</p></div>')
#            cityDiv.insert('<div class="jFormComponentSublabel"><p>City</p></div>')
#
#            if(self.unitedStatesOnly):
#                stateDiv.insert('<div class="jFormComponentSublabel"><p>State</p></div>')
#            }
#            else:
#                stateDiv.insert('<div class="jFormComponentSublabel"><p>State / Province / Region</p></div>')
#            }
#
#            if(self.unitedStatesOnly):
#                zipDiv.insert('<div class="jFormComponentSublabel"><p>Zip Code</p></div>')
#            }
#            else:
#                zipDiv.insert('<div class="jFormComponentSublabel"><p>Postal / Zip Code</p></div>')
#            }
#
#            countryDiv.insert('<div class="jFormComponentSublabel"><p>Country</p></div>')
#        }
#
#        # United States only switch
#        if(self.unitedStatesOnly):
#            countryDiv.setAttribute('style', 'display: none')
#        }
#
#        # Hide address line 2
#        if(self.addressLine2Hidden):
#            addressLine2Div.setAttribute('style', 'display: none')
#        }
#
#        # Insert the address components
#        componentDiv.insert(addressLine1Div)
#        componentDiv.insert(addressLine2Div)
#        componentDiv.insert(cityDiv)
#        componentDiv.insert(stateDiv)
#        componentDiv.insert(zipDiv)
#        componentDiv.insert(countryDiv)
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
#    # Address validations
#    def required(options):
#        errorMessageArray = {}
#        if(options['value'].addressLine1 == ''):
#            array_push(errorMessageArray, array('Street Address is required.'))
#        }
#        if(options['value'].city == ''):
#            array_push(errorMessageArray, array('City is required.'))
#        }
#        if(options['value'].state == ''):
#            array_push(errorMessageArray, array('State is required.'))
#        }
#        if(options['value'].zip == ''):
#            array_push(errorMessageArray, array('Zip is required.'))
#        }
#        if(options['value'].country == ''):
#            array_push(errorMessageArray, array('Country is required.'))
#        }
#        return sizeof(errorMessageArray) < 1 ? 'success' : errorMessageArray
#    }
#}
#
#?>
#
