#~  * A FormPage object contains FormSection objects and belongs to a Form object
#~  */
#class JFormPage:
#~     
#~     # General settings
#~     self.id
#~     self.class = 'jFormPage'
#~     self.style = ''
#~     self.jFormer
#~     self.jFormSectionArray = {}
#~     self.onBeforeScrollTo # array('function', 'notificationHtml')
#~     self.data
#~     self.anonymous = false

#~     # Title, description, submit instructions
#~     self.title = ''
#~     self.titleClass = 'jFormPageTitle'
#~     self.description = ''
#~     self.descriptionClass = 'jFormPageDescription'
#~     self.submitInstructions = ''
#~     self.submitInstructionsClass = 'jFormPageSubmitInstructions'

#~     # Validation
#~     self.errorMessageArray = {}

#~     # Options
#~     self.dependencyOptions = null

#~     /*
#~      * Constructor
#~      */
#~     def __construct(id, optionArray = {}, jFormSectionArray = {}):
#~         # Set the id
#~         self.id = id

#~         # Use the options hash to update object variables
#~         if(is_array(optionArray)):
#~             foreach(optionArray as option:value):
#~                 self.{option = value
#~             
#~         

#~         # Add the sections from the constructor
#~         foreach(jFormSectionArray as jFormSection):
#~             self.addJFormSection(jFormSection)
#~         

#~         return this
#~     

#~     def addJFormSection(jFormSection):
#~         jFormSection->parentJFormPage = this
#~         self.jFormSectionArray[jFormSection->id] = jFormSection
#~         return this
#~     

#~     def addJFormSections(jFormSections):
#~         if (is_array(jFormSections)):
#~             foreach (jFormSections as jFormSection):
#~                 jFormSection->parentJFormPage = this
#~                 self.jFormSectionArray[jFormSection->id] = jFormSection
#~             
#~         
#~         jFormSection->parentJFormPage = this
#~         self.jFormSectionArray[jFormSection->id] = jFormSection
#~         return this
#~     
#~     
#~     # Convenience method, no need to create a section to get components on the page
#~     def addJFormComponent(jFormComponent):
#~         # Create an anonymous section if necessary
#~         if(empty(self.jFormSectionArray)):
#~             self.addJFormSection(new JFormSection(self.id.'_section1', array('anonymous':true)))
#~         

#~         # Get the last section in the page
#~         lastJFormSection = end(self.jFormSectionArray)

#~         # If the last section exists and is anonymous, add the component to it
#~         if(!empty(lastJFormSection) && lastJFormSection->anonymous):
#~             lastJFormSection->addJFormComponent(jFormComponent)
#~         
#~         # If the last section in the page does not exist or is not anonymous, add a new anonymous section and add the component to it
#~         else:
#~             # Create an anonymous section
#~             anonymousSection = new JFormSection(self.id.'_section'.(sizeof(self.jFormSectionArray) + 1), array('anonymous':true))

#~             # Add the anonymous section to the page
#~             self.addJFormSection(anonymousSection->addJFormComponent(jFormComponent))
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
#~         foreach(self.jFormSectionArray as jFormSectionKey:jFormSection):
#~             self.data[jFormSectionKey] = jFormSection->getData()
#~         
#~         return self.data
#~     

#~     def setData(jFormPageData):
#~         foreach(jFormPageData as jFormSectionKey:jFormSectionData):
#~             self.jFormSectionArray[jFormSectionKey]->setData(jFormSectionData)
#~         
#~     

#~     def clearData():
#~         foreach(self.jFormSectionArray as jFormSection):
#~             jFormSection->clearData()
#~         
#~         self.data = null
#~     

#~     def validate():
#~         # Clear the error message array
#~         self.errorMessageArray = {}

#~         # Validate each section
#~         foreach(self.jFormSectionArray as jFormSection):
#~             self.errorMessageArray[jFormSection->id] = jFormSection->validate()
#~         

#~         return self.errorMessageArray
#~     

#~     def getOptions():
#~         options = {}
#~         options['options'] = {}
#~         options['jFormSections'] = {}

#~         foreach(self.jFormSectionArray as jFormSection):
#~             options['jFormSections'][jFormSection->id] = jFormSection->getOptions()
#~         

#~         if(!empty(self.onScrollTo)):
#~             options['options']['onScrollTo'] = self.onScrollTo
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

#~         if(empty(options['options'])):
#~             unset(options['options'])
#~         

#~         return options
#~     

#~     def updateRequiredText(requiredText):
#~         foreach(self.jFormSectionArray as jFormSection):
#~             jFormSection->updateRequiredText(requiredText)
#~         
#~     

#~     /**
#~      *
#~      * @return string
#~      */
#~     def __toString():
#~         # Page div
#~         jFormPageDiv = new JFormElement('div', array(
#~             'id':self.id,
#~             'class':self.class
#~         ))

#~         # Set the styile
#~         if(!empty(self.style)):
#~             jFormPageDiv->addToAttribute('style', self.style)
#~         

#~         # Add a title to the page
#~         if(!empty(self.title)):
#~             title = new JFormElement('div', array(
#~                 'class':self.titleClass
#~             ))
#~             title->update(self.title)
#~             jFormPageDiv->insert(title)
#~         

#~         # Add a description to the page
#~         if(!empty(self.description)):
#~             description = new JFormElement('div', array(
#~                 'class':self.descriptionClass
#~             ))
#~             description->update(self.description)
#~             jFormPageDiv->insert(description)
#~         

#~         # Add the form sections to the page
#~         foreach(self.jFormSectionArray as jFormSection):
#~             jFormPageDiv->insert(jFormSection)
#~         

#~         # Submit instructions
#~         if(!empty(self.submitInstructions)):
#~             submitInstruction = new JFormElement('div', array(
#~                 'class':self.submitInstructionsClass
#~             ))
#~             submitInstruction->update(self.submitInstructions)
#~             jFormPageDiv->insert(submitInstruction)
#~         

#~         return jFormPageDiv->__toString()
#~     

?>
