import hashlib

valeurHach = input("Entrez la valeur à hacher : ")

# MD5 hash
hashObject1 = hashlib.md5()
hashObject1.update(valeurHach.encode())
print("MD5 hash:", hashObject1.hexdigest())

# SHA1 hash
hashObject2 = hashlib.sha1()
hashObject2.update(valeurHach.encode())
print("SHA1 hash:", hashObject2.hexdigest())

# SHA224 hash
hashObject3 = hashlib.sha224()
hashObject3.update(valeurHach.encode())
print("SHA224 hash:", hashObject3.hexdigest())

# SHA256 hash
hashObject4 = hashlib.sha256()
hashObject4.update(valeurHach.encode())
print("SHA256 hash:", hashObject4.hexdigest())

# SHA512 hash
hashObject5 = hashlib.sha512()
hashObject5.update(valeurHach.encode())
print("SHA512 hash:", hashObject5.hexdigest())

