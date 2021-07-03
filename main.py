import hashlib

print("enter your text:")
x=input()
hash_object=hashlib.md5(x.encode())
md5_hash=hash_object.hexdigest()
print(md5_hash)