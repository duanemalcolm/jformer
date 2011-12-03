#class JFormComponentSingleLineText extends JFormComponent:
#    self.sublabel
#
#    /*
#     * Constructor
#     */
#    def __construct(id, label, optionArray = {}):
#        # Class variables
#        self.id = id
#        self.name = self.id
#        self.label = label
#        self.class = 'jFormComponentSingleLineText'
#        self.widthArray = array('shortest':'2em', 'short':'6em', 'mediumShort':'9em', 'medium':'12em', 'mediumLong':'15em', 'long':'18em', 'longest':'24em')
#
#        # Input options
#        self.initialValue = ''
#        self.type = 'text' # text, password, hidden
#        self.disabled = False
#        self.readOnly = False
#        self.maxLength = ''
#        self.width = ''
#        self.mask = ''
#        self.emptyValue = ''
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
#        # Make sure you have an options array to manipulate
#        if(!isset(options['options'])):
#            options['options']  = {}
#        }
#
#        # Mask
#        if(!empty(self.mask)):
#            options['options']['mask'] = self.mask
#        }
#
#        # Empty value
#        if(!empty(self.emptyValue)):
#            options['options']['emptyValue'] = self.emptyValue
#        }
#
#        # Clear the options key if there is nothing in it
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
#        # Add the input tag
#        input = new JFormElement('input', array(
#            'type':self.type,
#            'id':self.id,
#            'name':self.name,
#        ))
#        if(!empty(self.width)):
#            if(array_key_exists(self.width, self.widthArray)):
#                input.setAttribute('style', 'width: '.self.widthArray[self.width].'')
#            }
#            else:
#                input.setAttribute('style', 'width: '.self.width.'')
#            }
#        }
#        if(!empty(self.initialValue)):
#            input.setAttribute('value', self.initialValue)
#        }
#        if(!empty(self.maxLength)):
#            input.setAttribute('maxlength', self.maxLength)
#        }
#        if(!empty(self.mask)){
#            self.formComponentMeta['options']['mask']= self.mask
#        }
#        if(self.disabled):
#            input.setAttribute('disabled', 'disabled')
#        }
#        if(self.readOnly):
#            input.setAttribute('readonly', 'readonly')
#        }
#        if(self.enterSubmits):
#            input.addToAttribute('class', ' jFormComponentEnterSubmits')
#        }
#        div.insert(input)
#
#        if(!empty(self.sublabel)):
#            div.insert('<div class="jFormComponentSublabel">'.self.sublabel.'</div>')
#        }
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
#    # Validations
#
#    def alpha(options):
#        messageArray = array('Must only contain letters.')
#        return preg_match('/^[a-z_\s]+/i', options['value']) || options['value'] == '' ? 'success' : messageArray
#    }
#
#    def alphaDecimal(options):
#        messageArray = array('Must only contain letters, numbers, or periods.')
#        return preg_match('/^\w+/', options['value']) || options['value'] == '' ? 'success' : messageArray
#    }
#
#    def alphaNumeric(options):
#        messageArray = array('Must only contain letters or numbers.')
#        return preg_match('/^[a-z0-9_\s]+/i', options['value']) || options['value'] == '' ? 'success' : messageArray
#    }
#    
#    def blank(options):
#        messageArray = array('Must be blank.')
#        return strlen(trim(options['value'])) == 0 ? 'success' : messageArray
#    }
#    
#    def canadianPostal(options):
#        messageArray = array('Must be a valid Canadian postal code.')
#        return preg_match('/^[ABCEGHJKLMNPRSTVXY][0-9][A-Z] [0-9][A-Z][0-9]/', options['value']) || options['value'] == '' ? 'success' : messageArray
#    }
#    
#    def date(options):
#        messageArray = array('Must be a date in the mm/dd/yyyy format.')
#        return preg_match('/^(0?[1-9]|1[012])[\- \/.](0?[1-9]|[12][0-9]|3[01])[\- \/.](19|20)[0-9]{2}/', options['value']) || options['value'] == '' ? 'success' : messageArray
#    }
#    
#    def dateTime(options):
#        messageArray = array('Must be a date in the mm/dd/yyyy hh:mm:ss tt format. ss and tt are optional.')
#        return preg_match('/^(0?[1-9]|1[012])[\- \/.](0?[1-9]|[12][0-9]|3[01])[\- \/.](19|20)?[0-9]{2} [0-2]?\d:[0-5]\d(:[0-5]\d)?( ?(a|p)m)?/i', options['value']) || options['value'] == '' ? 'success' : messageArray
#    }
#    
#    def decimal(options):
#        # Can be negative and have a decimal value
#        # Do not accept commas in value as the DB does not accept them
#        messageArray = array('Must be a number without any commas. Decimal is optional.')
#        return preg_match('/^-?((\d+(\.\d+)?)|(\.\d+))/', options['value']) ? 'success' : messageArray
#    }
#    
#    def decimalNegative(options):
#        # Must be negative and have a decimal value
#        messageArray = array('Must be a negative number without any commas. Decimal is optional.')
#        #isDecimal = self.validations.decimal(options)
#        return (isDecimal == 'success' && (floatval(options['value']) < 0)) ? 'success' : messageArray
#    }
#    
#    def decimalPositive(options):
#        # Must be positive and have a decimal value
#        messageArray = array('Must be a positive number without any commas. Decimal is optional.')
#        #isDecimal = self.validations.decimal(options)
#        return (isDecimal == 'success' && (floatval(options['value']) > 0)) ? 'success' : messageArray
#    }
#       
#    def decimalZeroNegative(options):
#        # Must be negative and have a decimal value
#        messageArray = array('Must be zero or a negative number without any commas. Decimal is optional.')
#        #isDecimal = self.validations.decimal(options)
#        return (isDecimal == 'success' && (floatval(options['value']) <= 0)) ? 'success' : messageArray
#    }
#    
#    def decimalZeroPositive(options):
#        # Must be positive and have a decimal value
#        messageArray = array('Must be zero or a positive number without any commas. Decimal is optional.')
#        #isDecimal = self.validations.decimal(options)
#        return (isDecimal == 'success' && (floatval(options['value']) >= 0)) ? 'success' : messageArray
#    }
#    
#    def email(options):
#        messageArray = array('Must be a valid e-mail address.')
#        return preg_match('/^[A-Z0-9._%-\+]+@(?:[A-Z0-9\-]+\.)+[A-Z]{2,4}/i', options['value']) || options['value'] == '' ? 'success' : messageArray
#    }
#
#    def integer(options):
#        messageArray = array('Must be a whole number.')
#        return preg_match('/^-?\d+/', options['value']) ? 'success' : messageArray
#    }
#
#    def integerNegative(options):
#        messageArray = array('Must be a negative whole number.')
#        #isInteger = preg_match('/^-?\d+/', options['value'])
#        return (isInteger && (intval(options['value'], 10) < 0)) ? 'success' : messageArray
#    }
#
#    def integerPositive(options):
#        messageArray = array('Must be a positive whole number.')
#        #isInteger = preg_match('/^-?\d+/', options['value'])
#        return (isInteger && (intval(options['value'], 10) > 0)) ? 'success' : messageArray
#    }
#
#    def integerZeroNegative(options):
#        messageArray = array('Must be zero or a negative whole number.')
#        #isInteger = preg_match('/^-?\d+/', options['value'])
#        return (isInteger && (intval(options['value'], 10) <= 0)) ? 'success' : messageArray
#    }
#
#    def integerZeroPositive(options):
#        messageArray = array('Must be zero or a positive whole number.')
#        #isInteger = preg_match('/^-?\d+/', options['value'])
#        return (isInteger && (intval(options['value'], 10) >= 0)) ? 'success' : messageArray
#    }
#
#    def isbn(options):
#        #Match an ISBN
#        errorMessageArray = array('Must be a valid ISBN and consist of either ten or thirteen characters.')
#        #For ISBN-10
#        if(preg_match('/^(?=.{13})\d{1,5}([\- ])\d{1,7}\1\d{1,6}\1(\d|X)/', options['value'])):
#            errorMessageArray = 'sucess'
#        }
#        if(preg_match('/^\d{9}(\d|X)/', options['value'])):
#            errorMessageArray = 'sucess'
#        }
#        #For ISBN-13
#        if(preg_match('/^(?=.{17})\d{3}([\- ])\d{1,5}\1\d{1,7}\1\d{1,6}\1(\d|X)/' , options['value'])):
#            errorMessageArray = 'sucess'
#        }
#        if(preg_match('/^\d{3}[\- ]\d{9}(\d|X)/', options['value'])):
#            errorMessageArray = 'sucess'
#        }
#        #ISBN-13 without starting delimiter (Not a valid ISBN but less strict validation was requested)
#        if(preg_match('/^\d{12}(\d|X)/', options['value'])):
#            errorMessageArray = 'sucess'
#        }
#        return errorMessageArray
#    }
#
#    def length(options):
#        messageArray = array('Must be exactly ' . options['length'] .' characters long. Current value is '.strlen(options['value']).' characters.')
#        return strlen(options['value']) == options['length'] || options['value'] == '' ? 'success' : messageArray
#    }
#
#    def matches(options):
#        componentToMatch = self.parentJFormSection.parentJFormPage.jFormer.selectJFormComponent(options['matches'])
#        if(componentToMatch && componentToMatch.value == options['value']):
#            return 'success'
#        }
#        else:
#            return array('Does not match.')
#        }
#    }
#
#    def maxLength(options):
#        messageArray = array('Must be less than ' . options['maxLength'] . ' characters long. Current value is '.strlen(options['value']).' characters.')
#        return strlen(options['value']) <= options['maxLength'] || options['value'] == '' ? 'success' : messageArray
#    }
#
#    def maxFloat(options):
#        messageArray = array('Must be numeric and cannot have more than ' . options['maxFloat'] . ' decimal place(s).')
#        return preg_match('^-?((\\d+(\\.\\d{0,'+ options['maxFloat'] +'})?)|(\\.\\d{0,' . options['maxFloat'] . '}))', options['value'])  ? 'success' : messageArray
#    }
#
#    def maxValue(options):
#        messageArray = array('Must be numeric with a maximum value of ' . options['maxValue'] . '.')
#        return options['maxValue'] >= options['value'] ? 'success' : messageArray
#    }
#
#    def minLength(options):
#        messageArray = array('Must be at least ' . options['minLength'] . ' characters long. Current value is '.strlen(options['value']).' characters.')
#        return strlen(options['value']) >= options['minLength'] || options['value'] == '' ? 'success' : messageArray
#    }
#    
#    def minValue(options):
#        messageArray = array('Must be numeric with a minimum value of ' . options['minValue'] . '.')
#        return options['minValue'] <= options['value'] ? 'success' : messageArray
#    }
#
#    def money(options):
#        messageArray = array('Must be a valid dollar value.')
#        return preg_match('/^\?[1-9][0-9]{0,2}(,?[0-9]{3})*(\.[0-9]{2})?/', options['value']) || options['value'] == '' ? 'success' : messageArray
#    }
#
#    def moneyNegative(options):
#        messageArray = array('Must be a valid negative dollar value.')
#        return preg_match('/^((-?\)|(\-?)|(-))?((\d+(\.\d{2})?)|(\.\d{2}))/', options['value'], matches) && matches[0] < 0 || options['value'] == '' ? 'success' : messageArray
#    }
#
#    def moneyPositive(options):
#        messageArray = array('Must be a valid positive dollar value.')
#        return preg_match('/^((-?\)|(\-?)|(-))?((\d+(\.\d{2})?)|(\.\d{2}))/', options['value'], matches) && matches[0] > 0 || options['value'] == '' ? 'success' : messageArray
#    }
#
#    def moneyZeroNegative(options):
#        messageArray = array('Must be zero or a valid negative dollar value.')
#        return preg_match('/^((-?\)|(\-?)|(-))?((\d+(\.\d{2})?)|(\.\d{2}))/', options['value'], matches) && matches[0] <= 0 ? 'success' : messageArray
#    }
#
#    def moneyZeroPositive(options):
#        messageArray = array('Must be zero or a valid positive dollar value.')
#        return preg_match('/^((-?\)|(\-?)|(-))?((\d+(\.\d{2})?)|(\.\d{2}))/', options['value'], matches) && matches[0]= 0 || options['value'] == '' ? 'success' : messageArray
#    }
#
#    def password(options):
#        messageArray = array('Must be between 4 and 32 characters.')
#        return preg_match('/^.{4,32}/', options['value']) || options['value'] == '' ? 'success' : messageArray
#    }
#
#    def phone(options):
#        messageArray = array('Must be a 10 digit phone number.')
#        return preg_match('/^(1[\-. ]?)?\(?[0-9]{3}\)?[\-. ]?[0-9]{3}[\-. ]?[0-9]{4}/', options['value']) || options['value'] == '' ? 'success' : messageArray 
#    }
#
#    def postalZip(options):
#        messageArray = array('Must be a valid United States zip code, Canadian postal code, or United Kingdom postal code.')
#        postal = False
#        if(this.zip(options) == 'success'):
#            postal = True
#        }
#        if(this.canadianPostal(options) == 'success'):
#            postal = True
#        }
#        if(this.ukPostal(options) == 'success'):
#            postal = True
#        }
#        return postal ? 'success' : messageArray
#    }
#    
#    def required(options):
#        messageArray = array('Required.')
#        #return empty(options['value']) ? 'success' : messageArray # Break validation on purpose
#        return !empty(options['value']) || options['value'] == '0' ? 'success' : messageArray
#    }
#
#    def serverSide(options):
#        # Handle empty values
#        if(empty(options['value'])):
#            return 'success'
#        }
#
#        messageArray = {}
#
#        # Perform the server side check with a scrape
#        serverSideResponse = getUrlContent(options['url'].'&value='.options['value'])
#
#        # Can't read the URL
#        if(serverSideResponse['status'] != 'success'):
#            messageArray[] = 'This component could not be validated.'
#        }
#        # Read the URL
#        else:
#            serverSideResponse = json_decode(serverSideResponse['response'])
#            if(serverSideResponse.status == 'success'):
#                messageArray == 'success'
#            }
#            else:
#                messageArray = serverSideResponse.response
#            }
#        }
#
#        return messageArray
#
#        def getUrlContent(url, postData = None):
#            # Handle objects and arrays
#            curlHandler = curl_init()
#            curl_setopt(curlHandler, CURLOPT_URL, url)
#            curl_setopt(curlHandler, CURLOPT_FAILONERROR, 1)
#            curl_setopt(curlHandler, CURLOPT_TIMEOUT, 20) # Time out in seconds
#            curl_setopt(curlHandler, CURLOPT_RETURNTRANSFER, 1)
#            if (postData != None):
#                foreach (postData as key:&value):
#                    if (is_object(value) || is_array(value)):
#                        value = json_encode(value)
#                    }
#                }
#                curl_setopt(curlHandler, CURLOPT_POSTFIELDS, postData)
#            }
#            request = curl_exec(curlHandler)
#
#            if (!request):
#                response = array('status':'failure', 'response':'CURL error ' . curl_errno(curlHandler) . ': ' . curl_error(curlHandler))
#            } else:
#                response = array('status':'success', 'response':request)
#            }
#
#            return response
#        }
#    }
#
#    def ssn(options):
#        messageArray = array('Must be a valid United States social security number.')
#        return preg_match('/^\d{3}-?\d{2}-?\d{4}/i', options['value']) || options['value'] == '' ? 'success' : messageArray
#    }
#
#    def teenager(options):
#        messageArray = array('Must be at least 13 years old.')
#        if(self.date(options) == 'success'):
#            oldEnough = strtotime(options['value']) - strtotime('-13 years')
#        }
#        else:
#            return False
#        }
#        return oldEnough >= 0  ? 'success' : messageArray
#    }
#
#    def time(options):
#        messageArray = array('Must be a time in the hh:mm:ss tt format. ss and tt are optional.')
#        return preg_match('/^[0-2]?\d:[0-5]\d(:[0-5]\d)?( ?(a|p)m)?/i', options['value']) || options['value'] == '' ? 'success' : messageArray
#    }
#
#    def ukPostal(options):
#        messageArray = array('Must be a valid United Kingdom postal code.')
#        return preg_match('/^[A-Z]{1,2}[0-9][A-Z0-9]? [0-9][ABD-HJLNP-UW-Z]{2}/', options['value']) || options['value'] == '' ? 'success' : messageArray
#    }
#
#    def url(options):
#        messageArray = array('Must be a valid Internet address.')
#        return preg_match('/^((ht|f)tp(s)?:\/\/|www\.)?([\-A-Z0-9.]+)(\.[a-zA-Z]{2,4})(\/[\-A-Z0-9+&@#\/%=~_|!:,.]*)?(\?[\-A-Z0-9+&@#\/%=~_|!:,.]*)?/i', options['value']) || options['value'] == '' ? 'success' : messageArray
#    }
#
#    def username(options):
#        messageArray = array('Must use 4 to 32 characters and start with a letter.')
#        return preg_match('/^[A-Za-z](?=[A-Za-z0-9_.]{3,31})[a-zA-Z0-9_]*\.?[a-zA-Z0-9_]*/', options['value']) || options['value'] == '' ? 'success' : messageArray
#    }
#
#    def zip(options):
#        messageArray = array('Must be a valid United States zip code.')
#        return preg_match('/^[0-9]{5}(?:-[0-9]{4})?/', options['value']) || options['value'] == '' ? 'success' : messageArray
#    }
#
#}
#?>
