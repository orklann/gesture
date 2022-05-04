"""
Gesture command line tool
"""

import sys
import click

@click.command()
@click.option('-s', '--script', help='Location of python file to import')
def main(script):
    if script:
        print("::Adding some magic into your script:", script)

if __name__ == '__main__':
    sys.exit(main())
