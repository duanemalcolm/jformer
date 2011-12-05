#class JFormComponentLikert extends JFormComponent:
#    self.choiceArray = {}
#    self.statementArray = {}
#    self.showTableHeading = True
#    self.collapseLabelIntoTableHeading = False
#
#    /**
#     * Constructor
#     */
#    def __construct(id, label, choiceArray, statementArray, optionsArray):
#        # General settings
#        self.id = id
#        self.name = self.id
#        self.class = 'jFormComponentLikert'
#        self.label = label
#
#        self.choiceArray = choiceArray
#        self.statementArray = statementArray
#
#        # Initialize the abstract FormComponent object
#        self.initialize(optionsArray)
#    }
#
#    def getOptions():
#        options = parent::getOptions()
#
#        statementArray = {}
#        foreach(self.statementArray as statement):
#            statementArray[statement['name']] = {}
#
#            if(!empty(statement['validationOptions'])):
#                statementArray[statement['name']]['validationOptions'] = statement['validationOptions']
#            }
#
#            if(!empty(statement['triggerFunction'])):
#                statementArray[statement['name']]['triggerFunction'] = statement['triggerFunction']
#            }
#        }
#
#        options['options']['statementArray'] = statementArray
#
#        # Make sure you have an options array to manipulate
#        if(!isset(options['options'])):
#            options['options']  = {}
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
#        componentDiv = parent::generateComponentDiv(!self.collapseLabelIntoTableHeading)
#
#        # Create the table
#        table = new JFormElement('table', array('class':'jFormComponentLikertTable'))
#
#        # Generate the first row
#        if(self.showTableHeading):
#            tableHeadingRow = new JFormElement('tr', array('class':'jFormComponentLikertTableHeading'))
#
#            tableHeading = new JFormElement('th', array(
#                'class':'jFormComponentLikertStatementColumn',
#            ))
#            # Collapse the label into the heading if the option is set
#            if(self.collapseLabelIntoTableHeading):
#                tableHeadingLabel = new JFormElement('label', array(
#                    'class':'jFormComponentLikertStatementLabel',
#                ))
#                tableHeadingLabel.update(self.label)
#                # Add the required star to the label
#                if(in_array('required', self.validationOptions)):
#                    labelRequiredStarSpan = new JFormElement('span', array(
#                        'class':self.labelRequiredStarClass
#                    ))
#                    labelRequiredStarSpan.update(' *')
#                    tableHeadingLabel.insert(labelRequiredStarSpan)
#                }
#                tableHeading.insert(tableHeadingLabel)
#            }
#            tableHeadingRow.insert(tableHeading)
#
#            foreach(self.choiceArray as choice):
#                tableHeadingRow.insert('<th>'.choice['label'].'</th>')
#            }
#            table.insert(tableHeadingRow)
#        }
#        
#        # Insert each of the statements
#        statementCount = 0
#        foreach(self.statementArray as statement):
#            # Set the row style
#            if(statementCount % 2 == 0):
#                statementRowClass = 'jFormComponentLikertTableRowEven'
#            }
#            else:
#                statementRowClass = 'jFormComponentLikertTableRowOdd'
#            }
#
#            # Set the statement
#            statementRow = new JFormElement('tr', array('class':statementRowClass))
#            statementColumn = new JFormElement('td', array('class':'jFormComponentLikertStatementColumn'))
#            statementLabel = new JFormElement('label', array(
#                'class':'jFormComponentLikertStatementLabel',
#                'for':statement['name'].'-choice1',
#            ))
#            statementColumn.insert(statementLabel.insert(statement['statement']))
#
#            # Set the statement description (optional)
#            if(!empty(statement['description'])):
#                statementDescription = new JFormElement('div', array(
#                    'class':'jFormComponentLikertStatementDescription',
#                ))
#                statementColumn.insert(statementDescription.update(statement['description']))
#            }
#
#            # Insert a tip (optional)
#            if(!empty(statement['tip'])):
#                statementTip = new JFormElement('div', array(
#                    'class':'jFormComponentLikertStatementTip',
#                    'style':'display: none',
#                ))
#                statementColumn.insert(statementTip.update(statement['tip']))
#            }
#
#            statementRow.insert(statementColumn)
#
#            choiceCount = 1
#            foreach(self.choiceArray as choice):
#                choiceColumn = new JFormElement('td')
#
#                choiceInput = new JFormElement('input', array(
#                    'id':statement['name'].'-choice'.choiceCount,
#                    'type':'radio',
#                    'value':choice['value'],
#                    'name':statement['name'],
#                ))
#                # Set a selected value if defined
#                if(!empty(statement['selected'])):
#                    if(statement['selected'] == choice['value']):
#                        choiceInput.setAttribute('checked', 'checked')
#                    }
#                }
#                choiceColumn.insert(choiceInput)
#
#                # Choice sub labels
#                if(!empty(choice['sublabel'])):
#                    choiceSublabel = new JFormElement('label', array(
#                        'class':'jFormComponentLikertSublabel',
#                        'for':statement['name'].'-choice'.choiceCount,
#                    ))
#                    choiceSublabel.update(choice['sublabel'])
#                    choiceColumn.insert(choiceSublabel)
#                }
#
#                statementRow.insert(choiceColumn)
#                choiceCount++
#            }
#            statementCount++
#
#            table.insert(statementRow)
#        }
#
#        componentDiv.insert(table)
#
#        # Add any description (optional)
#        componentDiv = self.insertComponentDescription(componentDiv)
#
#        # Add a tip (optional)
#        componentDiv = self.insertComponentTip(componentDiv, self.id.'-div')
#
#        return componentDiv.__toString()
#    }
#
#    # Validation
#    def required(options):
#        errorMessageArray = {}
#        foreach(options['value'] as key:statement):
#            if(empty(statement)):
#                #print_r(key)
#                #print_r(statement)
#                array_push(errorMessageArray, array(key:'Required.'))
#            }
#        }
#
#        return sizeof(errorMessageArray) == 0 ? 'success' : errorMessageArray
#    }
#}
#
#class JFormComponentLikertStatement extends JFormComponent:
#    /**
#     * Constructor
#     */
#    def __construct(id, label, choiceArray, statementArray, optionsArray):
#        # General settings
#        self.id = id
#        self.name = self.id
#        self.class = 'jFormComponentLikertStatement'
#        self.label = label
#        # Initialize the abstract FormComponent object
#        self.initialize(optionsArray)
#    }
#
#    def  __toString():
#        return
#    }
#}
#
#?>
#
