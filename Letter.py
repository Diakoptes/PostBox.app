class Letter(MailBox):
    """
    Creating letters and administration them
    :param consigner: it tells user who send a letter
    """
    def __init__(self, consignor):
        super().__init__(self, name, owner_email)
    
        self.consignor = consignor
    
    def postman_gives_letter(self):
        """
        postman scans envelope or writes name of consignor 
        to the application 
        this creates a new letter with name which tells
        user who send a letter.
        """
        Letter.receive_letter()
    
    def anty_spam(self):
        """
        With this method user can marks from whom 
        does not want receive letters.
        """
