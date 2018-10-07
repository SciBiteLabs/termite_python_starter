"""

Example script for multipart call using requests.

"""""

import requests
import os

testfile = "./resources/medline_sample.zip"
username = '' #we will give you this on the hackathon day
password = '' #we will give you this on the hackathon day


def get_termite_xml(zipfile, format='medline.xml', output='xml'):
    """
    Function for sending a multipart request to TERMite.

    :param zipfile: zipped input file of medline data
    :param format: output format required
    :param output: output language required
    :return:
    """

    #url = 'http://localhost:9090/termite'
    url = 'https://ugm.scibite.com/termite'
    form_data = {
        'format': format,
        'output': output,
        'subsume': 'true',
        'rejectMinorHits' : 'true',
        'fuzzy' : 'true',
        'opts' : 'fzy.promote=true'
    }

    file_obj = open(zipfile, 'rb')
    file_name = os.path.basename(zipfile)
    binary_content = {"binary": (file_name, file_obj)}

    response = requests.post(url, data=form_data, files=binary_content, auth=(username, password), verify=False)

    return response.text


print(get_termite_xml(testfile))
