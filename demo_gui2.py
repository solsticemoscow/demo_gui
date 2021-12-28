import PySimpleGUI as sg
import base64
import subprocess
import sys
import os
import io
import smtplib  as smtp
from email.message import EmailMessage
from json import (load as jsonload, dump as jsondump)
from os import path

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib, io
import email
from datetime import datetime


def main():
    sg.theme('DarkTeal1')

    WHITE = 'white'
    BLACK = 'black'
    RED = 'red'
    ORANGE = 'orange'
    GREEN = '#00C853'
    BLUE = '#2196f2'
    INDIGO = '#8C9EFF'
    COLOR1 = '#1B5E20'
    LOG = '#263238'

    IMCANCEL = './IMAGES/remove128.png'
    IMDONE = './IMAGES/accept.png'

    col1 = sg.Column(
        [
            [
                sg.Text('LOGIN PAGE', font='Default 20', text_color=ORANGE, border_width=2, size=(30, 1), justification='c')
            ],
            [
                sg.T('Enter your credentials:', font='Default 10', size=(15, 1))
            ],

        ], justification='center', vertical_alignment='center'
    )
    col2 = sg.Column(
        [
            [
                sg.Text('Password:', size=(15, 1)),
                sg.Input(password_char='*', key='pass', size=(35, 1), default_text='1', background_color=WHITE, text_color=BLACK),
                sg.Text(size=(35, 1))
            ],
            [
                sg.Text('User:', size=(15, 1)),
                sg.Input(key='user', size=(35, 1), default_text='admin', background_color=WHITE, text_color=BLACK),
                sg.Text(size=(35, 1))
            ]
        ], justification='center', vertical_alignment='center'
    )

    col3 = sg.Column(
        [
            [
                sg.Button('Login', size=(10, 1), button_color=GREEN, key='l13')
            ]
        ], justification='c'
    )

    col4 = sg.Column(
        [
            [
                sg.Button('Exit', size=(10, 1), button_color=RED)
            ]
        ], justification='c'
    )


    def send_att_mail(to):
        try:
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

            me = 'smtp@karenkashop.com'
            you = to
            mail_pass = '***********'

            msg = MIMEMultipart("alternative")
            msg['Subject'] = 'CA Data'
            msg['From'] = 'info@karenkashop.com'
            msg['To'] = to

            filename = './FILES/SAMPLES/sample_csv1.csv'

            html = """\
            <html>
              <body>
                <p><b>Data from CA</b><br>
                </p>
              </body>
            </html>
            """

            part = MIMEText(html, "html")

            msg.attach(part)

            with open(filename, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
            encoders.encode_base64(part)

            part.add_header(
                "Content-Disposition",
                "attachment", filename=filename
            )
            msg.attach(part)

            s = smtplib.SMTP('mail.karenkashop.com', 587)
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login(me, mail_pass)
            s.sendmail(me, you, msg.as_string())
            s.quit()
            print('Send mail successfully.')
            return 'OK!'
        except Exception as error:
            print(f'Send mail error! Text: {error}')
            return error


    def run_splunk(app):
        import splunklib.client as client

        SPLUNK_HOST = 'localhost'
        SPLUNK_PORT = 8089
        SPLUNK_USER = 'admin'
        SPLUNK_PASS = '*********'


        splunk = client.connect(
            host=SPLUNK_HOST,
            port=SPLUNK_PORT,
            username=SPLUNK_USER,
            password=SPLUNK_PASS)

        applications = splunk.apps
        try:
            applications.create(app)
            print('ok')
            return 'OK!'
        except Exception as e:
            print(e)
            return e


        # appcollection = service.apps
        # my_app = appcollection.create('my_app')
        # my_app = appcollection['my_app']
        # appcollection.delete('my_app')



    def w_main():

        sg.theme('Black')

        col_top = sg.Column(
            [
                [
                    sg.Text('ACTION PAGE', font='Default 15', text_color=ORANGE, border_width=2, size=(30, 1), justification='c')
                ]
            ], justification='center', vertical_alignment='center'
        )

        # FRAME = sg.Frame(title='FRAME1', title_color=BLACK, element_justification='c', vertical_alignment=True, border_width=5, size=(100, 5), pad=(10, 2))

        column_settings = sg.Column(
            [
                [
                    sg.Frame('SETTINGS:', [
                        [
                            sg.Column(
                                [
                                    [
                                        sg.Frame('FROM:',
                                                 [
                                                     [
                                                         sg.Button(
                                                             button_text='Get data from DB',
                                                             size=(15, 1),
                                                             key='getdb',
                                                             font='Default 10',
                                                             auto_size_button=True,
                                                             # image_filename=IMAGE_EXIT,
                                                             image_size=(64, 64),
                                                             # disabled=False,
                                                             # disabled_button_color=BLACK,
                                                             border_width=3,
                                                             button_color=ORANGE
                                                         ),
                                                     ],
                                                     [
                                                         sg.Button('',
                                                                   image_filename=IMDONE,
                                                                   button_color=BLACK,
                                                                   image_size=(32, 32),
                                                                   key='getdone',
                                                                   border_width=0,
                                                                   visible=False,
                                                                   enable_events=True,
                                                                   )
                                                     ]
                                                 ],
                                                 size=(175, 100),
                                                 element_justification='c'
                                        )
                                    ]
                                ], size=(250, 125), justification='center', vertical_alignment='center'),
                            sg.Column(
                                [
                                    [
                                        sg.Frame('FROM:',
                                                 [
                                                     [
                                                         sg.Button(
                                                             button_text='Convert data to CSV',
                                                             size=(15, 1),
                                                             key='convertcsv',
                                                             font='Default 10',
                                                             auto_size_button=True,
                                                             # image_filename=IMAGE_EXIT,
                                                             image_size=(64, 64),
                                                             # disabled=False,
                                                             # disabled_button_color=BLACK,
                                                             border_width=3,
                                                             button_color=ORANGE,
                                                             enable_events=True
                                                         ),
                                                     ],
                                                     [
                                                         sg.Button('',
                                                                   image_filename=IMDONE,
                                                                   button_color=BLACK,
                                                                   image_size=(32, 32),
                                                                   key='convertdone',
                                                                   border_width=0,
                                                                   visible=False,
                                                                   enable_events=True,
                                                                   )
                                                     ]
                                                 ], size=(175, 100), element_justification='c'
                                                 )
                                    ]
                                ], size=(250, 125), justification='center', vertical_alignment='center')
                        ]
                    ], visible=True, font='Default 10', element_justification='c', size=(600, 150))
                ]
            ]
        )

        col_opt = sg.Column([
            [
                sg.Frame('OPTIONS:', [
                    [
                        sg.Column([
                            [
                                sg.Checkbox('To Splunk', key='check_splunk', default=False, enable_events=True,
                                            metadata=0, text_color=WHITE, size=(15, 1), disabled=False)
                            ],
                            [
                                sg.Checkbox('To mail', key='check_mail', default=False, enable_events=True,
                                            metadata=0, text_color=WHITE, size=(15, 1), disabled=False)
                            ]
                        ], size=(175, 100), justification='l')
                    ]
                ], visible=True, font='Default 10')
            ]
        ]
        )

        col_action = sg.Column([
            [
                sg.Frame('ACTIONS:', [
                    [
                        sg.Column([
                            [
                                sg.Text('Set mail address:', size=(15, 1)),
                                sg.Text(size=(15, 1))
                            ],
                            [
                                sg.Input(key='mailinput', size=(35, 2), background_color=WHITE, text_color=BLACK),
                                sg.Text(size=(15, 1))
                            ],
                            [
                                sg.Button('Send', size=(10, 1), button_color=GREEN, key='submit_mail')
                            ]
                        ], size=(235, 100), justification='r')
                    ]
                ], visible=False, font='Default 10', element_justification='r', key='actmail'),
                sg.Frame('ACTIONS:', [
                    [
                        sg.Column([
                            [
                                sg.Text('Set name for app:', size=(15, 1)),
                                sg.Text(size=(15, 1))
                            ],
                            [
                                sg.Input(key='splunkinput', size=(35, 2), background_color=WHITE, text_color=BLACK),
                                sg.Text(size=(15, 1))
                            ],
                            [
                                sg.Button('Create', size=(10, 1), button_color=GREEN, key='submit_splunk')
                            ]
                        ], size=(235, 100), justification='r')
                    ]
                ], visible=False, font='Default 10', element_justification='r', key='actsplunk')
            ]
        ]
        )




        column_log = sg.Column(
            [
                [
                    sg.Frame('LOG EVENTS:', [
                        [
                            sg.Column(
                                [
                                    [
                                        sg.Multiline(size=(100, 5), key='log1', reroute_stdout=True,
                                                     background_color=WHITE, text_color=LOG, no_scrollbar=False, autoscroll=True)
                                    ]

                                ], size=(500, 100), justification='c'
                            )
                        ]
                    ], visible=True, font='Default 15')
                ]
            ]
        )

        column_bottom = sg.Column(
            [
                [
                    sg.B('Exit', size=(15, 1), button_color=RED, auto_size_button=True)
                ]
            ], justification='center', vertical_alignment='center'
        )


        layout = [
            [col_top], [column_settings],
            [col_opt, col_action], [column_log], [column_bottom]
        ]

        window = sg.Window('WSETUP', layout, size=(500, 550))
        return window

    window = w_main()
    settings = None

    while True:
        event, values = window.read(timeout=100)
        if event == sg.WIN_CLOSED or event == 'Exit' or event == 'close' or event == 'ok' or event == 'submit':
            break
        if event == 'l11':
            state = window['l11'].metadata
            if state == 0:
                window['l12'].update(visible=True)
                window['l11'].metadata = 1
                window.Refresh()
            if state == 1:
                window['l12'].update(visible=False)
                window['l11'].metadata = 0
                window.Refresh()
        if event == 'check_splunk':
            state = window['check_splunk'].metadata
            if state == 0:
                msg = 'Enable SPLUNK option'
                window['log1'].update(msg+'\n', append=True)
                window['check_splunk'].update(text_color=GREEN)
                window['check_splunk'].metadata = 1
                window['actsplunk'].update(visible=True)
                window['check_mail'].update(disabled=True)
            if state == 1:
                window['check_splunk'].update(text_color=WHITE)
                window['check_splunk'].metadata = 0
                msg = 'Disable SPLUNK option'
                window['log1'].update(msg+'\n', append=True)
                window['actsplunk'].update(visible=False)
                window['check_mail'].update(disabled=False)
            window.Refresh()
        if event == 'check_mail':
            state = window['check_mail'].metadata
            if state == 0:
                msg = 'Enable mail option'
                window['log1'].update(msg+'\n', append=True)
                window['check_mail'].update(text_color=GREEN)
                window['check_mail'].metadata = 1
                window['check_splunk'].update(disabled=True)
                window['actmail'].update(visible=True)
            if state == 1:
                window['check_mail'].update(text_color=WHITE)
                window['check_mail'].metadata = 0
                msg = 'Disable mail option'
                window['log1'].update(msg+'\n', append=True)
                window['actmail'].update(visible=False)
                window['check_splunk'].update(disabled=False)
            window.Refresh()
        if event == 'getd':
            window['statusca'].update(text_color=GREEN)
            msg = 'Get settings'
            window['log1'].update(msg+'\n', append=True)
            window.Refresh()
        if event == 'savecsv':
            window['statuscsv'].update(text_color=GREEN)
            msg = 'Data saved to CSV'
            window['log1'].update(msg + '\n', append=True)
            window.Refresh()
        if event == 'submit_splunk':
            app = values['splunkinput']
            result = run_splunk(app)
            msg = str(result)
            window['log1'].update(msg+'\n', append=True)
        if event == 'submit_mail':
            to = values['mailinput']
            result = send_att_mail(to)
            msg = str(result)
            window['log1'].update(msg+'\n', append=True)
        if event == 'convertcsv':
            sg.Popup(title='Hi', custom_text='DONE', auto_close=True, auto_close_duration=3)
            window['convertdone'].update(visible=True)
            window.Refresh()

    window.close()


if __name__ == '__main__':
    main()