
import random
import argparse
import codecs
import os
import numpy
import numpy as np


# observations
class Observation:
    def __init__(self, stateseq, outputseq):
        self.stateseq  = stateseq   # sequence of states
        self.outputseq = outputseq  # sequence of outputs
    def __str__(self):
        return ' '.join(self.stateseq)+'\n'+' '.join(self.outputseq)+'\n'
    def __repr__(self):
        return self.__str__()
    def __len__(self):
        return len(self.outputseq)

# hmm model
class HMM:
    def __init__(self, transitions={}, emissions={}):
        """creates a model from transition and emission probabilities"""
        ## Both of these are dictionaries of dictionaries. e.g. :
        # {'#': {'C': 0.814506898514, 'V': 0.185493101486},
        #  'C': {'C': 0.625840873591, 'V': 0.374159126409},
        #  'V': {'C': 0.603126993184, 'V': 0.396873006816}}

        self.transitions = transitions
        self.emissions = emissions

    ## part 1 - you do this.
    def load(self, basename):

        # Initialize
        self.transitions = {}
        self.emissions = {}

        # Read transition probabilities
        with open(basename + '.trans') as f:
            for line in f:
                from_state, to_state, prob = line.split()

                if from_state == '#':
                    # Multiple initial states
                    if 'init' not in self.transitions:
                        self.transitions['init'] = {}
                    self.transitions['init'][to_state] = float(prob)

                else:
                    # Normal from state
                    if from_state not in self.transitions:
                        self.transitions[from_state] = {}
                    self.transitions[from_state][to_state] = float(prob)

        # Read emission probabilities
        with open(basename + '.emit') as f:
            for line in f:
                state, symbol, prob = line.split()
                if state not in self.emissions:
                    self.emissions[state] = {}
                self.emissions[state][symbol] = float(prob)

    ## you do this.
    def generate(self, n):

        states = []
        outputs = []

        # Initial state
        init_probs = list(self.transitions['init'].values())
        total = sum(init_probs)
        norm_init_probs = [x / total for x in init_probs]
        init_states = list(self.transitions['init'].keys())
        init_state = np.random.choice(init_states, p=norm_init_probs)
        states.append(init_state)

        # Generate sequence
        for i in range(n - 1):
            # Sample next state
            curr_state = states[-1]
            curr_state_probs = list(self.transitions[curr_state].values())
            total = sum(curr_state_probs)
            norm_curr_state_probs = [x / total for x in curr_state_probs]
            curr_state_states = list(self.transitions[curr_state].keys())
            next_state = np.random.choice(curr_state_states, p=norm_curr_state_probs)
            states.append(next_state)

            # Sample output
            output_probs = list(self.emissions[next_state].values())
            total = sum(output_probs)
            norm_output_probs = [x / total for x in output_probs]
            output_symbols = list(self.emissions[next_state].keys())
            output = np.random.choice(output_symbols, p=norm_output_probs)
            outputs.append(output)
        # print(Observation(states, outputs))
        return Observation(states, outputs)

    ## you do this: Implement the Viterbi alborithm. Given an Observation (a list of outputs or emissions)
    ## determine the most likely sequence of states.

    def forward(self, observation):
        # Initialize variables
        states = list(self.transitions['init'].keys())
        T = len(observation.outputseq)
        f = [{}]

        # Calculate initial forward probabilities
        for y in states:
            f[0][y] = self.transitions['init'][y] * self.emissions[y][observation.outputseq[0]]

        # Calculate forward probabilities for remaining outputs
        for t in range(1, T):
            f.append({})
            for y in states:
                f[t][y] = sum(
                    f[t - 1][y0] * self.transitions[y0][y] * self.emissions[y][observation.outputseq[t]] for y0 in
                    states)

        # Return final forward probabilities
        return f[-1]

    def viterbi(self, observation):
        """given an observation,
        find and return the state sequence that generated
        the output sequence, using the Viterbi algorithm.
        """


if __name__ == " __name__":
    parser = argparse.ArgumentParser(description='HMM model')
    parser.add_argument('--basename', default='two_english', help='basename for HMM model files')
    parser.add_argument('--n', type=int, default=20, help='number of output symbols to generate')
    args = parser.parse_args()

    model = HMM()
    model.load(args.basename)
    print(model.transitions)

    model.generate(args.n)
    print(model.transitions)

    model = HMM()
    model.load(args.basename)
    observations = model.generate(args.n)
    print(observations)
    probs = model.forward(observations)
    max_state = max(probs, key=probs.get)
    print(max_state)



