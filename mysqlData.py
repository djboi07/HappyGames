#The following mysql queries must be executed before runnning the main code

#CREATE DATABASE database_name;
#USE database_name;
#CREATE TABLE userpwd (username VARCHAR(30), password VARCHAR(30), status VARCHAR(1), PRIMARY KEY(username));
#CREATE TABLE leaderboard (username VARCHAR(30),tictactoe INT(4),rockpaperscissors INT(4),snakesandladders INT(4),handcricket INT(4),quadraticEquation INT(4),cards INT(4),memory INT(4),hangman INT(4),guessTheInteger INT(4),mathGame INT(4),overall INT(4),FOREIGN KEY (username) REFERENCES userpwd(username));
#CREATE TABLE hangman (countries VARCHAR(20),capitals VARCHAR(20),animals VARCHAR(20),mobiles VARCHAR(20),cars VARCHAR(20), fruits VARCHAR(20) ,vegetables VARCHAR(20),birds VARCHAR(20),flowers VARCHAR(20),proglang VARCHAR(20));
#CREATE TABLE quote username (saying VARCHAR(300),author VARCHAR(30));

#Run the following code after executing the sql query
user=''
pwd=''
db=''

import mysql.connector as my
c=my.connect(host='localhost',user=user,passwd=pwd,database=db)
cur=c.cursor()
cur.execute('delete from hangman')
c.commit()
c.close() 

countries=['india','turkey','bangladesh','russia','china','japan','unitedkingdom','canada','france','germany','qatar','uae','pakistan','afghanistan','greece','indonesia','australia','jordan','kenya','newzealand']
capitals=['newdelhi','istanbul','dhaka','moscow','beijing','tokyo','london','ottawa','paris','berlin','doha','abudhabi','islamabad','kabul','athens','jakarta','jerusalem','amman','nairobi','wellington']
animals=['buffalo','elephant','squirrel','lion','porcupine','cat','dog','bear','cow','rhinoceros','monkey','tiger','jackal','raccoon','sheep','goat','koala','kangaroo','snake','frog']
mobiles=['samsung','apple','huawei','xiaomi','lenovo','motorola','nokia','sony','vivo','oppo','micromax','honor','google','oneplus','asus','microsoft','blackberry','gionee','realme','sharp']
cars=['audi','honda','hyundai','mercedes','toyota','lincoln','jaguar','ford','chevrolet','volkswagen','tesla','ferrari','cadillac','datsun','bmw','lexus','mazda','nissan','volvo','subaru']
fruits=['BANANA','APPLE','GRAPE','STRAWBERRY','ORANGE','WATERMELON','AVOCADO','CHERRY','GUAVA','MANGO','LYCHEE','PAPAYA','PEACH','PINEAPPLE','POMEGRANATE','BLUEBERRY','DURIAN','KIWI','JACKFRUIT','GOOSEBERRY']
vegetables=['broccoli','cabbage','spinach','lettuce','garlic','onion','beetroot','potato','carrot','ginger','radish','cucumber','tomato','capsicum','beans','corn','celery','jalapeno','brinjal','cauliflower']
birds=['vulture','hawk','crow','sparrow','swallow','pigeon','eagle','penguin','ostrich','toucan','hummingbird','crane','flamingo','peacock','goose','duck','stork','turkey','seagull','parrot']
flowers=['rose','tulip','sunflower','lavender','lilac','daisy','daffodil','hyacinth','lily','marigold','petunia','bluebell','lotus','jasmine','dahlia','dandelion','laburnum','orchid','mistletoe','saffron']
proglang=['javascript','python','csharp','ruby','html','swift','mysql','oracle','unity','cobol','cplusplus','css','pascal','kotlin','php','teradata','flask','postgresql','bootstrap','django']

total=[]
for i in range(20):
    total+=[(countries[i].upper(),capitals[i].upper(),animals[i].upper(),mobiles[i].upper(),cars[i].upper(),fruits[i].upper(),vegetables[i].upper(),birds[i].upper(),flowers[i].upper(),proglang[i].upper())]

c=my.connect(host='localhost',user=user,passwd=pwd,database=db)
cur=c.cursor()

for i in total:
    print('insert into hangman values '+str(i)+';')
    cur.execute('insert into hangman values '+str(i))
    c.commit()

cur.execute('delete from quote')
c.commit() 
c.close()

quote={"Two things are infinite: the universe and human stupidity; and I'm not sure about the universe.":"Albert Einstein",
"So many books, so little time.":"Frank Zappa",
"A room without books is like a body without a soul.":'Marcus Tullius Cicero',
"You only live once, but if you do it right, once is enough.":'Mae West',
"Be the change that you wish to see in the world.":"Mahatma Gandhi",
"In three words I can sum up everything I've learned about life: it goes on.":"Robert Frost",
"If you want to know what a man's like, take a good look at how he treats his inferiors, not his equals.":"J.K. Rowling",
"No one can make you feel inferior without your consent.":"Eleanor Roosevelt",
"If you tell the truth, you don't have to remember anything.":"Mark Twain",
"Always forgive your enemies; nothing annoys them so much.":"Oscar Wilde",
"Live as if you were to die tomorrow. Learn as if you were to live forever.":"Mahatma Gandhi",
"The purpose of our lives is to be happy.":"Dalai Lama",
"Many of life’s failures are people who did not realize how close they were to success when they gave up.":"Thomas A. Edison",
"If you want to live a happy life, tie it to a goal, not to people or things.":"Albert Einstein",
"Money and success don’t change people; they merely amplify what is already there.":"Will Smith",
"The whole secret of a successful life is to find out what is one’s destiny to do, and then do it.":"Henry Ford",
"In order to write about life first you must live it":"Ernest Hemingway",
"Turn your wounds into wisdom.":"Oprah Winfrey",
"The unexamined life is not worth living.":"Socrates",
"Legends never die":"Gali Likith Sai",
"The way I see it, if you want the rainbow, you gotta put up with the rain.":"Dolly Parton",
"Do all the good you can, for all the people you can, in all the ways you can, as long as you can.":"Hillary Clinton",
"Don’t settle for what life gives you; make life better and build something.":"Ashton Kutcher",
"Everything negative – pressure, challenges – is all an opportunity for me to rise.":"Kobe Bryant",
"I like criticism. It makes you strong.":"LeBron James",
"You never really learn much from hearing yourself speak.":"George Clooney",
"Live for each second without hesitation.":"Elton John",
"Life is like riding a bicycle. To keep your balance, you must keep moving.":"Albert Einstein",
"Life is really simple, but men insist on making it complicated.":"Confucius",
"Life is a succession of lessons which must be lived to be understood.":"Helen Keller",
"My mama always said, life is like a box of chocolates. You never know what you’re gonna get.":"Forrest Gump",
"Keep calm and carry on.":"Winston Churchill",
"Life is a flower of which love is the honey.":"Victor Hugo",
"Life would be tragic if it weren’t funny.":"Stephen Hawking",
"Life’s tragedy is that we get old too soon and wise too late.":"Benjamin Franklin",
"I believe every human has a finite number of heartbeats. I don’t intend to waste any of mine.":"Neil Armstrong",
"":""
}
say=sorted(quote)
c=my.connect(host='localhost',user=user,passwd=pwd,database=db)
cur=c.cursor()
for i in say:
    print('insert into quote (saying,author) values ("'+i+'","'+ quote[i]+'")')
    cur.execute('insert into quote (saying,author) values ("'+i+'","'+ quote[i]+'")')
    c.commit()