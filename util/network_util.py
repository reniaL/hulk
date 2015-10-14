
import common_util
import logging
import urllib2
import re

DEFAULT_TIMEOUT = 10

def save_url_to_file(url, path, timeout=DEFAULT_TIMEOUT):
    try:
        common_util.make_parent_dirs(path[:path.rfind('/')])
        content = get_url_content(url, timeout)
        with open(path, 'wb') as f:
            f.write(content)
        return True
    except Exception as e:
        logging.exception(type(e).__name__)
        return False

def get_url_content(url, timeout=DEFAULT_TIMEOUT):
    return urllib2.urlopen(url, timeout=timeout).read()

if __name__ == '__main__':
    content = get_url_content('http://bing.com')
    print content
    