import requests

def get_html(link_to_the_site):
    try:
        response = requests.get(link_to_the_site)
        if response.status_code != 200:
            return None
        return response # here add field
    except:
        print('get html errror')
        return None 
