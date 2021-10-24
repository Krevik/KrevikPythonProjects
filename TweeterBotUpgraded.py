import tweepy
import time
import logging
import random
import _thread as thread
import threading
from datetime import datetime
from datetime import time as time_new

# Authenticate to Twitter
consumer_key_key = "cons_key";
consumer_secret_key = "cons_secr_key";
access_token_key = "access_token_key";
access_token_secret_key = "access_token_secr_key";
auth = tweepy.OAuthHandler(consumer_key_key, consumer_secret_key)
auth.set_access_token(access_token_key, access_token_secret_key)

#Constants
####checking if we want to shill
interactKeySet1 = ["shill me", "shill us", "shill your",
                   "show me", "show us", "show your",
                   "drop here", "drop your",
                   "give me", "give us", "give your",
                   "i want to buy", "i want to see",
                   "post me", "post us", "post your",
                   "should i buy", "should i get",
                   "drop time"];
interactKeySet2 = ["art", "nft", "cryptoart"];
####generating shilling text
shillKeySet1 = ["You might be interested about", "I think you may like", "You should check out",
                "Check", "You gonna love", "You should consider checking", "You may like", "Hey, check out",
                "You could have interest in", "Hey, please look at", "Take a look at", "Look at", "Check out",
                "Come and visit", "Come and see"];
shillKeySet2 = ["my", "that", "this"];
shillKeySet3 = ["", "most", "very", "totally", "hugely", "absolutely", "quite", "unconditionally"];
shillKeySet4 = ["gorgeous", "attractive", "brilliant", "colorful", "delightful", "elegant",
                "good-looking", "impressive", "lavish", "lovely", "luxurious", "pleasing",
                "splendid", "stunning", "superb", "dream", "fine", "grand", "luxuriant",
                "showy", "wonderful", "admirable", "amazing", "astonishing", "awesome", "brilliant",
                "cool", "excellent", "fabulous", "fantastic", "incredible", "magnificent", "marvelous",
                "outstanding", "phenomenal", "remarkable", "sensational", "strange", "wondrous",
                "divine", "staggering", "unheard-of"];
shillKeySet5 = ["NFT", "NFTs", "#NFT", "#NFTs"];
shillKeySet6 = ["Art", "Cryptoart", "Collection", "Drop", "Set", "Compilation"];
collections = ["https://opensea.io/collection/bismuth-crystals", "https://opensea.io/collection/pokemons-collectibles",
               "https://opensea.io/collection/crypto-rpg-equipment-gear", "https://opensea.io/collection/crypto-rpg-mobs-leveled",
               "https://opensea.io/collection/crypto-rpg-mobs-epicized", "https://opensea.io/collection/crypto-rpg-mobs-raritized",
               "https://opensea.io/collection/crypto-rpg-mobs", "https://opensea.io/collection/crypto-potatoes-k",
               "https://opensea.io/collection/big-krevik-abstract-collection", "https://opensea.io/collection/fonted-names-future-rot"];
####complimenting
NFTSites = ["rarible.com/collection/", "opensea.io/collection/", "solanart.io/collections/"];
complimentKeySet1 = ["gorgeous", "attractive", "brilliant", "colorful", "delightful", "elegant",
                "good-looking", "impressive", "lavish", "lovely", "luxurious", "pleasing",
                "splendid", "stunning", "superb", "dream", "fine", "grand", "luxuriant",
                "showy", "wonderful", "admirable", "amazing", "astonishing", "awesome", "brilliant",
                "cool", "excellent", "fabulous", "fantastic", "incredible", "magnificent", "marvelous",
                "outstanding", "phenomenal", "remarkable", "sensational", "strange", "wondrous",
                "divine", "staggering", "unheard-of"];
complimentKeySet2 = ["nft!", "nft collection!", "piece of art!", "artwork!", "cryptowork!", "token!"];
complimentKeySet3 = ["Author should consider art-making as full-time job :D",
                "I would like to have such artistic abilities.",
                "I feel jealous about the author...",
                "I am bad at compliments, but it's really breathtaking art."];
