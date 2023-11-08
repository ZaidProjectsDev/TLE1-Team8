from setuptools import setup, find_packages

setup(
    name="game_screen_reader",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "pytesseract",
        "pyautogui",
        "pyttsx3",
        # Add any other dependencies here
    ],
    entry_points={
        "console_scripts": [
            "game_screen_reader = game_screen_reader.main:main_function",
        ],
    },
)
