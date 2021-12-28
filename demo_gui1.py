import base64
import io
from PIL import Image
import PIL
import PySimpleGUI as sg
import clipboard

import sys
import os
import io

from functions import *

WHITE = 'white'
BLACK = 'black'
RED = 'red'
ORANGE = 'orange'
GREEN = '#00C853'
BLUE = '#2196f2'
INDIGO = '#8C9EFF'
COLOR1 = '#1B5E20'
LOG = '#263238'


IMAGE_ACCEPT = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAADvklEQVR4nLWX22scVRzHP+fM3txoGqQaC7HapmCD2sYaii2mtFEJu6mbsholrfgviIul2uamDyWC6JsI8QZikYY07m4utGCgNcmLgm1SfWkuYApaKpjabEmymfn50Nx2d3Z3kmy+TzPz+53z+f6GOWd+R+FQoWjooQVLH9UiNRZqr8J6ElTJ/ahMg5oEroEMGAa9sfrYXSfzqnwJtV3hbYYyWxS8Dfgd+r2n4Jw25ONYfWxsXQYazjc8cM899wGWiqAocghOVxL41PLNt/YH++ccGwhFQ7tMU10Anl0nOFXCsOGScKw+diuvgWD3sUotclHg0YLAlz0wpdDB3nD39awGQtHQLstUQ4WGr6L9aWjZv/pN6KWLw98c9pmm6tw0OICw3TRVd6Av4M0wUFRSfBqo3DT4ig4Ys562FAO1XeFtWCpSKILP5aNm+xG00rZxgUig+1j5sgFDmS0bWGop8hpeWl44Q+T5dzhZFcFQhl2aR4ucAlCBvkCxnvX8hfNNJie89UATex5ZWb0/3xzkk18/wxQzNVlI+E3PY1rNeesKAfe5fHx4sCUFDlBd9iLPbH06c4CiKOFOBrUWqdkofOm124H6Jy8ycnvUdpyyrJe0hdqbD7DFW5w1lq1ygNh4D59f/QJB7A0otUcrZEcu+KGyar4LfEvj7jczYvkq7xj5Kit8UTs1kLW8Q2XVvFf1LlppTlQ0ppiw++BWw3NVviSBLa5swd0PP8XJqghKrezWJyoaEYQfb8RoO9hsW3lsvMdJ5ctyAf8BW9MDU3dvMnFngvKS8pTnb1Uc55UnXqbUn7ljx8bjdIx87Riu4I6W+51MhhLJBKcHW7jxb2Y/YQePjq0NvqgJrZCr2aKJZIKmoVZbE+nwL0fXDEfgmgYZyJWUSCZoHmpjbHq8oPBFCz9p/4K3B5jJlTaTnKFpsDXDxIbgQsK/4O3XnW90zij4IV9+uonoWJyOUedfu42D7xfZyz3gH4A737BiTzH7Sp/j8tSVDcCZ0y6rIh6KTy4v8roL9e3AqfXOuEad7Q1Hz8Cqjujv26XNwJVNRwvDlm/+o6Xb9Ka0dMFUvyh4fFPguZpSgFh97JZCBwWmNgOuTSuYfjbIaNp6w93XDbe1T5DLBYMLw4aW/fHX47+nh2y7xvir8X/El6xV0A7MbwA9D5z1m54jdqcicHA4ret6bSdq4X2E42toXGcQOafd0h4PxW3/NY4NLKnhfMODCXcyqERqECqVYodAyeIk0yJMiuI3hQwki2b7LtVeSjiZ938FXILfqiUmogAAAABJRU5ErkJggg=='

