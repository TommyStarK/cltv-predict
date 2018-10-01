
from apyml import __version__ as apymlVersion, ExitStatus
from apyml.apyml import APYML
from apyml.context import Context
from apyml.internal import init_logger


def program(args: dict = None):
    mode, report = None, None

    if not args or not 'filepath' in args:
        raise RuntimeError('Unexpected error occurred.')
    if 'mode' in args:
        mode = args['mode']
    if 'report' in args:
        report = args['report']
    
    app = APYML(args['filepath'], mode=mode, report=report)
    app.run()
    app.report()

def main() -> int:
    from apyml.cli import parser
    args = vars(parser.parse_args())

    from . import ExitStatus
    exit_status = ExitStatus.OK

    try:
        Context()
        init_logger()
    except KeyboardInterrupt:
        raise
        exit_status = ExitStatus.CTRL_C
    else:
        try:
            program(args=args)
        except KeyboardInterrupt:
            raise
            exit_status = ExitStatus.CTRL_C
        except Exception as e:
            print(f'ERROR: {e}')
            exit_status = ExitStatus.ERROR
    return exit_status