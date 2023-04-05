import rsa,os,sys

with open('public.pem', 'rb') as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())

with open('private.pem', 'rb') as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())

class encryptClass():
    def __init__(self,public_key):
        self.public_key = public_key
    
    def lock(self,message,file):
        e_msg = rsa.encrypt(message.encode(),self.public_key)
        ## ENCRYPTED RSA
        with open(f'{file}','wb') as f:
            f.write(e_msg)
            print(f'locked up to {os.path.basename(f.name)}')

class decryptClass():
    def __init__(self,private_key):
        self.private_key=private_key

    def unlock(self,file):
        e_msg = open(f'{file}','rb').read()
        ## CLEARTEXT MESSAGE
        return rsa.decrypt(e_msg,self.private_key)


if __name__ == '__main__':
    message = sys.argv[1]
    ec = encryptClass(public_key)
    ec.lock(message,'test1.message')

    dc = decryptClass(private_key)
    print(dc.unlock('test1.message'))