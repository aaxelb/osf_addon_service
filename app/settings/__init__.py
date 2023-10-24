import sys
import warnings

# Don't check for secrets during tests to appease CI.
if sys.argv[:2] == ["manage.py", "test"]:
    from app.settings.test import *  # noqa
else:
    from app.settings.defaults import *  # noqa

try:
    from app.settings.local import *  # noqa
except ImportError:
    warnings.warn(
        "No settings file found. Did you remember to "
        "copy local-dist.py to local.py?",
        ImportWarning,
    )
