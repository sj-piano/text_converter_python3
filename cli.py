# Imports
import os
import sys
import argparse
import logging




# Local imports
# (Can't use relative imports because this is a top-level script)
import text_converter




# Shortcuts
from os.path import isdir, isfile, join
util = text_converter.util
v = util.validate




# Set up logger for this module. By default, it produces no output.
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
logger.setLevel(logging.ERROR)
log = logger.info
deb = logger.debug




# Notes
# Currently, we only support Latin-1 (UTF-8) to EML.




def setup(
    log_level = 'error',
    debug = False,
    log_timestamp = False,
    log_file = None,
    ):
  logger_name = 'cli'
  # Configure logger for this module.
  text_converter.util.module_logger.configure_module_logger(
    logger = logger,
    logger_name = logger_name,
    log_level = log_level,
    debug = debug,
    log_timestamp = log_timestamp,
    log_file = log_file,
  )
  deb('Setup complete.')
  # Configure logging levels for text_converter package.
  # By default, without setup, it logs at ERROR level.
  # Optionally, the package could be configured here to use a different log level, by e.g. passing in 'error' instead of log_level.
  text_converter.setup(
    log_level = log_level,
    debug = debug,
    log_timestamp = log_timestamp,
    log_file = log_file,
  )




def main():

  # Capture and parse command-line arguments.

  parser = argparse.ArgumentParser(
    description='Command-Line Interface (CLI) for using the text_converter package.'
  )

  parser.add_argument(
    '-t', '--task',
    help="Task to perform (default: '%(default)s').",
    default='hello',
  )

  parser.add_argument(
    '--input-file', dest='input_file',
    help="Path to file that contains input data (default: '%(default)s').",
    default='cli_input/input.txt',
  )

  parser.add_argument(
    '-l', '--log-level', type=str, dest='log_level',
    choices=['debug', 'info', 'warning', 'error'],
    help="Choose logging level (default: '%(default)s').",
    default='error',
  )

  parser.add_argument(
    '-d', '--debug',
    action='store_true',
    help="Sets log level to 'debug'. This overrides --log-level.",
  )

  parser.add_argument(
    '-s', '--log-timestamp', dest='log_timestamp',
    action='store_true',
    help="Choose whether to prepend a timestamp to each log line.",
  )

  parser.add_argument(
    '-x', '--log-to-file', dest='log_to_file',
    action='store_true',
    help="Choose whether to save log output to a file.",
  )

  parser.add_argument(
    '-z', '--log-file', dest='log_file',
    help="The path to the file that log output will be written to.",
    default='log_text_converter.txt',
  )

  a = parser.parse_args()

  # Check and analyse arguments
  if not a.log_to_file:
    a.log_file = None

  if a.task == 'convert':
    if not a.input_file:
      z = '--input-file <input_file_path>'
      msg = 'This argument must be supplied: {}'.format(z)
      raise ValueError(msg)
    a.input = open(a.input_file).read()

  # Setup
  setup(
    log_level = a.log_level,
    debug = a.debug,
    log_timestamp = a.log_timestamp,
    log_file = a.log_file,
  )

  # Note: If you add a new task function, then its name must be added to this list.
  tasks = """
hello hello2
get_python_version
convert
""".split()
  if a.task not in tasks:
    msg = "Unrecognised task: {}".format(a.task)
    msg += "\nTask list: {}".format(tasks)
    stop(msg)

  # Run top-level function (i.e. the appropriate task).
  globals()[a.task](a)




def hello(a):
  # Confirm:
  # - that we can run a simple task.
  # - that this tool has working logging.
  log('Log statement at INFO level')
  deb('Log statement at DEBUG level')
  print('hello world')




def hello2(a):
  # Confirm:
  # - that we can run a simple task from within the package.
  # - that the package has working logging.
  bitcoin_toolset.code.hello.hello()




def get_python_version(a):
  # Confirm:
  # - that we can run a shell command.
  check = util.misc.shell_tool_exists('python3')
  v.validate_boolean(check)
  if check is not True:
    msg = "Can't find 'python3' tool in bash shell'"
    raise ValueError(msg)
  cmd = 'python3 --version'
  output, exit_code = util.misc.run_local_cmd(cmd)
  if exit_code != 0:
    msg = "Ran command = '{x}', but got exit code = {c}".format(x=cmd, c=exit_code)
    raise ValueError(msg)
  print(output.strip())




def convert(a):
  output = text_converter.code.convert.utf8_latin_1_to_eml(a.input)
  print(output)




def stop(msg=None):
  if msg is not None:
    print(msg)
  import sys
  sys.exit()




if __name__ == '__main__':
  main()
