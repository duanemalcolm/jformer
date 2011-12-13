from element import Element

class _Component():
    '''
    An abstract Form Component object, should not be instantiated
    '''
    
    def __init__(self):
        '''
        Base class for form components.
        '''
        # General settings
        self._class = None
        self.value = None
        self.style = None
        self.parentJFormSection = None
        self.anonymous = False
    
        # Label
        self.label = None  # Must be implemented by child class
        self.labelClass = 'jFormComponentLabel'
        self.labelRequiredStarClass = 'jFormComponentLabelRequiredStar'
        self.requiredText = ' *' # can be overridden at the form level
    
        # Helpers
        self.tip = None
        self.tipClass = 'jFormComponentTip'
        self.description = None
        self.descriptionClass = 'jFormComponentDescription'
    
        # Options
        self.options = {}
        self.instanceOptions = None
        self.triggerFunction = None
        self.enterSubmits = False
        
        # Dependencies
        self.dependencyOptions = None
    
        # Validation
        self.validationOptions = {}
        self.errorMessageArray = None
        self.passedValidation = None
        self.showErrorTipOnce = False
        self.persistentTip = False


    def initialize(self, optionArray = {}):
        # Use the options hash to update object variables
        for option, value in optionArray.iteritems():
                self.options[option] = value
        
        # Allow users to pass a string into validation options
        if isinstance(self.validationOptions, str):
            self.validationOptions = [self.validationOptions]
        
    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def clearValue(self):
        self.value = None

#~     def validate():
#~         # Clear the error message array
#~         self.errorMessageArray = {
#
#~         # Only validate if the value isn't None - this is so dependencies aren't validated before they are unlocked
#~         if(self.value !== None):
#~             # Perform the validation
#~             self.reformValidations()
#
#~             # If you have instance values
#~             if(self.hasInstanceValues()):
#~                 # Walk through each of the instance values
#~                 foreach(self.value as instanceKey:instanceValue):
#~                     foreach(self.validationOptions as validationType:validationOptions):
#~                         validationOptions['value'] = instanceValue
#
#~                         # Get the validation response
#~                         validationResponse = self.validationType(validationOptions)
#
#~                         # Make sure you have an array to work with
#~                         if(!isset(self.errorMessageArray[instanceKey])):
#~                             self.errorMessageArray[instanceKey] = {
#~                         
#
#~                         if(validationResponse != 'success'):
#~                             self.passedValidation = False
#
#~                             if(is_array(validationResponse)):
#~                                 self.errorMessageArray[instanceKey] = array_merge(self.errorMessageArray[instanceKey], validationResponse)
#~                             
#~                             else:
#~                                 if(is_string(validationResponse)):
#~                                     self.errorMessageArray[instanceKey] = array_merge(self.errorMessageArray[instanceKey], array(validationResponse))
#~                                 
#~                                 else:
#~                                     self.errorMessageArray[instanceKey] = array_merge(self.errorMessageArray[instanceKey], array('There was a problem validating this component on the server.'))
#~                                 
#~                             
#~                         
#~                         # Use an empty array as a placeholder for instances that have passed validation
#~                         else:
#~                             if(sizeof(self.errorMessageArray[instanceKey]) == 0):
#~                                 self.errorMessageArray[instanceKey] = array('')
#~                             
#~                         
#~                     
#~                 
#~             
#~             # If there are no instance values
#~             else:
#~                 foreach(self.validationOptions as validationType:validationOptions):
#~                     validationOptions['value'] = self.value
#
#~                     # Get the validation response
#~                     validationResponse = self.validationType(validationOptions)
#~                     if(validationResponse != 'success'):
#~                         self.passedValidation = False
#~                         
#~                         if(is_array(validationResponse)):
#~                             self.errorMessageArray = array_merge(validationResponse, self.errorMessageArray)
#~                         
#~                         else:
#~                             if(is_string(validationResponse)):
#~                                 self.errorMessageArray = array_merge(array(validationResponse), self.errorMessageArray)
#~                             
#~                             else:
#~                                 self.errorMessageArray = array_merge(array('There was a problem validating this component on the server.'), self.errorMessageArray)
#~                             
#~                         
#~                     
#~                 
#~             
#
#~             return self.errorMessageArray
#~         
#~     
#
#~     def reformValidations(){
#~         reformedValidations = {
#~         foreach(self.validationOptions as validationType:validationOptions):
#~             # Check to see if the name of the def is actually an array index
#~             if(is_int(validationType)):
#~                 # The def is not an index, it becomes the name of the option with the value of an empty object
#~                 reformedValidations[validationOptions] =  {
#~             
#~             # If the validationOptions is a string
#~             else if(!is_array(validationOptions)):
#~                 reformedValidations[validationType] = {
#~                 reformedValidations[validationType][validationType] = validationOptions
#~             
#~             # If validationOptions is an object
#~             else if(is_array(validationOptions)):
#~                 if(isset(validationOptions[0])){
#~                     reformedValidations[validationType] = {
#~                     reformedValidations[validationType][validationType] = validationOptions
#~                  else:
#~                     reformedValidations[validationType] = validationOptions
#~         
#~         self.validationOptions = reformedValidations
#~     

    def getOptions(self):
        options = {}
        options['options'] = {}
        
        ### DM: not sure
        #~ options['type'] = get_class(this)
        options['type'] = self._class
        
        # Validation options
        if self.validationOptions:
            options['options']['validationOptions'] = self.validationOptions
        
        if self.showErrorTipOnce:
            options['options']['showErrorTipOnce'] = self.showErrorTipOnce
        
        if self.persistentTip:
            options['options']['persistentTip'] = self.persistentTip
        
        # Instances
        if self.instanceOptions:
            options['options']['instanceOptions'] = self.instanceOptions
            if not options['options']['instanceOptions'].has_key('addButtonText'):
                options['options']['instanceOptions']['addButtonText'] = 'Add Another'
            
            if not options['options']['instanceOptions'].has_key('removeButtonText'):
                options['options']['instanceOptions']['removeButtonText'] = 'Remove'
        
        # Trigger
        if self.triggerFunction:
            options['options']['triggerFunction'] = self.triggerFunction
        
        
        # Dependencies
        if self.dependencyOptions:
            # Make sure the dependentOn key is tied to an array
            if self.dependencyOptions.has_key('dependentOn') and not isinstance(self.dependencyOptions['dependentOn'], list):
                self.dependencyOptions['dependentOn'] = [self.dependencyOptions['dependentOn']]
            
            options['options']['dependencyOptions'] = self.dependencyOptions
        
        # Clear the options key if there is nothing in it
        if not options['options']:
            options.pop('options')
        
        return options
    
    def hasInstanceValues(self):
        return isinstance(self.value, list)
    

