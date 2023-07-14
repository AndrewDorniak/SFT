import platform
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))


from django.core.management import call_command
from src.sft.wsgi import get_wsgi_application


app = get_wsgi_application()


if platform.uname().system.lower() == 'linux':
    import gunicorn.app.base

    class StandaloneApplication(gunicorn.app.base.BaseApplication):

        def __init__(self, app, options=None):
            self.options = options or {}
            self.application = app
            super().__init__()

        def load_config(self):
            config = {
                key: value for key, value in self.options.items()
                if key in self.cfg.settings and value is not None
            }
            for key, value in config.items():
                self.cfg.set(key.lower(), value)

        def load(self):
            return self.application


if __name__ == '__main__':
    call_command('migrate')

    if platform.uname().system.lower() == 'linux':
        settings = {
            "bind": 'localhost:9010',
            "workers": 1,
            "timeout": 120,
            "accesslog": '-',
            "access_log_format": 'INFO:%(t)s %(m)s %(U)s %(H)s %(s)s',
            "reload": True,
        }
        StandaloneApplication(app, settings).run()
