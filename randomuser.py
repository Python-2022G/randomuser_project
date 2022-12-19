
import requests
import datetime

class RandomUser:
    def __init__(self, url: str) -> None:
        self.url = url

    def get_user_with_year(self, year: int) -> dict:
        '''return user with year
        
        Args:
            year (int): year
            
        Returns:    
            dict: user
        ''' 
        while True:  
            r=requests.get(self.url) 
            if r.status_code==200:
                j=r.json()['results'][0]
                s=j["dob"]["date"]
                y=datetime.datetime.strptime (s[:-5], "%Y-%m-%dT%H:%M:%S")
                if y.year==year:
                    return j
                
        

    def get_user_with_month(self, month: int) -> dict:
        '''return user with month
        
        Args:
            month (int): month
            
        Returns:   
            dict: user
        '''
        while True:  
            r=requests.get(self.url) 
            if r.status_code==200:
                j=r.json()['results'][0]
                s=j["dob"]["date"]
                y=datetime.datetime.strptime (s[:-5], "%Y-%m-%dT%H:%M:%S")
                if y.month==month:
                    return j
                
        

    def get_user_with_day(self, day: int) -> dict:
        '''return user with day
        
        Args:
            day (int): day
            
        Returns:   
            dict: user
        '''
        while True:  
            r=requests.get(self.url) 
            if r.status_code==200:
                j=r.json()['results'][0]
                s=j["dob"]["date"]
                y=datetime.datetime.strptime (s[:-5], "%Y-%m-%dT%H:%M:%S")
                if y.day==day:
                    return j
                

    def get_user_with_weekday(self, weekday: int) -> dict:
        '''return user with weekday
        
        Args:
            weekday (int): weekday ex: Monday
            
        Returns:   
            dict: user
        '''
        while True:  
            r=requests.get(self.url) 
            if r.status_code==200:
                j=r.json()['results'][0]
                s=j["dob"]["date"]
                y=datetime.datetime.strptime (s[:-5], "%Y-%m-%dT%H:%M:%S")
                if y.weekday()==weekday:
                    return j

    def get_user_by_gender(self, gender: str) -> dict:
        '''return user by gender
        
        Args:
            gender (str): gender (female, male)
            
        Returns:     
            dict: user
        '''
        pass

    def write_users_to_file(self, file_path: str, gender: str, count: int) -> bool:
        '''write the data of count users whose gender is equal to the given gender to file_path

        Notes:
            1. user data: {"full_name": first+" "+last, "gender": gender, "age": age}
            2. you must use get_user_by_gender method
        
        Args:
            file_path (str): file path
            gender (str): gender (female, male)
            count (int): how many users
            
        Returns:   
            bool: True if it is ok otherwise False
        '''
        pass


user = RandomUser('https://randomuser.me/api/')
print(user.get_user_with_year(1984))
print(user.get_user_with_month(12))
print(user.get_user_with_day(13))
print(user.get_user_with_weekday(1))
print(user.get_user_by_gender("male"))
print(user.write_users_to_file('users.json', 'male', 10))
