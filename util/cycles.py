"""
Evolve states and detect cycles.
"""

import copy
import itertools

def evolve_n(state, update, n):
    """
    nth value from update(state)
    """
    for i in range(n):
        state = update(state)
    return state

def eat_n(gen, n):
    """
    nth value from generator
    """
    for i in range(n-1):
        next(gen)
    
    return next(gen)

def make_generator(state, transition_func, reps=None):
    """
    state + update_func --> generator
    """
    if reps:
        iter = range(reps)
    else:
        iter = itertools.count()

    for _i in iter:
        state = transition_func(state)
        yield state

def detect_constant(state, transition_func, scoring_func=lambda x: x, threshhold=100):
    """
    iterate transition func until steady state seen
    """
    generation = 0
    last_state = None
    steady_count = 0

    while steady_count < threshhold:
        (last_state, state) = (copy.deepcopy(state), transition_func(state))
        generation += 1

        if scoring_func(last_state) == scoring_func(state):
            steady_count += 1
        else:
            steady_count = 0


    return generation, scoring_func(state)


def detect_cycle(state, transition_func, scoring_func=lambda x: x):
    """
    iterate transition func until duplicate seen

    start - first generation to repeat (start of cycle)
    end - generation where 1st dup seen (end of cycle)
    len - length of cycle
    s0 - first state of repeat


               start
               end
    0 --- 1 --- 2/9 --- 3 --- 4 
                |             |
                |             5
                8             /
                \\ -- 7 -- 6 -/

    """
    seen = {}
    generation = 0    

    while scoring_func(state) not in seen:
        seen[scoring_func(state)] = generation

        state = transition_func(state)
        generation += 1


    return {
        'start': seen[scoring_func(state)],
        'end': generation,
        'len': generation - seen[scoring_func(state)],
        's0': state,
        'tx': transition_func,
    }

def detect_cycle_it(it):
    """
    advance generator until duplicate seen
    """
    seen = {}
    found = False

    for (generation, state) in enumerate(it):
        if state in seen:
            found = True
            break
        seen[state] = generation

    return {
        'start': seen[state],
        'end': generation,
        'len': generation - seen[state],
        's0': state,
        'found': found
    }


def predict_cycle(cycle_info, target_ix):
    """
    predict nth value from detected cycle
    """
    offset = (target_ix - cycle_info['start']) % cycle_info['len']

    state = cycle_info['s0']
    for _i in range(offset):
        state = cycle_info['tx'](state)

    return state

def predict_cycle_it(cycle_info, target_ix, it):
    """
    predict nth value from detected cycle (generator)
    """
    offset = (target_ix - cycle_info['start']) % cycle_info['len']

    for _i in range(cycle_info['start']):
        next(it)

    for _i in range(offset):
        state = next(it)
    
    return state
               


