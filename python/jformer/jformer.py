from jformelement import Element
from jformsection import Section
from jformpage import Page

class JFormer():
    
    def __init__(self, id):
        self.id = id
        self._class = 'jFormer'
        self.action = None
        self.style = None
        self.jFormPageArray =:}
        self.jFormerId = None
        self.onSubmitFunctionServerSide = 'onSubmit'
        self.disableAnalytics = False
        self.setupPageScroller = True
        self.data = None
        # Title, description, and submission button
        self.title = ''
        self.titleClass = 'jFormerTitle'
        self.description = ''
        self.descriptionClass = 'jFormerDescription'
        self.submitButtonText = 'Submit'
        self.submitProcessingButtonText = 'Processing...'
        self.afterControl = ''
        self.cancelButton = False
        self.cancelButtonOnClick = ''
        self.cancelButtonText = 'Cancel'
        self.cancelButtonClass = 'cancelButton'
        # Form options
        self.alertsEnabled = True
        self.clientSideValidation = True
        self.debugMode = False
        self.validationTips = True
        # Page navigator
        self.pageNavigatorEnabled = False
        self.pageNavigator = []
        # Splash page
        self.splashPageEnabled = False
        self.splashPage = []
        # Animations
        self.animationOptions = None
        # Custom script execution before form submission
        self.onSubmitStartClientSide = ''
        self.onSubmitFinishClientSide = ''
        # Essential class variables
        self.status =:'status':'processing', 'response':'Form initialized.'}
        # Validation
        self.validationResponse = []
        self.validationPassed = None
        # Required Text
        self.requiredText = ' *'

        # Set the action dynamically
        # DM: unsure?
        #~ callingFile = debug_backtrace()
        #~ callingFile = str_replace("\\", "/", callingFile[0]['file'])
        #~ self.action = str_replace(_SERVER['DOCUMENT_ROOT'], '', callingFile)
        
        # Set defaults for the page navigator
        if self.pageNavigator == None:
            self.pageNavigatorEnabled = True
        elif self.pageNavigator == True:
            self.pageNavigator =:'position':'top'}

        # Set defaults for the splash page
        if self.splashPage == None:
            self.splashPageEnabled = True

        # Add the pages from the constructor
        # DM: will defally add pages after the class is instantiated
        #~ foreach (jFormPageArray as jFormPage):
            #~ self.addJFormPage(jFormPage)
        #~ }

    def addJFormPage(self, jFormPage):
        jFormPage.jFormer = self
        self.jFormPageArray[jFormPage.id] = jFormPage
        
