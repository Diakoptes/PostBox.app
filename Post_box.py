class MailBox:
    """
    Smart MailBox automation class
    """
    
    def __init__(self, name, owner_email):
        
        self.name = name
        self.quantity_letters = 80
        self.owner_email = owner_email
        
    """Notifications from the app""" 
    """----------------------"""
    
    def send_notification(self, notification_type) -> None:
        """
        Send notification to the owner with specific information
        :param self:
        :param notification_type: Type of notification eg. new_letter, _letter,
        :return: None
        """
        if notification_type == "new_letter":
            print(f"You have new letter in mailbox: {self.name}")
            print(f"Email sent to {self.owner_email}")
    
    def receive_letter(self) -> None:
        """
        MailBox send notification to user when it has got new letter
        :param self:
        :return: None
        """
        self.quantity_letters += 1
        self.send_notification("new_letter")
        
    def mail_box_overload_condition(self):
    """Notification about overload, max = 100 letters."""
    
        if self.quantity_letters >= 80 and self.quantity_letters <= 99:
            print(f"In your mailbox is only " + str(100-self.quantity_letters) + " slots.")
        elif self.quantity_letters == 100:
            print("Your mailbox is full, post office can't deliver you any message!")
        else:
            pass
        
    
    
    def open_box_without_authorization():
    """Notification about unauthorized open."""
    
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
    
    def get_the_letter(self):
    """When user pick up the letter"""
        
        self.letters.pop((self.name))
        self.quantity_letters -= 1

    def search_specyfic_message(self):
    """Searching specyfic name."""
    
        search = input("search: ")
        if search in self.box_history:
            print("You picked up those letter.")
        elif search in self.letters:
            print("It's waiting for you.")
        else:
            print("There is no such letter.")
    
    def full_history(self):
    """Full history."""
    
        for letter in self.box_history:
            if letter in self.letters:
                print(f"{letter} *unpicked")
            else:
                print(f"{letter} *picked")
    
    def delete_letter(self):
    """User could indicate letters for delete without read. 
    Even if postman doesn't have any letters for user it come and removes them."""
    
        print("You can remove letter whitout receive")

        for letter in self.letters: print(letter)
        remove_letter = input("Chose letter to remove: ")
        
        if remove_letter in self.letters:
            self.letters.remove(remove_letter)
            print("done")
        else:
            print("Give a correct name.") 
