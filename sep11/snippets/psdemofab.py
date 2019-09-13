from fabric import Connection
import cryptography
from pspassencoding import decode_password

import invoke
"""http://collabedit.com/8h9ch"""

password = b'gAAAAABc34IQGDFeOFcAqajbV4RQS_Pn-RFKzxq6fIssvrxdE1bmVRx0wCnHOe9b1ANnTwfLLYpp-FPGWE_zgglbqvCxBdUuWQ=='


try:
    password = decode_password('.hashkeys', password)
    conn = Connection('training@localhost', connect_kwargs={'password': password})

    result = conn.run('uname -a', hide=True)

    print('what we ran : ', result.command)
    print('where we host: ', result.connection.host)
    print('response :', result.stdout)
except invoke.exceptions.UnexpectedExit as err:
    print(err)