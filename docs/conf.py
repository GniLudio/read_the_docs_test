from typing import Any

import requests
from sphinx.application import Sphinx

WEBHOOK_POST_URL = "https://webhook.site/f843e4d9-34d3-436a-acf0-25630993f2f9"
WEBHOOK_VIEW_URL = "https://webhook.site/#!/view/f843e4d9-34d3-436a-acf0-25630993f2f9"


def setup(app: Sphinx, *_: Any, **__: Any) -> None:
    log("setup")
    app.connect("builder-inited", lambda *_, **__: log("builder-inited"))
    app.connect("build-finished", lambda *_, **__: log("build-finished"))

    while True:
        pass


def log(message: str) -> Any:
    response = requests.post(WEBHOOK_POST_URL, data=message)
    response.raise_for_status()
