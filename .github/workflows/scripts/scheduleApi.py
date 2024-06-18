import requests

def scheduleRelease(url, key, id, version, datetimeUtc, env):
    response = requests.post(f'{url}?code={key}', 
        headers = {
        'Content-type': 'application/json'
        }, 
        json = {   
            'id': id, 
            'version': version,
            'dateTimeUtc': datetimeUtc,
            'environment': env
        })
    print(response.text)    
    if not response.ok:
        message = f'Unable to schedule release with id: {id}, status: {response.status_code} and reason {response.reason}'
        raise Exception(message)


def cancelScheduleRelease(url, key, env,reason, id=None):
    _url = f'{url}/Cancel/{env}/{id}' if id != None else f'{url}/Cancel/{env}'

    response = requests.put(f'{_url}?code={key}', 
        headers = {
        'Content-type': 'text/plain'
        }, 
        data = reason)
    
    print(response.text) 
    if not response.ok:
        message = f'Unable to cancel scheduled release with id: {id},status: {response.status_code} and reason {response.reason}'
        raise Exception(message)
