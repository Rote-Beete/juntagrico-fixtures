from dataclasses import dataclass
from datetime import datetime, date


@dataclass
class Factory():

    def __init__(self,
                 user_id: int,
                 first_name: str,
                 last_name: str,
                 email: str,
                 addr_street: str,
                 addr_zipcode: str,
                 addr_location: str,
                 birthday: date,
                 phone: str,
                 mobile_phone: str="",
                 iban: str="",
                 confirmed: bool=False,
                 reachable_by_email: bool=False,
                 cancellation_date: date="",
                 deactivation_date: date="",
                 end_date: date="",
                 notes: str=""):
        self.user = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.addr_street = addr_street
        self.addr_zipcode = addr_zipcode
        self.addr_location = addr_location
        self.birthday = birthday
        self.phone = phone
        self.mobile_phone = mobile_phone
        self.iban = iban
        self.confirmed = confirmed
        self.reachable_by_email = reachable_by_email
        self.cancellation_date = cancellation_date
        self.deactivation_date = deactivation_date
        self.end_date = end_date
        self.notes = notes

    def encode(self):
        return self.__dict__
