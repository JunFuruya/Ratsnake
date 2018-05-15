# -*- coding: utf-8 -*-

import base64
import hashlib
import hmac
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
    
    def __init__(self, idcf_config):
        super().__init__(idcf_config)
        
        self.__api_key, self.__endpoint, self.__secret_key = super().get_config()
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
        query_string = '?'
        i = 1
        for key_value_pair in params:
            key, value = key_value_pair
            query_string += key + '=' + value
            
            if i < len(params):
                query_string += '&'
        return query_string
    
    def __get_signature(self, params):
        # sort tuples in alphabetical order
        sorted(params, key=itemgetter(0))
        
        query_string = self.__get_query_parameters(params)
        # lowercase the query string
        query_string.lower()
        # replace '+' for '%20'
        query_string.replace('+', '%20')        
        # create a hash stirng
        message_digest = hmac.new(self.__secret_key, query_string, hashlib.sha1).hexdigest()
        # Base64 encode and URL encode
        return b64encode(urlencode(message_digest))
    
    def get_virtual_machine_list(self):
        params = [
            ('command', 'listVirtualMachines'),
            ('account', ''),
            ('affinitygroupid', ''),
            ('details', ''),
            ('displayvm', ''),
            ('domainid', ''),
            ('forvirtualnetwork', ''),
            ('groupid', ''),
            ('hostid', ''),
            ('hypervisor', ''),
            ('id', ''),
            ('ids', ''),
            ('isoid', ''),
            ('isrecursive', ''),
            ('keypair', ''),
            ('keyword', ''),
            ('listall', ''),
            ('name', ''),
            ('networkid', ''),
            ('page', ''),
            ('pagesize', ''),
            ('podid', ''),
            ('projectid', ''),
            ('serviceofferingid', ''),
            ('state', ''),
            ('storageid', ''),
            ('tags', ''),
            ('templateid', ''),
            ('userid', ''),
            ('vpcid', ''),
            ('zoneid', '')
        ]
        params.append(('signature', self.__get_signature(params)))
        super().get(self.__endpoint + self.get_query_string(params))
        pass
    
    def start_virtual_machine(self):
        params = [
            ('command', 'startVirtualMachine'),
            ('id', ''),
            ('deploymentplanner', ''),
            ('hostid', '')
        ]

        params.append(('signature', self.__get_signature(params)))
        super().get(self.__endpoint + self.get_query_string(params))
        pass
    
    def stop_virtual_machine(self):
        params = [
            ('command', 'stopVirtualMachine'),
            ('id', ''),
            ('forced', '')
        ]
        params.append(('signature', self.__get_signature(params)))
        super().get(self.__endpoint + self.get_query_string(params))
        pass
