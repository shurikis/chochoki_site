import os
import sys

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'run':
        a = (' '.join(sys.argv[2:])).split('|')
        for i in a:
            os.system(i)
