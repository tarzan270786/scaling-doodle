class NFA:
    def __init__(self):
        self.num_states = 0
        self.states = []
        self.symbols = []
        self.num_accepting_states = 0
        self.accepting_states = []
        self.start_state = 0
        self.transition_functions = []


    def init_states(self):
        self.states = list(range(self.num_states))


    def print_nfa(self):
        print("No. of states:",self.num_states)
        print("States:",self.states)
        print("Symbols:",self.symbols)
        #print("No. of accepting states:",self.num_accepting_states)
        print("Accepting states:",self.accepting_states)
        print("Start state:",self.start_state)
        print("Transitions:",self.transition_functions)


    def construct_nfa_from_file(self, lines):
        self.num_states = int(lines[0])
        self.init_states()
        self.symbols = list(lines[1].strip())

        accepting_states_line = lines[2].split(" ")
        for index in range(len(accepting_states_line)):
                self.accepting_states.append(int(accepting_states_line[index]))
        self.num_accepting_states=len(self.accepting_states)
        self.startState = int(lines[3])
        
        
        for index in range(4, len(lines)):
            transition_func_line = lines[index].split(" ")
            
            starting_state = int(transition_func_line[0])
            transition_symbol = transition_func_line[1]
            ending_state = int(transition_func_line[2])
            
            transition_function = (starting_state, transition_symbol, ending_state);
            self.transition_functions.append(transition_function)        



class DFA:
    def __init__(self):
        self.num_states = 0
        self.symbols = []
        self.num_accepting_states = 0
        self.accepting_states = []
        self.start_state = 0
        self.transition_functions = []
        self.q = []
    
    
    def convert_from_nfa(self, nfa):
        self.symbols = nfa.symbols
        self.start_state = nfa.start_state

        nfa_transition_dict = {}
        dfa_transition_dict = {}
        
        for transition in nfa.transition_functions:
            starting_state = transition[0]
            transition_symbol = transition[1]
            ending_state = transition[2]
            
            if (starting_state, transition_symbol) in nfa_transition_dict:
                nfa_transition_dict[(starting_state, transition_symbol)].append(ending_state)
            else:
                nfa_transition_dict[(starting_state, transition_symbol)] = [ending_state]

        self.q.append((0,))
        
        for dfa_state in self.q:
            for symbol in nfa.symbols:
                if len(dfa_state) == 1 and (dfa_state[0], symbol) in nfa_transition_dict:
                    dfa_transition_dict[(dfa_state, symbol)] = nfa_transition_dict[(dfa_state[0], symbol)]
                    
                    if tuple(dfa_transition_dict[(dfa_state, symbol)]) not in self.q:
                        self.q.append(tuple(dfa_transition_dict[(dfa_state, symbol)]))
                else:
                    destinations = []
                    final_destination = []
                    
                    for nfa_state in dfa_state:
                        if (nfa_state, symbol) in nfa_transition_dict and nfa_transition_dict[(nfa_state, symbol)] not in destinations:
                            destinations.append(nfa_transition_dict[(nfa_state, symbol)])
                    
                    if not destinations:
                        final_destination.append(None)
                    else:  
                        for destination in destinations:
                            for value in destination:
                                if value not in final_destination:
                                    final_destination.append(value)
                        
                    dfa_transition_dict[(dfa_state, symbol)] = final_destination
                        
                    if tuple(final_destination) not in self.q:
                        self.q.append(tuple(final_destination))            
        for key in dfa_transition_dict:
            self.transition_functions.append((self.q.index(tuple(key[0])), key[1], self.q.index(tuple(dfa_transition_dict[key]))))
        
        for q_state in self.q:
            for nfa_accepting_state in nfa.accepting_states:
                if nfa_accepting_state in q_state:
                    self.accepting_states.append(self.q.index(q_state))
                    self.num_accepting_states += 1


    def print_dfa(self):
        print("No. of states:",len(self.q))
        print("Symbols:","".join(self.symbols))
        print("Accepting states:"," ".join(str(accepting_state) for accepting_state in self.accepting_states))
        print("Start state:",self.start_state)
        print("Transitions:")
        for transition in sorted(self.transition_functions):
            print(" ".join(str(value) for value in transition))

filename = input('Enter the name of the NFA file: ')
file = open(filename, 'r')
lines = file.readlines()
file.close()


nfa = NFA()
dfa = DFA()

nfa.construct_nfa_from_file(lines)
dfa.convert_from_nfa(nfa)
print("NFA:")
nfa.print_nfa()
print("\nDFA:")
dfa.print_dfa()