#     /**
#      * Generates the HTML for the FormComponent
#      * @return string
#      */
#     abstract def __toString()
    
    def generateComponentDiv(self, includeLabel=True):
        # Div tag contains everything about the component
        componentDiv = Element('div', {
            'id': self.id+'-wrapper',
            'class': 'jFormComponent '+self._class})

        # This causes issues with things that are dependent and should display by default
        # If the component has dependencies and the display type is hidden, hide by default
        # if(self.dependencyOptions !== None && isset(self.dependencyOptions['display']) && self.dependencyOptions['display'] == 'hide'):
        #    componentDiv.setAttribute('style', 'display: none')
        #

        # Style
        if self.style:
            componentDiv.addToAttribute('style', self.style)

        # Label tag
        if includeLabel:
            label = self.generateComponentLabel()
            componentDiv.insert(label)

        return componentDiv

    def updateRequiredText(self, requiredText):
        self.requiredText = requiredText
    
    def generateComponentLabel(self):
        if self.label == None:
            return ''

        label = Element('label', {
            'id':self.id+'-label',
            'for':self.id,
            'class':self.labelClass
            })
            
        label.update(self.label)
        
        # Add the required star to the label
        if 'required' in self.validationOptions:
            labelRequiredStarSpan = Element('span',
                {'class':self.labelRequiredStarClass})
            labelRequiredStarSpan.update(self.requiredText)
            label.insert(labelRequiredStarSpan)

        return label

#~     def insertComponentDescription(div):
#~         # Description
#~         if(!empty(self.description)):
#~             description = new JFormElement('div', array(
#~                 'id':self.id.'-description',
#~                 'class':self.descriptionClass
#~             ))
#~             description.update(self.description)
#
#~             div.insert(description)
#~         
#
#~         return div
#~     
#
#~     def insertComponentTip(div):
#~         # Create the tip div if not empty
#~         if(!empty(self.tip)):
#~             tipDiv = new JFormElement('div', array(
#~                 'id':self.id.'-tip',
#~                 'style':'display: none',
#~                 'class':self.tipClass,
#~             ))
#~             tipDiv.update(self.tip)
#~             div.insert(tipDiv)
#~         
#
#~         return div
#~     
#
#~     # Generic validations
#
#~     def required(options): # Just override this if necessary
#~         messageArray = array('Required.')
#~         #return empty(options['value']) ? 'success' : messageArray # Break validation on purpose
#~         return !empty(options['value']) || options['value'] == '0' ? 'success' : messageArray

