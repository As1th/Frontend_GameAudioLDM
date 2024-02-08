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
       
  
       