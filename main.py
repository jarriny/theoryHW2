from dfa import dfa
from transition import transition
import sys


def main(args):
    def main():
        states = {'q1', 'q2', 'q3'}
        alpha = {'0', '1'}
        transitions = {transition('q1', '0', 'q1'),
                       transition('q1', '1', 'q2'),
                       transition('q2', '0', 'q3'),
                       transition('q2', '1', 'q2'),
                       transition('q3', '0', 'q2'),
                       transition('q3', '1', 'q2')}
        start = 'q1'
        accept = {'q2'}
        fig_14 = dfa(states, alpha, transitions, start, accept)
        query = sys.stdin.read()

        

    if __name__ == "__main__":
        main()