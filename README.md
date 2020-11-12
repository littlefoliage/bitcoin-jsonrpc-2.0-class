# bitcoin-jsonrpc-2.0-class
A python wrapper class to call Bitcoin RPC server supporting batch requests

sample code:

serverURL='http://usr:pw@host:port'
host = RPCHost(serverURL)
    
blk_hash=host.call(['getblockhash','getblockhash'],[[1],[2]])
print(blk_hash)


another_test=host.call(['getblock','getblock'],[['0000000000000000000215b6528c759b26f205ab5998add132979962833d1130',1],
                                       ['000000000000000000011969bf02397097a07ab4da4f773c77ca69fb777f7852',1]])         
print(another_test)


#returns hash for the block in 'result'
[{'result': '00000000839a8e6886ab5951d76f411475428afc90947ee320161bbf18eb6048', 'error': None, 'id': None}, 
{'result': '000000006a625f06636b8bb6ac7b960a8d03705d1ace08b1a19da3fdcc99ddbd', 'error': None, 'id': None}]


[{'result': {'hash': '0000000000000000000215b6528c759b26f205ab5998add132979962833d1130', 'confirmations': 8, 'strippedsize': 913485, 'size': 1252906, 'weight': 3993361, 'height': 656652, 'version': 541065216, [omitting some output]},
{'result': {'hash': '000000000000000000011969bf02397097a07ab4da4f773c77ca69fb777f7852', 'confirmations': 6, 'strippedsize': 796005, 'size': 1605182, 'weight': 3993197, 'height': 656654, 'version': 536870912, 'versionHex': '20000000', 
[omitting some output]}]
