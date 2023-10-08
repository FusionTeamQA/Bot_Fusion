# -*- coding: utf-8 -*-
import time

import telebot
from datetime import datetime
from telebot import types
from session_db import connect_db
import setting
import sqlite3
import logging
import random
import os, sys
from config_db import host, user, password, db_name
from requests.exceptions import ConnectionError, ReadTimeout

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

# Загружаем список интересных фактов
f = open('data/facts.txt', 'r', encoding='UTF-8')
facts = f.read().split('\n')
f.close()

bot = telebot.TeleBot(setting.token)

user_dict = {}
user_chats = 0

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M")
print("date and time =", dt_string)


class User:

    def __init__(self, name):
        self.name = None
        self.age = None
        self.nums = None
        self.location = None
        self.experience = None
        self.format_work = None

        keys = ['name', 'age', 'nums', 'location', 'experience', 'format_work']
        for key in keys:
            self.key = None


@bot.message_handler(commands=['start'])  # стартовая команда
def start(message):
    connection = sqlite3.connect('bd/database_fusion.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users(
                    id INTEGER, 
                    user_first_name TEXT, 
                    user_last_name TEXT, 
                    username TEXT,
                    data_time varchar(50)
                    )''')
    connection.commit()
    people_id = message.from_user.id
    cursor.execute(f"SELECT id FROM users WHERE id = {people_id}")
    data = cursor.fetchone()
    if data is None:
        USER_ID = [message.from_user.id, message.from_user.first_name, message.from_user.last_name,
                   message.from_user.username, dt_string]
        cursor.execute("INSERT INTO users VALUES(?,?,?,?,?);", USER_ID)
        connection.commit()
    else:
        print(message.from_user.username)
    cursor.execute('''CREATE TABLE IF NOT EXISTS users_session(
                        id INTEGER,
                        user_first_name varchar(50),
                        user_last_name varchar(50),
                        username varchar(50),
                        data_time varchar(50)
                        )''')
    connection.commit()
    USER_ID = [message.from_user.id, message.from_user.first_name, message.from_user.last_name,
               message.from_user.username, dt_string]
    cursor.execute("INSERT INTO users_session VALUES(?,?,?,?,?);", USER_ID)
    connection.commit()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🇷🇺 Русский")
    btn2 = types.KeyboardButton('🇬🇧 English')
    markup.add(btn1)
    bot.send_message(message.from_user.id, "🇷🇺 Выберите язык / 🇬🇧 Choose your language", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Русский язык
    if message.text == '🇷🇺 Русский':
        logging.info('Start bot - ' + message.chat.username)
        print(message.chat.username)
        print('_____________________')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn2 = types.KeyboardButton('📢 Вакансии')
        btn5 = types.KeyboardButton('📝 Оставить заявку')
        btn11 = types.KeyboardButton('⚖️ Стажировка')
        btn1 = types.KeyboardButton("🌐 Сайт")
        btn3 = types.KeyboardButton('📁 Проекты')
        btn4 = types.KeyboardButton('📚 Блог')
        btn7 = types.KeyboardButton('👥 Мы в ВК')
        btn14 = types.KeyboardButton('💬 Мы на VC.RU')
        btn8 = types.KeyboardButton('🔥 Мы на Хабр')
        btn9 = types.KeyboardButton('🅱️ Мы на Behance')
        btn12 = types.KeyboardButton('📸 Мы в Instagram')
        btn13 = types.KeyboardButton('🎁 Получить факт о нас')
        btn10 = types.KeyboardButton('✍️️ Мы на LinkedIn')
        markup.add(btn2, btn5, btn11, btn1, btn3, btn4, btn7, btn8, btn9, btn10, btn12, btn14, btn13 )
        bot.send_message(message.from_user.id, "👋 Вас приветствует бот компании Fusion Tech", reply_markup=markup)
        bot.send_message(message.from_user.id, '👀 Выберите интересующий вас раздел')

    if message.text == 'русский':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn2 = types.KeyboardButton('📢 Вакансии')
        btn5 = types.KeyboardButton('📝 Оставить заявку')
        btn11 = types.KeyboardButton('⚖️ Стажировка')
        btn1 = types.KeyboardButton("🌐 Сайт")
        btn3 = types.KeyboardButton('📁 Проекты')
        btn4 = types.KeyboardButton('📚 Блог')
        btn14 = types.KeyboardButton('💬 Мы на VC.RU')
        btn7 = types.KeyboardButton('👥 Мы в ВК')
        btn8 = types.KeyboardButton('🔥 Мы на Хабр')
        btn9 = types.KeyboardButton('🅱️ Мы на Behance')
        btn12 = types.KeyboardButton('📸 Мы в Instagram')
        btn13 = types.KeyboardButton('🎁 Получить факт о нас')
        btn10 = types.KeyboardButton('✍️️ Мы на LinkedIn')
        markup.add(btn2, btn5, btn11, btn1, btn3, btn4, btn7, btn8, btn9, btn10, btn12, btn14, btn13 )
        bot.send_message(message.from_user.id, "👋 Вас приветствует бот компании Fusion Tech", reply_markup=markup)
        bot.send_message(message.from_user.id, '👀 Выберите интересующий вас раздел')

    if message.text == 'Русский':
        print(message.chat.username)
        print('_____________________')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn2 = types.KeyboardButton('📢 Вакансии')
        btn5 = types.KeyboardButton('📝 Оставить заявку')
        btn11 = types.KeyboardButton('⚖️ Стажировка')
        btn1 = types.KeyboardButton("🌐 Сайт")
        btn3 = types.KeyboardButton('📁 Проекты')
        btn4 = types.KeyboardButton('📚 Блог')
        btn7 = types.KeyboardButton('👥 Мы в ВК')
        btn14 = types.KeyboardButton('💬 Мы на VC.RU')
        btn8 = types.KeyboardButton('🔥 Мы на Хабр')
        btn9 = types.KeyboardButton('🅱️ Мы на Behance')
        btn12 = types.KeyboardButton('📸 Мы в Instagram')
        btn13 = types.KeyboardButton('🎁 Получить факт о нас')
        btn10 = types.KeyboardButton('✍️️ Мы на LinkedIn')
        markup.add(btn2, btn5, btn11, btn1, btn3, btn4, btn7, btn8, btn9, btn10, btn12, btn14, btn13 )
        bot.send_message(message.from_user.id, "👋 Вас приветствует бот компании Fusion Tech", reply_markup=markup)
        bot.send_message(message.from_user.id, '👀 Выберите интересующий вас раздел')

    elif message.text == '🔙 Вернуться к выбору языка':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🇷🇺 Русский")
        btn2 = types.KeyboardButton('🇬🇧 English')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, "🇷🇺 Выберите язык / 🇬🇧 Choose your language", reply_markup=markup)

    elif message.text == '🌐 Сайт':
        logging.info('Открыт раздел сайт, юзер - ' + message.chat.username)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup2 = types.InlineKeyboardMarkup()
        markup2.add(types.InlineKeyboardButton("Посетить веб-сайт", setting.website))
        bot.send_message(message.from_user.id,
                         'Наша гордость - наша история.👍 Перейти к сайту можно по ссылке ' + setting.website,
                         reply_markup=markup2, parse_mode='HTML')
    elif message.text == '📢 Вакансии':
        logging.info('Открыт раздел Вакансии, юзер - ' + message.chat.username)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        markup2 = types.InlineKeyboardMarkup()
        markup2.add(types.InlineKeyboardButton("Посмотреть вакансии на сайте", setting.vacansies))
        btn1 = types.KeyboardButton('React/React Native-разработчик')
        btn2 = types.KeyboardButton('Frontend-разработчик')
        btn3 = types.KeyboardButton('Fullstack-разработчик')
        btn4 = types.KeyboardButton('Менеджер по продажам (Sales Manager)')
        btn6 = types.KeyboardButton('Маркетолог-аналитик')
        btn7 = types.KeyboardButton('Лидогенератор')
        btn8 = types.KeyboardButton('Менеджер проектов')
        btn5 = types.KeyboardButton('Стажер-рекрутер')
        # btn9 = types.KeyboardButton('Офис-менеджер')
        # btn10 = types.KeyboardButton('Специалист по тендерам')
        # btn11 = types.KeyboardButton('DevOps')
        # btn12 = types.KeyboardButton('Стажер-Лидогенератор')
        # btn13 = types.KeyboardButton('Контент-менеджер')
        # btn14 = types.KeyboardButton('Графический дизайнер')
        btn15 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2, btn3, btn4, btn8, btn6, btn7, btn5, btn15)
        bot.send_message(message.from_user.id,
                         'Раздел: 📢 Вакансии\n \n👍🏻 Хочешь создавать лучшее? Тогда нам по пути! \n',
                         reply_markup=markup2, parse_mode='HTML')
        bot.send_message(message.from_user.id, '⬇ Или перейди на нужную вакансию по кнопкам ниже', reply_markup=markup)


    elif message.text == 'Frontend-разработчик':
        logging.info('Открыт раздел Frontend-разработчик, юзер - ' + message.chat.username)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        markup2 = types.InlineKeyboardMarkup()
        markup2.add(types.InlineKeyboardButton("Откликнуться", setting.Link_vacansies))
        items_task_frontend = ['Разработка веб-приложения с использованием React;',
                               'Typescript;',
                               'Material UI;',
                               'Styled components;',
                               'Redux + Redux Toolkit;',
                               'Socket.io']
        items_experience_frontend = ['React;',
                               'Typescript;',
                               'Redux+Redux Toolkit;',
                               'Material UI;',
                               'Styled components',
                               'Socket.io;',
                               'Крутой бонус, если есть опыт с Node.js;',
                               'Уровень английского не ниже B1;',
                               'Опыт от 2-х лет']
        list_task_frontend = '\n'.join([f'• {item}' for item in items_task_frontend])
        list_experience_frontend = '\n'.join([f'• {item}' for item in items_experience_frontend])
        bot.send_message(message.from_user.id,'Твои задачи:')
        bot.send_message(message.from_user.id, list_task_frontend)
        bot.send_message(message.from_user.id,'Твой опыт:')
        bot.send_message(message.from_user.id, list_experience_frontend, reply_markup=markup2, parse_mode='HTML')

    elif message.text == 'React/React Native-разработчик':
        logging.info('Открыт раздел React/React Native-разработчик, юзер - ' + message.chat.username)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        markup2 = types.InlineKeyboardMarkup()
        markup2.add(types.InlineKeyboardButton("Откликнуться", setting.Link_vacansies))
        items_task_reactNative = ['Уметь работать в команде;',
                               'быть вовлеченным в работу;',
                               'быть нацеленным на успех нашей компании и компании клиента;',
                               'иметь отличные навыки описания технических проблем;',
                               'уметь правильно формулировать и не стесняться задавать вопросы;',
                               'уметь эффективно коммуницировать с тестировщиками;',
                                'уметь расслабляться']
        items_experience_reactNative = ['опыт коммерческой разработки от 2 лет;',
                               'знание и умение использовать следующие технологии: React Native, Redux, Serverless,'
                               'JavaScript ES5/ES6, TypeScript, HTML5, CSS3, SASS/LESS, Responsive design, Webpack, npm;',
                               'знание и понимание принципов работы и паттернов React и Redux;',
                               'уверенные знания JavaScript, HTML, CSS а также DOM, BEM, SASS/LESS;',
                               'опыт работы с REST API;',
                               'опыт работы с babel, webpack, gulp, npm и т.д;',
                               'опыт работы с Git;',
                               'знание английского языка не ниже В2;',
                               'жирным плюсом будет опыт работы с SQL и Supabase.']
        list_task_reactNative = '\n'.join([f'• {item}' for item in items_task_reactNative])
        list_experience_reactNative = '\n'.join([f'• {item}' for item in items_experience_reactNative])
        bot.send_message(message.from_user.id,'Твои задачи:')
        bot.send_message(message.from_user.id, list_task_reactNative)
        bot.send_message(message.from_user.id,'Твой опыт:')
        bot.send_message(message.from_user.id, list_experience_reactNative, reply_markup=markup2, parse_mode='HTML')

    elif message.text == 'Fullstack-разработчик':
        logging.info('Открыт раздел Fullstack-разработчик, юзер - ' + message.chat.username)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        markup2 = types.InlineKeyboardMarkup()
        markup2.add(types.InlineKeyboardButton("Откликнуться", setting.Link_vacansies))
        items_task_fullstack = ['Разработка веб-приложения с использованием React;',
                               'Typescript;',
                               'Material UI;',
                               'Styled components;',
                               'Redux + Redux Toolkit;',
                               'Socket.io',
                               'Разработка серверной части веб-приложений;',
                               'Проектирование API и базы данных;',
                               'Разработка микросервисов.']
        items_experience_fullstack = ['React;',
                               'Typescript;',
                               'Redux+Redux Toolkit;',
                               'Material UI;',
                               'Styled components',
                               'Socket.io;',
                               'знание Node.js и понимание принципов его работы;',
                               'опыт с одним из фреймворков: Express, Nest.js, koa, Fastify;',
                               'опыт работы хотя бы с одним из TypeORM/Sequelize/Mongo;',
                               'опыт работы хотя бы с одним из AWS/GCP/Azure;',
                               'знание Docker, Nginx, Unix;',
                               'плюсом будет опыт разработки Serverless-приложений;',
                               'Уровень английского не ниже B1;',
                               'Опыт от 2-х лет']
        list_task_fullstack = '\n'.join([f'• {item}' for item in items_task_fullstack])
        list_experience_fullstack = '\n'.join([f'• {item}' for item in items_experience_fullstack])
        bot.send_message(message.from_user.id,'Твои задачи:')
        bot.send_message(message.from_user.id, list_task_fullstack)
        bot.send_message(message.from_user.id,'Твой опыт:')
        bot.send_message(message.from_user.id, list_experience_fullstack, reply_markup=markup2, parse_mode='HTML')

    elif message.text == 'Менеджер по продажам (Sales Manager)':
        logging.info('Открыт раздел Менеджер по продажам (Sales Manager), юзер - ' + message.chat.username)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        markup2 = types.InlineKeyboardMarkup()
        markup2.add(types.InlineKeyboardButton("Откликнуться", setting.Link_vacansies))
        items_task_salesManager = ['работа с текущей базой клиентов;',
                               'составление CV разработчиков;',
                               'согласование выхода на интервью;',
                               'выполнение вспомогательных задач, сопутствующих работе с клиентами;',
                               'ведение деловой переписки;',
                               'работа с документами (NDA, договора);',
                               'взаимодействие с менеджерами партнеров;',
                               'презентация компании;',
                               'поиск новых направлений аутстаффинга.']
        items_experience_salesManager = ['опыт в IT-продажах;',
                               'опыт работы с аутстаффингом;',
                               'Redux+Redux Toolkit;',
                               'знание английского НЕ требуется, но будет крутым бонусом.']
        list_task_salesManager = '\n'.join([f'• {item}' for item in items_task_salesManager])
        list_experience_salesManager = '\n'.join([f'• {item}' for item in items_experience_salesManager])
        bot.send_message(message.from_user.id,'Твои задачи:')
        bot.send_message(message.from_user.id, list_task_salesManager)
        bot.send_message(message.from_user.id,'Твой опыт:')
        bot.send_message(message.from_user.id, list_experience_salesManager, reply_markup=markup2, parse_mode='HTML')

    elif message.text == 'Стажер-рекрутер':
        logging.info('Открыт раздел Стажер-рекрутер, юзер - ' + message.chat.username)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        markup2 = types.InlineKeyboardMarkup()
        markup2.add(types.InlineKeyboardButton("Откликнуться", setting.Link_vacansies))
        items_task_stajer_recruiter = ['составление портрета кандидата;',
                               'поиск и подбор кандидатов по заданным вакансиям;',
                               'общение с кандидатами;',
                               'проведение первичных интервью.']
        items_experience_stajer_recruiter = ['вакансия подразумевает обучение работе с нужными инструментами по разработанному ментором плану;',
                               'важно иметь представление о рекрутинге;',
                               'уметь общаться с людьми;',
                               'быть грамотным (устная и письменная речь) и вежливым;',
                               'быть нацеленным не просто на закрытие вакансии, а на подбор эффективного члена команды.']
        list_task_stajer_recruiter = '\n'.join([f'• {item}' for item in items_task_stajer_recruiter])
        list_experience_stajer_recruiter = '\n'.join([f'• {item}' for item in items_experience_stajer_recruiter])
        bot.send_message(message.from_user.id,'Твои задачи:')
        bot.send_message(message.from_user.id, list_task_stajer_recruiter)
        bot.send_message(message.from_user.id,'Твой опыт:')
        bot.send_message(message.from_user.id, list_experience_stajer_recruiter, reply_markup=markup2, parse_mode='HTML')

    elif message.text == 'Маркетолог-аналитик':
        logging.info('Открыт раздел Маркетолог-аналитик, юзер - ' + message.chat.username)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        markup2 = types.InlineKeyboardMarkup()
        markup2.add(types.InlineKeyboardButton("Откликнуться", setting.Link_vacansies))
        items_task_marketolog_analytics = ['маркетинговый анализ;',
                               'маркетинговые исследования;',
                               'анализ внутреннего рынка и проработка новых ниш;',
                               'SWOT-анализ;',
                               'анализ конкурентной среды;',
                               'анализ данных;',
                               'разработка маркетинговой стратегии;',
                               'работа с рекламными кабинетами и метриками;',
                               'работа с инструментами сквозной аналитики;',
                               'работа с прочими маркетинговыми инструментами.']
        items_experience_marketolog_analytics = ['опыт работы со всеми вышеперечисленными задачами и маркетинговыми инструментами;',
                               'знание английского не требуется, но будет большим плюсом.']
        list_task_marketolog_analytics = '\n'.join([f'• {item}' for item in items_task_marketolog_analytics])
        list_experience_marketolog_analytics = '\n'.join([f'• {item}' for item in items_experience_marketolog_analytics])
        bot.send_message(message.from_user.id,'Твои задачи:')
        bot.send_message(message.from_user.id, list_task_marketolog_analytics)
        bot.send_message(message.from_user.id,'Твой опыт:')
        bot.send_message(message.from_user.id, list_experience_marketolog_analytics, reply_markup=markup2, parse_mode='HTML')

    elif message.text == 'Лидогенератор':
        logging.info('Открыт раздел Лидогенератор, юзер - ' + message.chat.username)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        markup2 = types.InlineKeyboardMarkup()
        markup2.add(types.InlineKeyboardButton("Откликнуться", setting.Link_vacansies))
        items_task_lidogenerator = ['генерация и постоянное наращивание базы иностранных лидов;',
                               'работа с соответствующими инструментами.']
        items_experience_lidogenerator = ['письменный английский от В1;',
                                                 'опыт работы 1+ год на позиции лидгенератора в IT;',
                                                 'высокий уровень коммуникативных навыков;',
                                                 'грамотная устная и письменная речь.']
        list_task_lidogenerator = '\n'.join([f'• {item}' for item in items_task_lidogenerator])
        list_experience_lidogenerator = '\n'.join([f'• {item}' for item in items_experience_lidogenerator])
        bot.send_message(message.from_user.id,'Твои задачи:')
        bot.send_message(message.from_user.id, list_task_lidogenerator)
        bot.send_message(message.from_user.id,'Твой опыт:')
        bot.send_message(message.from_user.id, list_experience_lidogenerator, reply_markup=markup2, parse_mode='HTML')

    elif message.text == 'Менеджер проектов':
        logging.info('Открыт раздел Стажер-рекрутер, юзер - ' + message.chat.username)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        markup2 = types.InlineKeyboardMarkup()
        markup2.add(types.InlineKeyboardButton("Откликнуться", setting.Link_vacansies))
        items_task_project_manager = ['планирование работ, сбор и анализ требований, постановка задач исполнителям, контроль результатов, сроков и бюджета;',
                               'созвоны с клиентами, управление их ожиданиями, совместная разработка роадмапов;',
                               'контроль своевременной оплаты от клиентов;',
                               'организация слаженной работы в проектной команде;',
                               'проактивность, участие в улучшении процессов компании.']
        items_experience_project_manager = ['релевантный опыт от 2-х лет;',
                               'разговорный английский уровня В2 и выше.']
        list_task_project_manager = '\n'.join([f'• {item}' for item in items_task_project_manager])
        list_experience_project_manager = '\n'.join([f'• {item}' for item in items_experience_project_manager])
        bot.send_message(message.from_user.id,'Твои задачи:')
        bot.send_message(message.from_user.id, list_task_project_manager)
        bot.send_message(message.from_user.id,'Твой опыт:')
        bot.send_message(message.from_user.id, list_experience_project_manager, reply_markup=markup2, parse_mode='HTML')

    elif message.text == '⚖️ Стажировка':
        logging.info('Открыт раздел Стажировка, юзер -' + message.chat.username)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('🕵🏼 Написать Даше (HR компании)')
        btn2 = types.KeyboardButton('📝 Оставить заявку')
        btn3 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, 'На данный момент мы обучаем кандидатов, имеющих базовые знания HTML, CSS, JS '
                                               'и уровень владения английским не ниже чтения технической документации. '
                                               'Преимуществом будут базовые знания React.js.', reply_markup=markup)
        time.sleep(1)
        bot.send_message(message.from_user.id, 'Почему мы предъявляем такие требования? На каждый этап стажировки отводится определенное время, за рамки которого желательно не выходить.'
                                               'Сроки достаточно сжатые, уложиться в них без базы будет сложно.', reply_markup=markup)
        time.sleep(1)
        bot.send_message(message.from_user.id, 'Обучение длится около 3-х месяцев (порой меньше, в зависимости от скорости усвоения материала). '
                                               'За вами закрепляется ментор, который дает теоретические и практические задания, а также постоянную обратную связь. '
                                               'Проходит обучение непосредственно на территории Fusion Lab, каждый будний день (8 часов в день/40 часов в неделю).', reply_markup=markup)
        time.sleep(1)
        bot.send_message(message.from_user.id, 'Конечный результат стажировки - фуллстек-разработчик (фронтенд на React.js , бэкенд на Node.js)', reply_markup=markup)
        time.sleep(1)
        bot.send_message(message.from_user.id, 'Форматы обучения: в офисе, удаленный и гибридный (в офисе и некоторые дни удаленно)', reply_markup=markup)
        time.sleep(1)
        bot.send_message(message.from_user.id, 'При успешном завершении стажировки компания предлагает официальное трудоустройство по ТК РФ.', reply_markup=markup)
        time.sleep(1)
        bot.send_message(message.from_user.id, 'Обучение бесплатное, стипендии не выплачиваются.', reply_markup=markup)
        time.sleep(3)
        bot.send_message(message.from_user.id, 'Оставьте заявку для дальнейшего собеседования или по всем вопросам и деталям пиши '
                         'Даше сюда --->>>' + setting.VK_HR)


    elif message.text == '📁 Проекты':
        logging.info('Открыт раздел Проекты, юзер - ' + message.chat.username)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        markup2 = types.InlineKeyboardMarkup()
        markup2.add(types.InlineKeyboardButton("Посмотреть наши проекты", setting.projects))
        bot.send_message(message.from_user.id,
                         'Раздел: 🚀 Проекты\n \n👍🏻📲 Перейти к разделу можно по ссылке ' + setting.projects,
                         reply_markup=markup2, parse_mode='HTML')

    elif message.text == '📚 Блог':
        logging.info('Открыт раздел Блог, юзер - ' + message.chat.username)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        markup2 = types.InlineKeyboardMarkup()
        markup2.add(types.InlineKeyboardButton("Почитать наш блог", setting.blog))
        bot.send_message(message.from_user.id,
                         'Раздел: 📚 Блог\n \n👍🏻 Свежие новости студии, работа и идеи\n \n📲 Перейти к разделу можно по ссылке ' + setting.blog,
                         reply_markup=markup2, parse_mode='HTML')

    elif message.text == '🔙 Главное меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn2 = types.KeyboardButton('📢 Вакансии')
        btn5 = types.KeyboardButton('📝 Оставить заявку')
        btn11 = types.KeyboardButton('⚖️ Стажировка')
        btn1 = types.KeyboardButton("🌐 Сайт")
        btn3 = types.KeyboardButton('📁 Проекты')
        btn4 = types.KeyboardButton('📚 Блог')
        btn7 = types.KeyboardButton('👥 Мы в ВК')
        btn14 = types.KeyboardButton('💬 Мы на VC.RU')
        btn8 = types.KeyboardButton('🔥 Мы на Хабр')
        btn9 = types.KeyboardButton('🅱️ Мы на Behance')
        btn12 = types.KeyboardButton('📸 Мы в Instagram')
        btn13 = types.KeyboardButton('🎁 Получить факт о нас')
        btn10 = types.KeyboardButton('✍️️ Мы на LinkedIn')
        markup.add(btn2, btn5, btn11, btn1, btn3, btn4, btn7, btn8, btn9, btn10, btn12, btn14, btn13 )
        bot.send_message(message.from_user.id, '👀 Выберите интересующий вас раздел', reply_markup=markup)

    elif message.text == '👥 Мы в ВК':
        logging.info('Открыт раздел ВК, юзер -' + message.chat.username)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('🕵🏼 Написать Даше (HR компании)')
        btn2 = types.KeyboardButton('✏️ Написать нам')
        btn3 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '⬇ Выбери то, что тебе интересно', reply_markup=markup)
        bot.send_message(message.from_user.id,
                         'Перейти к группе ВК можно по ссылке ' + setting.VK,
                         reply_markup=markup, parse_mode='HTML')
    # Small talk

    elif message.text == 'Привет!':
        bot.send_message(message.from_user.id, 'Привет!')

    elif message.text == 'привет!':
        bot.send_message(message.from_user.id, 'Привет!')

    elif message.text == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')

    elif message.text == 'как дела?':
        bot.send_message(message.from_user.id, 'Хорошо!')

    elif message.text == 'Как дела?':
        bot.send_message(message.from_user.id, 'Хорошо!')

    elif message.text == 'как дела':
        bot.send_message(message.from_user.id, 'Хорошо!')

    elif message.text == 'Заявка':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn2 = types.KeyboardButton('📢 Вакансии')
        btn5 = types.KeyboardButton('📝 Оставить заявку')
        bot.send_message(message.from_user.id, 'Оставьте заявку для дальнейшего собеседования', reply_markup=markup)
        markup.add(btn2, btn5)

    elif message.text == 'заявка':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn2 = types.KeyboardButton('📢 Вакансии')
        btn5 = types.KeyboardButton('📝 Оставить заявку')
        bot.send_message(message.from_user.id, 'Оставьте заявку для дальнейшего собеседования', reply_markup=markup)
        markup.add(btn2, btn5)

    elif message.text == 'собеседование':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn2 = types.KeyboardButton('📢 Вакансии')
        btn5 = types.KeyboardButton('📝 Оставить заявку')
        bot.send_message(message.from_user.id, 'Оставьте заявку для дальнейшего собеседования', reply_markup=markup)
        markup.add(btn2, btn5)

    elif message.text == 'работа':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn2 = types.KeyboardButton('📢 Вакансии')
        btn5 = types.KeyboardButton('📝 Оставить заявку')
        bot.send_message(message.from_user.id, 'Оставьте заявку для дальнейшего собеседования', reply_markup=markup)
        markup.add(btn2, btn5)

    elif message.text == 'вакансии':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn2 = types.KeyboardButton('📢 Вакансии')
        btn5 = types.KeyboardButton('📝 Оставить заявку')
        bot.send_message(message.from_user.id, 'Оставьте заявку для дальнейшего собеседования', reply_markup=markup)
        markup.add(btn2, btn5)

    elif message.text == 'хочу на собеседование':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn2 = types.KeyboardButton('📢 Вакансии')
        btn5 = types.KeyboardButton('📝 Оставить заявку')
        bot.send_message(message.from_user.id, 'Оставьте заявку для дальнейшего собеседования', reply_markup=markup)
        markup.add(btn2, btn5)

    elif message.text == 'пока':
        bot.send_message(message.from_user.id, 'Всего доброго, заходите еще')

    elif message.text == 'Пока':
        bot.send_message(message.from_user.id, 'Всего доброго, заходите еще')

    elif message.text == 'Новости':
        bot.send_message(message.from_user.id,
                         'Раздел: 📚 Блог\n \n👍🏻 Свежие новости студии, работа и идеи\n \n📲 Перейти к разделу можно по ссылке ' + setting.blog,
                         parse_mode='HTML')

    elif message.text == 'новости':
        bot.send_message(message.from_user.id,
                         'Раздел: 📚 Блог\n \n👍🏻 Свежие новости студии, работа и идеи\n \n📲 Перейти к разделу можно по ссылке ' + setting.blog,
                         parse_mode='HTML')

    elif message.text == '🕵🏼 Написать Даше (HR компании)':
        logging.info('Открыт раздел Написать Даше, юзер - ' + message.chat.username)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        markup2 = types.InlineKeyboardMarkup()
        markup2.add(types.InlineKeyboardButton("Откликнуться", setting.VK_HR))
        bot.send_message(message.from_user.id,
                         'По вопросу трудоустройства и стажировок пиши в сообщество, нашему HR Дарье по ссылке ' + setting.VK_HR,
                         reply_markup=markup2, parse_mode='HTML')

    elif message.text == '✏️ Написать нам':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        markup2 = types.InlineKeyboardMarkup()
        markup2.add(types.InlineKeyboardButton("Написать нам в ВКонтакте", setting.VK_GROUP_CHAT))
        bot.send_message(message.from_user.id,
                         'По общим вопросам пиши нам в сообщество, по ссылке ' + setting.VK_GROUP_CHAT,
                         reply_markup=markup2, parse_mode='HTML')

    elif message.text == '✍️️ Мы на LinkedIn':
        logging.info('Открыт раздел LinkedIn, юзер - ' + message.chat.username)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        markup2 = types.InlineKeyboardMarkup()
        markup2.add(types.InlineKeyboardButton("Перейти к нам на страницу", setting.LINKEDIN))
        bot.send_message(message.from_user.id, '\n Перейти к разделу можно по ссылке ' + setting.LINKEDIN,
                         reply_markup=markup2, parse_mode='HTML')

    elif message.text == '🅱️ Мы на Behance':
        logging.info('Открыт раздел Behance, юзер - ' + message.chat.username)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        markup2 = types.InlineKeyboardMarkup()
        markup2.add(types.InlineKeyboardButton("Перейти к нам на страницу", setting.BEHANCE))
        bot.send_message(message.from_user.id,
                         'With our expertise,we can suggest the best solutions for your project to make it as good as possible.'
                         '\n Перейти к разделу можно по ссылке ' + setting.BEHANCE,
                         reply_markup=markup2, parse_mode='HTML')

    elif message.text == '📸 Мы в Instagram':
        logging.info('Открыт раздел Instagram, юзер - ' + message.chat.username)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        markup2 = types.InlineKeyboardMarkup()
        markup2.add(types.InlineKeyboardButton("Перейти к нам на страницу", setting.INSTAGRAM))
        bot.send_message(message.from_user.id,
                         '🏆ТОП-100 работодателей России // Хабр Карьера'
                         '\n📍Taganrog // Yerevan // Claymont'
                         '\n Перейти к разделу можно по ссылке ' + setting.INSTAGRAM,
                         reply_markup=markup2, parse_mode='HTML')

    elif message.text == '💬 Мы на VC.RU':
        logging.info('Открыт раздел Хабр, юзер - ' + message.chat.username)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         'Об опыте развития IT-компании, бизнес-процессах, кейсах и решениях. \n Веб/мобильная разработка, UI/UX, '
                         'QA, проектный менеджмент, аудит проектов.'
                         '\n Перейти к разделу можно по ссылке ' + setting.VC_RU,
                         reply_markup=markup, parse_mode='HTML')

    elif message.text == '🔥 Мы на Хабр':
        logging.info('Открыт раздел Хабр, юзер - ' + message.chat.username)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        btn2 = types.KeyboardButton('Страница компании')
        btn3 = types.KeyboardButton('📰 Вакансии')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id,
                         'Найди работу по душе 🎉 \n В базе Хабр Карьеры всегда актуальные вакансии компании'
                         '\n Перейти к разделу можно по ссылке ' + setting.HABR,
                         reply_markup=markup, parse_mode='HTML')

    elif message.text == '🎁 Получить факт о нас':
        logging.info('Открыл раздел факты, юзер - ' + message.chat.username)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn2 = types.KeyboardButton('🎁 Факт')
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn2, btn1)
        bot.send_message(message.chat.id, 'Только факты. Только Fusion Tech', reply_markup=markup)
        bot.send_message(message.chat.id, 'Нажми "Факт", чтобы узнать что-то интересное о нас', reply_markup=markup)

    elif message.text == '🎁 Факт':
        answer = random.choice(facts)
        bot.send_message(message.chat.id, answer)


    elif message.text == 'Страница компании':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         "Мы Fusion Tech - компания, уже более 5-ти лет предоставляющая качественные веб и мобильные продукты, клиентский сервис, а также пропуск в мир IT через бесплатную стажировку в компании под наставничеством опытных кураторов.")
        bot.send_message(message.from_user.id,
                         'Почитать более подробно, а также подписаться на нашу компанию можно по ссылке ' + setting.HABR,
                         reply_markup=markup, parse_mode='HTML')

    elif message.text == '📝 Оставить заявку':
        logging.info('Старт заявки' + message.chat.username)
        chat_id = message.chat.id
        board = types.InlineKeyboardMarkup()
        cancel = types.InlineKeyboardButton(text="Отменить заявку", callback_data="Отмена")
        board.add(cancel)
        msg = bot.send_message(chat_id, "Добрый день, представьтесь пожалуйста.", reply_markup=board)
        bot.register_next_step_handler(msg, name_step)


def name_step(message, user=None):
    try:
        board = types.InlineKeyboardMarkup()
        cancel = types.InlineKeyboardButton(text="Отменить заявку", callback_data="Отмена")
        board.add(cancel)
        chat_id = message.chat.id
        name = message.text
        user = User(name)
        user_dict[chat_id] = user
        msg = bot.send_message(chat_id, "Укажите ваш возраст", reply_markup=board)
        bot.register_next_step_handler(msg, process_age_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def process_age_step(message):
    try:
        board = types.InlineKeyboardMarkup()
        cancel = types.InlineKeyboardButton(text="Отменить заявку", callback_data="Отмена")
        board.add(cancel)
        chat_id = message.chat.id
        age = message.text
        if not age.isdigit():
            msg = bot.send_message(chat_id, 'Возраст должен быть числом, введи его повторно: ')
            bot.register_next_step_handler(msg, process_age_step)
            return
        user = user_dict[chat_id]
        user.age = age
        msg = bot.send_message(chat_id, 'К какой специализации вы относитесь?', reply_markup=board)
        bot.register_next_step_handler(msg, process_spec_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def process_spec_step(message):
    try:
        board = types.InlineKeyboardMarkup()
        cancel = types.InlineKeyboardButton(text="Отменить заявку", callback_data="Отмена")
        board.add(cancel)
        chat_id = message.chat.id
        language = message.text
        user = user_dict[chat_id]
        user.languages = language
        msg = bot.send_message(chat_id, 'Локация', reply_markup=board)
        bot.register_next_step_handler(msg, process_location_step)
    except Exception as e:
        bot.reply_to(message, 'Непредвиденная ошибка')


def process_location_step(message):
    try:
        board = types.InlineKeyboardMarkup()
        cancel = types.InlineKeyboardButton(text="Отменить заявку", callback_data="Отмена")
        board.add(cancel)
        chat_id = message.chat.id
        location = message.text
        user = user_dict[chat_id]
        user.location = location
        msg = bot.send_message(chat_id, 'Формат работы (удаленно/офис)', reply_markup=board)
        bot.register_next_step_handler(msg, process_format_work_step)
    except Exception as e:
        bot.reply_to(message, 'Непредвиденная ошибка')


def process_format_work_step(message):
    try:
        board = types.InlineKeyboardMarkup()
        cancel = types.InlineKeyboardButton(text="Отменить заявку", callback_data="Отмена")
        board.add(cancel)
        chat_id = message.chat.id
        format_work = message.text
        user = user_dict[chat_id]
        user.format_work = format_work
        msg = bot.send_message(chat_id, 'Опыт работы?', reply_markup=board)
        bot.register_next_step_handler(msg, process_experience_step)
    except Exception as e:
        bot.reply_to(message, 'Непредвиденная ошибка')


def process_experience_step(message):
    try:
        board = types.InlineKeyboardMarkup()
        cancel = types.InlineKeyboardButton(text="Отменить заявку", callback_data="Отмена")
        board.add(cancel)
        chat_id = message.chat.id
        experience = message.text
        user = user_dict[chat_id]
        user.experience = experience
        msg = bot.send_message(chat_id,
                               'Вставьте ссылку на ваш профиль(GitHub,Behance,Dribbble,Figma,VK) если нет - напишите нет: ',
                               reply_markup=board)
        bot.register_next_step_handler(msg, process_git_acc_step)
    except Exception as e:
        bot.reply_to(message, 'Непредвиденная ошибка')


def process_git_acc_step(message):
    try:
        board = types.InlineKeyboardMarkup()
        cancel = types.InlineKeyboardButton(text="Отменить заявку", callback_data="Отмена")
        board.add(cancel)
        board = types.InlineKeyboardMarkup()
        cancel = types.InlineKeyboardButton(text="Отмена", callback_data="Отмена")
        board.add(cancel)
        chat_id = message.chat.id
        git_acc1 = message.text
        user = user_dict[chat_id]
        user.git_acc = git_acc1
        msg = bot.send_message(chat_id, "Контактные данные", reply_markup=board)
        bot.register_next_step_handler(msg, contnums)

    except Exception as e:
        bot.reply_to(message, 'Непредвиденная ошибка')


def contnums(message):
    try:
        board = types.InlineKeyboardMarkup()
        cancel = types.InlineKeyboardButton(text="Отменить заявку", callback_data="Отмена")
        board.add(cancel)
        chat_id = message.chat.id
        nums = message.text
        user = user_dict[chat_id]
        user.nums = nums
        chat_id = message.chat.id
        msg = bot.send_message(chat_id, "Основные навыки", reply_markup=board)
        bot.register_next_step_handler(msg, send_z)
    except Exception as e:
        bot.reply_to(message, 'Непредвиденная ошибка')


def send_z(message):
    connection = sqlite3.connect('bd/database_fusion.db')
    cursor = connection.cursor()
    chat_id = message.chat.id
    first_name = message.chat.first_name
    last_name = message.chat.last_name
    user_name = message.chat.username
    z = message.text  # text user
    app_text = []
    app_name_first = []
    app_name_last = []
    app_username = []
    app_name_first.append(first_name)
    app_name_last.append(last_name)
    app_username.append(user_name)
    app_text.append(z)
    user = user_dict[chat_id]
    user_chats = message.from_user.id
    bot.send_message(setting.admin_id_ugraswim, f'Поступил новый отклик от {app_name_first[0]} {app_name_last[0]} !\n'
                     + f'username в тг = @{app_username[0]} \n'
                     + f'Возраст  -  {user.age} \n'
                     + f'Локация  -  {user.location} \n'
                     + f'Опыт работы  -  {user.experience} \n'
                     + f'Специализация: {user.languages} \n'
                     + f'Основные навыки: - {app_text[0]} \n'
                     + f'Профиль github/социальная сеть  -  {user.git_acc} \n'
                     + f'Формат работы  -  {user.format_work} \n'
                     + f'Контактные данные: {user.nums} \n'

                     + f'ID юзера: {user_chats}')
    bot.send_message(setting.admin_hr_id, f'Поступил новый отклик от {app_name_first[0]} {app_name_last[0]} !\n'
                     + f'username в тг = @{app_username[0]} \n'
                     + f'Возраст  -  {user.age} \n'
                     + f'Локация  -  {user.location} \n'
                     + f'Опыт работы  -  {user.experience} \n'
                     + f'Специализация: {user.languages} \n'
                     + f'Основные навыки: - {app_text[0]} \n'
                     + f'Профиль github/социальная сеть  -  {user.git_acc} \n'
                     + f'Формат работы  -  {user.format_work} \n'
                     + f'Контактные данные: {user.nums} \n'

                     + f'ID юзера: {user_chats}')
    cursor.execute('''CREATE TABLE IF NOT EXISTS orders(
            id INTEGER,
            user_first_name varchar(50),
            user_last_name varchar(50),
            username varchar(50),
            location text,
            special text,
            nums text,
            data_time varchar(50)
            );''')
    connection.commit()
    id_people = message.from_user.id
    cursor.execute(f"SELECT id FROM orders WHERE id = {id_people}")
    user = user_dict[chat_id]
    data = cursor.fetchone()
    if data is None:
        order = [message.from_user.id,
                 message.from_user.first_name,
                 message.from_user.last_name,
                 message.from_user.username,
                 user.location,
                 user.languages,
                 user.nums,
                 dt_string]
        cursor.execute("INSERT INTO orders VALUES(?,?,?,?,?,?,?,?);", order)
        connection.commit()
        connection.close()
        app_name_first.clear()
        app_name_last.clear()
        app_username.clear()
        app_text.clear()
        logging.info('Заявка успешно отправлена от - ' + message.chat.username)
        bot.send_message(chat_id, "Заявка отправлена, мы свяжемся с Вами в ближайшее время")


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "Отмена":
            logging.warning('Хотел оставить заявку, нажал отмена - ' + call.message.chat.username)
            msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        text='Отмена заполнения заявки...Выберите нужный раздел:')
            bot.clear_step_handler(msg)


try:
    bot.infinity_polling(timeout=90, long_polling_timeout=5)
except (ConnectionError, ReadTimeout) as e:
    sys.stdout.flush()
    logging.exception('Ошибка подключения. Переподключение')
    os.execv(sys.argv[0], sys.argv)
else:
    bot.infinity_polling(timeout=90, long_polling_timeout=5)
