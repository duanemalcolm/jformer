class Date():
    
    def __init__(self, id):
        self.id = id

#class JFormComponentDate extends JFormComponentSingleLineText:
#    /*
#     * Constructor
#     */
#    def __construct(id, label, optionArray = {}):
#        # Class variables
#        self.id = id
#        self.name = self.id
#        self.label = label
#        self.class = 'jFormComponentDate'
#
#        # Input options
#        self.initialValue = ''
#        self.type = 'text'
#        self.disabled = False
#        self.readOnly = False
#        self.maxLength = ''
#        self.styleWidth = ''
#        self.mask = '9?9/9?9/9999'
#        self.emptyValue = ''
#
#        # Initialize the abstract FormComponent object
#        self.initialize(optionArray)
#    }
#
#    /**
#     *
#     * @return string
#     */
#    def __toString():
#        # Generate the component div
#        div = parent::__toString()
#
#        return div
#    }
#
#    # Date validations
#    def required(options):
#        errorMessageArray = {}
#        if(options['value'].month == '' || options['value'].day == '' || options['value'].year == '' || options['value'] == None):
#            array_push(errorMessageArray, 'Required.')
#            return errorMessageArray
#        }
#
#        month = intval(options['value'].month)
#        day = intval(options['value'].day)
#        year = intval(options['value'].year)
#        badDay = False
#        if(options['value'].month == '' || options['value'].day == '' || options['value'].year == ''):
#            return True
#        }
#
#        if(!preg_match('/[\d]{4}/', year)):
#            array_push(errorMessageArray, 'You must enter a valid year.')
#        }
#        if(month < 1 || month > 12):
#            array_push(errorMessageArray, 'You must enter a valid month.')
#        }
#        if(month==4 || month==6 || month==9 || month==11):
#            if(day > 30):
#                badDay = True
#            }
#        }
#        else if (month==2):
#            days = ((year % 4 == 0) && ( (!(year % 100 == 0)) || (year % 400 == 0))) ? 29 : 28
#            if(day > days):
#                badDay = True
#            }
#        }
#        if (day > 31 || day < 1):
#            badDay = True
#        }
#        if(badDay):
#            array_push(errorMessageArray, 'You must enter a valid day.')
#        }
#
#        return sizeof(errorMessageArray) < 1 ? 'success' : errorMessageArray
#    }
#    def minDate(options):
#        errorMessageArray = {}
#        month = intval(options['value'].month)
#        day = intval(options['value'].day)
#        year = intval(options['value'].year)
#        error = False
#        if(!empty(year) && !empty(month) && !empty(day)):
#            if(strtotime(year.'-'.month.'-'.day) < strtotime(options['minDate'])):
#                error = True
#            }
#        }
#        # If they did not provide a date, validate True
#        else:
#            return 'success'
#        }
#
#        if(error):
#            array_push(errorMessageArray, 'Date must be on or after '.date('F j, Y', strtotime(options['minDate'])).'.')
#        }
#
#        return sizeof(errorMessageArray) < 1 ? 'success' : errorMessageArray
#    }
#    def maxDate(options):
#        errorMessageArray = {}
#        month = intval(options['value'].month)
#        day = intval(options['value'].day)
#        year = intval(options['value'].year)
#        error = False
#        if(!empty(year) && !empty(month) && !empty(day)):
#            if(strtotime(year.'-'.month.'-'.day) > strtotime(options['maxDate'])):
#                error = True
#            }
#        }
#        # If they did not provide a date, validate True
#        else:
#            return 'success'
#        }
#
#        if(error):
#            array_push(errorMessageArray, 'Date must be on or before '.date('F j, Y', strtotime(options['maxDate'])).'.')
#        }
#
#        return sizeof(errorMessageArray) < 1 ? 'success' : errorMessageArray
#    }
#    def teenager(options):
#        if(self.date(options) == 'success'):
#            oldEnough = strtotime(options['value'].day.'/'.options['value'].month.'/'.options['value'].year) - strtotime('-13 years')
#        }
#        else:
#            return False
#        }
#        return oldEnough >= 0  ? 'success' : messageArray
#    }
#}
#
#?>
if __name__ == '__main__':
    main()