#~ def addJFormPages(jFormPages):
#        if (is_array(jFormPages)):
#            foreach (jFormPages as jFormPage):
#                jFormPage.jFormer = this
#                self.jFormPageArray[jFormPage.id] = jFormPage
#            }
#        }
#        jFormPage.jFormer = this
#        self.jFormPageArray[jFormPage.id] = jFormPage
#        return this
#    }
#
#    # Convenience method, no need to create a page or section to get components on the form
#    def addJFormComponent(jFormComponent):
#        # Create an anonymous page if necessary
#        if (empty(self.jFormPageArray)):
#            self.addJFormPage(new JFormPage(self.id . '_page1', array('anonymous':True)))
#        }
#
#        # Get the first page in the jFormPageArray
#        currentJFormPage = current(self.jFormPageArray)
#
#        # Get the last section in the page
#        lastJFormSection = end(currentJFormPage.jFormSectionArray)
#
#        # If the last section exists and is anonymous, add the component to it
#        if (!empty(lastJFormSection) && lastJFormSection.anonymous):
#            lastJFormSection.addJFormComponent(jFormComponent)
#        }
#        # If the last section in the page does not exist or is not anonymous, add a new anonymous section and add the component to it
#        else:
#            # Create an anonymous section
#            anonymousSection = new JFormSection(currentJFormPage.id . '_section' . (sizeof(currentJFormPage.jFormSectionArray) + 1), array('anonymous':True))
#
#            # Add the anonymous section to the page
#            currentJFormPage.addJFormSection(anonymousSection.addJFormComponent(jFormComponent))
#        }
#
#        return this
#    }
#
#    def addJFormComponentArray(jFormComponentArray):
#        foreach (jFormComponentArray as jFormComponent):
#            self.addJFormComponent(jFormComponent)
#        }
#        return this
#    }
#
#    # Convenience method, no need to create a to get a section on the form
#    def addJFormSection(jFormSection):
#        # Create an anonymous page if necessary
#        if (empty(self.jFormPageArray)):
#            self.addJFormPage(new JFormPage(self.id . '_page1', array('anonymous':True)))
#        }
#
#        # Get the first page in the jFormPageArray
#        currentJFormPage = current(self.jFormPageArray)
#
#        # Add the section to the first page
#        currentJFormPage.addJFormSection(jFormSection)
#
#        return this
#    }
#
#    def setStatus(status, response):
#        self.status = array('status':status, 'response':response)
#        return self.status
#    }
#
#    def resetStatus():
#        self.status = array('status':'processing', 'response':'Form status reset.')
#        return self.status
#    }
#
#    def getStatus():
#        return self.status
#    }
#
#    def validate():
#        # Update the form status
#        self.setStatus('processing', 'Validating component values.')
#
#        # Clear the validation response
#        self.validationResponse = {}
#
#        # Validate each page
#        foreach (self.jFormPageArray as jFormPage):
#            self.validationResponse[jFormPage.id] = jFormPage.validate()
#        }
#        # Walk through all of the pages to see if there are any errors
#        self.validationPassed = True
#
#        foreach (self.validationResponse as jFormPageKey:jFormPage):
#            foreach (jFormPage as jFormSectionKey:jFormSection):
#                # If there are section instances
#                if (jFormSection != None && array_key_exists(0, jFormSection) && is_array(jFormSection[0])):
#                    foreach (jFormSection as jFormSectionInstanceIndex:jFormSectionInstance):
#                        foreach (jFormSectionInstance as jFormComponentKey:jFormComponentErrorMessageArray):
#                            # If there are component instances
#                            if (jFormComponentErrorMessageArray != None && array_key_exists(0, jFormComponentErrorMessageArray) && is_array(jFormComponentErrorMessageArray[0])):
#                                foreach (jFormComponentErrorMessageArray as jFormComponentInstanceErrorMessageArray):
#                                    # If the first value is not empty, the component did not pass validation
#                                    if (!empty(jFormComponentInstanceErrorMessageArray[0]) || sizeof(jFormComponentInstanceErrorMessageArray) > 1):
#                                        self.validationPassed = False
#                                    }
#                                }
#                            } else:
#                                if (!empty(jFormComponentErrorMessageArray)):
#                                    self.validationPassed = False
#                                }
#                            }
#                        }
#                    }
#                }
#                # No section instances
#                else:
#                    foreach (jFormSection as jFormComponentErrorMessageArray):
#                        # Component instances
#                        if (jFormComponentErrorMessageArray != None && array_key_exists(0, jFormComponentErrorMessageArray) && is_array(jFormComponentErrorMessageArray[0])):
#                            foreach (jFormComponentErrorMessageArray as jFormComponentInstanceErrorMessageArray):
#                                # If the first value is not empty, the component did not pass validation
#                                if (!empty(jFormComponentInstanceErrorMessageArray[0]) || sizeof(jFormComponentInstanceErrorMessageArray) > 1):
#                                    self.validationPassed = False
#                                }
#                            }
#                        } else:
#                            if (!empty(jFormComponentErrorMessageArray)):
#                                self.validationPassed = False
#                            }
#                        }
#                    }
#                }
#            }
#        }
#
#        # Update the form status
#        self.setStatus('processing', 'Validation complete.')
#
#        return self.validationResponse
#    }
#
#    def getData():
#        self.data = {}
#
#        foreach (self.jFormPageArray as jFormPageKey:jFormPage):
#            if (!jFormPage.anonymous):
#                self.data[jFormPageKey] = jFormPage.getData()
#            } else:
#                foreach (jFormPage.jFormSectionArray as jFormSectionKey:jFormSection):
#                    if (!jFormSection.anonymous):
#                        self.data[jFormSectionKey] = jFormSection.getData()
#                    } else:
#                        foreach (jFormSection.jFormComponentArray as jFormComponentKey:jFormComponent):
#                            if (get_class(jFormComponent) != 'JFormComponentHtml'): # Don't include HTML components
#                                self.data[jFormComponentKey] = jFormComponent.getValue()
#                            }
#                        }
#                    }
#                }
#            }
#        }
#        return json_decode(json_encode(self.data))
#    }
#
#    def updateRequiredText(requiredText):
#        foreach(self.jFormPageArray as jFormPage):
#            jFormPage.updateRequiredText(requiredText)
#        }
#    }
#
#    def setInitialValues(formValues):
#        # Make sure we are always working with an object
#        if (!is_object(formValues)):
#            formValues = json_decode(urldecode(formValues))
#            if (!is_object(formValues)):
#                formValues = json_decode(urldecode(stripslashes(data)))
#            }
#        }
#
#        # Walk through the form object and apply initial values
#        foreach (formValues as formPageKey:formPageData):
#            self.formPageArray[formPageKey].setInitialValues(formPageData)
#        }
#    }
#
#    def setData(data, fileArray = {}):
#        # Get the form data as an object, handle apache auto-add slashes on post requests
#        jFormerData = json_decode(urldecode(data))
#        if (!is_object(jFormerData)):
#            jFormerData = json_decode(urldecode(stripslashes(data)))
#        }
#
#        # Clear all of the component values
#        self.clearData()
#
#        #print_r(jFormerData) exit()
#        #print_r(fileArray)
#        # Update the form status
#        self.setStatus('processing', 'Setting component values.')
#
#        # Assign all of the received JSON values to the form
#        foreach (jFormerData as jFormPageKey:jFormPageData):
#            self.jFormPageArray[jFormPageKey].setData(jFormPageData)
#        }
#
#        # Handle files
#        if (!empty(fileArray)):
#            foreach (fileArray as jFormComponentId:fileDataArray):
#                preg_match('/(-section([0-9])+)?(-instance([0-9])+)?:([A-Za-z0-9_-]+):([A-Za-z0-9_-]+)/', jFormComponentId, fileIdInfo)
#
#                jFormComponentId = str_replace(fileIdInfo[0], '', jFormComponentId)
#                jFormPageId = fileIdInfo[5]
#                jFormSectionId = fileIdInfo[6]
#
#                # Inside section instances
#                if (fileIdInfo[1] != None || (fileIdInfo[1] == None && array_key_exists(0, self.jFormPageArray[jFormPageId].jFormSectionArray[jFormSectionId].jFormComponentArray))):
#                    # section instance
#                    # set the instance index
#                    if (fileIdInfo[1] != None):
#                        jFormSectionInstanceIndex = fileIdInfo[2] - 1
#                    } else:
#                        # prime instance
#                        jFormSectionInstanceIndex = 0
#                    }
#                    # check to see if there is a component instance
#                    if (fileIdInfo[3] != None || (fileIdInfo[3] == None && is_array(self.jFormPageArray[jFormPageId].jFormSectionArray[jFormSectionId].jFormComponentArray[jFormSectionInstanceIndex][jFormComponentId].value))):
#                        # set the component instance index inside of a  section instance
#                        if (fileIdInfo[3] == None):
#                            jFormComponentInstanceIndex = 0
#                        } else:
#                            jFormComponentInstanceIndex = fileIdInfo[4] - 1
#                        }
#                        # set the value with a section and a component instance
#                        self.jFormPageArray[jFormPageId].jFormSectionArray[jFormSectionId].jFormComponentArray[jFormSectionInstanceIndex][jFormComponentId].value[jFormComponentInstanceIndex] = fileDataArray
#                    } else:
#                        # set the value with a section instance
#                        self.jFormPageArray[jFormPageId].jFormSectionArray[jFormSectionId].jFormComponentArray[jFormSectionInstanceIndex][jFormComponentId].value = fileDataArray
#                    }
#                }
#
#                # Not section instances
#                else:
#                    # has component instances
#                    if (fileIdInfo[3] != None || (fileIdInfo[3] == None && is_array(self.jFormPageArray[jFormPageId].jFormSectionArray[jFormSectionId].jFormComponentArray[jFormComponentId].value))):
#                        # set component  instance index
#                        if (fileIdInfo[3] == None):
#                            jFormComponentInstanceIndex = 0
#                        } else:
#                            jFormComponentInstanceIndex = fileIdInfo[4] - 1
#                        }
#                        self.jFormPageArray[jFormPageId].jFormSectionArray[jFormSectionId].jFormComponentArray[jFormComponentId].value[jFormComponentInstanceIndex] = fileDataArray
#                    } else:
#                        # no instances
#                        self.jFormPageArray[jFormPageId].jFormSectionArray[jFormSectionId].jFormComponentArray[jFormComponentId].value = fileDataArray
#                    }
#                }
#            }
#        }
#
#        return this
#    }
#
#    def clearData():
#        foreach (self.jFormPageArray as jFormPage):
#            jFormPage.clearData()
#        }
#        self.data = None
#    }
#
#    def clearAllComponentValues():
#        # Clear all of the components in the form
#        foreach (self.jFormPageArray as jFormPage):
#            foreach (jFormPage.jFormSectionArray as jFormSection):
#                foreach (jFormSection.jFormComponentArray as jFormComponent):
#                    jFormComponent.value = None
#                }
#            }
#        }
#    }
#
#    def select(id):
#        foreach (self.jFormPageArray as jformPageId:&jformPage):
#            if (id === jformPageId):
#                return jformPage
#            }
#            foreach (jformPage.jformSectionArray as jformSectionId:&jformSection):
#                if (id === jformSectionId):
#                    return jformSection
#                }
#                foreach (jformSection.jformComponentArray as jformComponentId:&jformComponent):
#                    if (is_array(jformComponent)):
#                        foreach (jformComponent as sectionInstanceComponentId:&sectionInstanceComponent):
#                            if (id === sectionInstanceComponentId):
#                                return sectionInstanceComponent
#                            }
#                        }
#                    }
#                    if (id === jformComponentId):
#                        return jformComponent
#                    }
#                }
#            }
#        }
#        return False
#    }
#
#    def remove(id):
#        foreach (self.formPageArray as formPageId:&formPage):
#            if (id == formPageId):
#                self.formPageArray[formPageId] = None
#                array_filter(self.formPageArray)
#                return True
#            }
#            foreach (formPage.formSectionArray as formSectionId:&formSection):
#                if (id == formSectionId):
#                    self.formPageArray[formPageId].formSectionArray[formSectionId] = None
#                    array_filter(self.formPageArray[formPageId].formSectionArray)
#                    return True
#                }
#                foreach (formSection.formComponentArray as formComponentId:&formComponent):
#                    if (id == formComponentId):
#                        self.formPageArray[formPageId].formSectionArray[formSectionId].formComponentArray[formComponentId] = None
#                        array_filter(self.formPageArray[formPageId].formSectionArray[formSectionId].formComponentArray)
#                        return True
#                    }
#                }
#            }
#        }
#        return False
#    }
#
#    def processRequest(silent = False):
#        # Are they trying to post a file that is too large?
#        if (isset(_SERVER['CONTENT_LENGTH']) && empty(_POST)):
#            self.setStatus('success', array('failureNoticeHtml':'Your request (' . round(_SERVER['CONTENT_LENGTH'] / 1024 / 1024, 1) . 'M) was too large for the server to handle. ' . ini_get('post_max_size') . ' is the maximum request size.'))
#            echo '
#                <script type="text/javascript" language="javascript">
#                    parent.' . self.id . 'Object.handleFormSubmissionResponse(' . json_encode(self.getStatus()) . ')
#                </script>
#            '
#            exit()
#        }
#
#        # Are they trying to post something to the form?
#        if (isset(_POST['jFormer']) && self.id == _POST['jFormerId'] || isset(_POST['jFormerTask'])):
#            # Process the form, get the form state, or display the form
#            if (isset(_POST['jFormer'])):
#                #echo json_encode(_POST)
#                onSubmitErrorMessageArray = {}
#
#                # Set the form components and validate the form
#                self.setData(_POST['jFormer'], _FILES)
#
#                #print_r(self.getData())
#                # Run validation
#                self.validate()
#                if (!self.validationPassed):
#                    self.setStatus('failure', array('validationFailed':self.validationResponse))
#                } else:
#                    try:
#                        onSubmitResponse = call_user_func(self.onSubmitFunctionServerSide, self.getData())
#                    } catch (Exception exception):
#                        onSubmitErrorMessageArray[] = exception.getTraceAsString()
#                    }
#
#                    # Make sure you actually get a callback response
#                    if (empty(onSubmitResponse)):
#                        onSubmitErrorMessageArray[] = '<p>The def <b>' . self.onSubmitFunctionServerSide . '</b> did not return a valid response.</p>'
#                    }
#
#                    # If there are no errors, it is a successful response
#                    if (empty(onSubmitErrorMessageArray)):
#                        self.setStatus('success', onSubmitResponse)
#                    } else:
#                        self.setStatus('failure', array('failureHtml':onSubmitErrorMessageArray))
#                    }
#                }
#
#                echo '
#                    <script type="text/javascript" language="javascript">
#                        parent.' . self.id . 'Object.handleFormSubmissionResponse(' . json_encode(self.getStatus()) . ')
#                    </script>
#                '
#
#                #echo json_encode(self.getValues())
#
#                exit()
#            }
#            # Get the form's status
#            else if (isset(_POST['jFormerTask']) && _POST['jFormerTask'] == 'getFormStatus'):
#                onSubmitResponse = self.getStatus()
#                echo json_encode(onSubmitResponse)
#                self.resetStatus()
#                exit()
#            }
#        }
#        # If they aren't trying to post something to the form
#        else if (!silent):
#            self.outputHtml()
#        }
#    }
#
#    def getOptions():
#        options = {}
#        options['options'] = {}
#        options['jFormPages'] = {}
#
#        # Get all of the pages
#        foreach (self.jFormPageArray as jFormPage):
#            options['jFormPages'][jFormPage.id] = jFormPage.getOptions()
#        }
#
#        # Set form options
#        if (!self.clientSideValidation):
#            options['options']['clientSideValidation'] = self.clientSideValidation
#        }
#        if (self.debugMode):
#            options['options']['debugMode'] = self.debugMode
#        }
#        if (!self.validationTips):
#            options['options']['validationTips'] = self.validationTips
#        }
#        if (!self.setupPageScroller):
#            options['options']['setupPageScroller'] = self.setupPageScroller
#        }
#        if (self.animationOptions !== None):
#            options['options']['animationOptions'] = self.animationOptions
#        }
#        if (self.pageNavigatorEnabled):
#            options['options']['pageNavigator'] = self.pageNavigator
#        }
#        if (self.splashPageEnabled):
#            options['options']['splashPage'] = self.splashPage
#            unset(options['options']['splashPage']['content'])
#        }
#        if (!empty(self.onSubmitStartClientSide)):
#            options['options']['onSubmitStart'] = self.onSubmitStartClientSide
#        }
#        if (!empty(self.onSubmitFinishClientSide)):
#            options['options']['onSubmitFinish'] = self.onSubmitFinishClientSide
#        }
#        if (!self.alertsEnabled):
#            options['options']['alertsEnabled'] = False
#        }
#        if (self.submitButtonText != 'Submit'):
#            options['options']['submitButtonText'] = self.submitButtonText
#        }
#        if (self.submitProcessingButtonText != 'Processing...'):
#            options['options']['submitProcessingButtonText'] = self.submitProcessingButtonText
#        }
#
#        if (empty(options['options'])):
#            unset(options['options'])
#        }
#
#        return options
#    }
#
#    def outputHtml():
#        echo self.getHtml()
#    }
#
#    def __toString():
#        element = self.getHtml()
#        return element.__toString()
#    }
#
#    def getHtml():
#        self.updateRequiredText(self.requiredText)
#        # Create the form
#        jFormElement = new JFormElement('form', array(
#                    'id':self.id,
#                    'target':self.id . '-iframe',
#                    'enctype':'multipart/form-data',
#                    'method':'post',
#                    'class':self.class,
#                    'action':self.action,
#                ))
#
#        if (!empty(self.onMouseOver)):
#            formJFormElement.attr('onmouseover', self.onMouseOver)
#        }
#
#        if (!empty(self.onMouseOut)):
#            formJFormElement.attr('onmouseout', self.onMouseOut)
#        }
#
#        # Set the style
#        if (!empty(self.style)):
#            jFormElement.addToAttribute('style', self.style)
#        }
#
#        # Global messages
#        if (self.alertsEnabled):
#            jFormerAlertWrapperDiv = new JFormElement('div', array(
#                        'class':'jFormerAlertWrapper',
#                        'style':'display: none',
#                    ))
#            alertDiv = new JFormElement('div', array(
#                        'class':'jFormerAlert',
#                    ))
#            jFormerAlertWrapperDiv.insert(alertDiv)
#            jFormElement.insert(jFormerAlertWrapperDiv)
#        }
#
#        # If a splash is enabled
#        if (self.splashPageEnabled):
#            # Create a splash page div
#            splashPageDiv = new JFormElement('div', array(
#                        'id':self.id . '-splash-page',
#                        'class':'jFormerSplashPage jFormPage',
#                    ))
#
#            # Set defaults if they aren't set
#            if (!isset(self.splashPage['content'])):
#                self.splashPage['content'] = ''
#            }
#            if (!isset(self.splashPage['splashButtonText'])):
#                self.splashPage['splashButtonText'] = 'Begin'
#            }
#
#            splashPageDiv.insert('<div class="jFormerSplashPageContent">' . self.splashPage['content'] . '</div>')
#
#            # Create a splash button if there is no custom button ID
#            if (!isset(self.splashPage['customButtonId'])):
#                splashLi = new JFormElement('li', array('class':'splashLi'))
#                splashButton = new JFormElement('button', array('class':'splashButton'))
#                splashButton.update(self.splashPage['splashButtonText'])
#                splashLi.insert(splashButton)
#            }
#        }
#
#        # Add a title to the form
#        if (!empty(self.title)):
#            title = new JFormElement('div', array(
#                        'class':self.titleClass
#                    ))
#            title.update(self.title)
#            jFormElement.insert(title)
#        }
#
#        # Add a description to the form
#        if (!empty(self.description)):
#            description = new JFormElement('div', array(
#                        'class':self.descriptionClass
#                    ))
#            description.update(self.description)
#            jFormElement.insert(description)
#        }
#
#        # Add the page navigator if enabled
#        if (self.pageNavigatorEnabled):
#            pageNavigatorDiv = new JFormElement('div', array(
#                        'class':'jFormPageNavigator',
#                    ))
#            if (isset(self.pageNavigator['position']) && self.pageNavigator['position'] == 'right'):
#                pageNavigatorDiv.addToAttribute('class', ' jFormPageNavigatorRight')
#            } else:
#                pageNavigatorDiv.addToAttribute('class', ' jFormPageNavigatorTop')
#            }
#
#            pageNavigatorUl = new JFormElement('ul', array(
#                    ))
#
#            jFormPageArrayCount = 0
#            foreach (self.jFormPageArray as jFormPageKey:jFormPage):
#                jFormPageArrayCount++
#
#                pageNavigatorLabel = new JFormElement('li', array(
#                            'id':'navigatePage' . jFormPageArrayCount,
#                            'class':'jFormPageNavigatorLink',
#                        ))
#
#                # If the label is numeric
#                if (isset(self.pageNavigator['label']) && self.pageNavigator['label'] == 'numeric'):
#                    pageNavigatorLabelText = 'Page ' . jFormPageArrayCount
#                } else:
#                    # Add a link prefix if there is a title
#                    if (!empty(jFormPage.title)):
#                        pageNavigatorLabelText = '<span class="jFormNavigatorLinkPrefix">' . jFormPageArrayCount . '</span> ' . strip_tags(jFormPage.title)
#                    } else:
#                        pageNavigatorLabelText = 'Page ' . jFormPageArrayCount
#                    }
#                }
#                pageNavigatorLabel.update(pageNavigatorLabelText)
#
#                if (jFormPageArrayCount != 1):
#                    pageNavigatorLabel.addToAttribute('class', ' jFormPageNavigatorLinkLocked')
#                } else:
#                    pageNavigatorLabel.addToAttribute('class', ' jFormPageNavigatorLinkUnlocked jFormPageNavigatorLinkActive')
#                }
#
#                pageNavigatorUl.insert(pageNavigatorLabel)
#            }
#
#            # Add the page navigator ul to the div
#            pageNavigatorDiv.insert(pageNavigatorUl)
#
#            jFormElement.insert(pageNavigatorDiv)
#        }
#
#        # Add the jFormerControl UL
#        jFormerControlUl = new JFormElement('ul', array(
#                    'class':'jFormerControl',
#                ))
#
#        # Create the cancel button
#        if (self.cancelButton):
#            cancelButtonLi = new JFormElement('li', array('class':'cancelLi'))
#            cancelButton = new JFormElement('button', array('class':self.cancelButtonClass))
#            cancelButton.update(self.cancelButtonText)
#
#            if (!empty(self.cancelButtonOnClick)):
#                cancelButton.attr('onclick', self.cancelButtonOnClick)
#            }
#
#            cancelButtonLi.append(cancelButton)
#        }
#
#        # Create the previous button
#        previousButtonLi = new JFormElement('li', array('class':'previousLi', 'style':'display: none'))
#        previousButton = new JFormElement('button', array('class':'previousButton'))
#        previousButton.update('Previous')
#        previousButtonLi.insert(previousButton)
#
#        # Create the next button
#        nextButtonLi = new JFormElement('li', array('class':'nextLi'))
#        nextButton = new JFormElement('button', array('class':'nextButton'))
#        nextButton.update(self.submitButtonText)
#        # Don't show the next button
#        if (self.splashPageEnabled):
#            nextButtonLi.setAttribute('style', 'display: none')
#        }
#        nextButtonLi.insert(nextButton)
#
#        # Add a splash page button if it exists
#        if (isset(splashLi)):
#            jFormerControlUl.insert(splashLi)
#        }
#
#        # Add the previous and next buttons
#        jFormerControlUl.insert(previousButtonLi)
#
#        if (self.cancelButton && self.cancelButtonLiBeforeNextButtonLi):
#            echo 'one'
#            jFormerControlUl.insert(cancelButtonLi)
#            jFormerControlUl.insert(nextButtonLi)
#        } else if (self.cancelButton):
#            echo 'two'
#            jFormerControlUl.insert(nextButtonLi)
#            jFormerControlUl.insert(cancelButtonLi)
#        } else:
#            jFormerControlUl.insert(nextButtonLi)
#        }
#
#        # Create the page wrapper and scrollers
#        jFormPageWrapper = new JFormElement('div', array('class':'jFormPageWrapper'))
#        jFormPageScroller = new JFormElement('div', array('class':'jFormPageScroller'))
#
#        # Add a splash page if it exists
#        if (isset(splashPageDiv)):
#            jFormPageScroller.insert(splashPageDiv)
#        }
#
#        # Add the form pages to the form
#        jFormPageCount = 0
#        foreach (self.jFormPageArray as jFormPage):
#            # Hide everything but the first page
#            if (jFormPageCount != 0 || (jFormPageCount == 0 && (self.splashPageEnabled))):
#                jFormPage.style .= 'display: none'
#            }
#
#            jFormPageScroller.insert(jFormPage)
#            jFormPageCount++
#        }
#
#        # Page wrapper wrapper
#        pageWrapperContainer = new JFormElement('div', array('class':'jFormWrapperContainer'))
#
#        # Insert the page wrapper and the jFormerControl UL to the form
#        jFormElement.insert(pageWrapperContainer.insert(jFormPageWrapper.insert(jFormPageScroller) . jFormerControlUl))
#
#        # Create a script tag to initialize jFormer JavaScript
#        script = new JFormElement('script', array(
#                    'type':'text/javascript',
#                    'language':'javascript'
#                ))
#
#        # Update the script tag
#        script.update('(document).ready(def (): ' . self.id . 'Object = new JFormer(\'' . self.id . '\', ' . json_encode(self.getOptions()) . ') })')
#        jFormElement.insert(script)
#
#        # Add a hidden iframe to handle the form posts
#        iframe = new JFormElement('iframe', array(
#                    'id':self.id . '-iframe',
#                    'name':self.id . '-iframe',
#                    'class':'jFormerIFrame',
#                    'frameborder':0,
#                    'src':'/empty.html',
#                        #'src':str_replace(_SERVER['DOCUMENT_ROOT'], '', __FILE__).'?iframe=True',
#                ))
#
#        if (self.debugMode):
#            iframe.addToAttribute('style', 'display:block')
#        }
#
#        jFormElement.insert(iframe)
#
#
#        # After control
#        if (!empty(self.afterControl)):
#            subSubmitInstructions = new JFormElement('div', array('class':'jFormerAfterControl'))
#            subSubmitInstructions.update(self.afterControl)
#            jFormElement.insert(subSubmitInstructions)
#        }
#
#        return jFormElement
#    }
#
#}
#
## Handle any requests that come to this file
#if (isset(_GET['iframe'])):
#    echo ''
#}
#?>
