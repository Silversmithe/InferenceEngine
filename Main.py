import InferenceEngine

if __name__ == '__main__':
    engine = InferenceEngine.InferenceEngine()
    engine.tell(['or', 'a', 'b'])
    engine.tell(['or', ['not', 'b']])
    engine.ask(['a'])
    engine.display_progress()
