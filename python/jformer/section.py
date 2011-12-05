
#~  * A FormSection object contains FormComponent objects and belongs to a FormPage object
#~  */
#class JFormSection:

#~     # General settings
#~     self.id
#~     self.class = 'jFormSection'
#~     self.style = ''
#~     self.parentJFormPage
#~     self.jFormComponentArray = {}
#~     self.data
#~     self.anonymous = false

#~     # Title, description, submit instructions
#~     self.title = ''
#~     self.titleClass = 'jFormSectionTitle'
#~     self.description = ''
#~     self.descriptionClass = 'jFormSectionDescription'

#~     # Options
#~     self.instanceOptions = null
#~     self.dependencyOptions = null

#~     # Validation
#~     self.errorMessageArray = {}

#~     /*
#~      * Constructor
#~      */
#~     def __construct(id, optionArray = {}, jFormComponentArray = {}):
#~         # Set the id
#~         self.id = id
#~      
#~         # Use the options hash to update object variables
#~         if(is_array(optionArray)):
#~             foreach(optionArray as option:value):
#~                 self.{option = value
#~             
#~         

#~         # Add the components from the constructor
#~         self.addJFormComponentArray(jFormComponentArray)

#~         return this
#~     

#~     def addJFormComponent(jFormComponent):
#~         jFormComponent->parentJFormSection = this
#~         self.jFormComponentArray[jFormComponent->id] = jFormComponent

#~         return this
#~     

#~     def addJFormComponents(jFormComponents):
#~         if (is_array(jFormComponents)):
#~             foreach (jFormComponentArray as jFormComponent):
#~                 jFormComponent->parentJFormSection = this
#~                 self.addJFormComponent(jFormComponent)
#~             
#~          else:
#~             jFormComponent->parentJFormSection = this
#~             self.jFormComponentArray[jFormComponent->id] = jFormComponent
#~         
#~         return this
#~     

#~     def addJFormComponentArray(jFormComponentArray):
#~         foreach(jFormComponentArray as jFormComponent):
#~             self.addJFormComponent(jFormComponent)
#~         
#~         return this
#~     

#~     def getData():
#~         self.data = {}

#~         # Check to see if jFormComponent array contains instances
#~         if(array_key_exists(0, self.jFormComponentArray) && is_array(self.jFormComponentArray[0])):
#~             foreach(self.jFormComponentArray as jFormComponentArrayInstanceIndex:jFormComponentArrayInstance):
#~                 foreach(jFormComponentArrayInstance as jFormComponentKey:jFormComponent):
#~                     if(get_class(jFormComponent) != 'JFormComponentHtml'): # Don't include HTML components
#~                         self.data[jFormComponentArrayInstanceIndex][jFormComponentKey] = jFormComponent->getValue()
#~                     
#~                 
#~             
#~         
#~         # If the section does not have instances
#~         else:
#~             foreach(self.jFormComponentArray as jFormComponentKey:jFormComponent):
#~                 if(get_class(jFormComponent) != 'JFormComponentHtml'): # Don't include HTML components
#~                     self.data[jFormComponentKey] = jFormComponent->getValue()
#~                 
#~             
#~         

#~         return self.data
#~     

#~     def setData(jFormSectionData):
#~         # Handle multiple instances
#~         if(is_array(jFormSectionData)):
#~             newJFormComponentArray = {}
#~             
#~             # Go through each section instance
#~             foreach(jFormSectionData as jFormSectionIndex:jFormSection):
#~                 # Create a clone of the jFormComponentArray
#~                 newJFormComponentArray[jFormSectionIndex] = unserialize(serialize(self.jFormComponentArray))

#~                 # Go through each component in the instanced section
#~                 foreach(jFormSection as jFormComponentKey:jFormComponentValue):
#~                     # Set the value of the clone
#~                     newJFormComponentArray[jFormSectionIndex][jFormComponentKey]->setValue(jFormComponentValue)
#~                 
#~             
#~             self.jFormComponentArray = newJFormComponentArray
#~         
#~         # Single instance
#~         else:
#~             # Go through each component
#~             foreach(jFormSectionData as jFormComponentKey:jFormComponentValue):
#~                 self.jFormComponentArray[jFormComponentKey]->setValue(jFormComponentValue)
#~             
#~         
#~     

