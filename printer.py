"""
animethemes-dl custom print
allows the use of quiet and no-color
"""
import sys
from globals import Opts


def color_category(category):
    """
    adds color to a category and puts it in brackets
    """
    if Opts.Print.no_color:
        return '['+category+']'
    
    color = {
        'progress':'\033[32m',
        'get':'\033[1;33m',
        'download':'\033[1;36m',
        'convert':'\033[36m',
        'parse':'\033[34m',
        'error':'\033[1;31m'
    }
    endcolor='\033[m'

    return '['+color[category]+category+endcolor+']'

def fprint(category,message='',start='',end='\n'):
    """
    animethemes-dl custom print function
    colors a given category and then it puts it in brackets
    if no message is given, the category will be printed like a normal `print`
    """
    if Opts.Print.quiet:
        return
    if message:
        message = start+color_category(category)+' '+str(message)+end
        sys.stdout.write(message)
    else:
        sys.stdout.write(start+str(category)+end)
