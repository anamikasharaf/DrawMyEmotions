# DrawMyEmotions

# Objective:

This project will take an input tweet and will perform sentiment analysis on it. Based on the emotions detected in the analysis, this system will represent those sentiment in form of an abstract art. This art will be tweeted as a response to the input tweet.

## 1> Sentiment Analysis

I will be taking the help of “http://text-processing.com/api/sentiment/ “ to analyze the sentiment.

This API returns a json file with probability for each [neg,neutral,pos] label.

for example

$ curl -d "text=great" http://text-processing.com/api/sentiment/


{


        "probability": {
                "neg": 0.39680315784838732,
                "neutral": 0.28207586364297021,
                "pos": 0.60319684215161262
        },
        
        
        "label": "pos"
        
        
}

## 2> Tweeter Account and Input Tweet

I have created a twitterbot account. 

After connecting from my twitter account, I read the input tweet into a string and do sentiment analysis on that.

## 3> Creating Art

I am creating a abstract art based on emotion. Color palette is selected at random. There are four layers of color on the canvas. background color, foreground color, layer1, layer2. Each layer of color has it’s own palette which gets selected randomly.

I have divided the canvas into four quadrant. At a given time I work with combination of randomly picked two quadrant. Once quadrant is picked my layer1 and layer2 color’s quadrant will be picked based on which quadrant foreground art getting created. All the shapes are random and I use variation of different shapes to have more effect.

I save the postscript file and convert that into a .png file with high quality.

## 4> Tokenized Sentiment Analysis

Apart from using sentiment analysis, to be more precise on emotion, emotion_dict dictionary is referred.

If the emotion is found to be sad by sentiment analysis then it refers the dictionary to find out whether the emotion is anger, disgust, fear or sad. I use lemmatization to be more precise with words.

For Example:

>> tok = lmtzr.lemmatize(“smiling”,’v’)

>> print tok

>> smile


## 5> Research for emotions and colors representation

->For Happy Instance

I have chosen palette of orange and pink

Orange
Sharing red's energizing aspects, but to a safer degree, orange is a good way to add excitement to a site without severity. It is generally playful. It can even signify health, suggesting vitality and vibrance.

Pink
The connotations with childhood and with sugary treats gives it a sweet, sometimes innocent appeal (not surprisingly a self-perpetuating cycle). It is also traditionally used with love and romantic themes

->For Sad Instance

I have chosen palette of black and grey

Black
The black color is the absence of color. Black is a mysterious color that is typically associated with the unknown or the negative.
It keeps things bottled up inside, hidden from the world.

Grey
The color gray is an unemotional color. It is detached, neutral, impartial and indecisive - the fence-sitter.

->For Neutral Instance

I have chosen palette of brown

Brown
The color brown is a serious, down-to-earth color signifying stability, structure and support.

->For Fear Instance

I have chosen palette of indigo and red

Indigo
Indigo energy is fearful, oversensitive, undisciplined and a wishful thinker who never really gets it done.

Red
Red implies passionate and aggressive behavior

->For Anger Instance

I have chosen palette of red

Red
Red implies passionate and aggressive behavior

->For Disgust Instance

I have chosen palette of Green-Yellow and Blue-Green



Researches has been done from:

www.areconnecting.com

https://goo.gl/26VCbl

https://goo.gl/fkQbyd



 
