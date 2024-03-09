from ._anvil_designer import InputTemplate
from anvil import *
import anvil.server
import base64
import anvil.media


class Input(InputTemplate):
  
   
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
  
  def generate_button_click(self, **event_args):
    # Regular expression pattern to match alphanumeric characters
    alphanumeric_pattern = re.compile(r'^[a-zA-Z0-9\s]+$')

    # Validate prompt and negative prompt
    if not alphanumeric_pattern.match(self.prompt.text) or not alphanumeric_pattern.match(self.negative_prompt.text):
        # Display error alert
        alert("Error: Prompts should only contain alphanumeric characters.")
        return
    # Call the google colab function and pass it the parameters
    audio_base64_list = anvil.server.call('GenerateAudio', 
                                self.prompt.text, self.negative_prompt.text, int(self.number_of_gens.selected_value)
                                )
    for index, audio_base64 in enumerate(audio_base64_list):
        # Call the JavaScript function to save the audio data
        anvil.js.call('SaveAudioFromBytes', audio_base64, index)
   
    open_form('Output', gens= self.number_of_gens.selected_value)
  

    
    


