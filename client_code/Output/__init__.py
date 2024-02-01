from ._anvil_designer import OutputTemplate
from anvil import *
import anvil.server

class Output(OutputTemplate):
  Audio1Checked = 0
  Audio2Checked = 0
  Audio3Checked = 0
  Audio4Checked = 0
  Audio5Checked = 0
  Audio6Checked = 0
  Audio7Checked = 0
  Audio8Checked = 0
  Audio9Checked = 0
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  def PlayAudio1(self, **event_args):
    self.call_js('PlayAudio1')

  def CheckAudio1(self, **event_args):
    if self.audio_check_1.checked:
       self.audio_play_1.background = 'theme:Primary 500'
    else:
       self.audio_play_1.background = 'theme:Gray 600'
       
       