from ghidra.program.model.listing import CodeUnit
from ghidra.program.model.symbol import SourceType

# currentAddress is ghidra.program.model.address.GenericAddress
# currentAddress には、Listing で選択している行のアドレスが自動的に参照される
# そのため、事前にターゲットになる関数のアドレスを選択しておく
program = getCurrentProgram()
fm = program.getFunctionManager()
function = fm.getFunctionAt(currentAddress)

# 関数内の呼び出しアドレスを列挙する(呼び出し順ではない)
calls = function.getCalledFunctions(monitor)
for c in calls:
    print(c)

# 関数内の Call 命令を順に列挙することで呼び出し順序を維持して出力する
for i in program.listing.getInstructions(function.body, True):
    print(i)
