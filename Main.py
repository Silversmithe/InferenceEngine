import part3
from part2 import InferenceEngine
import part2
import part1

if __name__ == '__main__':
    ask = ['d']
    result = None

    engine = part2.InferenceEngine()
    engine.tell(['implies', 'a', 'b'])
    engine.tell(['implies', 'b', 'c'])
    engine.tell(['a'])

    result = engine.ask(ask)

    engine.display_progress()
    print "\nasking: ", ask, " ---> ", result
