from ._anvil_designer import OutputTemplate
from anvil import *
import anvil.server
numberOfGenerations = 0
class Output(OutputTemplate):

  def __init__(self, gens, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    numberOfGenerations = int(gens)
    for i in range(1, 10):
        # Get the checkbox and button components by name
        checkbox = getattr(self, f'audio_check_{i}')
        button = getattr(self, f'audio_play_{i}')
        
        # Check if the current index is greater than the number of generations
        if i > numberOfGenerations:
            # Hide the checkbox and button if the index is greater
            checkbox.visible = False
            button.visible = False
        else:
            # Show the checkbox and button if the index is less than or equal to the number of generations
            checkbox.visible = True
            button.visible = True
    # Any code you write here will run before the form opens.


  def ExportAssets(self, **event_args):
    audio_variables = [
        self.audio_check_1, self.audio_check_2, self.audio_check_3,
        self.audio_check_4, self.audio_check_5, self.audio_check_6,
        self.audio_check_7, self.audio_check_8, self.audio_check_9
    ]
    
    for i, checkbox in enumerate(audio_variables):
        if checkbox.checked:
            # Trigger download for this audio number
            self.call_js('DownloadSavedAudio', i)


  def PlayAudio(self, **event_args):
    # Extract the number from the button name
    button_name = event_args['sender'].tooltip
    audio_number = int(button_name.split()[-1]) - 1
    
    # Call the JavaScript function with the extracted audio number
    self.call_js('PlaySavedAudio', audio_number)
    
  
  
  def CheckAudio1(self, **event_args):
    self.CheckAudio(self.audio_check_1, self.audio_play_1)

  def CheckAudio2(self, **event_args):
    self.CheckAudio(self.audio_check_2, self.audio_play_2)
  def CheckAudio3(self, **event_args):
    self.CheckAudio(self.audio_check_3, self.audio_play_3)
  def CheckAudio4(self, **event_args):
    self.CheckAudio(self.audio_check_4, self.audio_play_4)
  def CheckAudio5(self, **event_args):
    self.CheckAudio(self.audio_check_5, self.audio_play_5)
  def CheckAudio6(self, **event_args):
    self.CheckAudio(self.audio_check_6, self.audio_play_6)
  def CheckAudio7(self, **event_args):
    self.CheckAudio(self.audio_check_7, self.audio_play_7)
  def CheckAudio8(self, **event_args):
    self.CheckAudio(self.audio_check_8, self.audio_play_8)
  def CheckAudio9(self, **event_args):
    self.CheckAudio(self.audio_check_9, self.audio_play_9)

  def CheckAudio(self, checkbox, player):
    if checkbox.checked:
       player.background = 'theme:Primary 500'
    else:
       player.background = 'theme:Gray 600'
       
  
       