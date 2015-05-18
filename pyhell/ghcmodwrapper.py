from subprocess import check_output

def browse(module):
    out = check_output(["ghc-mod", "browse", "-d", module], universal_newlines=True)
    return [sig.split(" :: ")[0] for sig in out.splitlines()]

def modules():
    print("listing modules")
    out = check_output(["ghc-mod", "modules"], universal_newlines=True)
    return out.splitlines()