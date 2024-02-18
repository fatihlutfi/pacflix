from datetime import datetime
from dateutil.relativedelta import relativedelta

class pacflix():
    list_of_referral_code = []
    
    
    def __init__(self, user_name):
        self.user_name = user_name
        self.start_date = None
        self.end_date = None
        self.current_plan = None
        self.duration = 0
        
        pacflix.list_of_referral_code.append(self.user_name)
        print( f"Your account succsessfully created, share this code '{self.user_name}' to your friend")
        
    def list_plan(self):
        print("List of Paccflix Plan")
        print("1. Basic Plan")
        print("SD, 1 Device, Movie, 120000")
        print()
        print("2. Standard Plan.")
        print("HD, 2 Device, Movie + Sport, 160000")
        print()
        print("3. Premium Plan.")
        print("UHD, 4 Device, Movie + Sport + Original, 200000")
        
    def chek_plan(self):
        if (self.current_plan == None):
            print("You do not have any subs yet.")
        else:
            print(f"your current plan is {self.current_plan}")
            print(f"Start Subs at {self.start_date}")
            print(f"End subs at {self.end_date}")
            
    def purchase(self, new_plan, ref_code, duration):
        total_price = 0
        
        if ((ref_code != None) and ref_code in pacflix.list_of_referral_code):
            self.duration = duration
            self.start_date = datetime.now()
            self.end_date = self.start_date + relativedelta (months = duration)
            
            if new_plan == "Basic Plan":
                self.current_plan = "Basic Plan"
                total_price = (120000-(120000*0.04))
                print(f"You're selected Basic Plan with referral code from {ref_code}, price {total_price}")
                
            elif new_plan == "Standard Plan":
                self.current_plan = "Standard Plan"
                total_price = (160000-(160000*0.04))
                print(f"You're selected Standard Plan with referral code from {ref_code}, price {total_price}")
            elif new_plan == "Premium Plan":
                self.current_plan = "Premium Plan"
                total_price = (200000-(200000*0.04))
                print(f"You're selected Premium Plan with referral code from {ref_code} , price {total_price}")
            else:
                self.duration = 0
                self.start_date = None
                self.end_date = None
                print("Your Plan not Valid!")
            
        elif ((ref_code != None) and ref_code not in pacflix.list_of_referral_code):
            print("Your referral code is not valid!")
            
        elif(ref_code == None):
            self.duration = duration
            self.start_date = datetime.now()
            self.end_date = self.start_date + relativedelta (months = duration)
            
            if new_plan == "Basic Plan":
                self.current_plan = "Basic Plan"
                total_price = 120000
                print(f"You're selected Basic Plan, price {total_price}")
                
            elif new_plan == "Standard Plan":
                self.current_plan = "Standard Plan"
                total_price = 160000
                print(f"You're selected Standard Plan, price {total_price}")
                
            elif new_plan == "Premium Plan":
                self.current_plan = "Premium Plan"
                total_price = 200000
                print(f"You're selected Premium Plan, price {total_price}")
            else:
                self.duration = 0
                self.start_date = None
                self.end_date = None
                print("Your Plan not Valid!")
                
        else:
            print ("Something bad happend")
            
    def upgrade_plan(self, new_plan ):
        subs_time = self.end_date - datetime.now()
        total_price = 0
        
        if (subs_time.days > 360):
            if (self.current_plan == "Basic Plan"):
                if (new_plan == "Standard Plan"):
                    self.current_plan = "Standart Plan"
                    total_price = (160000 - (160000 * 0.5))
                    print(f'Upgrade to {self.current_plan}, price + discount {total_price}')
                    
                elif (new_plan == "Premium Plan"):
                    self.current_plan = "Premium Plan"
                    total_price = (200000 - (200000 * 0.5))
                    print(f'Upgrade to {self.current_plan}, price + discount {total_price}')
                    
                else:
                    print("Your selected new plan invalid")                    
                    
            elif (self.current_plan == "Standard Plan"):
                if(new_plan == "Premium Plan"):
                    self.current_plan = "Premium Plan"
                    total_price = (200000 - (200000 * 0.5))
                    print(f'Upgrade to {self.current_plan}, price + discount {total_price}')
                else:
                    print("Your selected new plan invalid")
                
            else:
                print("You're in highest tier, you can't down grade")
                
        else:
            if (self.current_plan == "Basic Plan"):
                if (new_plan == "Standard Plan"):
                    self.current_plan = "Standart Plan"
                    total_price = 160000
                    print(f'Upgrade to {self.current_plan}, price {total_price}')
                    
                elif (new_plan == "Premium Plan"):
                    self.current_plan = "Premium Plan"
                    total_price = 200000
                    print(f'Upgrade to {self.current_plan}, price {total_price}')
                    
                else:
                    print("Your selected new plan invalid")                    
                    
            elif (self.current_plan == "Standard Plan"):
                if(new_plan == "Premium Plan"):
                    self.current_plan = "Premium Plan"
                    total_price = 200000
                    print(f'Upgrade to {self.current_plan}, price {total_price}')
                else:
                    print("Your selected new plan invalid")
                
            else:
                print("You're in highest tier, you can't down grade") 