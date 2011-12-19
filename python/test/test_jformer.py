import unittest
import doctest

import jformer

#~ class Test(unittest.TestCase):
    #~ """Unit tests for jformer."""
#~ 
    #~ def test_doctests_jformer(self):
        #~ """Run jformer doctests"""
        #~ doctest.testmod(jformer)
        #~ 
    #~ def test_doctests_jformelement(self):
        #~ """Run jformer doctests"""
        #~ doctest.testmod(jformer.element)
        #~ 
    #~ def test_jformer(self):
        #~ form = jformer.Form('login')
        #~ form.title = 'House of'
        #~ self.assertEqual('login', form.id)
        #~ page = jformer.Page('mypage')
        #~ page.title = 'Duane'
        #~ form.addJFormPage(page)
    #~ 
    #~ def test_jformer_element(self):
        #~ elem = jformer.Element('div')
        #~ self.assertEqual('div', elem.tag)
        #~ 
        #~ 
    #~ def test_jformer_add_page(self):
        #~ form = jformer.JFormer('login')
        #~ form.addJFormPage([])

#~ class TestPage(unittest.TestCase):
    #~ """Unit tests for jformer Page."""
    #~ 
    #~ def test_doctests_jformpage(self):
        #~ """Run jformer doctests"""
        #~ doctest.testmod(jformer.page)
        #~ 
    #~ def test_get_options(self):
        #~ page = jformer.Page('house')
        #~ options = page.getOptions()
        #~ self.assertEqual({}, options)
        #~ 
        #~ 
    #~ def test_jformer_add_page(self):
        #~ form = jformer.JFormer('login')
        #~ form.addJFormPage([])

class TestSection(unittest.TestCase):
    """Unit tests for jformer Page."""
    
    def test_doctests_jformpage(self):
        """Run jformer doctests"""
        doctest.testmod(jformer.section)
        
    def test_init(self):
        section = jformer.Section('magic')
        self.assertEqual(section.id, 'magic')
        self.assertEqual(section._class, 'jFormSection')
        self.assertEqual(section.style, '')
        self.assertEqual(section.parentJFormPage, None)
        self.assertEqual(section.jFormComponentArray, {})
        self.assertEqual(section.data, None)
        self.assertEqual(section.anonymous, False)
        self.assertEqual(section.title, '')
        self.assertEqual(section.titleClass, 'jFormSectionTitle')
        self.assertEqual(section.description, '')
        self.assertEqual(section.descriptionClass, 'jFormSectionDescription')
        self.assertEqual(section.instanceOptions, None)
        self.assertEqual(section.dependencyOptions, None)
        self.assertEqual(section.errorMessageArray, {})
        
    #~ def test_jformer_add_page(self):
        #~ form = jformer.JFormer('login')
        #~ form.addJFormPage([])

