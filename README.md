# freeipa-automation-user-creation
This code automatically creates user accounts from a CSV input file. It uses [Python FreeIPA client](https://python-freeipa.readthedocs.io/en/latest/) to access and modify FreeIPA.

## Prerequisites
* Python v3.12.4
* `.env` file:
   * Create a `.env` file that contains information on:
      * `users_file` : path for `.csv` file containing user information
      * `freeipa_host`: hostname of FreeIPA to connect to
      * `ipa_username` : username with admin privileges that can access the FreeIPA
      * `ipa_password` : corresponding password 
      ```
        users_file=input-template.csv

        freeipa_host=freeipa.host.name
        ipa_username=your.username
        ipa_password=your.password
      ```

## How to use
1. Create the `.env` file in the root folder.
2. Run `python main.py`.
