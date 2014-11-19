def multiple_args(*args):
    for arg in args:
        print arg
        

def key_args(**kwargs):
    for key in kwargs:
        print key, '=', kwargs[key]

multiple_args()        
multiple_args(123, 'dupa', 222)

key_args()
key_args(arg1=123)
key_args(arg1=123, name='dupa')