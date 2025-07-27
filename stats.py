def get_num_words(file_contents):
    words = file_contents.split()
    num_words = len(words)
    return num_words
    
def get_num_characters(file_contents):
    char_counts = {}
    for word in file_contents.split():
        for char in word:
            char = char.lower()
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
    return char_counts 

def sort_on(char_counts):
    return char_counts['num']

def get_sorted_list(char_counts):
    sorted_dict = []
    
    for k in char_counts:
        sorted_dict.append({"char" : k, "num" : char_counts[k]})
        
    sorted_dict.sort(reverse = True, key = sort_on)
    return sorted_dict
        