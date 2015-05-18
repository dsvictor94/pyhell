from subprocess import check_output, DEVNULL

def execute(hf):
    out = check_output(["ghc", "-e", hf.hs_code], stderr=DEVNULL)
    if out:
        return out.decode("utf-8")
    else:
        raise Exception("HaskellError")

def istype(hf, t):
    code = "({})::{}".format(hf.hs_code, t)
    out = check_output(["ghc", "-e", code], stderr=DEVNULL)
    return bool(out)