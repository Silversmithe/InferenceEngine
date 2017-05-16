import InferenceEngine
import Resolution

if __name__ == '__main__':
    engine = InferenceEngine.InferenceEngine()
    engine.tell(['or', 'a', 'b'])
    engine.tell(['or', ['not', 'b']])
    print "\n", engine.ask(['not', 'a']), "\n"
    # engine.display_progress()

