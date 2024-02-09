def word_frequency(text):
    
    words = text.split()
    word_freq = {}
    for word in words:
        word = word.lower()  
        word = word.strip('.,!?;:"')
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    
    sorted_word_freq = sorted(word_freq.items())

    return sorted_word_freq


if __name__ == "__main__":
    input_text = input("Enter your text: ")
    sorted_word_freq = word_frequency(input_text)
   
    for word, freq in sorted_word_freq:
        print(f"{word}, {freq}")




        d=dict()
s=input("enter the string:")
for i in s.split():
    d[i]=d.get(i,0)+1
print(sorted(d.items()))