####dropping eth address
ethDropKeySet1 = ["drop your", "post your", "post"];
ethDropKeySet2 = ["eth"];
ethDropKeySet3 = ["wallet", "address"];
ethDropKeySet4 = ["give"];
####nightcafe stuff
nightcafeWordSet1 = ["Hey there", "Hi there", "Hello there", "Welcome", "Hey buddy"];
nightcafeWordSet2 = ["check that", "look at that", "check that out", "please look at", "come and have a look"];

#################
keyWordsSet1 = ['nft', 'rarible', 'opensea', 'airdrop', 'cryptoart', '#nft', '#rarible', '#opensea', '#cryptoart', 'NftKrev'];
keyWordsSet2 = ['drop', 'show', 'i need', 'post your', 'post yours', 'shill', 'should i get', 'i buy', 'i should buy', 'should i buy', 'time nft', 'drop time', 'share', 'your favourite'];
keyWordsSet3 = ['nft', 'art'];
keyWordsSet4 = ['monkey', 'mankey', "eth wallet", "wallet", "my drop", "check this link", "check link", "check it out", "check this"];
keyWordsSet5 = ['airdrop', 'rt', "retweet", "giveway", "opensea.io/"];
keyWordsSet6 = ['eth', '#eth'];
keyWordsSet7 = ['adress', 'wallet'];


myETHWalletAdress = "0xE59FfC3689af47fC501Ce84A2F1cf3C435a67869";
NightCafeCreation = "https://creator.nightcafe.studio/creation/YeIPCfoGtgLKZv7AQ7HP";
NightCafeMention = "@NightcafeStudio";

repliedTweetsIDsCollector = [];
tweetsToLikeIDCollector = [];
usersIDToFollowCollector = [];

api = tweepy.API(auth, wait_on_rate_limit=True)

def login():
    result = False;
    api = tweepy.API(auth, wait_on_rate_limit=True)
    try:
        api.verify_credentials();
        print("Successfully Logged In");
        result = True;
    except:
        print("Error Loggin in");
        result = False;
    return result;

def publishTweet(text):
    try:
        api = tweepy.API(auth, wait_on_rate_limit=True)
        api.update_status(text);
        print(f"Successfully published a tweet with text: {text}");
    except:
        print("Couldn't publish a Tweet");
        time.sleep(random.randint(60,120));

def replyToTweet(tweet, text):
    if("Krzysztof" not in tweet.user.name and "NftKrev" not in tweet.user.name):
        if(tweet.id not in repliedTweetsIDsCollector):
            try:
                api.update_status(status=text, in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)
                print(f"Answered to {tweet.user.name} : {text}");
            except:
                print(f"Couldn't answer to {tweet.user.name}");
                time.sleep(30);
            if(len(repliedTweetsIDsCollector) > 600):
                repliedTweetsIDsCollector.clear();
            repliedTweetsIDsCollector.append(tweet.id);
            time.sleep(random.randint(30,60));

def getRandomFromList(list1):
    return list1[random.randint(0, len(list1) - 1)];

#def pickRandomCompliment():
    #result = "";

    #wordSet1 = ["What an amazing", "Woah, nice", "I love that", "I like that", "I think it might get popular as", "One of bests", "Very good looking", "Amazing", "Beautifull", "Such a unique", "What a unique"];
    #wordSet2 = ["Art work", "NFT", "nft", "nft work", "crypto work", "masterpiece", "artwork", "art", "token"];
    #wordSet3 = ["Author should consider art-making as full-time job :D", "I would like to have such artistic abilities.", "I feel jealous about the author...", "I am bad at compliments, but it's really breathtaking art."];

    #resultPool = [];
    #x = 1;
    #while(x < 4):
        #x = x + 1;
        #compliment = getRandomFromList(wordSet1) + " " + getRandomFromList(wordSet2) + ".";
        #if(random.randint(0,2) == 1):
            #compliment = compliment + getRandomFromList(wordSet3);
        #resultPool.append(compliment);
    #return result;

def retweetTweet(tweet):
    if(random.randint(0,20) == 5):
        try:
            api = tweepy.API(auth, wait_on_rate_limit=True)
            api.retweet(int(tweet.id));
            print(f"Successfully retweeted a tweet of: {tweet.user.name}");
        except:
            print(f"Couldn't retweet a Tweet of: {tweet.user.name}");
            time.sleep(random.randint(60,120));

def isAnyWordPresent(list1, text):
    result = False;
    for word in list1:
        if word.lower() in text.lower():
            return True;
    return result;

