# Reinforcement-Learning-MAB

## About
Independent project done as part of EECE490W course (Intro to RL) taught at POSTECH. In this assignment, we were supposed to design our game and implement the multi-armed bandit algorithm to train an agent on this *game*. The rules for the same were as follows:
1.	Create your own arbitrary environment for a single agent. 
2.	There should be more than five possible actions among each state. 
3.	Use a win/lose (or termination) rule. 
4.	Every win or lose should be determined right after an executed action (example: rock-scissors-paper game.)
5.	Design the opponent or environment reasonably (the environment could act simply but it must not be foolish).

For my project, the topic I chose was speed dating. More specifically, the algorithm, with different policies, will slightly/strongly nudge a person putting effort into pursuing a partner. I believe this is suitable because the gambler (person) has initially no knowledge about the machine (partner), there are >= 5 choices at every state and there is a good scope of trade-off between exploitation and exploration

## Execution
One simply needs to run ```python main.py``` to execute experiments and trial according to the agent and policies as defined in the file ```main.py```, and generate appropriate graphs dictating number of times an optimal choice was made 

## Author
Vansh Gupta: https://github.com/V-G-spec

## License
Copyright -2020 - Indian Institute of Technology, Delhi

Part of course EECE490W: Introduction to Reinforcement Learning
