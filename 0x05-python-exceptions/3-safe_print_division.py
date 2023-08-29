#!/usr/bin/python3

   try:
        result = a/b
    except:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return (result)
