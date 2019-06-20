# diffe hellman key exchange
# public domain
g = 5
n = 3

# protected data

class Alice():

    def __init__(self):
        global g
        global n
        self.privatekey = 2
        self.

    def show_public_key(self):
        print(self.publickey)

    def get_shared_secret(self, bob_publickey):
        

class Bob():

    def __init__(self):
        global g
        global n
        self.privatekey = 7
        self.publickey = (g^self.privatekey)%n

    def show_public_key(self):
        print(self.publickey)


"""
al = Alice()
al.show_public_key()
bob = Bob()
bob.show_public_key()
"""
