from blowfish import Blowfish

if __name__ == '__main__':
    if not Blowfish.testVectors():
        print "WARNING: The implementation doesn't pass algorithm test vectors!"
    else:
        print "The implementation passes algorithm test vectors (ECB)."



    key = open("key.txt","r").read()
    cipher = Blowfish(key)

    # print "Testing block encrypt:"
    # text = 'testtest'
    # print "\tText:\t\t%s" % text
    # crypted = cipher.encrypt(text)
    # print "\tEncrypted:\t%s" % repr(crypted)
    # decrypted = cipher.decrypt(crypted)
    # print "\tDecrypted:\t%s" % decrypted

    print "Testing CTR encrypt:"
    cipher.initCTR()
    text = str(open("input.txt", "r").read())
    print "\tText:\t\t", text
    crypted = cipher.encryptCTR(text)
    print "\tEncrypted:\t", repr(crypted)
    cipher.initCTR()
    decrypted = cipher.decryptCTR(crypted)
    print "\tDecrypted:\t", decrypted