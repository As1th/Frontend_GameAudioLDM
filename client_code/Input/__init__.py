from ._anvil_designer import InputTemplate
from anvil import *
import anvil.server
class Input(InputTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
 
    # Any code you write here will run before the form opens.
  
  def generate_button_click(self, **event_args):
    open_form('Output')
    self.call_js('PlayAudio1')
    """This method is called when the button is clicked"""
    # Call the google colab function and pass it the iris measurements
    iris_category = anvil.server.call('test', 
                                self.prompt.text
                                )
    # If a category is returned set our species 
    if iris_category:
      self.negativePrompt.text = "The species is " + iris_category

    open_form('Output')

  def PlayAudio1(self, **event_args):
    sound = self.call_js('PlayAudio1')
    
    


