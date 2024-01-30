from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  def player_click(self, **event_args):
    """This method is called when the button is clicked"""
    src_url = anvil.server.call('load_url')
    self.audio_player.call_js('loadClip', src_url)
  def generate_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    # Call the google colab function and pass it the iris measurements
    iris_category = anvil.server.call('test', 
                                self.prompt.text
                                )
    # If a category is returned set our species 
    if iris_category:
     
      self.negativePrompt.text = "The species is " + iris_category

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def button_1_click(self, **event_args):
    self.call_js('PlaySound')

