#!/usr/bin/env python3
import numpy as np
import pickle
import json
import pandas as pd

class Agent:
    def __init__(self, bandit, policy, gamma = None):
        self.policy = policy
        self.nA = bandit.nA
        self._value_estimates = np.zeros(self.nA)
        self.action_attempts = np.zeros(self.nA)
        self.t = 0
        self.last_action = None
        self.gamma = gamma

    def reset(self):
        self._value_estimates[:] = 0
        self.action_attempts[:] = 0
        self.last_action = None
        self.t = 0

    def choose(self):
        action = self.policy.choose(self)
        self.last_action = action
        return action

    def observe(self, reward):
        # define "la" to shorten code
        la = self.last_action
        self.action_attempts[la] += 1

        normalizer = self.gamma if self.gamma is not None \
                                else 1/self.action_attempts[la]

        # Q value of last action
        q_la = self._value_estimates[la]
        self._value_estimates[la] = q_la + normalizer*(reward - q_la)

    def __str__(self):
        return 'f/{}'.format(str(self.policy))

    @property
    def value_estimates(self):
        return self._value_estimates   
    
    
class DateBandit:

    def __init__(self, nA : int = 10, mode : str = "winloss", path: str = "dating_partial.pickle"):
        """
        params
            nA (int) : Number of Action
            mode (str) : Reward mode "winloss" or "dividend"
        return None
        """
        
        #######################################################
        #######################################################
        #######################################################
        
        df = pd.read_csv('speed-dating.csv')
        df['index1'] = df.index

        df['distinguisher'] = list(zip(df['sports'], df['tvsports'], df['exercise'], df['dining'], df['museums'], df['art'], df['hiking'], df['gaming'], df['clubbing'], df['reading'], df['tv'], df['theater'], df['movies'], df['concerts'], df['music'], df['shopping'], df['yoga']))

        df1 = df[['index1', 'distinguisher', 'd_age', 'samerace', 'pref_o_attractive', 'pref_o_intelligence', 'pref_o_funny', 'pref_o_shared_interests', 'attractive_o', 'intelligence_o', 'funny_o', 'shared_interests_o', 'attractive_partner', 'intelligence_partner', 'funny_partner', 'shared_interests_partner', 'interests_correlate', 'like', 'guess_prob_liked', 'match']]
        df1 = df1.fillna(df1.mean())
        
        df1['distinguisher2'] = df1['distinguisher'].apply(lambda x: '-'.join([str(i) for i in x]))
        # df1['sortType1'] = df1['interests_correlate']*(df1[['attractive_partner', 'attractive_o']].min(axis=1) + df1[['intelligence_partner', 'intelligence_o']].min(axis=1) + df1[['funny_partner', 'funny_o']].min(axis=1))
        df1['sortType1'] = df1['interests_correlate']*(df1['attractive_partner'] + df1['intelligence_partner'] + df1['funny_partner'])
        df1['sortType2'] = df1['interests_correlate']*df1[['like', 'guess_prob_liked']].min(axis=1)
        
        df1 = df1.drop('distinguisher', 1)
        
        races = df1.sort_values(['sortType1'],ascending=False).groupby('distinguisher2')[['index1', 'sortType1', 'sortType2', 'd_age', 'samerace', 'pref_o_attractive', 'pref_o_intelligence', 'pref_o_funny', 'pref_o_shared_interests', 'attractive_o', 'intelligence_o', 'funny_o', 'shared_interests_o', 'attractive_partner', 'intelligence_partner', 'funny_partner', 'shared_interests_partner', 'interests_correlate', 'like', 'guess_prob_liked', 'match']].apply(lambda x: x.set_index('index1').to_dict(orient='index')).to_dict()
        
        #######################################################
        #######################################################
        #######################################################
        
        self.mode = mode
        # with open(path, 'rb') as handle:
        #     races = json.load(handle, encoding= 'unicode_escape)
        datesg5 = []

        for person, partners in races.items():
            #print(races[person]==partners)
            if len(races[person]) >=5:
                datesg5.append(partners)
        
        self.races = datesg5
        self.nA = nA
        self.counter = 0

    def reset(self):
#        shuffled_index = np.random.permutation(np.arange(12))
#        shuffled_races = []
#        for race in self.races:
#            shuffled_races.append([race[idx] for idx in shuffled_index])
#        self.races = shuffled_races
        np.random.shuffle(self.races)
        self.counter = 0 

    def pull(self, action):
        """
        params:
            race (list): races[racecode], racecode (str)
            pick (int): race index
        """
        self.counter+=1
        #print(action)
        race = self.races[self.counter%len(self.races)]
        action = action+int(list(race.keys())[0])
        # print(list(race.keys())[0], action)
        if (action > int(list(race.keys())[-1])):
            return (0, False)
        # try: 
        if (race[action]['match'] == 1):
            # return (200, True) if self.mode == "winloss" else 20*(max(race[action]["like"], race[action]["guess_prob_liked"] - abs(race[action]["like"] - race[action]["guess_prob_liked"])), True) # win
            return (10, True) if self.mode == "winloss" else (1.7*min(race[action]["like"], race[action]["guess_prob_liked"]), True) # win

        # except KeyError:
        return (0, False) # lose
        
        # return (0, False) # lose
    
    
    
if __name__=="__main__":
    main()

