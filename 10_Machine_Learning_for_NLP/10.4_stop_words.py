imran_khan_speech : str = """

Statement by Prime Minister Imran Khan
SCO COUNCIL OF HEADS OF STATE
(Bishkek, Kyrgyz Republic, 14 June 2019)
    (Extended Format)
Excellency,
Mr. Sooronbay Jeenbekov,
President of the Kyrgyz Republic,
Honourable Heads of Member and Observer States,
Excellencies, Ladies and Gentlemen!
I am delighted to join leaders from SCO Member and Observer States in this beautiful city of Bishkek. 
I extend our gratitude to President Jeenbekov, the Government and people of Kyrgyz Republic for their gracious hospitality.

The Kyrgyz Republic’s natural beauty and rich traditions make it the pearl of the SCO region.

We congratulate Kyrgyzstan for its excellent stewardship of SCO since the historic Qingdao Summit in China last year.
As the Russian Federation takes the baton, we are confident that SCO’s onward march would continue apace.
Excellencies,
Pakistan has historic ties with the nations and countries represented around this table. 
We may be new to the SCO family, but our links are deep and abiding.
SCO is the modern expression of our historic roots.
Our economic linkages are equally compelling.
Pakistan provides the vital connectivity between the Middle East and China and Central and South Asia.
  These geographic proximities and economic imperatives draw us closer to SCO.
Excellencies,
Pakistan today is a country of over 200 million resilient and enterprising people.
Pakistan is an attractive investment destination and a large market endowed with a rich array of resources.
Our predominantly young population is imbued with immense energy and creativity.
Our other endowments include a vast pool of skilled human resource, a large agrarian base, tremendous tourism potential, diverse mineral wealth, and a developed IT infrastructure.
Pakistan’s foreign policy outlook is anchored on the inextricable link between peace and development.
We build partnerships based on mutual respect, sovereign equality and equal benefit. 
The China-Pakistan Economic Corridor (CPEC), the flagship project of President Xi’s far-sighted Belt and Road Initiative, is fast reaching fruition.
Gwadar Port, at its southern end, marks the only point of convergence of the maritime Belt and the overland Road.
I was in China in April, for the 2nd Belt and Road Forum, where we also launched the next phase of CPEC, and concluded an upgraded Pakistan-China Free Trade Agreement.
In time, CPEC is destined to catalyze the creation of an integrated pan-Asian sphere of shared prosperity.

Excellencies,
The world stands at a cross-roads.
For the first time in ages, we are seeing the advent of a multi-polar global order. 
Epicentres of economic power and growth momentum are shifting eastwards.
Regional integration is speeding up. 
Disruptive technologies are maturing.

Threats from terrorism to climate change to narcotics to bacterial resistance continue to loom large on humanity.
There are increasing barriers to open trade and innovation.
Meanwhile, growing intolerance and Islamophobia are threatening to accentuate religious fault-lines. 
For its part, Pakistan condemns terrorism in all its forms and manifestations, including State-terrorism against people under illegal occupation.
We are among the few countries to have successfully turned the tide against terrorism and at a heavy cost to our soldiers and our population. 
Pakistan remains ready to share its experience and expertise in counter terrorism.
We will also remain actively engaged in SCO’s counter-terrorism initiatives.
Excellencies,
There is finally a realization that the conflict in Afghanistan has no military solution. 
Pakistan is fully supporting efforts for peace and reconciliation, through an Afghan-led and Afghan-owned peace process. 
We deem this to be part of a shared responsibility and, therefore, appreciate the positive contributions being made by China, Russia and Afghanistan’s immediate neighbours. 
SCO’s support for post-conflict Afghanistan will remain crucial.
Excellencies,
South Asia continues to be challenged by common enemies: poverty, illiteracy, disease and under-development. 
Political differences and unresolved disputes further compound this predicament.
Enduring peace and prosperity in South Asia will remain elusive until the main dynamic in South Asia is shifted from confrontation to cooperation. 
It is important to seize the opportunities for peaceful resolution of outstanding disputes and collective endeavours for regional prosperity. 
Excellencies,
The evolving situation in the Gulf and Middle East is a matter of great concern.
We join the SCO members in urging the parties to exercise restraint, take steps to de-escalate the situation, and find solutions through diplomatic means. 
We believe implementation of the Joint Comprehensive Plan of Action by all parties is essential for international and regional stability.
Excellencies,
As a Sportsman, I have always considered the playground to be a remarkable teacher.
Sports teach us that opportunities knock at our door in the shape of challenges.
They inculcate sportsman spirit, fair play, justice and comraderie – values that are at the core of SCO’s philosophy.
On the turf of international politics, there is an opening for SCO to play its role in framing a brave new world.
I suggest the following eight-pronged course of action: 
1)  Reinforce our vision of cooperation, that rejects confrontation, and advance the imperatives of peaceful co-existence at the regional and international levels.
2)      Galvanize the “Shanghai Spirit” to strengthen SCO’s core mandate of mitigating the risks of conflict, fostering confidence, and promoting stability.

3)      Finalize arrangements for trade in local currencies, and set up SCO Fund and SCO Development Bank to catalyze the trans-regional development agenda.
4)      Synergize the various region-wide connectivity initiatives, and work on complementing infrastructure connectivity with soft connectivity, including digital, cultural, touristic, and academic.
I propose setting up SCO Culture & Tourism Corridors, clustering multiple SCO destinations into a single package.
5)      Making SCO more relevant to the daily lives of citizens by promoting food security and enhancing cooperation in health and humanitarian sectors.
6)      Take the lead role in establishing a comprehensive framework for combating corruption and white collar crime to prevent billions of dollars annually money laundered from developing world on to offshore accounts.
7)      Prioritize women and youth empowerment by focusing inter-alia on strengthening the Women Forum and the Youth Council and mandating them to promote gender mainstreaming, skills acquisition and jobs mobility.
8)      Bridge the gap between region-specific research and policy by launching feasibilities for creating SCO Centres of Excellence on Poverty Alleviation, something which the whole world can learn from the Chinese experience,  De-Radicalization, Connectivity, and New Technologies.
Excellencies,
We have every resource, and every reason, to turn our dreams into reality.
A far-reaching vision, strength of will, ownership, and synergy in our efforts will help us in successfully achieving this transformation.           

I Thank You!

"""

