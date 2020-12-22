import string
import nltk
nltk.download('words')
original_words = nltk.corpus.words.words()
word_list = [word.lower() for word in original_words]
result = list(string.ascii_lowercase) 
print(result)
# print(word_list) 





def encrypt(words, key):
    encrypt_result = ''
    for char in words.lower():
        if char in result:
            encrypted_let = result[result.index(words.lower) + key % len (result)]
            encrypt_result += encrypted_let
        else:
            encrypt_result += char
    return  encrypt_result



# def decrypt(words, key):
#     return encrypt(words, -1*key)