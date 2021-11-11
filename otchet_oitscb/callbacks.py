from datetime import datetime

import dash
import pandas as pd
from dash.dependencies import Output, Input

import otchet_oitscb
import otchet_oitscb.log_writer as lw
from otchet_oitscb.params import zik, bgu_list, cat_list_bgu, name_list_bgu, sub_bgu, cat_list_zkgu, name_list_zkgu, \
    sub_zkgu


def get_dates(start_date, end_date):
    start_date_d = datetime.strptime(start_date, '%Y-%m-%d')
    end_date_d = datetime.strptime(end_date, '%Y-%m-%d')
    delta = end_date_d - start_date_d
    prev_start_date_d = start_date_d - delta

    return start_date_d, end_date_d, prev_start_date_d


def register_callbacks(app):
    @app.callback(
        Output('loading-output-2', 'children'),
        Output('load_data', 'data'),
        Output('btn_load_prev_data', 'children'),
        Output('btn_load_prev_data', 'hidden'),
        Output('loading-output-3', 'children'),
        Output('load_prev_data', 'data'),
        Output('btn_load_curr_data', 'style'),
        Output('btn_load_prev_data', 'style'),
        Input('upload_data', 'contents'),
        Input('upload_data', 'filename'),
        Input('period', 'start_date'),
        Input('period', 'end_date'),
        Input('upload_prev_data', 'contents'),
        Input('upload_prev_data', 'filename')
    )
    def save_data(contents, filename, start_date, end_date, prev_contents, prev_filename):
        if (not start_date and not end_date) or (start_date and not end_date) or not contents:
            return dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, \
                   dash.no_update, dash.no_update
        if contents and not prev_contents:
            start_date_d, end_date_d, prev_date_d = get_dates(start_date, end_date)

            incoming_df = otchet_oitscb.parse_contents(contents=contents, filename=filename)

            period = ' '.join(['Загрузите данные за период с ', prev_date_d.strftime('%d-%m-%Y'), ' по ',
                               start_date_d.strftime('%d-%m-%Y')])

            return '', incoming_df.to_dict('records'), period, False, dash.no_update, dash.no_update, \
                   dict(backgroundColor='#7aa95c', color='black'), dash.no_update
        if prev_contents:
            incoming_df_1 = otchet_oitscb.parse_contents(contents=prev_contents, filename=prev_filename)
            return "", dash.no_update, dash.no_update, dash.no_update, '', incoming_df_1.to_dict('records'), \
                   dash.no_update, dict(backgroundColor='#7aa95c', color='black')

    @app.callback(
        Output('test', 'children'),
        Output('btn_make_report', 'style'),
        Input('load_data', 'data'),
        Input('load_prev_data', 'data'),
        Input('btn_make_report', 'n_clicks'),
        Input('period', 'start_date'),
        Input('period', 'end_date')
    )
    def build_report(data, prev_data, click, start_date, end_date):
        if click:
            df = pd.DataFrame(data)
            prev_df = pd.DataFrame(prev_data)
            if len(df) > 0 and len(prev_df) > 0:
                start_date_d, end_date_d, prev_date_d = get_dates(start_date, end_date)
                df_zkgu = otchet_oitscb.create_report(
                    df=df,
                    prev_df=prev_df,
                    start_date=start_date_d,
                    end_date=end_date_d,
                    prev_date=prev_date_d,
                    area=zik
                )
                df_bgu = otchet_oitscb.create_report(
                    df=df,
                    prev_df=prev_df,
                    start_date=start_date_d,
                    end_date=end_date_d,
                    prev_date=prev_date_d,
                    area=bgu_list
                )
                bgu_cat_df = otchet_oitscb.create_report_cat(
                    df=df,
                    prev_df=prev_df,
                    start_date=start_date_d,
                    end_date=end_date_d,
                    prev_date=prev_date_d,
                    cat_list=cat_list_bgu,
                    name_list=name_list_bgu,
                    sub=sub_bgu
                )
                zkgu_cat_df = otchet_oitscb.create_report_cat(
                    df=df,
                    prev_df=prev_df,
                    start_date=start_date_d,
                    end_date=end_date_d,
                    prev_date=prev_date_d,
                    cat_list=cat_list_zkgu,
                    name_list=name_list_zkgu,
                    sub=sub_zkgu
                )

                df_list = [df_bgu, bgu_cat_df, df_zkgu, zkgu_cat_df]

                otchet_oitscb.write_to_word(
                    header_list=otchet_oitscb.params.headers_lists,
                    df_list=df_list)
                lw.log_writer('Формирование отчета завершено')
                return '1', dict(backgroundColor='#7aa95c', margin='5px 40px', color='black')
            return dash.no_update, dash.no_update

        return '1', dict(margin='5px 40px')

    @app.callback(
        Output("download_report", "data"),
        Input("btn_save_report", "n_clicks"),
        prevent_initial_call=True,
    )
    def func(n_clicks):
        lw.log_writer('Скачивание файла с отчетом успешно завершено')
        return dash.dcc.send_file(
            "./downloads/report.docx"
        )
