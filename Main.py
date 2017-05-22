import part3
import part2
import part1

if __name__ == '__main__':
    # ask = ['c']
    # result = None
    #
    # engine = part2.InferenceEngine()
    # engine.tell(['or', ['not', 'a'], 'b'])
    # engine.tell(['or', ['not', 'b'], 'c'])
    # engine.tell(['a'])
    #
    # result = engine.ask(ask)
    #
    # print "\nasking: ", ask, " ---> ", result
    # engine.display_progress()

    given = ['not', ['or', 'a', 'b', ['not', 'c']]]

    print part3.__demorgan__(given)
