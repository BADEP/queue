import odoo.tools

from .runner import QueueJobRunner


def main():
    odoo.tools.config.parse_config(setup_logging=True)
    runner = QueueJobRunner.from_environ_or_config()
    runner.run()


if __name__ == "__main__":
    main()
