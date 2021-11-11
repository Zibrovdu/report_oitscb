import dateutil.utils
from dash import dcc
from dash import html


def serve_layout():
    layout = html.Div([
        html.Div([
            html.H2('Еженедельный отчет ОИТСЦБ'),
            html.A([
                html.Img(
                    src="assets/data-visualization.png"
                )
            ],
                href='#modal-1',
                className='js-modal-open link')
        ],
            className='banner'),
        html.Br(),
        html.Br(),
        html.Div([
            html.Div([
                html.Label(
                    'Выберите период за который необходимо сформировать отчет: ',
                    className='period_lbl'
                ),
                dcc.DatePickerRange(
                    id='period',
                    display_format='DD/MM/YYYY',
                    first_day_of_week=1,
                    max_date_allowed=dateutil.utils.today(),
                    className='date_picker_style'
                )
            ]),
            html.Div([
                html.Div([
                    dcc.Upload(
                        html.Button(
                            'Загрузить файл с данными',
                            id='btn_load_curr_data',
                            hidden=False,
                            className='btn_loaders'
                        ),
                        id='upload_data',
                        className='btn_load'
                    ),
                    dcc.Loading(
                        id="loading-2",
                        children=[
                            html.Div([
                                html.Div(
                                    id="loading-output-2",

                                    className='output_report'
                                )
                            ])
                        ],
                        type="circle",
                    )
                ],
                    className='div_load_btn'
                ),
                dcc.Store(id='load_data'),
            ]
            ),
            html.Div([
                html.Div([
                    dcc.Upload(
                        html.Button(
                            children='Загрузить файл с данными прошедшей недели',
                            id='btn_load_prev_data',
                            hidden=True,
                            className='btn_loaders'
                        ),
                        id='upload_prev_data',
                        className='btn_load'
                    ),

                    html.Div([
                        html.Div(
                            id="loading-output-3",

                            className='output_report'
                        )
                    ])
                ],
                    className='div_load_btn'
                ),
                dcc.Store(id='load_prev_data'),
            ]
            ),
            html.Div([
                html.Button(
                    "Сформировать отчет",
                    id="btn_make_report",
                    className='btn_loaders',
                    # hidden=True
                ),
            ]),

            html.Div([
                html.Span(id='test', hidden=True),
                html.Button(
                    "Скачать отчет",
                    id="btn_save_report",
                    className='btn_save_rep',
                    # hidden=True
                ),
                dcc.Download(id="download_report")
            ])

        ]),

        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        'История изменений'
                    ],
                        className='modal__dialog-header-content'
                    ),
                    html.Div([
                        html.Button([
                            html.Span('x')
                        ],
                            className='js-modal-close modal__dialog-header-close-btn'
                        )
                    ],
                        className='modal__dialog-header-close'
                    )
                ],
                    className='modal__dialog-header'
                ),
                html.Div([
                    html.Br(),
                    html.Div([
                        dcc.Textarea(
                            value="",
                            readOnly=True,
                            className='frame-history'
                        )
                    ]),
                    html.Br(),
                ],
                    className='modal__dialog-body'
                ),
                html.Div([
                    html.Button(
                        'Close',
                        className='js-modal-close modal__dialog-footer-close-btn'
                    )
                ],
                    className='modal__dialog-footer'
                )
            ],
                className='modal__dialog'
            )
        ],
            id='modal-1',
            className='modal_history modal--l'
        ),
        html.Script(
            src='assets/js/main.js'
        ),
    ])
    return layout
