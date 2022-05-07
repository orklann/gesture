"""
Gesture command line tool
"""

import os
import sys
import click

def import_script(script):
    if not script:
        print("Please specify a script file by using -s option. Exiting...")
        return
    full_path = os.path.abspath(script)
    if not os.path.exists(full_path):
        print('"%s" not found, exiting...' % full_path)
        return
    sys.path.append(os.path.dirname(full_path))
    base_name = os.path.basename(full_path)
    module_name = os.path.splitext(base_name)[0]
    __import__(module_name)
    print("Imported", full_path)

@click.command()
@click.option('-s', '--script', help='Location of python file to import')
def main(script):
    import_script(script)

if __name__ == '__main__':
    sys.exit(main())
