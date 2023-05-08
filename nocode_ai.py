import string
import streamlit as st

#convert text to lowercase
def to_lowercase(text):
    return text.lower()

#convert text to uppercase
def to_uppercase(text):
    return text.upper()

#renmoval of stopwords
def remove_stopwords(text):
        stopwords_list = set(['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"])
        words = text.split()
        filtered_words = [word for word in words if word.lower() not in stopwords_list]
        text = " ".join(filtered_words)
        return text

#removal of emojis
def remove_emojis(text):
    emoji_ranges =[range(0x1F600, 0x1F64F),  # emoticons 
                    range(0x1F300, 0x1F5FF),  # symbols & pictographs
                    range(0x1F680, 0x1F6FF),  # transport & map symbols
                    range(0x2600, 0x26FF),    # miscellaneous symbols
                    range(0x2700, 0x27BF),    # dingbats
                    range(0xFE00, 0xFE0F),    # variation selectors
                    range(0x1F900, 0x1F9FF),  # supplemental symbols and pictographs
                    range(0x1F1E6, 0x1F1FF),  # flags (iOS)
                    range(0x1F918, 0x1F918),  # sign of the horns
                    range(0x1F911, 0x1F917),  # hand gestures
                    range(0x1F600, 0x1F64F),  # emoticons
                    range(0x1F680, 0x1F6FF),  # transport & map symbols
                    range(0x1F300, 0x1F5FF),  # symbols & pictographs
                    range(0x1F4F0, 0x1F4FF),  # office and communication symbols
                    range(0x1F195, 0x1F19A),  # new and popular symbols
                    range(0x1F918, 0x1F91F),  # hand signs
                    range(0x1F920, 0x1F927),  # people and body parts
                    range(0x1F300, 0x1F5FF),  # symbols & pictographs
                    range(0x1F3FB, 0x1F3FF)]  # skin tone modifiers
    
    cleaned_text = ""
    for char in text:
        if not any(ord(char) in emoji_range_chars for emoji_range_chars in emoji_ranges):
            cleaned_text += char
    
    return cleaned_text

#removal of special characters
def remove_special_chars(text):
    """Remove special characters from text"""
    special_chars = "!@#$%^&*()_-+={}[]|\:;\"'<>,.?/~`"
    result = ""
    for char in text:
        if char not in special_chars:
            result += char
    return result 

#removal of numbers
def remove_numbers(text):
    """Remove numbers from text"""
    result = ""
    for char in text:
        if not char.isnumeric():
            result += char
    return result  

#removal of urls
def remove_urls(text):
    cleaned_text = text.split(" ")
    cleaned_text = [word for word in cleaned_text if not word.startswith("http://") and not word.startswith("https://")]
    cleaned_text = " ".join(cleaned_text)
    return cleaned_text

#removal of html tags
def remove_html_tags(text):
        # Split text into words
        words = text.split(" ")

        # Loop through each word and remove any tags
        cleaned_words = []
        in_tag = False
        for word in words:
            if "<" in word:
                in_tag = True
            if ">" in word:
                in_tag = False
                continue
            if not in_tag:
                cleaned_words.append(word)

        # Join the cleaned words back into a string
        cleaned_text = " ".join(cleaned_words)
        return cleaned_text
    

#removal of whitespaces
def remove_whitespaces(text):
        whitespaces_text = text.strip()
        return whitespaces_text 
    

# import numpy as np

# def num2words(num):
#     """
#     Convert a number to its word representation.
#     """
#     # Define word representations for numbers up to 20
#     ones = np.array(['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'])
    
#     # Define word representations for tens
#     tens = np.array(['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'])
    
#     # Define word representations for powers of 10
#     powers_of_10 = np.array(['', 'thousand', 'million', 'billion', 'trillion'])
    
#     # Convert the number to a string
#     num_str = str(num)
    
#     # Pad the number with zeros if necessary
#     if len(num_str) % 3 != 0:
#         num_str = '0'*(3 - len(num_str) % 3) + num_str
    
#     # Break the number into groups of three digits
#     groups = np.array([int(num_str[i:i+3]) for i in range(0, len(num_str), 3)])
    
#     # Initialize an empty string to hold the word representation
#     words = ''
    
#     # Loop over the groups of digits
#     for i in range(len(groups)):
#         # Get the current group of digits
#         group = groups[i]
        
#         # Get the hundreds digit
#         hundreds_digit = group // 100
        
#         # Get the tens and ones digits
#         tens_ones_digits = group % 100
        
#         # Convert the hundreds digit to a word, if it is not zero
#         if hundreds_digit != 0:
#             words += ones[hundreds_digit] + ' hundred '
        
#         # Convert the tens and ones digits to a word
#         if tens_ones_digits < 20:
#             words += ones[tens_ones_digits]
#         else:
#             tens_digit = tens[tens_ones_digits // 10]
#             ones_digit = ones[tens_ones_digits % 10]
#             words += tens_digit + ' ' + ones_digit
        
#         # Add the word representation of the power of 10 to the end of the word, if necessary
#         if group != 0:
#             words += ' ' + powers_of_10[len(groups) - i - 1]
    
#     # Return the word representation
#     return words.strip()

# def named_entity_recognition(text):
#     entities = []
#     words = text.split()

#     for i in range(len(words)):
#         if words[i][0].isupper():
#             entity = words[i]
#             for j in range(i+1, len(words)):
#                 if words[j][0].isupper():
#                     entity += " " + words[j]
#                 else:
#                     break
#             entities.append(entity)

#     return entities


#stemming    
def stem_text(text):
    stemmed_text = " "
    for word in text.split():
        for prefix in ["un", "in", "dis", "re", "pre", "post", "ex", "inter", "co", "trans", "sub", "super", "auto", "anti", "bi", "de", "en", "fore", "mid", "over", "out", "under", "up", "mini", "multi", "non", "poly", "pseudo", "retro", "semi", "tele", "tri", "ultra", "uni", "micro", "macro", "mega", "meta", "nano", "neo", "pan", "para", "proto", "syn", "thermo", "hepta", "octo", "penta", "hex", "hexa", "deca", "centi", "kilo", "milli", "pico"]:
            if word.startswith(prefix):
                stemmed_text = stemmed_text + word[len(prefix):]+" "
                break
        else:
            for suffix in ["s", "es", "ed", "ing"]:
                if word.endswith(suffix):
                    stemmed_text = stemmed_text + word[:-len(suffix)] + " "
                    break
            else:
                stemmed_text = stemmed_text + word + " "
    return stemmed_text


#tokenization
def tokenize(text):
    """
    A simple tokenizer that splits a sentence into words based on whitespace.
    """
    words = text.split()
    return words
    
    
def preprocess_text(text, techniques):
    if 'to_lowercase' in techniques:
        text = to_lowercase(text)
    if 'to_uppercase' in techniques:
        text = to_uppercase(text)
    if 'remove_stopwords' in techniques:
        text = remove_stopwords(text)
    if 'remove_emojis' in techniques:
        text = remove_emojis(text)
    if 'remove_special_chars' in techniques:
        text = remove_special_chars(text)
    if 'remove_numbers' in techniques:
        text = remove_numbers(text)
    if 'remove_urls' in techniques:
        text = remove_urls(text)
    if 'remove_html_tags' in techniques:
        text = remove_html_tags(text)
    if 'remove_whitespace' in techniques:
        text = remove_whitespace(text)
#     if 'num2words' in techniques:
#         text = num2words(text)
#     if 'named_entity_recognition' in techniques:
#         text = named_entity_recognition(text)
    if 'stem_text' in techniques:
        text = stem_text(text)
    if 'tokenize' in techniques:
        text = tokenize(text)
    return text

st.title("Barathsmart NO-CODE AI!")
st.header("Text Preprocessing App")
text = st.text_area("Enter some text to preprocess:")
st.sidebar.title("Select techniques to apply")

preprocess_all = st.sidebar.checkbox("Preprocess all techniques")

to_lowercase_checkbox = st.sidebar.checkbox("Convert to lowercase")
to_uppercase_checkbox = st.sidebar.checkbox("Convert to uppercase")
remove_stopwords_checkbox = st.sidebar.checkbox("Remove stopwords")
remove_emojis_checkbox = st.sidebar.checkbox("Remove emojis")
remove_special_chars_checkbox = st.sidebar.checkbox("Remove_special chars")
remove_numbers_checkbox = st.sidebar.checkbox("Remove numbers")
remove_urls_checkbox = st.sidebar.checkbox("remove_urls")
remove_html_tags_checkbox = st.sidebar.checkbox("remove_html_tags")
remove_extra_whitespace_checkbox = st.sidebar.checkbox("Remove extra whitespace")
# remove_num2words_checkbox = st.sidebar.checkbox("num2words")
# named_entity_recognition_checkbox = st.sidebar.checkbox("named_entity_recognition")
stem_text_checkbox = st.sidebar.checkbox("stem_text")
tokenize_checkbox = st.sidebar.checkbox("tokenize")



techniques = []
if preprocess_all:
    techniques = [ 'to_lowercase','to_uppercase',
                  'remove_stopwords','remove_emojis','remove_special_chars', 'remove_numbers','remove_urls','remove_html_tags', 'remove_extra_whitespace','stem_text','tokenize']
else:
    if to_lowercase_checkbox:
        techniques.append('to_lowercase')
    if to_uppercase_checkbox:
        techniques.append('to_uppercase')   
    if remove_stopwords_checkbox:
        techniques.append('remove_stopwords')
    if remove_emojis_checkbox:
        techniques.append('remove_emojis')
    if remove_special_chars:
        techniques.append('remove_special_chars')
    if remove_numbers_checkbox:
        techniques.append('remove_numbers')
    if remove_urls_checkbox:
        techniques.append('remove_urls')
    if remove_html_tags_checkbox:
        techniques.append('remove_html_tags')
    if remove_extra_whitespace_checkbox:
        techniques.append('remove_extra_whitespace')
#     if remove_num2words_checkbox:
#         techniques.append('num2words')
#     if named_entity_recognition_checkbox:
#         techniques.append('named_entity_recognition')
    if stem_text_checkbox:
        techniques.append('stem_text')
    if tokenize_checkbox:
        techniques.append('tokenize')
   
        
# def browse_files(): 
#     file_path = st.file_uploader("Upload a file", type=["txt", "csv", "xlsx"])
#     if file_path is not None:
#         st.success("File uploaded!")
#         return file_path

# file_path = browse_files()
# if file_path:
#     st.write("You selected:", file_path)
    
if st.button("Preprocess"):
    if text:
        preprocessed_text = preprocess_text(text, techniques)
        st.write(preprocessed_text)
    else:
        st.warning("Please enter some text to preprocess.")       