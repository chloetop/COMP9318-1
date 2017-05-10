## import modules here
import pandas as pd
from math import log 
################# Question 1 #################

raw_data = pd.read_csv('./asset/data.txt', sep='\t')
def tokenize(sms):
    return sms.split(' ')

def get_freq_of_tokens(sms):
    tokens = {}
    for token in tokenize(sms):
        if token not in tokens:
            tokens[token] = 1
        else:
            tokens[token] += 1
    return tokens

training_data = []
for index in range(len(raw_data)):
    training_data.append((get_freq_of_tokens(raw_data.iloc[index].text), raw_data.iloc[index].category))
sms='I am not spam'


def multinomial_nb(training_data, sms):# do not change the heading of the function
    pass # **replace** this line with your code
    Dic_total={}
    Dic_spam={}
    Dic_ham={}
    N_ham=0
    N_spam=0
    N_total=len(training_data)
    for index in range(len(training_data)):
                if(training_data[index][-1]=='spam'):
                        N_spam+=1
                        Dic_spam.update(training_data[index][0])
                        Dic_total.update(training_data[index][0])
                elif (training_data[index][-1]=='ham'):
                        N_ham=N_ham+1
                        Dic_ham.update(training_data[index][0])
                        Dic_total.update(training_data[index][0])       
    spam_prior=N_spam/float(N_total)
    ham_prior=N_ham/float(N_total)
    cond_prob = {'spam': {}, 'ham': {}}
    score_spam=spam_prior
    score_ham=ham_prior
    len_spam=len(Dic_spam)
    len_ham=len(Dic_ham)
    len_total=len(Dic_total)
    print(len_spam)
    for term in Dic_total:
        try:
            term_spam_count=Dic_spam[term]
            #print(term,term_spam_count)
            cond_prob['spam'][term]= (term_spam_count+1)/float(len(Dic_spam)+len_total)
        except KeyError:
            pass
    for term in Dic_total:
        try:
            term_ham_count=Dic_ham[term]
            #print(term_ham_count)
            cond_prob['ham'][term] = (term_ham_count+1)/float(len(Dic_ham)+len_total)
        except KeyError:
            pass
    likehood=cond_prob
    for term in sms:
            try:
                score_spam *=likehood['spam'][term]
               # print(term,score_spam)
            except KeyError as e:
                score_spam*=1/float(len(Dic_spam)+len_total)
            try:
                score_ham *=likehood['ham'][term]
                #print('ham',score_ham)
            except KeyError as e:
                score_ham*=1/float(len(Dic_ham)+len_total)
    ratio= score_spam/score_ham
    return ratio


    
print(multinomial_nb(training_data, tokenize(sms)))


