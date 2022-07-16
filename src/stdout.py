"""
Function for internal uses
"""
def output_response(response, _json: bool = False):
    out = '\n\n\n'
    out += f"\nHEADERS: \n{response.headers}\n\n"
    out += f"REQUEST: \n{response.request.method} {response.url}\n\n"
    out += f"RESPONSE (json): \n{response.status_code}\n{response.json()}\n" if _json \
        else f"RESPONSE (text): \n{response.status_code}\n{response.text}\n"
    print(out)
