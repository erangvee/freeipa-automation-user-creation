import pandas as pd

from python_freeipa import ClientMeta




client = ClientMeta('id.philsa.gov.ph')
client.login(xxx,xxx)
user = client.user_add('user.test.1', 'User', 'Test 1', 'User Test 1', o_preferredlanguage='EN')
print(user)