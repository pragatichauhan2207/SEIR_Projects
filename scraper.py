from bs4 import BeautifulSoup
import requests 
import sys 
import re



def main():
    arg_len = len(sys.argv)
    if (arg_len != 2):
        print("Kindly Enter the url first")
        sys.exit(1)
        
# Taking URL from command line
    url = sys.argv[1].strip()
    print("Your entered url is: " ,url)


    # get_response = requests.get(url)
    # print(get_response.text)

 # fetching the webpage
    try:
        get_response = requests.get(url)
    except:
        print("Error in fetching this URL:", url)
        return None
    

    soup = BeautifulSoup(get_response.text,"html.parser")

    
    if(soup.title and soup.title.text):
        titles = soup.title.text
        print("Titles are:")
        print(titles)
    else:
        print("This page contains no title")
    print("\n")
    

    if soup.body:
        body = soup.body.get_text(separator="\n")
        print("Body_text Page is : ")
        print(body)
    else:
        print("This page contains no body tag")



    print("\n")

# Storing unique links using set
    links_set =set()
    links = soup.find_all("a")      #BeautifulSoup tag object
    for link in links:
        href = link.get("href")
        if href is not None:
            links_set.add(href)

# Printing all links
    
    print("Set of unique links is:")
    # Print all the links
    for link in links_set:
        print(link)



    


if __name__ == "__main__":
    main()
