import nltk
#nltk.download('stopwords')

#prompt user to enter company's name
company = int(input("Get word count. Press \n0:JnT\n1:Pos Laju\n2:CityLink\n3:DHL\n"))
article = ["jnt", "poslaju", "citylink", "dhl"]

jnt = ["\n1. MCMC Issues Warning To J&T Express Over Video Showing Staff Mishandling Customers' Parcels",
       "2. J&T Express Experience Decline In Ordered Items Following Bad Publicity",
       "3. J&T Express anticipates promising 11.11 big sale"]

poslaju = ["\n1. PosLaju Recognized by Frost & Sullivan for Dominating the Delivery Service Market in Malaysia on the Strength of its Vast Channel Network",
           "2. Delivery by PosLaju needs to be improved",
           "3. MCO: Pos Malaysia says parcel volume rises but other businesses affected"]

citylink = ["\n1. CITY-LINK EXPRESS Maintains Its Fast & Reliable Service With Isuzu",
            "2. City-Link mulls Main Market listing in three years",
            "3. City-Link Express Aims For Fast Delivery And Customer Satisfaction With Isuzu"]

dhl = ["\n1. How DHL continues to make its people top priority through the most challenging times",
       "2. Digitalisation the way forward for DHL Express",
       "3. DHL Express Malaysia partners Aerodyne Group on drone delivery services"]

if company == 0:
    for i in range(0, len(jnt)):
        print(jnt[i])
    display = input("Please select title: ")
if company == 1:
    for i in range(0, len(poslaju)):
        print(poslaju[i])
    display = input("Please select title: ")
if company == 2:
    for i in range(0, len(citylink)):
        print(citylink[i])
    display = input("Please select title: ")
if company == 3:
    for i in range(0, len(dhl)):
        print(dhl[i])
    display = input("Please select title: ")

# Open the file in read mode
text = open("articles\\" + article[company] + "-article-%s.txt" % display, "r", encoding="utf8")

# Create an empty dictionary
d = dict()

# Initialize word count
wordcount = 0

# Loop through each line of the file
for line in text:
    # Remove the leading spaces and newline character
    line = line.strip()

    # Convert the characters in line to
    # lowercase to avoid case mismatch
    line = line.lower()

    # Split the line into words
    words = line.split(" ")

    # Iterate over each word in line
    for word in words:
        wordcount += 1
        # Check if the word is already in dictionary
        if word in d:
            # Increment count of word by 1
            d[word] = d[word] + 1
        else:
            # Add the word to dictionary with count 1
            d[word] = 1

# Print the contents of dictionary to a txt file
output = open("articles-wordcount\\" + article[company] + "-output-%s.txt" % display, "w")
for key in list(d.keys()):
    output.write(key + ":" + str(d[key]) + "\n")

output.close()

print("\n" + str(wordcount), "words found and removed and stored in %s-output-%s.txt" % (article[company], display))


