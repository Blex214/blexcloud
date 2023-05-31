import PySimpleGUI as sg
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import pandas as pd


def plot_word_cloud(words):
    print('Plotting...')
    stopwords=set(STOPWORDS)
    comment_words=''
    for val in words:
        val = str(val)
        tokens = val.split()
        for i in range(len(tokens)):
            tokens[i] = tokens[i].lower()
        
        comment_words += " ".join(tokens)+" "
    
    wordcloud = WordCloud(width = 800, height = 800,
                background_color ='white',
                stopwords = stopwords,
                min_font_size = 10).generate(comment_words)
    plt.imshow(wordcloud, interpolation = 'nearest') 
    plt.axis('off')
    return plt.show()