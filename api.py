import requests

class FacebookAPI:
    """
    Class to interact with the Facebook API.

    Attributes:
    - access_token: str
        The access token required to authenticate and authorize API requests.
    """

    def __init__(self, access_token: str):
        """
        Constructor to instantiate the FacebookAPI class.

        Parameters:
        - access_token: str
            The access token required to authenticate and authorize API requests.
        """

        self.access_token = access_token

    def make_api_request(self, endpoint: str, params: dict = None):
        """
        Makes a request to the Facebook API.

        Parameters:
        - endpoint: str
            The API endpoint to make the request to.
        - params: dict, optional
            Additional parameters to include in the request.

        Returns:
        - dict:
            The JSON response from the API.

        Raises:
        - requests.exceptions.RequestException:
            If there is an error making the API request.
        """

        # Constructing the API URL
        url = f"https://graph.facebook.com/{endpoint}"

        # Adding the access token to the request parameters
        if params is None:
            params = {}
        params["access_token"] = self.access_token

        try:
            # Making the API request
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an exception if the request was not successful
            return response.json()
        except requests.exceptions.RequestException as e:
            raise e

# Example usage of the FacebookAPI class:

# Initialize the FacebookAPI instance with an access token
access_token = "YOUR_ACCESS_TOKEN"
facebook_api = FacebookAPI(access_token)

# Make a request to the Facebook API
endpoint = "me"
params = {"fields": "id,name,email"}
response = facebook_api.make_api_request(endpoint, params)

# Print the response
print(response)