class TestElement(unittest.TestCase):
    """Unit tests for jformer Page."""
    
    def test_doctests_jformpage(self):
        """Run jformer doctests"""
        doctest.testmod(jformer.element)
        
    def test_init(self):
        e = jformer.Element('password', {
                'type':'password',
                'validationOptions':{'required': 'password'},
                'tip': '<p>Password is 12345</p>'
                })
        
        #~ self.assertEqual({}, options)
    
    def test_init(self):
        e = jformer.Element('password', {'attr1':'val1'})
        self.assertEqual({'attr1': 'val1'}, e.attributeArray)
    
    def test_set_get_attributes(self):
        e = jformer.Element('password')
        e.setAttribute('attr1', 'val1')
        self.assertEqual({'attr1': 'val1'}, e.attributeArray)
        e.setAttribute('attr2', 2)
        self.assertEqual({'attr1':'val1', 'attr2':2}, e.attributeArray)
        e.setAttribute({'attr3':3, 'attr4':'val4'})
        self.assertEqual({'attr1':'val1', 'attr2':2, 'attr3':3,
                         'attr4':'val4'}, e.attributeArray)
        e.setAttribute({'attr3':'val3', 'attr4':'val4'})
        self.assertEqual({'attr1':'val1', 'attr2':2, 'attr3':'val3',
                         'attr4':'val4'}, e.attributeArray)
        e.setAttribute('attr2', 'val2')
        self.assertEqual({'attr1':'val1', 'attr2':'val2',
                         'attr3':'val3', 'attr4':'val4'},
                         e.attributeArray)
        e.setAttribute({'attr2': {'attr2a':'a'}})
        self.assertEqual({'attr1':'val1', 'attr2':{'attr2a':'a'},
                         'attr3':'val3', 'attr4':'val4'},
                         e.attributeArray)
        
        # Test getAttribute
        self.assertEqual(None, e.getAttribute('doesnt_exist'))
        self.assertEqual('val3', e.getAttribute('attr3'))
        self.assertEqual({'attr2a':'a'}, e.getAttribute('attr2'))
        self.assertEqual(None, e.getAttribute('still_doesnt_exist'))
        
    def test_add_attributes(self):
        e = jformer.Element('password', {'attr1': 'val1'})
        e.addToAttribute('attr1', 'val1a')
        self.assertEqual('val1 val1a', e.attributeArray['attr1'])
        
    def test_add_class_name(self):
        e = jformer.Element('password')
        e.addClassName('passwd')
        self.assertEqual('passwd', e.attributeArray['class'])
        e.addClassName('left')
        self.assertEqual('passwd left', e.attributeArray['class'])
    
    def test_add_class_name(self):
        e = jformer.Element('password')
        e.addClassName('passwd')
        self.assertEqual('passwd', e.attributeArray['class'])
        e.addClassName('left')
        self.assertEqual('passwd left', e.attributeArray['class'])
    
    def test_insert(self):
        e = jformer.Element('password')
        e.insert('<p>Keep it secret</p>')
        self.assertEqual('<p>Keep it secret</p>', e.innerHtml[0])
        div = jformer.Element('div')
        e.insert(div)
        self.assertEqual(div, e.innerHtml[1])
        
    def test_update(self):
        e = jformer.Element('password')
        e.insert('<p>Keep it secret</p>')
        div = jformer.Element('div')
        e.update(div)
        self.assertEqual(div, e.innerHtml[0])
    
    def test_build_str(self):
        e = jformer.Element('div', {'class':'bordered', 'id':'mydiv'})
        div = jformer.Element('div')
        div.insert('House of Cards')
        e.insert(div)
        e.insert('<p>Keep it secret</p>')
        self.assertEqual(e.build(), '<div class="bordered" ' +
                         'id="mydiv"><div>House of Cards</div>' +
                         '<p>Keep it secret</p></div>')
        e = jformer.Element('img', {'src':'profile.jpg'})
        self.assertEqual(e.build(), '<img src="profile.jpg" />')
        self.assertEqual(e.__str__(), '<img src="profile.jpg" />')
        

