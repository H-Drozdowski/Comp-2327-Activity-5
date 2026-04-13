"""A client program written to verify correctness of the activity 
classes.
"""

from sports_app.sports_app import SportsApp

# GIVEN:
from PySide6.QtWidgets import QApplication
import sys

__author__ = "ACE Faculty"
__version__ = "1.0.0"

def main() -> None:
    """The main function of the program."""

    app = QApplication(sys.argv)
    window = SportsApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
