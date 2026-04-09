"""
nginx-configurator — Nginx configuration generator with load balancing and SSL templates
"""
import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)


def main() -> int:
    """Entry point for nginx-configurator."""
    logger.info("Starting application...")

    try:
        logger.info("Application initialized successfully")
        return 0
    except Exception as exc:
        logger.exception("Fatal error: %s", exc)
        return 1


if __name__ == "__main__":
    sys.exit(main())
