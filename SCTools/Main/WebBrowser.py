# # # Testing Browser Ideas In Python 


# #################################################################################################################################################



# import sys
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
# from PyQt5.QtWebEngineWidgets import *

# class Browser(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.initUI()

#         self.is_window_on_top = True
#         # Initialize variables for window dragging and resizing

#         self.is_resizing = False

#         self.is_dragging = False
#         self.offset = None

#     def mousePressEvent(self, event):
#         if event.button() == Qt.RightButton:
#             self.is_dragging = True
#             self.offset = event.pos()

#     def mouseMoveEvent(self, event):
#         if self.is_dragging:
#             self.move(event.globalPos() - self.offset)

#     def mouseReleaseEvent(self, event):
#         if event.button() == Qt.RightButton:
#             self.is_dragging = False
#             self.offset = None

#     def initUI(self):
#         # Create the browser window
#         self.browser = QWebEngineView()
#         self.setCentralWidget(self.browser)

#         # Create the menu bar
#         menu_bar = self.menuBar()

#         # Create the "File" menu
#         file_menu = menu_bar.addMenu('File')

#         # # Create the "Toggle Borderless Mode" action
#         # toggle_borderless_action = QAction('Toggle Borderless Mode', self)
#         # toggle_borderless_action.triggered.connect(self.toggle_borderless)
#         # file_menu.addAction(toggle_borderless_action)

#         # # Create the "Force Window to Front" action
#         # force_window_to_front_action = QAction('Force Window to Front', self)
#         # force_window_to_front_action.triggered.connect(self.force_window_to_front)
#         # file_menu.addAction(force_window_to_front_action)

#         # Create the URL bar
#         self.url_bar = QLineEdit()
#         self.url_bar.returnPressed.connect(self.navigate)
#         self.url_bar.setFixedHeight(25)

#         # Create the back button
#         back_button = QPushButton('<')
#         back_button.clicked.connect(self.browser.back)

#         # Create the forward button
#         forward_button = QPushButton('>')
#         forward_button.clicked.connect(self.browser.forward)

#         # Create the home button
#         home_button = QPushButton('Home')
#         home_button.clicked.connect(self.navigate_home)


#         # Create the "Toggle Borderless Mode" 
#         toggle_borderless_action = QPushButton('Borderless Mode')
#         toggle_borderless_action.clicked.connect(self.toggle_borderless)
 
#         # Create the "Force Window to Front" 
#         force_window_to_front_action = QPushButton('Window to Front')
#         force_window_to_front_action.clicked.connect(self.force_window_to_front)




#         # Create the navigation bar
#         navigation_bar = QHBoxLayout()
#         navigation_bar.addWidget(toggle_borderless_action)
#         navigation_bar.addWidget(force_window_to_front_action)
#         navigation_bar.addWidget(back_button)
#         navigation_bar.addWidget(forward_button)
#         navigation_bar.addWidget(home_button)



#         navigation_bar.addWidget(self.url_bar)

#         # Create the main widget
#         main_widget = QWidget()
#         main_widget.setLayout(QVBoxLayout())
#         main_widget.layout().addLayout(navigation_bar)
#         main_widget.layout().addWidget(self.browser)

#         self.setCentralWidget(main_widget)

#         # Load the default page
#         self.browser.setUrl(QUrl('https://www.google.com'))

#         # Set the window properties
#         self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
#         self.setGeometry(100, 100, 800, 600)
#         self.show()

#     def navigate(self):
#         # Navigate to the URL in the URL bar
#         url = self.url_bar.text()
#         if not url.startswith('http://') and not url.startswith('https://'):
#             url = 'http://' + url

#         self.browser.setUrl(QUrl(url))


#     def navigate_home(self):
#         # Navigate to the home page
#         self.browser.setUrl(QUrl('https://www.google.com'))

#     def toggle_borderless(self):
#         # Toggle the borderless mode
#         if self.windowFlags() & Qt.FramelessWindowHint:
#             self.setWindowFlags(Qt.Window)
#         else:
#             self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)

#         self.show()
        

#     def force_window_to_front(self):
#         if self.is_window_on_top:
#             # Allow other windows to be in front
#             self.setWindowFlags(self.windowFlags() & ~Qt.WindowStaysOnTopHint)
           
#         else:
#             # Force the window to be in front of all other windows
#             self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)

#         # Update the window state and toggle the flag
#         self.setWindowState(self.windowState() | Qt.WindowActive)
#         self.show()
#         self.is_window_on_top = not self.is_window_on_top


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     browser = Browser()
#     sys.exit(app.exec_())

    
# #################################################################################################################################################