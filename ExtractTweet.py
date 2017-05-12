_author__ = 'anamika.sharaf

import pdb  # This is the Python debugger
import sys
import tweepy, time, glob, random, os
import subprocess
import json
from nltk.stem.wordnet import WordNetLemmatizer
from Generate_Art import generate_happy_art, generate_sad_art, generate_neutral_art
from Generate_Art import generate_fear_art,generate_anger_art,generate_disgust_art

# Master emotion dictionary
emotion_dict = dict()

#Connecting to Twitter application
def authenticate_twitter_handle():
    #Corresponding information from my Twitter application:
    CONSUMER_KEY = '########################'
    CONSUMER_SECRET = '############################'
    ACCESS_TOKEN = '###############################'
    ACCESS_TOKEN_SECRET = '#############################'
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    return api

#Analyzing the tweet string and labelling with emotion
def sentiment_analysis(input_string):
    text_to_examine = 'text=' + input_string
    arg_list = ['curl', '-d', text_to_examine, 'http://text-processing.com/api/sentiment/']
    output = subprocess.check_output(arg_list)
    tokens = output.split(":")
    assert(len(tokens) == 6)
    label = tokens[5]
    label = label.replace("\"", "")
    label = label.replace("}", "")
    label_neg = tokens[2].split(',')
    label_neg = label_neg[0]
    label_neutral = tokens[3].split(',')
    label_neutral = label_neutral[0]
    label_pos = tokens[4].split(',')
    label_pos = label_pos[0].split('}')
    label_pos = label_pos[0]
    label_final = tokens[5]
    label_final = label_final.replace("\"", "")
    label_final = label_final.replace("}", "")
    label_final = label_final.split()
    label_final = label_final[0]
    if (label_final == "pos"):
        label_return = label_final + label_pos
        return label_return
    if (label_final == "neg"):
        label_return = label_final + label_neg
        return label_return
    if (label_final == "neutral"):
        label_return = label_final + label_neutral
        return label_return
    return 0

#tokenized sentiment dictionary
def load_emotion_data():
    # Read the emotion data file
    f = open("Emotion_Detect_Data.txt", "r")
    for line in f:
        line = line.strip().decode("utf-8")
        tokens = line.split(",")
        try:
            assert(len(tokens) == 2)
        except:
            pdb.set_trace()
        k = tokens[0].strip()
        v = tokens[1].strip()
        if k not in emotion_dict:
            emotion_dict[k] = v

#retrieving the emotion out of input string
def retrieve_emotion(input_string):
    load_emotion_data()
    input_sent = input_string
    lmtzr = WordNetLemmatizer()
    input_sent = input_sent.strip()
    line_tokens = input_sent.split()
    emotion_string = ""
    for tok in line_tokens:
        tok = tok.strip()
        tok = lmtzr.lemmatize(tok,'v') #lemmatization on each word is done
        if tok in emotion_dict:
            emotion_string += " " + emotion_dict[tok]
    return emotion_string

#returns the emotion which occurs the most
def get_best_emotion(emotion_string):
    if len(emotion_string) > 0:  
        number_tokens = emotion_string.strip().split()
        emo_list = [0] * 5
        for tok in number_tokens:
            emo_list[int(tok) - 1] += 1
        max_emo = max(emo_list)
        max_elem_idx = [i for i, j in enumerate(emo_list) if j == max_emo]
        return (max_elem_idx[0] + 1)
    else:
        return 2 #otherwise returns sad emotion reference

#finding strongest emotions
# 2= sad
# 3= fear
# 4= anger
# 5= disgust
# a collaboration of sentiment anaysis and the tokenized distionary
def emotion_detect_dictionary(input_string,emotion_detected):
    emotion_string = retrieve_emotion(input_string).split()
    emotion_detected = emotion_detected.split()
    label = emotion_detected[0]
    value = emotion_detected[1]
    value = float(value)
    emotion = ""
    if (label == "pos"):
        emotion = "happy"
    elif (label == "neutral"):
        emotion = "neutral"
    elif (label == "neg"):
        emo_string = retrieve_emotion(input_string)
        emo_num = get_best_emotion(emo_string) 
        if(emo_num == 2):
            emotion = "sad"
        elif(emo_num == 3):
            emotion = "fear"
        elif(emo_num == 4):
            emotion = "anger"
        elif(emo_num == 5):
            emotion = "disgust"
    return emotion

#decides which art to be build for the input tweet
def process_art(api):
    while True:
        l = api.home_timeline()
        top = l[0]
        if (top.id != l[1].id and ("https://" not in top.text)):
            input_string = top.text
            emotion_detected = sentiment_analysis(input_string)
            emotion = emotion_detect_dictionary(input_string,emotion_detected)
            if(emotion == "happy"):
                generate_happy_art()
            elif(emotion == "sad"):
                generate_sad_art()
            elif(emotion == "neutral"):
                generate_neutral_art()
            elif(emotion == "fear"):
                generate_fear_art()
            elif(emotion == "anger"):
                generate_anger_art()
            elif(emotion == "disgust"):
                generate_disgust_art()
            post_twitter(api)
        time.sleep(60)

#post art on twitter
def post_twitter(api):
    folder = "Your_directory_path/final_image.png"
    api.update_with_media(folder, status='Your words in art!')

#main function
def main():
    api = authenticate_twitter_handle()
    process_art(api)
    

if __name__=="__main__":
    main()
