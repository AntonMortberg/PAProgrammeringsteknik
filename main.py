from TextUI import *
from GraphicalUI import *
import sys


if len(sys.argv) > 1:
    if sys.argv[1] == "-g":  # för att start det grafiska istället för det textbaserade
        maing()
else:
    main()
