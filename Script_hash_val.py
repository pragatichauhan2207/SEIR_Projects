import re,requests,sys
from bs4 import BeautifulSoup


# Calculating hash value using rolling_hashFn for a word
def rolling_hash_fn(word):
    p = 53
    m = 2**64
    hash_val = 0
    power = 1

    for i in range(len(word)):
        hash_val += ord(word[i])* power
        power *= p

    return hash_val % m


# COmputing Simhash of body Text
def Simhash(body):

    bit = 64

    words = re.findall(r'[a-zA-Z0-9]+', body.lower())

    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] +=1
        else:
            word_count[word] = 1
        
    # Testing dict

    # count = 10
    # for key in word_count:
    #     print(key,":",word_count[key])
    #     count += 1
    #     if count==10:
    #         break


     # Create a vector of 64 zeros
    
    vector_bit =[0] * bit
    for word in word_count:
        freq = word_count[word]
        hash_val = rolling_hash_fn(word)

        for i in range(bit):
            i_bit = (hash_val >> i) & 1
            if i_bit == 1:
                vector_bit[i] += freq
            else:
                vector_bit[i] -= freq

# Converting vector into final simhash
    simhash = 0
    for i in range(bit):
        if vector_bit[i] >= 0:
            simhash |= (1 << i)

    return simhash


#calculating number of common bits between two hashes
def bits_common(hash1, hash2, total_bits):

    xor = hash1 ^ hash2
    count = 0

    for i in range(total_bits):
        curr_bit = (xor >> i) & 1
        if curr_bit == 1:
            count += 1

    common_bits = total_bits - count
    return common_bits
    
#Extracting body text from URL
def extract_body(url):

    try:
        get_response = requests.get(url)
    except:
        print("Error fetching URL:", url)
        return None

    soup = BeautifulSoup(get_response.text, "html.parser")

    if soup.body:
        body = soup.body.get_text(separator="\n")
        return body
    else:
        print("This page contains no body tag")
        return None
    


def main():
    bits = 64


    arg_len = len(sys.argv)

    if arg_len != 3:
        print("Kindly recheck your input")
        sys.exit(1)

    url1 = sys.argv[1]
    url2 = sys.argv[2]

    body1 = extract_body(url1)
    if body1 is None:
        sys.exit(1)

    body2 = extract_body(url2)
    if body2 is None:
        sys.exit(1)

    hash1 = Simhash(body1)
    hash2 = Simhash(body2)

    print("Simhash of URL1:", hash1)
    print("Simhash of URL2:", hash2)

    common= bits_common(hash1, hash2, bits)

    print("Common bits:", common)
    print("Similarity percentage:", (common/bits)*100)



if __name__ == "__main__":
    main()
