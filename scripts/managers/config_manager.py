import json

from ..utils.constants import Constants
from ..utils import paths


class ConfigManager:
    """
    This class manages the config.json file.
    """

    # the last saved config values
    remove_used_messages = True
    use_all_chat = False
    enable_ally_death = True
    enable_ally_kill = True
    enable_self_death = True
    enable_self_kill = True
    current_preset_name = None
    show_help = True

    @classmethod
    def update_current_config_values(cls, config: dict):
        """
        Updates the current config values.
        """
        cls.remove_used_messages = config.get(Constants.REMOVE_USED_MESSAGES, True)
        cls.use_all_chat = config.get(Constants.USE_ALL_CHAT, False)
        cls.enable_ally_death = config.get(Constants.ENABLE_ALLY_DEATH, True)
        cls.enable_ally_kill = config.get(Constants.ENABLE_ALLY_KILL, True)
        cls.enable_self_death = config.get(Constants.ENABLE_SELF_DEATH, True)
        cls.enable_self_kill = config.get(Constants.ENABLE_SELF_KILL, True)
        cls.current_preset_name = config.get(Constants.CURRENT_PRESET_NAME, None)
        cls.show_help = config.get(Constants.SHOW_HELP, True)

    @classmethod
    def load(cls):
        """
        Loads the config.
        """
        with open(paths.get_config_json_path(), "r", encoding="utf-8") as file:
            return json.load(file)

    @classmethod
    def save(cls, config: dict):
        """
        Saves the config.
        """
        with open(paths.get_config_json_path(), "w", encoding="utf-8") as file:
            json.dump(config, file, indent=4)

        cls.update_current_config_values(config)
