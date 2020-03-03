
# Given a valid (IPv4) IP address, return a defanged version of that IP address.

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')
        
        # if built in string function is not allowed
        #
        # defang = ''
        # for i in address:
        #     if i == '.':
        #         i = '[.]'
        #     defang += i
        # return defang