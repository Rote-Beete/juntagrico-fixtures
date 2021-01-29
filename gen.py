#!/usr/bin/env python

# imports
from lib import Fixture
from lib import User

# execution
if __name__ == "__main__":

    userlist = Fixture.Factory(model="juntagrico-member", offset=1)
    userlist.add(
        User.Factory(
            user_id=userlist.len() + 1,
            first_name="Foo",
            last_name="Bar",
            email="foo@bar.buz",
            addr_street="Foo Bar Buz",
            addr_zipcode="04223",
            addr_location="FooBar",
            birthday="1970-01-01",
            phone="+49 800 23 42",
            reachable_by_email=True))

    print(userlist.get_json())
