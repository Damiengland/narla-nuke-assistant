# menu.py for Nuke
# This script adds a "Chatbot" menu to Nuke's main menu bar.

import nuke
from python import panel, chatbot

# This global variable will hold the panel instance to prevent creating duplicates.
chatbot_panel_instance = None

def open_chatbot_panel():
    """
    Creates and shows the Nuke Chatbot panel.
    If the panel already exists, it brings it to the front instead of creating a new one.
    """
    global chatbot_panel_instance

    # If the panel has already been created, just show it and bring it to the front.
    if chatbot_panel_instance:
        chatbot_panel_instance.show()
        chatbot_panel_instance.raise_() # This brings the window on top of others
    # Otherwise, create a new panel instance.
    else:
        chatbot_logic = chatbot.Chatbot()
        chatbot_panel_instance = panel.NukeChatbotPanel(chatbot_logic)
        chatbot_panel_instance.resize(400, 600)
        chatbot_panel_instance.show()
        # Pro-tip: For a more robust tool, you could modify your NukeChatbotPanel
        # class to set chatbot_panel_instance back to None when the window is closed.

# --- Menu Integration ---
# This code runs when Nuke starts and automatically builds the menu.

# 1. Get Nuke's main menu bar
menubar = nuke.menu('Nuke')

# 2. Create a new top-level menu named "Chatbot"
chatbot_menu = menubar.addMenu('Chatbot')

# 3. Add a command to the menu that calls our function
# The first argument is the menu item's label, and the second is the function to run.
chatbot_menu.addCommand('Open Narla', open_chatbot_panel)
