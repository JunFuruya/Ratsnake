#-*- UTF-8 -*-

import base64
import hashlib
import hmac
import time
import urllib.parse

from app.infrastructure.base_api import BaseApi

'''
IDCF Cloud Api module
'''
class IdcfCloudApi(BaseApi):
    '''
    manage idcf cloud
    '''
    __api_key = ''
    __endpoint = ''
    __secret_key = ''
    # TODO: erase this variable after implementing choosing vm feature
    __vm_id = ''
    
    def __init__(self, idcf_config):
        super().__init__(idcf_config)
        
        # TODO: erase this variable after implementing choosing vm feature
        self.__api_key, self.__endpoint, self.__secret_key, self.__vm_id = idcf_config.get_config()
        
        import pprint
        pprint.pprint(self.__endpoint)
        #クラウドIDを検索する
        #getCloudIdentifier
        #GET /client/api?command=getCloudIdentifier{?userid}

        #Response parameters
        #cloudidentifier: The cloud identifier
        #signature :The signed response for the cloud identifier
        #userid: The user ID for the cloud identifier
        pass

    def __get_query_parameters(self, params):
        # create a query string
        #query_string = '?'
        i = 1
        for key_value_pair in params:
            key, value = key_value_pair
            query_string += key + '=' + value
            
            if i < len(params):
                query_string += '&'
        return query_string
    
    def __get_signature(self, params):
        # sort tuples in alphabetical order
        sorted(params)
        # lowercase the query string, replace '+' for '%20'
        query_string = urllib.parse.urlencode(params).lower().replace('+', '%20')
        import pprint
        pprint.pprint(query_string)
        # create a hash stirng
        message_digest = hmac.new(bytes(self.__secret_key, 'ascii'), bytes(query_string, 'ascii'), hashlib.sha256).hexdigest()
        # Base64 encode and URL encode
        return urllib.parse.quote(base64.b64encode(message_digest.encode('utf-8')))
    
    def get_virtual_machine_list(self):
        params = {
            'command': 'listVirtualMachines',
            'account': '',
            'affinitygroupid': '',
            'details': '',
            'displayvm': '',
            'domainid': '',
            'forvirtualnetwork': '',
            'groupid': '',
            'hostid': '',
            'hypervisor': '',
            'id': '',
            'ids': '',
            'isoid': '',
            'isrecursive': '',
            'keypair': '',
            'keyword': '',
            'listall': '',
            'name': '',
            'networkid': '',
            'page': '',
            'pagesize': '',
            'podid': '',
            'projectid': '',
            'serviceofferingid': '',
            'state': '',
            'storageid': '',
            'tags': '',
            'templateid': '',
            'userid': '',
            'vpcid': '',
            'zoneid': '',
            'apikey': self.__api_key
        }
        params.update({'signature' : self.__get_signature(params)})
        expiration = int(time.time()) + 30
        super().get(self.__endpoint + '?' + urllib.parse.urlencode(params))
        pass
    
    def start_virtual_machine(self):
        #TODO: should be able to choose a spescific vm
        id = self.__vm_id

        params = {
            'command': 'startVirtualMachine',
            'id': id, #TODO: should be able to choose a spescific vm
            'deploymentplanner': '',
            'hostid': '',
            'apikey': self.__api_key,
        }

        params.update({'signature' : self.__get_signature(params)})
        import pprint
        pprint.pprint(params)
        super().get(self.__endpoint + '?' + urllib.parse.urlencode(params))
        pass
    
    def stop_virtual_machine(self):
        #TODO: should be able to choose a spescific vm
        id = self.__vm_id
        params = {
            'command': 'stopVirtualMachine',
            'id': id,
            'forced': '',
            'apikey': self.__api_key,
        }
        params.update({'apikey': self.__api_key, 'signature' : self.__get_signature(params)})
        super().get(self.__endpoint + self.__get_query_parameters(params))
        pass
