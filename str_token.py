# global keyword has risk, H.Shirouzu

next_str = None

# if targ_str is None, tokenize trail substring
def str_token(targ_str=None):
    global next_str

    if not targ_str:
        if not next_str:
            return None
        targ_str = next_str

    tlist = targ_str.split(maxsplit=1)

    if len(tlist) == 2:
        next_str = tlist[1]
        return  tlist[0]

    elif len(tlist) == 1:
        next_str = None
        return  tlist[0]

    else:   # len(tlist) == 0
        next_str = None
        return  None


def test1():
    command_line = "hello.exe harg1 harg2 harg3"

    ret = str_token(command_line)

    while ret:
        print("cmdline", ret)
        ret = str_token()
    print()


def test2():
    command_line1 = "hello.exe harg1 harg2 harg3"
    command_line2 = "byebye.exe barg1 barg2 barg3"

    ret1 = str_token(command_line1)
    ret2 = str_token(command_line2)

    while ret1 and ret2:
        print("cmdline1", ret1)
        ret1 = str_token()

        print("cmdline2", ret2)
        ret2 = str_token()
    print()

test1()
# output is following.
#
# cmdline hello.exe
# cmdline harg1
# cmdline harg2
# cmdline harg3


test2() # why test2 is not good? how to fix it?
# output is following.
#
# cmdline1 hello.exe
# cmdline2 byebye.exe
# cmdline1 barg1  <-- what?
# cmdline2 barg2

