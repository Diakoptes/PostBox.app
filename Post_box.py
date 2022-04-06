class MailBox:
    """
    Smart MailBox initialization
    :param name: mailbox device name       
    :param owner_email: email used for notification
    """
    
    def __init__(self, owner_email):
        self.is_blocked = False # self.get_postbox_status("is_blocked")
        self.letters_quantity = 0
        self.max_quota = 100
        self.owner_email = owner_email
    
    def voice_message(self, message):
        """Informs postman about spam and overload"""
        
        return message

    def is_spam(self, status):
        """Checks whether the letter is on the spam list"""
        
        return status    

    def send_notification(message):
        """Sends notification about letters quantity and new letters."""
        
        return message

    def new_letter(self):
        """
        Informs postman about the postbox is blocked,
        informs postman about a letter is spam,
        sends notification to user and starts voice message to postman, about quota exceeded and postbox blocked,
        """

        if self.is_blocked == True:
            self.voice_message("postbox is blocked")
            self.send_notification("Letters quota is exceeded.") 
            pass

        if self.is_spam() == True:
            self.voice_message("spam")
            self.is_blocked = True
            pass

        if self.is_quota_exceeded() == True:
            self.send_notification("Letters quota is exceeded.")
            self.is_blocked = True
            pass

        if self.is_spam == False and self.is_quota_exceeded() == False:
            self.is_blocked == False
            self.quantity_letters += 1
            self.send_notification("You have a new letter.")
            self.is_quota_exceeded()
            pass
      
    def is_quota_exceeded(self):
        """Checks how many slots there is for letter."""
        
        if self.quantity_letters >= self.max_quota * 0.8:
            self.send_notification("Postbox  almost full you have less than 20 percent.")
            return False

        elif self.quantity_letters > self.max_quota * 0.5:
            self.send_notification("Your postbox is full more than fifty percent.")
            return False
        
        elif self.quantity_letters == self.max_quota:
            return True
        else:
            return False

    def get_postbox_status(self, feature):
        """In the future check GPIO pin and ask for block mechanism status"""
        
        if feature == "is _blocked":
            return False