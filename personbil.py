#Detta är en klass som ärver fordon och man kan skapa egna Objekt av
class Personbil:
    

    #constructor körs först när klass objektet initieras
    def __init__(self, bagagevolym):
        self.bagagevolym = bagagevolym
        
        
    #funktioner som tillhör en klass kallas för metoder=Metods"
    def set_bagagevolym(self, bagagevolym):
        self.bagagevolym = bagagevolym

    def get_bagagevolym(self):
        return self.bagagevolym
    
    