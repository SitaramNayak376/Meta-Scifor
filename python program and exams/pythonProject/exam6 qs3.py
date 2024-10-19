class Nokia1:
    def __init__(self):
        self.model = "Nokia 1"
    def make_call(self):
        print("Making a call from Nokia 1")
    def send_sms(self):
        print("Sending SMS from Nokia 1")
class Nokia2(Nokia1):
    def __init__(self):
        super().__init__()
        self.model = "Nokia 2"
    def make_call(self):
        print("Making a call from Nokia 2 with improved audio quality")
    def send_sms(self):
        print("Sending SMS from Nokia 2 with better typing experience")
    def take_photo(self):
        print("Taking photo with Nokia 2")
class Nokia3(Nokia2):
    def __init__(self):
        super().__init__()
        self.model = "Nokia 3"
    def make_call(self):
        print("Making a call from Nokia 3 with HD voice quality")
    def send_sms(self):
        print("Sending SMS from Nokia 3 with predictive text")
    def take_photo(self):
        print("Taking high-resolution photo with Nokia 3")
    def browse_internet(self):
        print("Browsing internet on Nokia 3")

class Nokia4(Nokia3):
    def __init__(self):
        super().__init__()
        self.model = "Nokia 4"
    def make_call(self):
        print("Making a call from Nokia 4 with noise-cancellation technology")
    def send_sms(self):
        print("Sending SMS from Nokia 4 with enhanced security")
    def take_photo(self):
        print("Taking ultra-high-definition photo with Nokia 4")
    def browse_internet(self):
        print("Browsing internet on Nokia 4 with 5G support")
    def use_virtual_reality(self):
        print("Using Virtual Reality feature on Nokia 4")
def demonstrate_phone_features(phone):
    print(f"Model: {phone.model}")
    phone.make_call()
    phone.send_sms()
    if hasattr(phone, 'take_photo'):
        phone.take_photo()
    if hasattr(phone, 'browse_internet'):
        phone.browse_internet()
    if hasattr(phone, 'use_virtual_reality'):
        phone.use_virtual_reality()
    print()

nokia1 = Nokia1()
nokia2 = Nokia2()
nokia3 = Nokia3()
nokia4 = Nokia4()

demonstrate_phone_features(nokia1)
demonstrate_phone_features(nokia2)
demonstrate_phone_features(nokia3)
demonstrate_phone_features(nokia4)