#######################################

import nltk
nltk.download('stopwords')

# Stop words remove with portstemmer

from nltk.stem import PorterStemmer

from nltk.corpus import stopwords

print(stopwords.words('english') , '\n')

print(len(stopwords.words('english') ), '\n')

stemmer = PorterStemmer()

# 1- sentence tokenizer

sentences = nltk.sent_tokenize(imran_khan_speech) 

# Apply stopwords and filter and then apply stemming

print('Stop words remove and apply portstemmer : \n')

for i in range(len(sentences)):
    
    words = nltk.word_tokenize(sentences[i])   # tokenize each word of the sentence
    
    # check if words are not present in the stop words then stem taht word and store in the list
    stem_words = [stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
    
    # converting all the list of stem words into sentences
    sentences[i] = " ".join(stem_words)

print(sentences , '\n')

############################

# stop words remove with snowball stemmer

from nltk.stem import SnowballStemmer

snow_ball_stemmer = SnowballStemmer('english')

sentences = nltk.sent_tokenize(imran_khan_speech) 

print('Stop words remove and apply snowballstemmer : \n')

for i in range(len(sentences)):
    
    words = nltk.word_tokenize(sentences[i])   # tokenize each word of the sentence
    
    # check if words are not present in the stop words then stem taht word and store in the list
    stem_words = [snow_ball_stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
    
    # converting all the list of stem words into sentences
    sentences[i] = " ".join(stem_words)

print(sentences , '\n')

#######################################

# stopwords remove with lemmatization

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

sentences = nltk.sent_tokenize(imran_khan_speech) 

print('Stop words remove and apply lemmatization with post tag \'n\' : \n')

for i in range(len(sentences)):
    
    words = nltk.word_tokenize(sentences[i])   # tokenize each word of the sentence
    
    # check if words are not present in the stop words then stem taht word and store in the list
    stem_words = [lemmatizer.lemmatize(word , pos = 'n') for word in words if word not in set(stopwords.words('english'))]
    
    # converting all the list of stem words into sentences
    sentences[i] = " ".join(stem_words)

print(sentences , '\n')

###########################################

# stopwords remove with lemmatization

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

sentences = nltk.sent_tokenize(imran_khan_speech) 

print('Stop words remove and apply lemmatization with post tag \'v\' : \n')

for i in range(len(sentences)):
    
    words = nltk.word_tokenize(sentences[i])   # tokenize each word of the sentence
    
    # check if words are not present in the stop words then stem taht word and store in the list
    stem_words = [lemmatizer.lemmatize(word , pos = 'v').lower() for word in words if word not in set(stopwords.words('english'))]
    
    # converting all the list of stem words into sentences
    sentences[i] = " ".join(stem_words)

print(sentences , '\n')
