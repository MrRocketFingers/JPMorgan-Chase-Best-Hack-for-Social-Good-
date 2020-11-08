import numpy as np #not used yet
from matplotlib import pyplot as plt #plot the histogram


#get more accurate salaries for better output
major_dic= {"Communication": 45,
            "Business": 50, "STEM": 65,
            "Education ": 45, "MD":250,
            "MBA": 100, "Liberal Arts": 40,
            "Law" : 95} #Major Inforation
#3 var... salary, debt, interst rate, year of graduation (depending on what the user puts in) 
#Histogram name = the key in dictionary
#var which equal salary to major * increase
#var which equal to debt * intreset
ages = [10,20]# sample 
bin_edges = [0,10,20,30,40,50,60,70,80,90,100]

plt.hist(ages, bins = 5, edgecolor ='black')
plt.show()


#x=years
#y= money
'''
def compute_histogram(self, image):
    """Computes the histogram of the input image
    takes as input:
    image: a grey scale image
    returns a histogram as a list"""
    hist = [0] * 256
    X, Y = image.shape

    for x in range(X):
        for y in range(Y):
            hist[int(image[x, y])] += 1

    return hist
    '''

# Make calculations for Charts.js
# Total Debt = (Loan Amount * Interest Rate) + Loan Amount
# How much does a student need to pay monthly? (the amount that covers the interest and principle)