#def doesProvokeMeToReplyCollection(tweet):
    #return (isAnyWordPresent(keyWordsSet2, tweet.text) and isAnyWordPresent(keyWordsSet3, tweet.text) and not isAnyWordPresent(keyWordsSet4, tweet.text));

#def doesProvokeMeToComplimentTheCollection(tweet):
    #return isAnyWordPresent(["opensea.io/"], tweet.text) and ("KrevikNFT" not in tweet.user.name and "NFT_KREVIK" not in tweet.user.name);

def doesProvokeMeToRetweet(tweet):
    return (isAnyWordPresent(keyWordsSet5, tweet.text) and isAnyWordPresent(keyWordsSet3, tweet.text));

def doesProvokeToRetweet1(tweet):
    return isAnyWordPresent(["rt", "retweet"], tweet.text);
    
def publishSomeTweet():
    tweetTexts = generateTweetTexts();
    tweetText = tweetTexts[random.randint(0, len(tweetTexts)-1)];
    try:
        publishTweet(tweetText);
        print("Published a tweet");
    except:
        print("Couldn't make a tweet.")

def doesProvokeMeToShill(tweet):
    result = False;
    if(isAnyWordPresent(interactKeySet1, tweet.text) and isAnyWordPresent(interactKeySet2, tweet.text)
       and not isAnyWordPresent(["Krev"], tweet.text)):
        result = True;
    return result;

def doesProvokeMeToComplimentTheCollection(tweet):
    return isAnyWordPresent(NFTSites, tweet.text) and not isAnyWordPresent(["Krev"], tweet.text);

def doesProvokeMeToDropETHAddress(tweet):
    return isAnyWordPresent(ethDropKeySet1, tweet.text) and isAnyWordPresent(ethDropKeySet2, tweet.text) and isAnyWordPresent(ethDropKeySet3, tweet.text) and isAnyWordPresent(ethDropKeySet4, tweet.text);

def doesProvokeMeToTagFriends(tweet):
    return isAnyWordPresent(tagKeySet1, tweet.text) and isAnyWordPresent(tagKeySet2, tweet.text);

def getShillText():
    result = "";
    result = result + getRandomFromList(shillKeySet1) + " " + getRandomFromList(shillKeySet2) + " ";
    result = result + getRandomFromList(shillKeySet3) + " " + getRandomFromList(shillKeySet4) + " ";
    result = result + getRandomFromList(shillKeySet5) + " " + getRandomFromList(shillKeySet6) + "\n";
    result = result + getRandomFromList(collections) + "\n";
    result = result + "#opensea";
    return result;

def getRandomCompliment():
    resultPool = [];
    for word1 in complimentKeySet1:
        for word2 in complimentKeySet2:
            string = "What a " + word1 + " " + word2;
            if(random.randint(1,3) == 2):
                string = string + " " + getRandomFromList(complimentKeySet3);
            resultPool.append(string);
    return getRandomFromList(resultPool);

def handleTweet(tweet):
    #check if we don't like it already
    if(not tweet.favorited):
        is_reply = False;
        #check if the tweet is a reply
        if tweet.in_reply_to_status_id is not None:
            # Tweet is a reply
            is_reply = True
        shilled = False;
        retweeted=False;
        complimented = False;
        dropETHAddress = False;
        #does provoke me to drop eth address
        if(doesProvokeMeToDropETHAddress(tweet)):
            dropETHAddress = True;
        #check if we want to shill under the tweet that can't be reply
        if doesProvokeMeToShill(tweet) and not is_reply and not dropETHAddress:
            replyToTweet(tweet, getShillText());
            shilled=True;
        #check if we want to compliment the collection
        if doesProvokeMeToComplimentTheCollection(tweet) and not dropETHAddress:
            replyToTweet(tweet, getRandomCompliment());
            complimented=True;
            #5% chance that we retweet it
            if random.randint(1,20) == 5:
                retweetTweet(tweet);
                retweeted = True;
        #check if we want to drop our eth address (giveaways)
        if not retweeted and not is_reply:
            if dropETHAddress:
                if doesProvokeMeToRetweet(tweet):
                    retweetTweet(tweet);
                    retweeted = True;
                replyToTweet(tweet, myETHWalletAdress);
            
        retweeted = False;
        #if(doesProvokeMeToReplyCollection(tweet)):
            #replyToTweet(tweet, pickRandomCollectionOfMine());
        #if(doesProvokeMeToComplimentTheCollection(tweet)):
            #replyToTweet(tweet, pickRandomCompliment());
        #if(doesProvokeMeToRetweet(tweet)):
            #retweetTweet(tweet);
            #retweeted = True;
        #if(doesProvokeMeToDropETHAddress(tweet)):
            #replyToTweet(tweet, myETHWalletAdress);
            #if(doesProvokeToRetweet1(tweet) and not retweeted):
                #retweetTweet(tweet);
                #retweeted = True;
    time.sleep(random.randint(10,25));

