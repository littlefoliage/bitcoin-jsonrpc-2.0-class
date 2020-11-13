# bitcoin-jsonrpc-2.0-class
A python wrapper class to call Bitcoin RPC server supporting batch requests

Forked from https://kryptomusing.wordpress.com/2017/06/12/bitcoin-rpc-via-python/

Original class RPCHost is preserved.
New class RPCHost_batch is created for batch requests.
sample code:


if __name__=='__main__':
    serverURL='http://usr:pw@host:port'
    host = RPCHost(serverURL)
    host_batch= RPCHost_batch(serverURL)
    
    print(host.call('getblockhash',1))                  #00000000839a8e6886ab5951d76f411475428afc90947ee320161bbf18eb6048
    #print(host.call('getblockhash',10000000))          #this will fail
    print(host.call('getblockcount'))                   #656687
    
    print(host_batch.call(['getblockhash',
                           'getblockhash',
                           'getblockcount'] ,
                          [[1],
                           [10000000],
                           []]))
                           
                           
    ######################################
    result:


[{'request': 'getblockhash', 'params': [1], 'result': '00000000839a8e6886ab5951d76f411475428afc90947ee320161bbf18eb6048', 'error': None}, 
{'request': 'getblockhash', 'params': [10000000], 'result': None, 'error': {'code': -8, 'message': 'Block height out of range'}}, 
{'request': 'getblockcount', 'params': [], 'result': 656687, 'error': None}]
