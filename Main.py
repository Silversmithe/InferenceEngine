import part2
import part1

if __name__ == '__main__':
    ask = ['d']
    result = None

    engine = part2.InferenceEngine()
    engine.tell(['or', ['not', 'a'], 'b'])
    engine.tell(['or', ['not', 'b'], 'c'])
    engine.tell(['a'])

    result = engine.ask(ask)

    print "\nasking: ", ask, " ---> ", result
    # engine.display_progress()
