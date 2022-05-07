"""
Gesture command line tool
"""

import os
import sys
import click

def import_script(script):
    full_path = os.path.abspath(script)
    if not os.path.exists(full_path):
        raise Exception("%s file not found, please check it and try again!" % full_path)
    sys.path.append(os.path.dirname(full_path))
    base_name = os.path.basename(full_path)
    module_name = os.path.splitext(base_name)[0]
    print("Imported ", full_path)
    __import__(module_name)

@click.command()
@click.option('-s', '--script', help='Location of python file to import')
def main(script):
    if script:
        import_script(script)

if __name__ == '__main__':
    sys.exit(main())
