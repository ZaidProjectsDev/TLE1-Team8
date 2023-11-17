class Localization:
    def __init__(self):

        self.language = None
        self.languages = {"english", "dutch"}
        self.default_language = "english"
        self.localization_table = {
            "confirm_button_01": {"english": "Confirm", "dutch": "Bevestigen"},
            "enable_screen_reader_window": {"english": "Enable Screen Reader X", "dutch": "Bevestigen"},
            "disable_screen_reader_window": {"english": "Disable Screen Reader", "dutch": "Bevestigen"},
            "find_game_windows": {"english": "Find Game Open Windows", "dutch": "Bevestigen"},
            "bark_current_game_window": {"english": "Current Active Game is : ", "dutch": "De actieve spel is :"},
            "bark_no_game_window": {"english": "There is no game selected: ", "dutch": "Er is geen geselecteerde speel:"},
            "language_toggle_button": {"english": "Language : English: ",
                                    "dutch": "Taal : Nederlands:"},
            # Add more entries for other keys as needed
        }

    def set_language(self, language):
        # Set the current language if it is a valid language, otherwise use the default language
        self.language = language.lower() if language.lower() in self.languages else self.default_language

    def get_translation(self, key):
        if self.language is None:
            self.set_language(self.default_language)
        # Get the translation for the specified key in the current language or default to English
        return self.localization_table.get(key, {}).get(self.language, f"Translation not available for {self.language}")


# # Example usage:
# localization = Localization()
#
# # Set language to English (default)
# print(localization.get_translation("confirm_button_01"))  # Output: Confirm
#
# # Set language to Dutch
# localization.set_language("dutch")
# print(localization.get_translation("confirm_button_01"))  # Output: Bevestigen
