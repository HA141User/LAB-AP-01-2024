class SecretCode:
    def __init__(self): #Memanggil self.code
        self.code = 0
    def get_code(self):
        try:
            return self.code
        except Exception as e:
            print(f"Error getting code: {e}")
            return None
    def set_code(self, new_code):
        try:
            self.code = new_code
        except Exception as e:
            print(f"Error setting code: {e}")