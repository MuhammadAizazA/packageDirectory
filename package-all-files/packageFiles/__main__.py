import sys
from packageFiles import module

def main(): 
    if(len(sys.argv)>1):
        module.function_for([*sys.argv[1::],'Called from __main__.py with arguments'])
    else:
        module.function_for(['ABC',123,'9090','Called from __main__.py'])

if __name__=='__main__':
    main()