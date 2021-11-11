import pandas as pd


def no_data():
    df = pd.DataFrame(columns=['task_number', 'reg_date', 'status', 'assign_group', 'wait', 'func_area', 'specialist',
                               'solve_date', 'is_sla', 'count_of_returns', 'work_time_solve', 'count_escalation_tasks',
                               'analytics'])
    return df


def load_df(df):
    df.drop(['Unnamed: 0', '№ п/п', 'ИТ-Сервис', 'Время Закрытия Инцидента (MSK)', 'Приоритет',
             '№ Обращения - Источника эскалации', 'Функция', 'Код Решения Заявки', 'Ошибка ППО Инцидента',
             'Время Решения Инцидента (план) (MSK)', 'Кем Последний раз переоткрывался Инцидент',
             'Место оказания услуг', 'Расположение Заявителя Инцидента', 'Описание Инцидента',
             'Резолюция Решения Инцидента', 'Количество постановок Инцидента в Ожидание'],
            axis=1,
            inplace=True)
    df.columns = ['task_number', 'reg_date', 'status', 'assign_group', 'wait', 'func_area', 'specialist', 'solve_date',
                  'is_sla', 'count_of_returns', 'work_time_solve', 'count_escalation_tasks', 'analytics']

    return df