class TestComponent(unittest.TestCase):
    """Unit tests for jformer Page."""
    
    def test_doctests(self):
        """Run jformer doctests"""
        doctest.testmod(jformer.component)
        
    def test_init(self):
        c = jformer._Component()
        self.assertEqual(c._class, None)
        self.assertEqual(c.value, None)
        self.assertEqual(c.style, None)
        self.assertEqual(c.parentJFormSection, None)
        self.assertEqual(c.anonymous, False)
        self.assertEqual(c.label, None)
        self.assertEqual(c.labelClass, 'jFormComponentLabel')
        self.assertEqual(c.labelRequiredStarClass,
                         'jFormComponentLabelRequiredStar')
        self.assertEqual(c.requiredText, ' *')
        self.assertEqual(c.tip, None)
        self.assertEqual(c.tipClass, 'jFormComponentTip')
        self.assertEqual(c.description, None)
        self.assertEqual(c.descriptionClass,
                         'jFormComponentDescription')
        self.assertEqual(c.instanceOptions, None)
        self.assertEqual(c.triggerFunction, None)
        self.assertEqual(c.enterSubmits, False)
        self.assertEqual(c.dependencyOptions, None)
        self.assertEqual(c.validationOptions, {})
        self.assertEqual(c.errorMessageArray, None)
        self.assertEqual(c.passedValidation, None)
        self.assertEqual(c.showErrorTipOnce, False)
        self.assertEqual(c.persistentTip, False)
    
    def test_initialize(self):
        c = jformer._Component()
        c.validationOptions = 'required'
        c.initialize({'attr1': 'value1', 'attr2': 'value2'})
        self.assertEqual(c.validationOptions, ['required'])
        self.assertEqual(c.options, {'attr1': 'value1', 
                         'attr2': 'value2'})
        
    def test_get_set_clear_value(self):
        c = jformer._Component()
        c.setValue('House')
        self.assertEqual(c.value, 'House')
        value = c.getValue()
        self.assertEqual(value, 'House')
        c.clearValue()
        self.assertEqual(c.value, None)
    
    def test_get_options_empty(self):
        c = jformer._Component()
        self.assertEqual(c.getOptions(), {'type': None})
    
    def test_get_options_validation(self):
        c = jformer._Component()
        c.validationOptions = ['required', 'password']
        self.assertEqual(c.getOptions(), {'type': None,
            'options': {'validationOptions': ['required', 'password']}})
        
    def test_get_options_show_error_tip_once(self):
        c = jformer._Component()
        c.showErrorTipOnce = True
        self.assertEqual(c.getOptions(), {'type': None,
            'options': {'showErrorTipOnce': True}})
        
    def test_get_options_persistent_tip(self):
        c = jformer._Component()
        c.persistentTip = True
        self.assertEqual(c.getOptions(), {'type': None,
            'options': {'persistentTip': True}})
        
    def test_get_options_instance(self):
        c = jformer._Component()
        c.instanceOptions = {
            'max': 3,
            'addButtonText': 'Add Team',
            'removeButtonText': 'Remove Team'}
        self.assertEqual(c.getOptions(), {'type': None,
            'options': {'instanceOptions': {
            'max': 3, 
            'removeButtonText': 'Remove Team', 
            'addButtonText': 'Add Team'}}})
            
    def test_get_options_trigger(self):
        c = jformer._Component()
        c.triggerFunction = 'addValues();'
        self.assertEqual(c.getOptions(), {'type': None,
            'options': {'triggerFunction': 'addValues();'}})
        
    def test_get_options_dependency(self):
        c = jformer._Component()
        c.dependencyOptions = {
            'dependentOn': 'billing_shipping',
            'display': 'hide',
            'jsFunction': '$("#billing_shipping-choice1").is(":checked");'}
        self.assertEqual(c.getOptions(), {'type': None,
            'options': {'dependencyOptions': {
            'dependentOn': ['billing_shipping'],
            'display': 'hide',
            'jsFunction': '$("#billing_shipping-choice1").is(":checked");'}}})
    
    def test_has_instance_values(self):
        c = jformer._Component()
        self.assertEqual(c.hasInstanceValues(), False)
        c.value = '1'
        self.assertEqual(c.hasInstanceValues(), False)
        c.value = ['1', '2']
        self.assertEqual(c.hasInstanceValues(), True)
    
    def test_update_required_text(self):
        c = jformer._Component()
        self.assertEqual(c.requiredText, ' *')
        c.updateRequiredText('So like required')
        self.assertEqual(c.requiredText, 'So like required')
    
    def test_generate_component_div(self):
        c = jformer._Component()
        setattr(c, 'id', 'magic')
        c._class = 'blue_border'
        self.assertEqual(c.generateComponentDiv().__str__(),
            '<div id="magic-wrapper" class="jFormComponent blue_border"></div>')
        c.style = 'color: blue;'
        self.assertEqual(c.generateComponentDiv().__str__(),
            '<div style="color: blue;" id="magic-wrapper" ' +
            'class="jFormComponent blue_border"></div>')
        c.label = 'Name:'
        self.assertEqual(c.generateComponentDiv().__str__(),
            '<div style="color: blue;" id="magic-wrapper" ' +
            'class="jFormComponent blue_border">' +
            '<label id="magic-label" for="magic" ' +
            'class="jFormComponentLabel">Name:</label></div>')
        
    def test_generate_component_label(self):
        c = jformer._Component()
        setattr(c, 'id', 'magic')
        self.assertEqual(c.generateComponentLabel(), '')
        c.label = 'Name:'
        self.assertEqual(c.generateComponentLabel().__str__(),
            '<label id="magic-label" for="magic" class="jFormComponentLabel">Name:</label>')
        c.validationOptions = ['required', 'password']
        self.assertEqual(c.generateComponentLabel().__str__(),
            '<label id="magic-label" for="magic" class="jFormComponentLabel">Name:<span class="jFormComponentLabelRequiredStar"> *</span></label>')
    
    def test_insert_component_description(self):
        from element import Element
        c = jformer._Component()
        setattr(c, 'id', 'magic')
        div = Element('div', {})
        div = c.insertComponentDescription(div)
        self.assertEqual(div.__str__(), '<div></div>')
        c.description = 'My description'
        div = c.insertComponentDescription(div)
        self.assertEqual(div.__str__(),
            '<div><div id="magic-description" class="jFormComponentDescription">My description</div></div>')
        
    def test_insert_component_tip(self):
        from element import Element
        c = jformer._Component()
        setattr(c, 'id', 'magic')
        div = Element('div', {})
        div = c.insertComponentTip(div)
        self.assertEqual(div.__str__(), '<div></div>')
        c.tip = 'Put on your best smile'
        div = c.insertComponentTip(div)
        self.assertEqual(div.__str__(),
            '<div><div style="display: none" id="magic-tip" class="jFormComponentTip">Put on your best smile</div></div>')
        
    def test_required(self):
        c = jformer._Component()
        self.assertRaises(ValueError, c.required, {})
        self.assertEqual(c.required({'value':None}), ['Required.'])
        self.assertEqual(c.required({'value':''}), ['Required.'])
        self.assertEqual(c.required({'value':'0'}), 'success')
        self.assertEqual(c.required({'value':'magic'}), 'success')
        
        
