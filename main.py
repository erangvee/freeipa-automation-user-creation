import pandas as pd
import os

from dotenv import load_dotenv
from python_freeipa import ClientMeta

def create_account(row):
    # create user account
    user = client.user_add(row.username, row.firstname, row.lastname, row.fullname,
                            o_userpassword=row.password,
                            o_preferredlanguage='EN',
                            o_ipasshpubkey=row.ssh_pubkey)
    print("User account created: ", user)

    # add user to group/s
    for group in row.group.split(','):
        client.group_add_member(group,
                                o_user=row.username)
        print("User "+row.username+" added to group "+group)

# load .env file
load_dotenv()
users_file = os.getenv("users_file")
freeipa_host = os.getenv("freeipa_host")
ipa_username = os.getenv("ipa_username")
ipa_password = os.getenv("ipa_password")

# load users list and data into dataframe
users = pd.read_csv(users_file)

users = users.replace({float('nan'): None}) # replace all blanks with None
print(users['ssh_pubkey'])
# log in to freeipa
client = ClientMeta(freeipa_host)
client.login(ipa_username, ipa_password)

# apply create_account function to users dataframe
users.apply(create_account, axis=1)

print("DONE processing")