#class JFormComponentFile extends JFormComponent:
#    /*
#     * Constructor
#     */
#    def __construct(id, label, optionArray = {}):
#        # Class variables
#        self.id = id
#        self.name = self.id
#        self.class = 'jFormComponentFile'
#        self.label = label
#        self.inputClass = 'file'
#
#        #style hacking
#        self.customStyle = True
#
#        # Input options
#        self.type = 'file'
#        self.disabled = False
#        self.maxLength = ''
#        self.styleWidth = ''
#
#        # Initialize the abstract FormComponent object
#        self.initialize(optionArray)
#    }
#
#    def hasInstanceValues():
#        return isset(self.value[0])
#    }
#
#    def getOptions():
#        options = parent::getOptions()
#
#        if(self.customStyle):
#            options['options']['customStyle'] = True
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
#        pseudoFileWrapper = new JFormElement('div', array(
#            'class':'pseudoFile',
#            'style':'position:absolute'
#        ))
#
#        pseudoFileInput = new JFormElement('input', array (
#           'type'=> 'text',
#           'disabled':'disabled',
#        ))
#
#        pseudoFileButton = new JFormElement('button', array (
#           'onclick':'return False',
#           'disabled':'disabled'
#        ))
#        pseudoFileButton.update('Browse...')
#        pseudoFileWrapper.insert(pseudoFileInput)
#        pseudoFileWrapper.insert(pseudoFileButton)
#
#        input = new JFormElement('input', array(
#            'type':self.type,
#            'id':self.id,
#            'name':self.name,
#            'class':self.inputClass,
#            'size'=> 15,
#        ))
#        if(!empty(self.styleWidth)):
#            input.setAttribute('style', 'width: '.self.styleWidth.'')
#        }
#        if(!empty(self.maxLength)):
#            input.setAttribute('maxlength', self.maxLength)
#        }
#        if(self.disabled):
#            input.setAttribute('disabled', 'disabled')
#        }
#        if(self.customStyle){
#            input.addClassName('hidden')
#            div.insert(pseudoFileWrapper)
#        }
#        div.insert(input)
#
#        # Add any description (optional)
#        div = self.insertComponentDescription(div)
#
#        # Add a tip (optional)
#        div = self.insertComponentTip(div)
#
#        return div.__toString()
#    }
#    def required(options):
#        messageArray = array('Required.')
#        return !empty(options['value']) ? 'success' : messageArray
#    }
#
#    def extension(options):
#        messageArray = array('Must have the .'.options.extension.' extension.')
#        extensionRegex = '/\.'.options.extension.'/'
#        return options['value']['name'] == '' || preg_match(extensionRegex , options['value']['name']) ? 'success' : messageArray
#    }
#
#    def extensionType(options):
#        extensionType
#        messageArray = array('Incorrect file type.')
#        
#        if(is_array(options['extensionType'])):
#            extensionType = '/\.('.implode('|', options['extensionType']).')/'
#        }
#        else:
#            extensionObject = new stdClass()
#            extensionObject.image = '/\.(bmp|gif|jpg|png|psd|psp|thm|tif)/i'
#            extensionObject.document = '/\.(doc|docx|log|msg|pages|rtf|txt|wpd|wps)/i'
#            extensionObject.audio = '/\.(aac|aif|iff|m3u|mid|midi|mp3|mpa|ra|wav|wma)/i'
#            extensionObject.video = '/\.(3g2|3gp|asf|asx|avi|flv|mov|mp4|mpg|rm|swf|vob|wmv)/i'
#            extensionObject.web = '/\.(asp|css|htm|html|js|jsp|php|rss|xhtml)/i'
#            extensionType = extensionObject.options['extensionType']
#            messageArray = array('Must be an '.options['extensionType'].' file type.')
#        }
#        return empty(options['value']) || preg_match(extensionType , options['value']['name']) ? 'success' : messageArray
#    }
#    def size(options):
#        if(empty(options['value'])){
#            return 'success'
#        }
#        # they will give filesize in kb
#        fileSizeInKb = self.value['size'] / 1024
#        return fileSizeInKb <= options['size'] ? 'success' : array('File must be smaller then ' . options['size'].'kb. File is '.round(fileSizeInKb, 2). 'kb.')
#    }
#    def imageDimensions(options):
#        if(empty(options['value'])){
#            return 'success'
#        }
#        imageInfo = getimagesize(self.value['tmp_name'])
#
#        # Check to see if the file is an image
#        if(!imageInfo):
#            return array("File is not a valid image file.")
#        } else:
#            errorMessageArray = {}
#            width = imageInfo[0]
#            height = imageInfo[1]
#            if(width > options['width']):
#                errorMessageArray[] = array('The image must be less then '.options['width'].'px wide. File is '.width. 'px.')
#            }
#            if(height > options['height']):
#                errorMessageArray[] = array('The image must be less then '.options['height'].'px tall. File is '.height. 'px.')
#            }
#        }
#        return empty(errorMessageArray) ? 'success' : errorMessageArray
#    }
#
#    def minImageDimensions(options):
#        if(empty(options['value'])){
#            return 'success'
#        }
#        imageInfo = getimagesize(self.value['tmp_name'])
#
#        # Check to see if the file is an image
#        if(!imageInfo):
#            return array("File is not a valid image file.")
#        }
#        else:
#            errorMessageArray = {}
#            width = imageInfo[0]
#            height = imageInfo[1]
#            if(width < options['width']):
#                errorMessageArray[] = array('The image must at least then '.options['width'].'px wide. File is '.width. 'px.')
#            }
#            if(height < options['height']):
#                errorMessageArray[] = array('The image must at least then '.options['height'].'px tall. File is '.height. 'px.')
#            }
#        }
#        return empty(errorMessageArray) ? 'success' : errorMessageArray
#    }
#}
#
#?>
#
