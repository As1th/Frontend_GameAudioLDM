from ._anvil_designer import OutputTemplate
from anvil import *
import anvil.server

class Output(OutputTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  def PlayAudio1(self, **event_args):
    self.call_js('PlayAudio1')