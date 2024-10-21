import logging


def configure_logging(
        app_logger: str = '',
        level: str = 'DEBUG',
        disable_loggers: list[tuple] = []
) -> None:

    FORMAT = f"[%(levelname)s]\t| [%(asctime)s] | %(filename)s:%(lineno)d\t| %(message)s"
    logging.basicConfig(
        level=level,
        format=FORMAT
    )

    for logger_name, level in disable_loggers:
        logging.getLogger(logger_name).setLevel(level)

    