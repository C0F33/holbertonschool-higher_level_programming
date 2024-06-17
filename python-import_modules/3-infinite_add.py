#!/usr/bin/python3

import sys

result = sum(int(arg) for arg in sys.argv[1:])

print(result)
if __name__ == "__main__":
    main()
