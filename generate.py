import rsa

public_key, private_key = rsa.newkeys(1024)

print(private_key)


with open('public.pem', 'wb') as f:
    f.write(public_key.save_pkcs1('PEM'))

with open('private.pem', 'wb') as f:
    f.write(private_key.save_pkcs1('PEM'))