import nltk
#nltk.download('stopwords')

# Adding custom stopwords
stopwords = nltk.corpus.stopwords.words('english')
newStopWords = ["a", "about", "above", "after", "again", "against", "ain", "all", "am", "an", "and", "any", "are","aren","aren't","as","at","be","because","been","before","being","below","between","both","but","by","can","couldn","couldn't","d","did","didn","didn't","do","does","doesn","doesn't","doing","don","don't","down","during","each","few","for","from","further","had","hadn","hadn't","has","hasn","hasn't","have","haven","haven't","having","he","her","here","hers","herself","him","himself","his","how","i","if","in","into","is","isn","isn't","it","it's","its","itself","just","ll","m","ma","me","mightn","mightn't","more","most","mustn","mustn't","my","myself","needn","needn't","no","nor","not","now","o","of","off","on","once","only","or","other","our","ours","ourselves","out","over","own","re","s","same","shan","shan't","she","she's","should","should've","shouldn","shouldn't","so","some","such","t","than","that","that'll","the","their","theirs","them","themselves","then","there","these","they","this","those","through","to","too","under","until","up","ve","very","was","wasn","wasn't","we","were","weren","weren't","what","when","where","which","while","who","whom","why","will","with","won","won't","wouldn","wouldn't","y","you","you'd","you'll","you're","you've","your","yours","yourself","yourselves","could","he'd","he'll","he's","here's","how's","i'd","i'll","i'm","i've","let's","ought","she'd","she'll","that's","there's","they'd","they'll","they're","they've","we'd","we'll","we're","we've","what's","when's","where's","who's","why's","would","able","abst","accordance","according","accordingly","across","act","actually","added","adj","affected","affecting","affects","afterwards","ah","almost","alone","along","already","also","although","always","among","amongst","announce","another","anybody","anyhow","anymore","anyone","anything","anyway","anyways","anywhere","apparently","approximately","arent","arise","around","aside","ask","asking","auth","available","away","awfully","b","back","became","become","becomes","becoming","beforehand","begin","beginning","beginnings","begins","behind","believe","beside","besides","beyond","biol","brief","briefly","c","ca","came","cannot","can't","cause","causes","certain","certainly","co","com","come","comes","contain","containing","contains","couldnt","date","different","done","downwards","due","e","ed","edu","effect","eg","eight","eighty","either","else","elsewhere","end","ending","enough","especially","et","etc","even","ever","every","everybody","everyone","everything","everywhere","ex","except","f","far","ff","fifth","first","five","fix","followed","following","follows","former","formerly","forth","found","four","furthermore","g","gave","get","gets","getting","give","given","gives","giving","go","goes","gone","got","gotten","h","happens","hardly","hed","hence","hereafter","hereby","herein","heres","hereupon","hes","hi","hid","hither","home","howbeit","however","hundred","id","ie","im","immediate","immediately","importance","important","inc","indeed","index","information","instead","invention","inward","itd","it'll","j","k","keep","keeps","kept","kg","km","know","known","knows","l","largely","last","lately","later","latter","latterly","least","less","lest","let","lets","like","liked","likely","line","little","'ll","look","looking","looks","ltd","made","mainly","make","makes","many","may","maybe","mean","means","meantime","meanwhile","merely","mg","might","million","miss","ml","moreover","mostly","mr","mrs","much","mug","must","n","na","name","namely","nay","nd","near","nearly","necessarily","necessary","need","needs","neither","never","nevertheless","new","next","nine","ninety","nobody","non","none","nonetheless","noone","normally","nos","noted","nothing","nowhere","obtain","obtained","obviously","often","oh","ok","okay","old","omitted","one","ones","onto","ord","others","otherwise","outside","overall","owing","p","page","pages","part","particular","particularly","past","per","perhaps","placed","please","plus","poorly","possible","possibly","potentially","pp","predominantly","present","previously","primarily","probably","promptly","proud","provides","put","q","que","quickly","quite","qv","r","ran","rather","rd","readily","really","recent","recently","ref","refs","regarding","regardless","regards","related","relatively","research","respectively","resulted","resulting","results","right","run","said","saw","say","saying","says","sec","section","see","seeing","seem","seemed","seeming","seems","seen","self","selves","sent","seven","several","shall","shed","shes","show","showed","shown","showns","shows","significant","significantly","similar","similarly","since","six","slightly","somebody","somehow","someone","somethan","something","sometime","sometimes","somewhat","somewhere","soon","sorry","specifically","specified","specify","specifying","still","stop","strongly","sub","substantially","successfully","sufficiently","suggest","sup","sure","take","taken","taking","tell","tends","th","thank","thanks","thanx","thats","that've","thence","thereafter","thereby","thered","therefore","therein","there'll","thereof","therere","theres","thereto","thereupon","there've","theyd","theyre","think","thou","though","thoughh","thousand","throug","throughout","thru","thus","til","tip","together","took","toward","towards","tried","tries","truly","try","trying","ts","twice","two","u","un","unfortunately","unless","unlike","unlikely","unto","upon","ups","us","use","used","useful","usefully","usefulness","uses","using","usually","v","value","various","'ve","via","viz","vol","vols","vs","w","want","wants","wasnt","way","wed","welcome","went","werent","whatever","what'll","whats","whence","whenever","whereafter","whereas","whereby","wherein","wheres","whereupon","wherever","whether","whim","whither","whod","whoever","whole","who'll","whomever","whos","whose","widely","willing","wish","within","without","wont","words","world","wouldnt","www","x","yes","yet","youd","youre","z","zero","a's","ain't","allow","allows","apart","appear","appreciate","appropriate","associated","best","better","c'mon","c's","cant","changes","clearly","concerning","consequently","consider","considering","corresponding","course","currently","definitely","described","despite","entirely","exactly","example","going","greetings","hello","help","hopefully","ignored","inasmuch","indicate","indicated","indicates","inner","insofar","it'd","keep","keeps","novel","presumably","reasonably","second","secondly","sensible","serious","seriously","sure","t's","third","thorough","thoroughly","three","well","wonder"]
stopwords.extend(newStopWords)