#~     def clearData():
#~         # Check to see if jFormComponent array contains instances
#~         if(array_key_exists(0, self.jFormComponentArray) && is_array(self.jFormComponentArray[0])):
#~             foreach(self.jFormComponentArray as jFormComponentArrayInstanceIndex:jFormComponentArrayInstance):
#~                 foreach(jFormComponentArrayInstance as jFormComponentKey:jFormComponent):
#~                     jFormComponent->clearValue()
#~                 
#~             
#~         
#~         # If the section does not have instances
#~         else:
#~             foreach(self.jFormComponentArray as jFormComponent):
#~                 jFormComponent->clearValue()
#~             
#~         
#~         self.data = null
#~     

#~     def validate():
#~         # Clear the error message array
#~         self.errorMessageArray = {}

#~         # If we have instances, return an array
#~         if(array_key_exists(0, self.jFormComponentArray) && is_array(self.jFormComponentArray[0])):
#~             foreach(self.jFormComponentArray as jFormComponentArrayInstanceIndex:jFormComponentArrayInstance):
#~                 foreach(jFormComponentArrayInstance as jFormComponentKey:jFormComponent):
#~                     self.errorMessageArray[jFormComponentArrayInstanceIndex][jFormComponent->id] = jFormComponent->validate()
#~                 
#~             
#~         
#~         # If the section does not have instances, return an single dimension array
#~         else:
#~             foreach(self.jFormComponentArray as jFormComponent):
#~                 self.errorMessageArray[jFormComponent->id] = jFormComponent->validate()
#~             
#~         

#~         return self.errorMessageArray
#~     

#~     def updateRequiredText(requiredText):
#~         foreach(self.jFormComponentArray as jFormComponent):
#~             jFormComponent->updateRequiredText(requiredText)
#~         
#~     

#~     def getOptions():
#~         options = {}
#~         options['options'] = {}
#~         options['jFormComponents'] = {}
#~         
#~         # Instances
#~         if(!empty(self.instanceOptions)):
#~             options['options']['instanceOptions'] = self.instanceOptions
#~             if(!isset(options['options']['instanceOptions']['addButtonText'])):
#~                 options['options']['instanceOptions']['addButtonText'] = 'Add Another'
#~             
#~             if(!isset(options['options']['instanceOptions']['removeButtonText'])):
#~                 options['options']['instanceOptions']['removeButtonText'] = 'Remove'
#~             
#~         

#~         # Dependencies
#~         if(!empty(self.dependencyOptions)):
#~             # Make sure the dependentOn key is tied to an array
#~             if(isset(self.dependencyOptions['dependentOn']) && !is_array(self.dependencyOptions['dependentOn'])):
#~                 self.dependencyOptions['dependentOn'] = array(self.dependencyOptions['dependentOn'])
#~             
#~             options['options']['dependencyOptions'] = self.dependencyOptions
#~         

#~         # Get options for each of the jFormComponents
#~         foreach(self.jFormComponentArray as jFormComponent):
#~             # Don't get options for JFormComponentHtml objects
#~             if(get_class(jFormComponent) != 'JFormComponentHtml'):
#~                 options['jFormComponents'][jFormComponent->id] = jFormComponent->getOptions()
#~             
#~         

#~         if(empty(options['options'])):
#~             unset(options['options'])
#~         

#~         return options
#~     

#~     /**
#~      *
#~      * @return string
#~      */
#~     def __toString():
#~         # Section fieldset
#~         jFormSectionDiv = new JFormElement('div', array(
#~             'id':self.id,
#~             'class':self.class
#~         ))

#~         # This causes issues with things that are dependent and should display by default
#~         # If the section has dependencies and the display type is hidden, hide by default
#~         #if(self.dependencyOptions !== null && isset(self.dependencyOptions['display']) && self.dependencyOptions['display'] == 'hide'):
#~         #    jFormSectionDiv->setAttribute('style', 'display: none')
#~         #

#~         # Set the style
#~         if(!empty(self.style)):
#~             jFormSectionDiv->addToAttribute('style', self.style)
#~         

#~         # Add a title to the page
#~         if(!empty(self.title)):
#~             title = new JFormElement('div', array(
#~                 'class':self.titleClass
#~             ))
#~             title->update(self.title)
#~             jFormSectionDiv->insert(title)
#~         

#~         # Add a description to the page
#~         if(!empty(self.description)):
#~             description = new JFormElement('div', array(
#~                 'class':self.descriptionClass
#~             ))
#~             description->update(self.description)
#~             jFormSectionDiv->insert(description)
#~         

#~         # Add the form sections to the page
#~         foreach(self.jFormComponentArray as jFormComponentArray):
#~             jFormSectionDiv->insert(jFormComponentArray)
#~         
#~         
#~         return jFormSectionDiv->__toString()
#~     

?>
