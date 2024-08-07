class Constants:
    """
    This class contains all constants.
    """

    # menu types
    MAIN_MENU = "main_menu"
    TOGGLE_EVENTS_MENU = "toggle_events_menu"
    PRESET_MENU = "preset_menu"
    WAITING_MENU = "waiting_menu"
    IN_GAME_MENU = "in_game_menu"

    # relative paths
    REL_CONFIG_JSON_PATH = "../config/config.json"
    REL_PRESETS_DIR_PATH = "../presets"

    # default values
    NEW_PRESET_NAME = "New Preset"

    # config
    REMOVE_USED_MESSAGES = "removeUsedMessages"
    USE_ALL_CHAT = "useAllChat"
    ENABLE_ALLY_DEATH = "enable_ally_death"
    ENABLE_ALLY_KILL = "enable_ally_kill"
    ENABLE_SELF_DEATH = "enable_self_death"
    ENABLE_SELF_KILL = "enable_self_kill"
    CURRENT_PRESET_NAME = "currentPresetName"
    SHOW_HELP = "showHelp"

    # events
    SELF_KILL = "self_kill"
    SELF_DEATH = "self_death"
    ALLY_KILL = "ally_kill"
    ALLY_DEATH = "ally_death"

    # thread variables
    INTERVAL = 4