#prompt user to enter company's name
company = int(input("Get stopwords count. Press \n0:JnT\n1:Pos Laju\n2:CityLink\n3:DHL\n4: Gdex\n"))
article = ["jnt", "poslaju", "citylink", "dhl", "gdex"]

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

gdex = ["\n1. Announcing: GDEX Berhad (KLSE:GDEX) Stock Increased An Energizing 115% In The Last Year",
        "2. GDEX expansion, diversification accelerates domestic e-commerce logistics growth",
        "3. Enhancing delivery via the digital platform"]

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
if company == 4:
    for i in range(0, len(dhl)):
        print(gdex[i])
    display = input("Please select title: ")

print("\nCounting Stopwords for selected article............")

# Open the file in read mode
text = open("articles\\" + article[company] + "-article-%s.txt" % display, "r", encoding="utf8")

# Create an empty dictionary
d = dict()

# Initialize stopwords found variables
sw_found = 0

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
        if word in stopwords:
            # It's on the stopwords list
            sw_found += 1
        else:
            # The word is not in the stopwords list
            if word in d:
                # Increment count of word by 1
                d[word] = d[word] + 1
            else:
                # Add the word to dictionary with count 1
                d[word] = 1

# Print the contents of dictionary to a txt file
output = open("articles-stopwords\\" + article[company] + "-stopwords-%s.txt" % display, "w")
for key in list(d.keys()):
    output.write(key + ":" + str(d[key]) + "\n")
output.close()

print("\n" + str(sw_found), "stop words found and removed. Words that are not a stopwords are stored in %s-stopwords-%s.txt" % (article[company], display))
