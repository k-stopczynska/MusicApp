import requests


def get_querystring(search_term):
    search_param = input(search_term).strip().lower()
    if len(search_param) > 0:
        querystring = {"term": search_param, "locale": "en-US"}
        return querystring
    else:
        querystring = get_querystring(search_term)
        return querystring

def get_response(method, url, headers, params=None, data=None):
    try:
        if method == "GET":
            response = requests.get(url, headers=headers, params=params)
            if response.status_code == 200:
                return response
        if method == "POST":
            response = requests.post(url, headers=headers, data=data)
            if response.status_code == 200:
                return response
    except requests.exceptions.HTTPError as error_HTTP:
        print("Http Error:", error_HTTP)
    except requests.exceptions.ConnectionError as err_connect:
        print("Error Connecting:", err_connect)
    except requests.exceptions.Timeout as err_timeout:
        print("Timeout Error:", err_timeout)
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else", err)