def getFewHashtags(list1):
    amount = random.randint(5, len(list1) - 1);
    result = [];
    x = 1;
    while(x < amount):
        hashtag = getRandomFromList(list1);
        while(hashtag in result):
            hashtag = getRandomFromList(list1);
        result.append(hashtag);
        x = x + 1
    return result;

def generateRandomTweetText():
    result = '';
    tweetsPool = [];
    #Normal tweets
    wordSet1 = ["Drop here", "Shill here", "Show here", "Post here", "Give here", "Flex here", "Flex to community", "Shill me", "Shill us", "Show me", "Show us", "Show to community", "Give us"];
    wordSet2 = ["your best", "best", "best in your opinion", "your unsold", "unsold", "underrated", "most underrated", "your underrated", "your most underrated", "your precious", "precious", "valuable", "your most valuable",
                "your desired", "your most desired", "most popular", "the most expensive", "some cheap", "cheapest", "some new", "unseen", "some unseen", "upcoming", "not popular", "forgotten", "unique", "hottest", "your unique",
                "your hottest", "your new", "your upcoming", "your most recent", "coolest"];
    wordSet3 = ["NFT", "NFTs", "NFT's", "nft", "nfts", "nft's", "collection", "NFT collection", "NFTs collection", "NFT's collection", "nft collection", "nfts collection", "nft's collection", "NFT work", "nft work",
                "nft piece", "NFT piece", "nft artpiece", "NFT artpiece", "NFT Masterwork", "nft masterwork", "NFT Art", "nft art", "NFT Painting", "nft painting"];
    wordSet4 = ["!", ".", ".", "."];
    phraseSet1 = ["I want to see it!", "We want to see it!", "Don't be so shy!", "I need inspiration.", "#NFTCommunity will be proud of you!", "Show it to NFT Community!", "My friend was asking me about it.", "Let the world see it!",
                "Like, Follow and retweet.", "Let's help it getting famous.", "Support the creator.", "Support #NFTCommunity !", "Follow for follow?", "Make it best-year Art!", "@Opensea look here!",
                "@Rarible might be interested about it too :)", "Are you curious about #ETH next week price too?", "I am so excited about NFT Projects!", "Did you know that van-gogh was faster about NFTs than you?",
                "I want the world to see it", "I want to support you!", "Let the #NFTCollectors fight for it!", "It's good to have the NFT before it will explode :)"];
    
    hashtagsList = ["NFT", "NFTs", "NFTWork", "NFTArt", "CryptoArt", "CryptoWork", "opensea", "rarible", "mintable", "solart", "foundation", "eth", "polygon", "NFTCommunity", "Artist", "Artists", "openseanft",
                    "Shilltime", "Droptime", "DropNFT", "DigitalArt"];
    x = 0;
    while(x < 10):
        x = x + 1;
        #generate text
        tweetText = getRandomFromList(wordSet1) + " " + getRandomFromList(wordSet2) + " " + getRandomFromList(wordSet3) + getRandomFromList(wordSet4);
        if(random.randint(0,2) == 1):
            tweetText = tweetText + " ";
            tweetText = tweetText + str(getRandomFromList(phraseSet1));
        #add hashtags
        tweetText = tweetText + "\n";
        hashtags = getFewHashtags(hashtagsList);
        for hashtag in hashtags:
            tweetText = tweetText + str("#" + hashtag + " ");
        #add it to the pool
        tweetsPool.append(tweetText);

    result = tweetsPool[random.randint(0, len(tweetsPool) - 1)];
    return result;

def publishRandomTweet():
    publishTweet(generateRandomTweetText());

class TwittingThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID;
        self.name = name;
        self.counter = counter;
    def run(self):
        print("Starting Twitting Thread");
        while True:
            #checkTime();
            now = datetime.now()
            now_time = now.time()
            if now_time >= time_new(8,00):
                publishRandomTweet();
            time.sleep(random.randint(4*60*60, 8*60*60));

def checkTime():
    now = datetime.now()
    now_time = now.time()
    if now_time >= time_new(22,00) or now_time <= time_new(8,00):
        time.sleep(random.randint(1*60*60, 2*60*60));

def likeSomeTweet():
    if(len(tweetsToLikeIDCollector) > 1):
        tweetID = tweetsToLikeIDCollector[random.randint(0, len(tweetsToLikeIDCollector) - 1)];
        try:
            api = tweepy.API(auth, wait_on_rate_limit=True)
            api.create_favorite(tweetID);
            print(f"Successfully liked tweet with id: {tweetID}");
        except:
            print(f"Couldn't like tweet with id: {tweetID}");

def followSomeUser():
    if(len(usersIDToFollowCollector) > 1):
        userID = usersIDToFollowCollector[random.randint(0, len(usersIDToFollowCollector) - 1)];
        try:
            api = tweepy.API(auth, wait_on_rate_limit=True)
            api.create_friendship(user_id=int(userID));
            print(f"Successfully followed user with id: {userID}");
        except:
            print(f"Couldn't follow user with id: {userID}");
            time.sleep(random.randint(30*60, 120*60));

class LikingThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID;
        self.name = name;
        self.counter = counter;
    def run(self):
        print("Starting Liking Thread");
        while True:
            checkTime();
            if(len(tweetsToLikeIDCollector) > 1):
                likeSomeTweet();
            time.sleep(random.randint(60,120));

class NFTStreamListener(tweepy.Stream):
    api1 = tweepy.API(auth, wait_on_rate_limit=True)
    def __init__(self, api=api1):
        super(NFTStreamListener,self).__init__(consumer_key_key,consumer_secret_key,access_token_key,access_token_secret_key)
    #function to collect tweets 
    def on_status (self,status):
        #checkTime();
        tweet = status;
        handleTweet(tweet);
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_error disconnects the stream
            return False

class NFTStreamListeningThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("Starting Stream Listening Thread");
        while True:
            #checkTime();
            stream = NFTStreamListener()
            stream.filter(track=keyWordsSet1)
            time.sleep(random.randint(20,30));


def generateNightCafeText():
    wordSet1 = ["Hey there", "Hi there", "Hello there", "Welcome", "Hey buddy"];
    wordSet2 = ["check that", "look at that", "check that out", "please look at", "come and have a look"];
    result = "" + getRandomFromList(nightcafeWordSet1) + " " + getRandomFromList(nightcafeWordSet2) + "\n";
    result = result + "https://creator.nightcafe.studio/" + str(random.randint(0,9999999)) + "\n";
    result = result + "@NightcafeStudio";        
    return result;

class NightCafeThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("Starting Night Cafe Thread");
        while True:
            text = generateNightCafeText();
            publishTweet(text);
            time.sleep(random.randint(1,2));
            api = tweepy.API(auth, wait_on_rate_limit=True)
            timeline = tweepy.Cursor(api.user_timeline).items(10);
            for tweet in timeline:
                if "@NightcafeStudio" in tweet.text:
                    api.destroy_status(tweet.id)
            time.sleep(random.randint(60,360));

class FollowingThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID;
        self.name = name;
        self.counter = counter;
    def run(self):
        print("Starting Follow Followers Thread");
        while True:
            #checkTime();
            if(len(usersIDToFollowCollector) > 1):
                followSomeUser();
                time.sleep(random.randint(31,45));

            

# Create new threads
thread1 = NFTStreamListeningThread(1, "Thread-1", 1);
#thread2 = LikingThread(2, "Thread-2", 2);
thread3 = FollowingThread(3, "Thread-3", 3);
thread4 = TwittingThread(4, "Thread-4", 4);
#thread5 = NightCafeThread(5, "Thread-5", 5);

def runBot():
    login();
    thread1.start();
    #thread2.start();
    thread3.start();
    thread4.start();
    #thread5.start();

runBot();