#!/usr/bin/env python3
"""A multi-line comment to describe the script,
made with triple quotes"""

def main(): #all ode should appear within a function
    """all functions have multiline commnets to descrive them"""

    my_string="your code would go here"  #vars use _ not camelcase
    print(my_string)  #print to standard-out

# calling main() using this technique allows others to import code
if __name__=="__main__":
    main()
