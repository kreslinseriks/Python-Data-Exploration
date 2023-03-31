import string

# Function to count letter frequency
def count_letters(filename):
    # Create an empty dictionary to store letter frequencies
    letter_freq = {}

    # Open the file and read its contents
    with open(filename, 'r') as f:
        text = f.read()

    # Remove all non-letter characters and convert to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation + string.digits + '\n'))
    text = text.lower()

    # Loop through each character in the text and update the dictionary
    for char in text:
        if char.isalpha():
            if char in letter_freq:
                letter_freq[char] += 1
            else:
                letter_freq[char] = 1

    # Sort the dictionary by frequency in decreasing order
    sorted_letter_freq = sorted(letter_freq.items(), key=lambda x: x[1], reverse=True)

    return sorted_letter_freq


# Get the filenames from the user
filename1 = input("Enter a file name: ")
filename2 = input("Enter a file name: ")

# Count the letter frequencies for both files
freq1 = count_letters(filename1)
freq2 = count_letters(filename2)

# Print the frequencies for both files side by side
print("{:<10s}{:<10s}{:<10s}{:<10s}".format("Letter", "Freq1", "Letter", "Freq2"))
print("-" * 40)

for i in range(max(len(freq1), len(freq2))):
    if i < len(freq1):
        letter1, freq1_count = freq1[i]
        freq1_percent = freq1_count / sum([freq for _, freq in freq1]) * 100
        freq1_percent = "{:.1f}%".format(freq1_percent)
    else:
        letter1, freq1_count, freq1_percent = "", "", ""

    if i < len(freq2):
        letter2, freq2_count = freq2[i]
        freq2_percent = freq2_count / sum([freq for _, freq in freq2]) * 100
        freq2_percent = "{:.1f}%".format(freq2_percent)
    else:
        letter2, freq2_count, freq2_percent = "", "", ""

    print("{:<10s}{:<10d}{:<10s}{:<10d}".format(letter1, freq1_count, letter2, freq2_count))
    print("{:<10s}{:<10s}{:<10s}{:<10s}".format("", freq1_percent, "", freq2_percent))
    print()
