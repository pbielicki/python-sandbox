
def var_args_fn(*args):
    print args

var_args_fn()
var_args_fn(1, 2)

def var_args_fn2(argname, *args):
    print args

var_args_fn2(argname=1)
var_args_fn2(1, 2, 3)
# error: positional arguments must come first
# var_args_fn2(argname=1, 2, 3)


def var_args_fn3(**kwargs):
    print kwargs

var_args_fn3(arg1=1, arg2=2)

# error: no positional arguments accepted
var_args_fn3(1, 2, 3)

