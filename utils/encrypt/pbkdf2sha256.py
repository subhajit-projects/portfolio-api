from passlib.hash import pbkdf2_sha256

class pbkdf2sha256:
    def encrypt(self, raw_password):
        encrypted = None

        if raw_password != None and raw_password != "" :
            encrypted = pbkdf2_sha256.hash(raw_password).split("$pbkdf2-sha256")[1]

        return encrypted
    
    def verify(self, raw_password, hash_password):
        matched = False
        if raw_password != None and raw_password != "" and hash_password != None and hash_password != "" :
            matched = pbkdf2_sha256.verify(raw_password, "$pbkdf2-sha256"+hash_password)
        
        return matched