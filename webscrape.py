from instagramy import InstagramUser
import requests
import webbrowser
if __name__ == '__main__':
    # a_session = requests.Session()
    # a_session.get('https://instagram.com')
    # session_cookies = a_session.cookies
    # cookies_dictionary = session_cookies.get_dict()
    # print(cookies_dictionary)
    SessionId = requests.session().cookies.get('SESSIONID')
    print(SessionId)
    sessionId = "428255808%3Aoz68L78fPfJY1p%3A12"
    user = InstagramUser('thelukeschengus', sessionid=sessionId)
    print(user.biography)