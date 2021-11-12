"""
https://leetcode.com/problems/push-dominoes/

There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

You are given a string dominoes representing the initial state where:

dominoes[i] = 'L', if the ith domino has been pushed to the left,
dominoes[i] = 'R', if the ith domino has been pushed to the right, and
dominoes[i] = '.', if the ith domino has not been pushed.
Return a string representing the final state.


Example 1:
Input: dominoes = "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.

Example 2:
Input: dominoes = ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."
"""


""""
Count the fouce of each brick

first round, counting the fouce to Right
second round, counting the force to Left

if 

"""


class Solution:
    def pushDominoes(self, dominoes):

        dos = list(dominoes)
        dolen = len(dos)
        forces = [0 for i in range(len(dos))]
        force = 0
        for i in range(len(forces)):
            # ! set to right forces
            if dos[i] == "R":
                force = dolen
            elif dos[i] == "L":
                force = 0
            else:
                force = max(force-1, 0)
            force[i] += force

        for i in range(len(forces)-1, -1, -1):
            # ! set to left forces
            if dos[i] == "L":
                force = dolen
            elif dos[i] == "R":
                force = 0
            else:
                force = max(force-1, 0)
            force[i] -= force

        s = []

        for i in range(len(forces)):
            if forces[i] > 0:
                s.append("R")
            elif forces[i] < 0:
                s.append("L")
            else:
                s.append(".")
        return "".join(s)


def pushDominoes(dominoes):

    dos = list(dominoes)
    dolen = len(dos)
    forces = [0 for i in range(len(dos))]
    force = 0
    for i in range(len(forces)):
        # ! set to right forces
        if dos[i] == "R":
            force = dolen
        elif dos[i] == "L":
            force = 0
        else:
            force = max(force-1, 0)
        forces[i] += force
    print(forces)
    for i in range(len(forces)-1, -1, -1):
        # ! set to left forces
        if dos[i] == "L":
            force = dolen
        elif dos[i] == "R":
            force = 0
        else:
            force = max(force-1, 0)
        forces[i] -= force

    s = []
    print(forces)
    for i in range(len(forces)):
        if forces[i] > 0:
            s.append("R")
        elif forces[i] < 0:
            s.append("L")
        else:
            s.append(".")
    return "".join(s)


pushDominoes(".L.R...LR..L..")