class TestTextArea(unittest.TestCase):
    """Unit tests for jformer TextArea."""
    
    def test_doctests_jformpage(self):
        """Run jformer doctests"""
        doctest.testmod(jformer.textarea)
        
    def test_init(self):
        c = jformer.TextArea('magic', 'Magic Text Area')
        self.assertEqual(c.id, 'magic')
        self.assertEqual(c.label, 'Magic Text Area')
    
    def test_get_option_basic(self):
        c = jformer.TextArea('magic', 'Magic Text Area')
        self.assertEqual(c.getOptions(), {'type': 'jFormComponentTextArea'})
        c.validationOptions = ['required', 'password']
        self.assertEqual(c.getOptions(), {'type': 'jFormComponentTextArea',
            'options': {'validationOptions': ['required', 'password']}})
    
    def test_get_option_extras(self):
        c = jformer.TextArea('magic', 'Magic Text Area')
        self.assertEqual(c.getOptions(), {'type': 'jFormComponentTextArea'})
        c.allowTabbing = True
        c.emptyValue = 'Enter some magic here'
        c.autoGrow = True
        self.assertEqual(c.getOptions(), {'type': 'jFormComponentTextArea',
            'options': {'emptyValue': 'Enter some magic here',
            'allowTabbing': True, 'autoGrow': True}})
        
    def test_str(self):
        c = jformer.TextArea('magic', 'Magic Text Area')
        self.assertEqual(c.__str__(), '<div id="magic-wrapper" ' +
            'class="jFormComponent jFormComponentTextArea">' +
            '<label id="magic-label" for="magic" '+
            'class="jFormComponentLabel">Magic Text Area</label>' +
            '<textarea class="textArea" name="magic" id="magic">' +
            '</textarea></div>')
    
        
if __name__ == "__main__":
    unittest.main()
