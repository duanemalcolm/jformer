import unittest
import doctest

import jformer
import jformelement

class Test(unittest.TestCase):
    """Unit tests for jformer."""

    def test_doctests(self):
        """Run jformer doctests"""
        doctest.testmod(jformer)
        doctest.testmod(jformelement)
        
    def test_jformer(self):
        form = jformer.JFormer('login')
        self.assertEqual('login', form.id)
    
    
    def test_jformer_element(self):
        elem = jformer.Element('div')
        self.assertEqual('div', elem.tag)
        
        
    #~ def test_jformer_add_page(self):
        #~ form = jformer.JFormer('login')
        #~ form.addJFormPage([])

if __name__ == "__main__":
    unittest.main()
