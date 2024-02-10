from ._anvil_designer import InputTemplate
from anvil import *
import anvil.server
import base64
import anvil.media

class Input(InputTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # Any code you write here will run before the form opens  
    
  
  def generate_button_click(self, **event_args):
    
    
    # Call the google colab function and pass it the iris measurements
    audio_base64 = anvil.server.call('test', 
                                self.prompt.text, self.negative_prompt.text, 3
                                )
     
    if audio_base64:
      self.negative_prompt.text = "The species is " + audio_base64
    

    
   

    audio_data = []
    audio_data.append(audio_base64)
    audio_data.append(audio_2)
    #for audio in audio_data: 
    #  self.call_js('SaveAudioFromBytes',audio, audio_data.index(audio))
    self.call_js('SaveAudioFromBytes',audio_base64, 0)
    self.call_js('SaveAudioFromBytes',audio_2, 1)
   
    open_form('Output', gens= self.number_of_gens.selected_value)
  

    
    


