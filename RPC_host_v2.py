import requests,json
class RPCHost(object):
    def __init__(self, url):
        self._session = requests.Session()
        self._url = url
        self._headers = {'content-type': 'application/json'}
    def call(self, rpcMethod, *params):
        payload = json.dumps({"method": rpcMethod, "params": list(params), "jsonrpc": "2.0"})
        tries = 5
        hadConnectionFailures = False
        while True:
            try:
                response = self._session.post(self._url, headers=self._headers, data=payload)
            except requests.exceptions.ConnectionError:
                tries -= 1
                if tries == 0:
                    raise Exception('Failed to connect for remote procedure call.')
                hadFailedConnections = True
                print("Couldn't connect for remote procedure call, will sleep for five seconds and then try again ({} more tries)".format(tries))
                time.sleep(10)
            else:
                if hadConnectionFailures:
                    print('Connected for remote procedure call after retry.')
                break
        if not response.status_code in (200, 500):
            raise Exception('RPC connection failure: ' + str(response.status_code) + ' ' + response.reason)
        responseJSON = response.json()
        if 'error' in responseJSON and responseJSON['error'] != None:
            raise Exception('Error in RPC call: ' + str(responseJSON['error']))
        return responseJSON['result']

class RPCHost_batch(object):
    def __init__(self, url):
        self._session = requests.Session()
        self._url = url
        self._headers = {'content-type': 'application/json'}
    def call(self, rpcMethod, tags, params):
        payload=None        
        BATCH_SIZE=3000
        returnJSON=[]
        request_list=[]
        result_list=[]
        
        if len(rpcMethod) != len(params) or len(rpcMethod) !=  len(tags):
            raise Exception('different length of method,tags and params')
        else:
            
            input_len=len(rpcMethod)
    
            request_list=[]
            
            batch_request_list=[]
            
            
            for i in range(0,input_len):
                batch_request_list.append({'request':{"method": rpcMethod[i], "params": list(params[i]), "jsonrpc": "2.0"},
                                           'tag':tags[i]
                                           }
                                           )
                if (i!=0 and i%BATCH_SIZE==0) or i == input_len-1:
                    request_list.append([batch_request_list])
                    batch_request_list=[]
            for each_batch in request_list:
                raw_request=[]
                for each_request in each_batch[0]:
                    raw_request.append(each_request['request'])
                                     
                payload = json.dumps(raw_request)
                
                response = self._session.post(self._url, headers=self._headers, data=payload)
                
                if not response.status_code in (200, 500):
                    raise Exception('RPC connection failure: ' + str(response.status_code) + ' ' + response.reason)                
                responseJSON = response.json()
                
                for  i in range(0,len(each_batch[0])):
                    returnJSON.append({ 'request': each_batch[0][i]['request'],
                                        'tag':each_batch[0][i]['tag'],
                                        'result':responseJSON[i]['result'],
                                        'error':responseJSON[i]['error']})                
        return returnJSON 
