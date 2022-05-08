"""
Gesture command line tool
"""

import os
import sys
import click
from .server import Server

def show_banner():
    banner = """
                                      ,----,                               
                                    ,/   .`|                               
  ,----..      ,---,. .--.--.     ,`   .'  :          ,-.----.      ,---,. 
 /   /   \   ,'  .' |/  /    '. ;    ;     /      ,--,\    /  \   ,'  .' | 
|   :     :,---.'   |  :  /`. .'___,/    ,'     ,'_ /|;   :    \,---.'   | 
.   |  ;. /|   |   .;  |  |--`|    :     | .--. |  | :|   | .\ :|   |   .' 
.   ; /--` :   :  |-|  :  ;_  ;    |.';  ,'_ /| :  . |.   : |: |:   :  |-, 
;   | ;  __:   |  ;/|\  \    ``----'  |  |  ' | |  . .|   |  \ ::   |  ;/| 
|   : |.' .|   :   .' `----.   \  '   :  |  | ' |  | ||   : .  /|   :   .' 
.   | '_.' |   |  |-, __ \  \  |  |   |  :  | | :  ' ;;   | |  \|   |  |-, 
'   ; : \  '   :  ;/|/  /`--'  /  '   :  |  ; ' |  | '|   | ;\  '   :  ;/| 
'   | '/  .|   |    '--'.     /   ;   |.':  | : ;  ; |:   ' | \.|   |    \ 
|   :    / |   :   .' `--'---'    '---'  '  :  `--'   :   : :-' |   :   .' 
 \   \ .'  |   | ,'                      :  ,      .-.|   |.'   |   | ,'   
  `---`    `----'                         `--`----'   `---'     `----'     
    """
    print(banner)

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
    print("Imported script:", full_path)

@click.command()
@click.option('-s', '--script', help='Location of python file to import')
def main(script):
    show_banner()
    import_script(script)
    server = Server()
    server.start()

if __name__ == '__main__':
    sys.exit(main())
