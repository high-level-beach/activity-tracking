import fitbit
import gather_keys_oauth2 as Oauth2
from settings import FITBIT_CLIENT_ID, FITBIT_CLIENT_SECRET

server=Oauth2.OAuth2Server(FITBIT_CLIENT_ID, FITBIT_CLIENT_SECRET)
server.browser_authorize()

ACCESS_TOKEN=str(server.fitbit.client.session.token['access_token'])
REFRESH_TOKEN=str(server.fitbit.client.session.token['refresh_token'])

auth2_client=fitbit.Fitbit(
    FITBIT_CLIENT_ID,
    FITBIT_CLIENT_SECRET,
    oauth2=True,
    access_token=ACCESS_TOKEN,
    refresh_token=REFRESH_TOKEN
)