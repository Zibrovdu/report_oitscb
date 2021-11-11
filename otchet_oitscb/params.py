zik = ['Зарплата и кадры (ЗиК)']

bgu_list = ['Бухгалтерский учет (БУ)', 'Миграция в ЭБ 2020', 'Система казначейских платежей',
            'Автоматизированное раб. место Центр. Бухгалтерии (АРМ ЦБ)']

oitscb_group = 'ЦА 1С_Группа сопровождения (ПУНФА, ПУиО, ПУК)'

tech_group = 'ЦА 1С_Группа технологического обеспечения (МБУ)'

headers_lists = [
    'Подсистемы управления нефинансовыми активами и подсистему учета и отчетности ГИИС ЭБ',
    'Категории обращений (ПУНФА, ПУиО)',
    'Подсистемы учета оплаты труда ГИИС ЭБ',
    'Категории обращений (ПУОТ)'
]


uchet_nfa = ['Учет НФА']
integracia_asfk_pur = ['Обмен с АСФК', 'АСФК', 'Проблемы интеграции 1С-АСФК‚ 1С-ПУР', 'ПУР']
rpd_docs = ['Проблемы с РПД и кассой']
spravochnik = ['Справочники']
nastroiki_punfa_puio = ['ПУНФА‚ ПУиО', 'Настройки в ПУНФА‚ ПУиО']
otchetnost_b = ['Регламентированная‚ бухгалтерская‚ налоговая и статистическая отчетность',
                'Регламентированная‚ бухгалтерская‚ налоговая и статистическая отчетность']
raschet_afl_person = ['Расчеты с подотчетными лицами', 'Командирование']
nalog = ['Расчет налогов‚ взносов']
izvescheniya = ['Извещения (ЭДО)']
income = ['Учет начисления доходов']
other_bgu = ['Статусная модель‚ роли/полномочия', 'Статусная модель‚ роли/полномочия',
             'Статусная модель‚ роли/полномочия', 'Доступ в базы', 'Администрирование учётной записи пользователя']
sankcia = ['Вопросы санкционирования']
teh_analiz = ['Технологический анализ', 'Регламентные операции (закрытие года)']
inventarizacia = ['Инвентарзация (НФА‚ расчеты)‚ акты сверки взаиморасчетов']
migration_bgu = ['Миграция БГУ']
uchet_postupl_uslug = ['Поступление услуг‚ работ‚ начисление доходов‚ в т.ч. будущих периодов']
integracia = ['Заработная плата (сводно-расчетная ведомость‚ договора ГПХ‚ справочники)']
likvidnost = ['Ликвидность']

raschet_zp = ['Расчет и выплата заработной платы', 'Расчет и выплата заработной платы']
eisuks = ['ЕИСУ КС']
kadrovie_docs = ['Ввод кадровых и прочих документов', 'ШР']
system_settings = ['Настройка зарплатного проекта', 'Системные настройки']
raschet_nalog = ['Расчет налогов‚ взносов']
migration_zkgu = ['Миграция ЗКГУ', 'Миграция ЗКГУ']
otchetnost_z = ['Формирование отчетности (по налогам‚ взносам‚ статистика)']
other_zkgu = ['Администрирование', 'Запуск процедур‚ обработок', 'Настройка подписи (Jinn-Client)']
tabel = ['Табель‚ график работы']
integracia_zkgu = ['Настройки интеграции (с БГУ‚ зарплатный проект)', 'Настройки интеграции (с БГУ‚ зарплатный проект)',
                   'Уполномоченный представитель‚ Калуга Астрал']
gpkh = ['ГПХ']
stipendia = ['Расчет стипендии', 'Расчёт стипендии']

cat_list_bgu = [
    uchet_nfa, integracia_asfk_pur, rpd_docs, spravochnik, nastroiki_punfa_puio, otchetnost_b, raschet_afl_person,
    nalog, izvescheniya, income, sankcia, teh_analiz, inventarizacia, migration_bgu, uchet_postupl_uslug, integracia,
    likvidnost, other_bgu
]
name_list_bgu = [
    'Учет НФА', 'АСФК, ПУР', 'Проблемы с РПД и кассой', 'Проблемы при работе со справочниками', 'Настройка ПУНФА, ПУиО',
    'Формирование отчетности (регламентированной, бухгалтерской, налоговой, статистической; стандартных отчетов)',
    'Расчеты с подотчетными лицами', 'Расчет налогов', 'Извещения', 'Учет доходов', 'Санкционирование',
    'Вопросы по технологическому анализу', 'Инвентаризация', 'Миграция', 'Учет поступления услуг',
    'Настройка интеграции БГУ/ЗКГУ', 'Ликвидность', 'Прочие'
]

cat_list_zkgu = [
    raschet_zp, eisuks, kadrovie_docs, system_settings, raschet_nalog, migration_zkgu, otchetnost_z, tabel,
    integracia_zkgu, gpkh, stipendia, other_zkgu
]

name_list_zkgu = [
    'Расчет и выплата заработной платы', 'ЕИСУ КС (интеграция с ЕИСУКС +обращения в тех поддержку ЕИСУКС)',
    'Ввод кадровых и прочих документов',
    'Вопросы по системным настройкам (справочник начислений и удержаний, прочие справочники ПУОТ)',
    'Расчет налогов‚ взносов', 'Вопросы миграции', 'Формирование отчетности (по налогам‚ взносам‚ статистика)',
    'Табель‚ график работы', 'Настройки интеграций (с БГУ, зарплатный проект)', 'ГПХ', 'Расчёт стипендии',
    'прочие вопросы '
]

sub_bgu = 'ПУНФА, ПУиО'

sub_zkgu = 'ПУОТ'