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
    # engine.display_progress()
    # print "\nasking: ", ask, " ---> ", result
    given = ['or', ['and', 'a', 'd'], 'b', ['not', ['not', 'c']]]
    print part3.__search_and_convert__(given, part2.__not__)
