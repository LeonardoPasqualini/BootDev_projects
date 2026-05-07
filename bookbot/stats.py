def get_num_words(text):
    return len(text.split())

def get_num_char(text):
    words = text.split()
    count_dict = {}
    for word in words:
        for char in word:
            lower_char = char.lower()
            if lower_char in count_dict:
                count_dict[lower_char] += 1
            else:
                count_dict[lower_char] = 1
    return count_dict

def sort_on(items):
    return items["num"]

def get_report(char_dict):
    report_list = []
    
    for key in char_dict:
        report_list.append({"char": key, "num": char_dict[key]})
        
    report_list.sort(reverse=True, key=sort_on)
    
    return report_list