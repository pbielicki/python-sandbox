'''
write an input_integer function

* calls raw_input to get a value from the user
* converts the value to an integer
* if this fails, it prompts again, until the user
  has provided a valid input or pressed Ctrl-C
* if the user pressed Ctrl-C, the function must return None

'''

def input_integer():
    try:
        answer = raw_input('> ')
    except KeyboardInterrupt:
        return None
    try:
        return int(answer)
    except ValueError:
        print 'not a number. Try again.'
        return input_integer()


print 'give me a number:'
print input_integer()
