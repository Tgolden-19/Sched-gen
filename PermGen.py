"""
Created by Tristan Golden
Date created: 12/22/20
The purpose of this exercise is to find the ideal number of permutations of a am+pm schedule for a single person
and also to reveal exactly what all possibilities would look like
"""

perms = [[0] * 7] * 2187
shift = 0     # bounds are 0-2 0 = off, 1 = am, 2 = pm
count = 0

def checkval(shift):
    """
    :param: val = the value deciding which shift
    :return: returns the reset value of shift decider after it has been reset (resets to 0)
    checks the shift decider value to see if it went out of bounds
    bounds are 0-2 0 = off, 1 = am, 2 = pm
    """
    if shift > 2 or shift < 0:
        shift = 0
    return shift

def gen_perms(perms):
    """
    Generates a completely new permutation of a weekly schedule
    :param perms: 2d array of permutations
    :return: new permutation that has not already appeared in the set
    """
    row = 0
    col = 0
    shift = 0  # bounds are 0-2 0 = off, 1 = am, 2 = pm



# def checkrep(perms, row , col):
#     """
#     Checks if the current permutation at index stated is going to turn out to be a repetition of an older permutation
#     :param perms: array where the permutations are kept
#     :param row: index of the row where current value is being placed
#     :param col: index of col where current value is being placed
#     :return: True if permutation is going to be a repetition at current index
#     """

def compareperm(perms, currperm):
    """
    checks a permutation against older permutation from a permutation history (perms)
    :param perms: 2d array of permutations
    :param currperm: Array of current permutation to be compared to another
    :return: True if permutation is not new
    """
    for i in perms:
        for j in range(len(i)):
            if currperm[j] == i[j]:
                return False
    return True





def printperms(perms):
    for i in perms:
        print(str(i) + "\n")



# -----------------------------------------------------restructure on 12/23/21 12:11pm ----------------------------------------------------

