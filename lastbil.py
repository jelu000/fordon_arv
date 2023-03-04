#Detta är en klass som ärver fordon och man kan skapa egna Objekt av
class Lastbil:
    

    #constructor körs först när klass objektet initieras
    def __init__(self, flakvolym):
        self.flakvolym = flakvolym
        
        
    #funktioner som tillhör en klass kallas för metoder=Metods"
    def set_flakvolym(self, flakvolym):
        self.flakvolym = flakvolym

    def get_flakvolym(self):
        return self.flakvolym
    