from ghidra.app.decompiler import DecompInterface, PrettyPrinter
from ghidra.util.task import ConsoleTaskMonitor

decomp = DecompInterface()
decomp.openProgram(currentProgram)

# currentAddress には、Listing で選択している行のアドレスが自動的に参照される
# そのため、事前にターゲットになる関数のアドレスを選択しておく
fn = getFunctionContaining(currentAddress)
decomp_results = decomp.decompileFunction(fn, 30, monitor)

if decomp_results.decompileCompleted():
    pp = PrettyPrinter(fn, decomp_results.getCCodeMarkup())
    code = pp.print(False).getC()
    print(code)
else:
    print("There was an error in decompilation!")
