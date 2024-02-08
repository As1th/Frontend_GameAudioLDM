from ._anvil_designer import InputTemplate
from anvil import *
import anvil.server
import base64


class Input(InputTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
 
    # Any code you write here will run before the form opens.
  
  def generate_button_click(self, **event_args):
    
    """This method is called when the button is clicked"""
    # Call the google colab function and pass it the iris measurements
    audio_base64 = anvil.server.call('test', 
                                self.prompt.text, self.negative_prompt.text, 1
                                )
    # If a category is returned set our species 
    if audio_base64:
      self.negative_prompt.text = "The species is " + audio_base64
    audio_bytes = base64.b64decode(audio_base64)

    #
    audio_base64 = 
    #
    self.call_js('PlayAudioFromBytes',audio_base64)

    #open_form('Output')

  def PlayAudio1(self, **event_args):
    sound = self.call_js('PlayAudio1')
    
    


