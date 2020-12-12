'''
Tests for jwt flask app.
'''
import os
import json
import pytest

import main

SECRET = 'TestSecret'
TOKEN = 'eyJwYXlsb2FkIjoiSk83cUdZYldMRVFSUGs4bGRXa2pxV2M2NUQvc1RLNkRsUU9CbGExQlp4Q0R6Wjgra3hVWnExaWcvSFlQWGF2bUdHOFZwMkhaaUJFMzg0aWtDdGpCclZSeVo3cmJLaTdnOVVuNzljc3Y2MzNpd0NSbnpDa3VsUHppdjdaT2YwVFpKVjJORVpvaHVrWi9XNFZqVmZQQTBBVFIvaE1CVW9pQzJNWFBkckZCWjlqQjEyZi8zQ0tEVXJCcmJEWS9OZE8ra1lpd2IwMkVDaGZlU1lsYTB5S1B5UTJnR1dJa3NFbm03VEhSNUFnaDFLZmJLdXVVYkpZdHNZU2R3dnozd0pNaVNQMkoyRnU1bXlsYTd5NkpqekpyU28vdGdFSW13MnVyei9Yb0h2VWFnZTJRL1FPeThFTGIraFhLeE55TjUrTThHZmYwbi9LRE9EWDNJblFrSG8yMUYyZmw5a2NrWm9NNzI5R21iUGFBQlBGYXZtVU1VRE5UZ1lCQWxNbEZZc0dncEIxSVVJR0ZvKzJxcTZtMUpHbSt4cnhTVkVmYkJlSW1GTlhhL1FvUHEvVUE5OWNvRk9IckNSaTdHSjFkMWFGeHd3WExlQ2pZUEpxNEN1TDhHbTFleHpGMzdlWHY1dk0zVGs0UFRFK21uYStQaCtJODZzV1ZlTjdEL1RLcHIrWFdBZlg0Wm1SRUFQQzBMTnFDbTRnUXhyQ1g0OFE5cERSZldldnVOTHhBSHduRXl1MUwyVWlKamNTMTVhL2ZRdCtGd3BJQXpHb2pOWnI4SUQ3V0Z6dG50MjZwak0ybWt5TmhSSEJESnpwYjZOUStjaEhXazhza3A4YmdlU2p2c0tUbHVleGRuK1pDMTZHL29KUVY2T3ZmWHo4citKRUxmcmFXR3ljTmZJbU5GUE40dk9PUFNuUVJUNi9wODRvNHFlS1RhdTlEYmxrT3krblVrT3RnNnIwdGgxRFEzakt3ZlNoRVFrbmRpeStYMFRycC9LMXVHd1pMT3lnSGtPK2h0S1JZbVRRQjU1M2hXQlJ2eUY4UDV3cTZZYXpWYWt5N3NoMUZ4RFptZ21jbHhING52dlZWbHpMK1M3NHh2QTMyK2Nzc3JYOEFyaTVpN21MdllXQmxlWDFnU0Fvb2JFQUU0OUd5UlZHakVrOUZqUHdGWDZKL3greGNnQlZ0RzYrc0FUVHVmakNvOWcyei9RNU96WWMxVWwyTVlFRGZpY0UraXZFR25VUittci9xcXdVRks1U25Od0RxUnlvQTQwcFgyL1M4WGdlRGE1LzBLRlF4amJTWE5LS0VKaXJ6VXFEcGozTFFuVFdYZWN3NTMvYldSSUt5SmdXK2Z3WWpRMnRCK2VDK1phbzloQzFpUUN4N0tkS3JtTC9lUlp4Uy9seGJldVVoRnJuaTk3L3A4cmFEeVJJYW5nbTk5SmxxNmVabVd1eWFvRFJrYWpOYXVvUWdjdkV5U0lZZFZja2ZNbzVtREFGOHNaTmoyVFdjVmF0SW5VczdYS0diNUxEbk1TNnciLCJkYXRha2V5IjoiQVFFQkFIakI3L2lnd01nNE5Qd2F1cnhTSVl4NEhmbnh1R2MvNDhiRHd2d0RwTllXWmdBQUFINHdmQVlKS29aSWh2Y05BUWNHb0c4d2JRSUJBREJvQmdrcWhraUc5dzBCQndFd0hnWUpZSVpJQVdVREJBRXVNQkVFREpOT2d3MWRQRlNrYWRqQmVBSUJFSUE3Unc5YzI1VUNsT0xZU2JCVVJlNVk3Rnh6TGYrM3V5MUhEcllUSGtaWGprZmIxV1B1blJablJZWmFrc21HV05rTFRqVUJreExRdC8zWkl5TT0iLCJ2ZXJzaW9uIjoiMiIsInR5cGUiOiJEQVRBX0tFWSIsImV4cGlyYXRpb24iOjE2MDc4MjM0MDJ9'
EMAIL = 'wolf@thedoor.com'
PASSWORD = 'huff-puff'

@pytest.fixture
def client():
    os.environ['JWT_SECRET'] = SECRET
    main.APP.config['TESTING'] = True
    client = main.APP.test_client()

    yield client



def test_health(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == 'Healthy'


def test_auth(client):
    body = {'email': EMAIL,
            'password': PASSWORD}
    response = client.post('/auth', 
                           data=json.dumps(body),
                           content_type='application/json')

    assert response.status_code == 200
    token = response.json['token']
    assert token is not None
