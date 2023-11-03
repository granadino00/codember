from requests import get

URL = "https://codember.dev/data/message_01.txt"

def to_array(data):
    return data.strip().replace('\n', '').split(' ')

def count_words(data):
    dict_counted_words = {}

    for animal in data:
        try:            
            dict_counted_words[animal] += 1
        except KeyError:
            dict_counted_words[animal] = 1

    counted_words_str = "".join([f'{key}{value}' for key, value in dict_counted_words.items()])

    return counted_words_str
    

def main():
    data = get(URL).text
    print(count_words(to_array(data)))

if __name__ == '__main__':
    main()