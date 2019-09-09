#!/usr/bin/env python3
from mainpackage import main_script
from mainpackage.subpackage import sub_script

if __name__ == '__main__':
    main_script.print_main()
    sub_script.print_sub()
