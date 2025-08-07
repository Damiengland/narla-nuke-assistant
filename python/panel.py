# NukeChatbotPanel.py
# NARLA (NUKES AI RAG LLM ASSISTANT)

from PySide6 import QtWidgets, QtCore, QtGui

# --- Custom Chat Bubble Widget ---
# This custom widget gives us full control over the bubble's appearance.
class ChatBubble(QtWidgets.QWidget):
    """
    A custom widget that draws a chat bubble with rounded corners.
    """
    # Define colors and parameters as class variables for easy access
    USER_BG_COLOR = QtGui.QColor(0, 120, 212)
    BOT_BG_COLOR = QtGui.QColor(58, 58, 58)
    USER_TEXT_COLOR = QtGui.QColor("white")
    BOT_TEXT_COLOR = QtGui.QColor("white")
    BOT_NAME_COLOR = QtGui.QColor(249, 180, 27)
    
    RADIUS = 15
    PADDING = 10

    def __init__(self, text, is_user_message):
        super().__init__()
        self.is_user_message = is_user_message
        
        # Use a label to display the text within the bubble
        self.label = QtWidgets.QLabel(text)
        self.label.setWordWrap(True)
        self.label.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        
        # Set text color based on who sent the message
        text_color = self.USER_TEXT_COLOR if self.is_user_message else self.BOT_TEXT_COLOR
        self.label.setStyleSheet(f"color: {text_color.name()};")

        # Use a layout to manage the label within the widget
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.label)
        # Set margins to create padding inside the bubble
        layout.setContentsMargins(self.PADDING, self.PADDING, self.PADDING, self.PADDING)

    def paintEvent(self, event):
        """
        Override the paint event to draw the custom bubble shape.
        """
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing) # For smooth corners

        # Choose the background color
        bg_color = self.USER_BG_COLOR
        painter.setBrush(QtGui.QBrush(bg_color))
        painter.setPen(QtCore.Qt.NoPen) # No border

        # Create a painter path to define the custom shape
        path = QtGui.QPainterPath()
        rect = self.rect()
        
        # Draw a rounded rectangle, but flatten one corner
        if self.is_user_message:
            # User bubble: flat top-right corner
            path.moveTo(rect.bottomLeft() + QtCore.QPoint(0, -self.RADIUS))
            path.arcTo(rect.bottomLeft().x(), rect.bottomLeft().y() - self.RADIUS * 2, self.RADIUS * 2, self.RADIUS * 2, 180, 90)
            path.lineTo(rect.bottomRight() - QtCore.QPoint(self.RADIUS, 0))
            path.arcTo(rect.bottomRight().x() - self.RADIUS * 2, rect.bottomRight().y() - self.RADIUS * 2, self.RADIUS * 2, self.RADIUS * 2, 270, 90)
            path.lineTo(rect.topRight()) # Flat corner
            path.lineTo(rect.topLeft() + QtCore.QPoint(self.RADIUS, 0))
            path.arcTo(rect.topLeft().x(), rect.topLeft().y(), self.RADIUS * 2, self.RADIUS * 2, 90, 90)


        path.closeSubpath()
        painter.drawPath(path)


class NukeChatbotPanel(QtWidgets.QWidget):
    """
    A chatbot panel that uses a QListWidget and custom ChatBubble widgets.
    """
    def __init__(self, chatbot, parent=None):
        super(NukeChatbotPanel, self).__init__(parent)

        self.chatbot = chatbot
        
        self.setWindowTitle("NARLA")
        self.setObjectName("NARLA")
        
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(8)

        # Use a QListWidget to hold the chat bubbles
        self.chat_history = QtWidgets.QListWidget()
        self.chat_history.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.chat_history.setStyleSheet("QListWidget { border: none; background-color: rgb(58, 58, 58); }")
        
        self.input_line = QtWidgets.QLineEdit()
        self.input_line.setPlaceholderText("Ask a question and press Enter...")
        self.input_line.setFont(QtGui.QFont("Arial", 10))
        
        main_layout.addWidget(self.chat_history)
        main_layout.addWidget(self.input_line)

        self.input_line.returnPressed.connect(self.handle_user_input)

    def add_bubble(self, text, is_user_message):
        """
        Creates a ChatBubble, wraps it in a layout for alignment,
        and adds it to the QListWidget.
        """
        bubble = ChatBubble(text, is_user_message)
        
        # Use a container widget and layout to align the bubble left or right
        container_widget = QtWidgets.QWidget()
        layout = QtWidgets.QHBoxLayout(container_widget)
        layout.setContentsMargins(0, 5, 0, 5) # Add vertical spacing between bubbles
        
        if is_user_message:
            layout.addStretch() # Push bubble to the right
            layout.addWidget(bubble)
            layout.addSpacing(5) # Small margin from the edge
        else:
            layout.addSpacing(5) # Small margin from the edge
            layout.addWidget(bubble)
            layout.addStretch() # Push bubble to the left
            
        # Create a QListWidgetItem to hold our custom widget
        list_item = QtWidgets.QListWidgetItem(self.chat_history)
        # Set its size hint to make sure the widget is displayed correctly
        list_item.setSizeHint(container_widget.sizeHint())
        
        self.chat_history.addItem(list_item)
        self.chat_history.setItemWidget(list_item, container_widget)
        self.chat_history.scrollToBottom()

    def handle_user_input(self):
        user_message = self.input_line.text().strip()
        if not user_message:
            return

        # Add the user's message
        user_text = f"<b>You:</b> {user_message}"
        self.add_bubble(user_text, True)

        # Get and add the bot's response
        bot_response = self.get_bot_response(user_message)
        formatted_response = bot_response.replace('\n', '<br>')
        bot_text = f"<b style='color:{ChatBubble.BOT_NAME_COLOR.name()};'>Narla:</b><br>{formatted_response}"
        self.add_bubble(bot_text, False)

        self.input_line.clear()

    def get_bot_response(self, message):

        response = self.chatbot.ask(message)
        print(response)
        return response.get('answer')

    
    


        
