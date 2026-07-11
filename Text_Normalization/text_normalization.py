## while creating the object, first it call __new___ magic methods and then __init__
class Textnormalization:
    def __init__(self,data):
        self.data=data
        self.start()
    #     self.normalizedtext()
    # def normalizedtext(data):
    def start(self):
        
        print("""
              1. converting strings to lower case
              2. removing puntuations
              3. Removing Spl Characters
              4. Handling emojis( sentimental demojize/ replace text)
              5. Removing extra space
              6. contractions or Expanding the words/ Abbrevations
              7. Correcting the words 
               """)
        
        
    def str_lowercase(self,data):
        # should return updated text
        self.data=self.data.lower()
        print(1.--------)
        self.string_lowercase()
        opti_puntuation(input("enter yes or no"))
        if op_puntu=="yes"
    def remove_puntuation(self,data):
        chars=self.data
        import string
        if 
        puntuations=string.puntuations
        for char in puntuations:
            chars=chars.replace(char,"")
        self.data=chars # this is updating data  or we can use return keyword
        
        
        
    def remove_splchars(self,data):
        
        chars=self.data
        for char in chars:
            if not char.isalnum() and not ord(char)==32: # expect this remove 
                chars=chars.replace(char,"")
        self.data=chars
                
                
                
    def handle_emojis(self,data):
        pass
    
    
    def contractions(self,data):
        pass
    
    
    def correct_the_words(self,data):
        pass


obj=Textnormalization("corrcting wods inn the txt noemalixztionn")
obj.str_lowercase())