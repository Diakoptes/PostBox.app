"""This is a mailbox app"""

class MailBox():
    
    def __init__(self, name):
        
        self.name = name
        self.quantity_letters = 80
        self.letters = []
        self.box_history = []
        
    """Notifications from the app""" 
    """----------------------"""

    """MailBox send notification to user when it has got new letter."""      
    def receive_message(self):
        
        print(f"You have one new message from {self.name}.")
        self.quantity_letters += 1
        self.letters.append((self.name))
        self.box_history.append((self.name))
        print(f"You have {self.quantity_letters} deliverd letters.")
        print("Do you want to see every deliverd letters?")
        choice = input("yes/no:" )
        if choice == "yes":
            for m in self.letters:
                print(m)
                break
        else:
            pass

    """Notification about overload, max = 100 letters."""
        
    def mail_box_overload_condition(self):
        
        if self.quantity_letters >= 80 and self.quantity_letters <= 99:
            print(f"In your mailbox is only " + str(100-self.quantity_letters) + " slots.")
        elif self.quantity_letters == 100:
            print("Your mailbox is full, post office can't deliver you any message!")
        else:
            pass
        
    """Notification about unauthorized open."""
    
    def open_box_without_authorization():
        
        burglary = False

        while burglary:
            """Postbox sending message to security and user"""
            print("ALARM!")
            break
        else:
            pass
            #print("Everything it's fine.")
        
    """User funcionality"""
    """-----------------"""

    """When user pick up the letter"""
    def get_the_letter(self):
        self.letters.pop((self.name))
        self.quantity_letters -= 1

    """Searching specyfic name."""
    def search_specyfic_message(self):
        search = input("search: ")
        if search in self.box_history:
            print("You picked up those letter.")
        elif search in self.letters:
            print("It's waiting for you.")
        else:
            print("There is no such letter.")
    
    """Full history."""
    def full_history(self):
        for letter in self.box_history:
            if letter in self.letters:
                print(f"{letter} *unpicked")
            else:
                print(f"{letter} *picked")
    
    """User could indicate letters for delete without read. 
    Even if postman doesn't have any letters for user it come and removes them."""
    def delete_letter(self):

        print("You can remove letter whitout receive")

        for letter in self.letters: print(letter)
        remove_letter = input("Chose letter to remove: ")
        
        if remove_letter in self.letters:
            self.letters.remove(remove_letter)
            print("done")
        else:
            print("Give a correct name.") 
