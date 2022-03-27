class MailBox:
    """
    Smart MailBox initialization
    :param name: mailbox device name       
    :param owner_email: email used for notification
    """
    
    def __init__(self, name, owner_email):
        
        self.name = name
        self.quantity_letters = 80
        self.owner_email = owner_email
        self.notification_type = ""
        self.lock_check = ""
        
    """
    Notifications from the app
    """ 
    
    def send_notification(self, notification_type) -> None:
        """
        Send notification to the owner with specific information
        :param self:
        :param notification_type: Type of notification eg. 
            new_letter, _letter, _overload,brake_in
        :return: None
        """
        if notification_type == "new_letter":
            print(f"You have new letter in mailbox: {self.name}")
            print(f"Email sent to {self.owner_email}")
        elif notification_type == "_overload":
            print(f"{self.name} is overload")
            print(f"Email sent to {self.owner_email}")
        elif notification_type == "brake_in":
            print(f"breaking into the {self.name}")
            print(f"Email sent to {self.owner_email}")
            
    def receive_letter(self) -> None:
        """
        MailBox send notification to user when it has got new letter
        :param self:
        :return: None
        """
        self.quantity_letters += 1
        self.send_notification("new_letter")    
        
    def mail_box_overload_condition(self) -> None:
        """
        Notification about overload, max = 100 letters.
        """
    
        if self.quantity_letters >= 80 and self.quantity_letters <= 99:
            print(f"In your mailbox is only " + str(100-self.quantity_letters) + " slots.")
            self.send_notification("_overload")   
        elif self.quantity_letters == 100:
            print("Your mailbox is full, post office can't deliver you any message!")
            print(f"Email sent to {self.owner_email}")
            self.send_notification("_overload")   
        else:
            pass
    
    def lock_(self):
        """Mailbox is close."""
        pass
    
    def open_(self):
        """Mailbox is open."""
        pass
    
    def lock_check(self) -> None:
        """
        Notification about unauthorized open.
        """
        pass
    
        
    """
    User funcionality
    """
    
    def get_letter(self):
        """when you pick up the letter from the mailbox"""
        self.quantity_letters -= 1