def w_main():
    import PySimpleGUI as sg
    sg.theme('Black')

    col_top = sg.Column(
        [
            [
                sg.Text('Follow step-by-step actions', font='Default 15', text_color=WHITE, border_width=2, size=(30, 1),
                        justification='c')
            ]
        ], justification='center', vertical_alignment='center'
    )


    column_step1 = sg.Column(
        [
            [
                sg.Frame('STEP 1:', [
                    [
                        sg.Text(
                            text='Create telegram bot and set API key, then click on button bellow (see https://core.telegram.org/bots):',
                            size=(65, 2),
                            font=("Helvetica", 8, "italic"),
                            justification='c')
                    ],
                    [
                        sg.Input(
                            key='api',
                            size=(65, 2),
                            focus=True,
                            background_color=WHITE,
                            text_color=BLACK
                        ),
                        sg.Text(size=(35, 2)),
                    ],
                    [
                        sg.Button(
                            button_text='Create python app',
                            key='bcreatepy',
                            size=(15, 1),
                            border_width=5,
                            button_color=GREEN,
                            auto_size_button=True,
                            font='Default 10',
                            enable_events=True
                        ),
                        sg.Image(
                            data=IMAGE_ACCEPT,
                            key='step1_done',
                            visible=False
                        )
                    ]
                ],
                         title_color=ORANGE,
                         key='step1',
                         visible=True,
                         font='Default 12',
                         title_location='n',
                         element_justification='c',
                         size=(600, 150))
            ]
        ]
    )

    column_step2 = sg.Column(
        [
            [
                sg.Frame('STEP 2:', [
                    [
                        sg.Text(
                            text='Run tests and see report:',
                            size=(65, 1),
                            font=("Helvetica", 8, "italic"),
                            justification='c')
                    ],
                    [
                        sg.Button(
                                button_text='Run tests',
                                key='bruntests',
                                size=(15, 1),
                                border_width=5,
                                button_color=BLACK,
                                auto_size_button=True,
                                disabled=True,
                                enable_events=True,
                                font='Default 10'
                            ),
                        sg.Image(
                            data=IMAGE_ACCEPT,
                            key='step2_done',
                            visible=False
                        )
                    ]
                ],
                         key='step2',
                         title_color=ORANGE,
                         visible=True,
                         font='Default 12',
                         title_location='n',
                         element_justification='c',
                         size=(600, 125)
                         )
            ]
        ]
    )

    column_step3 = sg.Column(
        [
            [
                sg.Frame('STEP 3:', [
                    [
                        sg.Text(
                            text='Create docker App:',
                            size=(65, 1),
                            font=("Helvetica", 8, "italic"),
                            justification='c'),
                        sg.Text(size=(35, 1))
                    ],
                    [
                        sg.Button(
                            button_text='Create docker app',
                            key='createdocker',
                            size=(15, 1),
                            border_width=5,
                            button_color=BLACK,
                            disabled=True,
                            auto_size_button=True,
                            font='Default 10'
                        ),
                        sg.Image(
                            data=IMAGE_ACCEPT,
                            key='step3_done',
                            visible=False
                        )
                    ]
                ], title_color=ORANGE, visible=True, font='Default 12', title_location='n', element_justification='c', size=(225, 100))
            ]
        ]
    )

    column_step4 = sg.Column(
        [
            [
                sg.Frame('STEP 4:', [
                    [
                        sg.Text(
                            text='Deploy App to cloud via Ansible:',
                            size=(65, 1),
                            font=("Helvetica", 8, "italic"),
                            justification='c'
                        ),
                    ],
                    [
                        sg.Button(
                            button_text='Create docker app',
                            key='deploydocker',
                            size=(15, 1),
                            border_width=5,
                            button_color=BLACK,
                            disabled=True,
                            auto_size_button=True,
                            font='Default 10'
                        ),
                        sg.Image(
                            data=IMAGE_ACCEPT,
                            key='step4_done',
                            visible=False
                        )
                    ]
                ], title_color=ORANGE, visible=True, font='Default 12', title_location='n', element_justification='c', size=(225, 100))
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
                                    sg.Multiline(size=(100, 10), key='log1', reroute_stdout=True,
                                                 background_color=WHITE, text_color=LOG, no_scrollbar=False,
                                                 autoscroll=True, font='Default 8')
                                ]

                            ], size=(500, 150), justification='c'
                        )
                    ]
                ], visible=True, font='Default 12', title_location='n', title_color=ORANGE)
            ]
        ]
    )

    column_bottom = sg.Column(
        [
            [
                sg.B('Re-run', size=(15, 1), key='rerun', button_color=GREEN, auto_size_button=True, border_width=5),
                sg.B('Exit', size=(15, 1), button_color=RED, auto_size_button=True, border_width=5)
            ]
        ], justification='center', vertical_alignment='center'
    )

    layout = [
        [col_top], [column_step1],
        [column_step2], [column_step3, column_step4], [column_log], [column_bottom]
    ]

    window = sg.Window('WSETUP', layout, size=(500, 700))
    return window

def main():
    sg.theme('DarkTeal1')
    window = w_main()

    while True:
        event, values = window.read(timeout=100)
        if event == sg.WIN_CLOSED or event == 'Exit' or event == 'close' or event == 'ok' or event == 'submit':
            break
        if event == 'bcreatepy':
            api = values['api']
            if len(str(api)) != 46:
                msg1 = 'Its not correct key!'
                window['log1'].update(msg1 + '\n', append=True)
                window.Refresh()
            elif len(str(api)) == 46:
                msg1 = copy_file()
                window['log1'].update(msg1 + '\n', append=True)
                api = values['api']
                result = ini_write(api)
                msg2 = str(result)
                window['log1'].update(msg2 + '\n', append=True)
                window['bcreatepy'].update(button_color=BLACK)
                window['bcreatepy'].update(disabled=True)
                window['bruntests'].update(button_color=GREEN)
                window['bruntests'].update(disabled=False)
                window['step1_done'].update(visible=True)
                window.Refresh()
        if event == 'bruntests':
            msg1 = run_tests()
            window['log1'].update(msg1 + '\n', append=True)
            window['bruntests'].update(button_color=BLACK)
            window['bruntests'].update(disabled=True)
            window['createdocker'].update(button_color=GREEN)
            window['createdocker'].update(disabled=False)
            window['step2_done'].update(visible=True)
            window.Refresh()
        if event == 'createdocker':
            msg1 = create_docker()
            window['log1'].update(msg1 + '\n', append=True)
            window['createdocker'].update(button_color=BLACK)
            window['createdocker'].update(disabled=True)
            window['deploydocker'].update(button_color=GREEN)
            window['deploydocker'].update(disabled=False)
            window['step3_done'].update(visible=True)
            window.Refresh()
        if event == 'rerun':
            window.close()
            window = w_main()
    window.close()


if __name__ == '__main__':
    main()