import pytest

GALAXY_S8_USER_AGENT = 'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36'
GALAXY_S7_USER_AGENT = 'Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36'
GALAXY_S7_EDGE_USER_AGENT = 'Mozilla/5.0 (Linux; Android 6.0.1; SM-G935S Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36'

ANDROID_UA = [GALAXY_S8_USER_AGENT,
              GALAXY_S7_USER_AGENT,
              GALAXY_S7_EDGE_USER_AGENT]

IPHONE_X_USER_AGENT = 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
IPHONE_8_USER_AGENT = 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'
IPHONE_XR_USER_AGENT = 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1'

IOS_UA = [IPHONE_X_USER_AGENT,
          IPHONE_8_USER_AGENT,
          IPHONE_XR_USER_AGENT]

WIN10_EDGE_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'
CHROMEBOOK_USER_AGENT = 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36'
MAC_OS_X_SAFARI_USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'


DESKTOP_UA = [WIN10_EDGE_USER_AGENT,
              CHROMEBOOK_USER_AGENT,
              MAC_OS_X_SAFARI_USER_AGENT]

USER_AGENTS = sum([ANDROID_UA,
                   IOS_UA,
                   DESKTOP_UA],
                  [])


@pytest.fixture(scope='session', params=USER_AGENTS)
def user_agents(request):
    return request.param
