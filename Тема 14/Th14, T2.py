# =============================================================================
# Write a decorator that takes a list of stop words and replaces them with * inside 
# the decorated function
# 
# ```
# 
# def stop_words(words: list):
# 
#     pass
# 
#  
# 
# @stop_words(['pepsi', 'BMW'])
# 
# def create_slogan(name: str) -> str:
# 
#     return f"{name} drinks pepsi in his brand new BMW!"
# 
#  
# 
# assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
# 
# ```
# =============================================================================

list_stop_words = ['pepsi', 'BMW'] 

def stop_words(func, list_stop_words=list_stop_words):
    def wrap(sentence):
        list_of_words = sentence.split()
        new_list_of_words = []
        for word in list_of_words:
            if word in list_stop_words or word[:-1] in list_stop_words:
                new_list_of_words.append('*')
                continue
            new_list_of_words.append(word)
        new_sentence = ' '.join(new_list_of_words)
        return func(new_sentence)
    return wrap       

@stop_words
def create_slogan(sentence):
    return sentence


if __name__ == '__main__':
    print(create_slogan('Steve drinks pepsi, in his brand new BMW!'))
    