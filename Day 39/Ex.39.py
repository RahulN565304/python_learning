class Instrument:
    def __init__(self, name):
        self.name = name
        
    def play(self):
        print("Instrument is playing")
        
class StringInstrument(Instrument):
    def tune(self):
        print("Tuning strings")
        
class PercussionInstrument(Instrument):
    def beat(self):
        print("Beating rhythm")
        
class Guitar(StringInstrument):
    def play(self):
        print("Strumming the guitar")
        
class Drum(PercussionInstrument):
    def play(self):
        print("Hitting the drum")
        
class Piano(StringInstrument, PercussionInstrument):
    def play(self):
        print("Playing the piano")
        
guitar = Guitar("Yamaha Guitar")
drum = Drum("Roland Drum")
piano = Piano("Steinway Piano")

guitar.play()
guitar.tune()
drum.play()
drum.beat()
piano.play()
piano.tune()
piano.beat()