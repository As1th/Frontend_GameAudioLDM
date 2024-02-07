from ._anvil_designer import InputTemplate
from anvil import *
import anvil.server
class Input(InputTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
 
    # Any code you write here will run before the form opens.
  
  def generate_button_click(self, **event_args):
    
    """This method is called when the button is clicked"""
    # Call the google colab function and pass it the iris measurements
    audio = anvil.server.call('test', 
                                self.prompt.text, self.negative_prompt.text, 1
                                )
    # If a category is returned set our species 
    if audio:
      self.negative_prompt.text = "The species is " + audio

    #open_form('Output')

  def PlayAudio1(self, **event_args):
    sound = self.call_js('PlayAudio1')
    
    


