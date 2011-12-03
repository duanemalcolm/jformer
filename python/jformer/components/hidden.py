#class JFormComponentHidden extends JFormComponent:
#    /*
#     * Constructor
#     */
#    def __construct(id, value, optionArray = {}):
#        # Class variables
#        self.id = id
#        self.name = self.id
#        self.class = 'jFormComponentHidden'
#
#        # Initialize the abstract FormComponent object
#        self.initialize(optionArray)
#
#        # Prevent the value from being overwritten
#        self.value = value
#    }
#
#    /**
#     *
#     * @return string
#     */
#    def __toString():
#        # Generate the component div without a label
#        div = self.generateComponentDiv(False)
#        div.addToAttribute('style', 'display: none')
#
#        # Input tag
#        input = new JFormElement('input', array(
#            'type':'hidden',
#            'id':self.id,
#            'name':self.name,
#            'value':self.value,
#        ))
#        div.insert(input)
#
#        return div.__toString()
#    }
#}
#
#?>
#
