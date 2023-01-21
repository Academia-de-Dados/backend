from sentry_sdk import init
from sentry_sdk.integrations.logging import LoggingIntegration, EventHandler
from loguru import logger
from logging import DEBUG
from garcom.config import get_dsn_sentry

loggers = logger

init(
    dsn=get_dsn_sentry(),
    integrations=[
        LoggingIntegration(
            level=None, event_level=None
        )
    ],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)

loggers.add(EventHandler(level=DEBUG), format="{time} {level} {message}")