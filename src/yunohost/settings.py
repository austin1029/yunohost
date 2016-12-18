import os
import yaml


SETTINGS_PATH = "/etc/yunohost/settings.yaml"

DEFAULT_VALUES = {
    "example": "value",
}


def settings_get(key, default):
    return _get_settings().get(key, default)


def settings_list():
    return _get_settings()


def settings_exists(key):
    return key in _get_settings()


def settings_set(key, value):
    settings = _get_settings()

    settings[key] = value

    # TODO error handling
    result = yaml.dump(settings)

    with open(SETTINGS_PATH, "w") as settings_fd:
        settings_fd.write(result)

    return "ok"


def settings_remove(key, silently_fail=False):
    settings = _get_settings()

    del settings[key]

    # TODO error handling
    result = yaml.dump(settings)

    with open(SETTINGS_PATH, "w") as settings_fd:
        settings_fd.write(result)

    return "ok"


def _get_settings():
    settings = DEFAULT_VALUES.copy()

    if not os.path.exists(SETTINGS_PATH):
        return settings

    # TODO error handling
    with open(SETTINGS_PATH) as settings_fd:
        settings.update(yaml.load(settings_fd))

    return settings
