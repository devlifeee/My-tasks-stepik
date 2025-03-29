a = "abcd"
key = "*d%#"
text_to_encrypt = input()
text_to_decrypt = input()

translation_table = str.maketrans(a, key)
encrypted_text = text_to_encrypt.translate(translation_table)
decrypted_text = text_to_decrypt.translate((str.maketrans(key, a)))
print(encrypted_text)
print(decrypted_text)

###############################################################################
#alphabet = input()                                                           #
#key = input()                                                                #
#text_to_encrypt = input()                                                    #
#text_to_decrypt = input()                                                    #
#                                                                             #
#translation_table = str.maketrans(alphabet, key)                             #
#encrypted_text = text_to_encrypt.translate(translation_table)                #
#decrypted_text = text_to_decrypt.translate(str.maketrans(key, alphabet))     #
#                                                                             #
#print(encrypted_text)                                                        #
#print(decrypted_text)                                                        #
###############################################################################