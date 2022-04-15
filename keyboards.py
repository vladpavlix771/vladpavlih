import telebot


#Главное Меню
keyboardMain = telebot.types.ReplyKeyboardMarkup(True)
keyboardMain.row('Заказать', 'Профиль')
keyboardMain.row('История', 'Правила')
keyboardMain.row('Support', 'Работа')
#keyboardMain.row('Отзывы')

#Меню профиля
profile = telebot.types.ReplyKeyboardMarkup(True)
profile.row('Пополнить', 'Работа')
profile.row('Хочу скидку', 'Диспуты')
profile.row('Назад')

#Оплата (Оплатил)
oplata_oplatil = telebot.types.ReplyKeyboardMarkup(True)
oplata_oplatil.row('Оплатил','Отменить')

#Оплата Биткоин
oplata_bitcoin = telebot.types.ReplyKeyboardMarkup(True)
oplata_bitcoin.row = ('Проверить оплату')
oplata_bitcoin.row = ('Отменить')

#Оплата Карта
oplata_karta = telebot.types.ReplyKeyboardMarkup(True)
oplata_karta.row = ('Проверить перевод')
oplata_karta.row = ('Отменить')

#Пополнение
popolnenie =  telebot.types.ReplyKeyboardMarkup(True)
popolnenie.row('Пополнить счет')
popolnenie.row('Отменить')

oplata = telebot.types.ReplyKeyboardMarkup(True)
oplata.row('QIWI', 'BTC')
oplata.row('Банк.Картой')
oplata.row('Отменить')


#Админ меню
admin = telebot.types.ReplyKeyboardMarkup(True)
admin.row('Изменить Карту','Изменить Qiwi')
admin.row('Изменить BTC')
admin.row('Количество нариков')
admin.row('Отменить')

#Города 1
city = telebot.types.ReplyKeyboardMarkup(True)
city.row('Москва', 'С.Петербург')
city.row('Казань', 'Екатеринбург')
city.row('Сочи', 'Краснодар')
city.row('Севастополь', 'Ессентуки')
city.row('Отменить', '2')

#Города 2
cityto = telebot.types.ReplyKeyboardMarkup(True)
cityto.row('Симферополь', 'Александровское')
cityto.row('Железноводск', 'Иноземцево')
cityto.row('Кисловодск', 'Лермонтов')
cityto.row('Невинномысск', 'Пятигорск')
cityto.row('1', 'Отменить', '3')

#Города 3
cityfree = telebot.types.ReplyKeyboardMarkup(True)
cityfree.row('Светлоград', 'Ставрополь')
cityfree.row('Майский', 'Нальчик')
cityfree.row('Прохладный', 'Мин Воды')
cityfree.row('Уссурийск', 'Курган')
cityfree.row('2', 'Отменить', '4')

#Города 4
cityfo = telebot.types.ReplyKeyboardMarkup(True)
cityfo.row('Шадринск', 'Каменск-Уральский')
cityfo.row('Нижний Тагил', 'Серов')
cityfo.row('Тюмень', 'Ужур')
cityfo.row('Снежинск', 'Челябинск')
cityfo.row('3', 'Отменить', '5')

#Города 5
cityfive = telebot.types.ReplyKeyboardMarkup(True)
cityfive.row('Бахчисарай', 'Ачинск')
cityfive.row('Назарово', 'Магнитогорск')
cityfive.row('Шарыпово', 'Уфа')
cityfive.row('4', 'Отменить', )


#Районы Москва
moskow_rayons = telebot.types.ReplyKeyboardMarkup(True)
moskow_rayons.row('Измайлово','Внуково')
moskow_rayons.row('Сокольники','Кунцево')
moskow_rayons.row('Крюково', 'Лефортово')
moskow_rayons.row('Выхино', 'Медведково')
moskow_rayons.row('Щукино', 'Якиманка')
moskow_rayons.row('Отменить')

#Районы С.Петербург
sankt_rayons = telebot.types.ReplyKeyboardMarkup(True)
sankt_rayons.row('Центральный', 'Невский')
sankt_rayons.row('Кировский', 'Московский')
sankt_rayons.row('Петроградский', 'Василеостровской')
sankt_rayons.row('Отменить')

#Районы Казань
kazan_rayons = telebot.types.ReplyKeyboardMarkup(True)
kazan_rayons.row('Советский', 'Кировский')
kazan_rayons.row('Приволжский', 'Вахитовский')
kazan_rayons.row('Ново-Савиновский', 'Московский')
kazan_rayons.row('Отменить')

#Районы Екатеринбург
ekb_rayons = telebot.types.ReplyKeyboardMarkup(True)
ekb_rayons.row('Верх-Исетский', 'Кировский')
ekb_rayons.row('Железнодорожный', 'Ленинский')
ekb_rayons.row('Октябрьский')
ekb_rayons.row('Отменить')

#Районы Сочи
sochi_rayons = telebot.types.ReplyKeyboardMarkup(True)
sochi_rayons.row('Центральный', 'Адлерский')
sochi_rayons.row('Хостинский', 'Лазаревский')
sochi_rayons.row('Отменить')

#Районы Краснодар
krasnodar_rayons = telebot.types.ReplyKeyboardMarkup(True)
krasnodar_rayons.row('Западный', 'Прикубанский')
krasnodar_rayons.row('Карасунский', 'Центральный')
krasnodar_rayons.row('Юбилейный', 'Фестивальный')
krasnodar_rayons.row('Черемушки', 'Пашковка')
krasnodar_rayons.row('Отменить')

#Районы Севастополь
sevaa_rayons = telebot.types.ReplyKeyboardMarkup(True)
sevaa_rayons.row('Ленинский', 'Нахимовский')
sevaa_rayons.row('Гагаринский', 'Балаклавский')
sevaa_rayons.row('Терновка', 'Верхнесадовое')
sevaa_rayons.row('Отменить')

#Районы Симферополь
simfer_rayons = telebot.types.ReplyKeyboardMarkup(True)
simfer_rayons.row('Железнодорожный', 'Киевский')
simfer_rayons.row('ГРЭС', 'Центральный')
simfer_rayons.row('Отменить')

#Районы Александровское
aleksandr_rayons = telebot.types.ReplyKeyboardMarkup(True)
aleksandr_rayons.row('Александровский район')
aleksandr_rayons.row('Отменить')

#Районы Ессентуки
esentyk_rayons = telebot.types.ReplyKeyboardMarkup(True)
esentyk_rayons.row('Ветеран', 'Белый Уголь')
esentyk_rayons.row('Курортная зона', 'Заполотно')
esentyk_rayons.row('Отменить')

#Районы Железноводск
geleznovodsk_rayons = telebot.types.ReplyKeyboardMarkup(True)
geleznovodsk_rayons.row('Железноводск')
geleznovodsk_rayons.row('Отменить')

#Районы Иноземцево
inozemcevo_rayons = telebot.types.ReplyKeyboardMarkup(True)
inozemcevo_rayons.row('Иноземцево')
inozemcevo_rayons.row('Отменить')

#Районы Кисловодск
kislovodsk_rayons = telebot.types.ReplyKeyboardMarkup(True)
kislovodsk_rayons.row('район Въезда', 'район рынка')
kislovodsk_rayons.row('Отменить')

#Районы Лермонтов
lermontov_rayons = telebot.types.ReplyKeyboardMarkup(True)
lermontov_rayons.row('Лермонтов')
lermontov_rayons.row('Отменить')

#Районы невинномысск
nevinomisk_rayons = telebot.types.ReplyKeyboardMarkup(True)
nevinomisk_rayons.row('Головное', 'Комета')
nevinomisk_rayons.row('Красная Деревня', 'Молодежка')
nevinomisk_rayons.row('Рождественское')
nevinomisk_rayons.row('Отменить')

#Районы Пятигорск
pitigorsk_rayons = telebot.types.ReplyKeyboardMarkup(True)
pitigorsk_rayons.row('Белая Ромашка', 'Бештау')
pitigorsk_rayons.row('Энергетик', 'Горапост')
pitigorsk_rayons.row('Скачки')
krasnodar_rayons.row('Отменить')

#Районы Светлоград
Svetlograd_rayons = telebot.types.ReplyKeyboardMarkup(True)
Svetlograd_rayons.row('Светлоград')
Svetlograd_rayons.row('Отменить')

#Районы Ставрополь
Stavropol_rayons = telebot.types.ReplyKeyboardMarkup(True)
Stavropol_rayons.row('Ленинский', 'Октябрьский')
Stavropol_rayons.row('Промышленный')
Stavropol_rayons.row('Отменить')

#Районы Майский
May_rayons = telebot.types.ReplyKeyboardMarkup(True)
May_rayons.row('Майский')
May_rayons.row('Отменить')

#Районы Нальчик
Nalchik_rayons = telebot.types.ReplyKeyboardMarkup(True)
Nalchik_rayons.row('Завокзальный', 'Горный')
Nalchik_rayons.row('Дубки', 'Затишье')
Nalchik_rayons.row('Стрелка', 'Центр')
Nalchik_rayons.row('Отменить')

#Районы Прохладный
Cool_rayons = telebot.types.ReplyKeyboardMarkup(True)
Cool_rayons.row('Больничный', 'Дружба')
Cool_rayons.row('Шанхай', 'Ремзавод')
Cool_rayons.row('Отменить')

#Районы Мин Воды
Water_rayons = telebot.types.ReplyKeyboardMarkup(True)
Water_rayons.row('1-й микрорайон', '2-й микрорайон')
Water_rayons.row('микрорайон Центральный', 'поселок 4-й километр')
Water_rayons.row('Отменить')

#Районы Уссурийск
Ussuriysk_rayons = telebot.types.ReplyKeyboardMarkup(True)
Ussuriysk_rayons.row('Центральный', 'Семи Ветров')
Ussuriysk_rayons.row('Железнодорожная слободка', 'Междуречье')
Ussuriysk_rayons.row('Восход', 'Доброполье')
Ussuriysk_rayons.row('Отменить')

#Районы Курган
Kurgan_rayons = telebot.types.ReplyKeyboardMarkup(True)
Kurgan_rayons.row('Заозёрный', 'Рябково')
Kurgan_rayons.row('Центральный', 'Северный')
Kurgan_rayons.row('Энергетики', 'Западный')
Kurgan_rayons.row('Восточный', '3-й микрорайон')
Kurgan_rayons.row('2-й микрорайон', 'микрорайон КСМ')
Kurgan_rayons.row('Отменить')

#Районы Шадринск
Shadrinsk_rayons = telebot.types.ReplyKeyboardMarkup(True)
Shadrinsk_rayons.row('Треугольник депо', 'Центральный')
Shadrinsk_rayons.row('Отменить')

#Районы Каменск-Уральский
Kamensk_rayons = telebot.types.ReplyKeyboardMarkup(True)
Kamensk_rayons.row('Красногорский', 'Синарский')
Kamensk_rayons.row('Отменить')

#Районы Нижний Тагил
Tagil_rayons = telebot.types.ReplyKeyboardMarkup(True)
Tagil_rayons.row('Ленинский', 'Тагилстроевский')
Tagil_rayons.row('Дзержинский', 'Пригородный')
Tagil_rayons.row('Отменить')

#Районы Серов       
Serov_rayons = telebot.types.ReplyKeyboardMarkup(True)
Serov_rayons.row('Вятчино', 'ГРЭС')
Serov_rayons.row('Завокзальный', 'Металлургов')
Serov_rayons.row('Новая Кола', 'Новое Медянкино')
Serov_rayons.row('Отменить')

#Районы Тюмень
Tyumen_rayons = telebot.types.ReplyKeyboardMarkup(True)
Tyumen_rayons.row('Центральный', 'Ленинский')
Tyumen_rayons.row('Калининский', 'Восточный')
Tyumen_rayons.row('Отменить')

#Районы Ужур
Uzhur_rayons = telebot.types.ReplyKeyboardMarkup(True)
Uzhur_rayons.row('Ужур')
Uzhur_rayons.row('Отменить')

#Районы Снежинск
Snezhinsk_rayons = telebot.types.ReplyKeyboardMarkup(True)
Snezhinsk_rayons.row('Снежинск')
Snezhinsk_rayons.row('Отменить')

#Районы Челябинск
Chelyabinsk_rayons = telebot.types.ReplyKeyboardMarkup(True)
Chelyabinsk_rayons.row('Калининский', 'Металлургический')
Chelyabinsk_rayons.row('Курчатовский', 'Советский')
Chelyabinsk_rayons.row('Ленинский', 'Тракторозаводский')
Chelyabinsk_rayons.row('Центральный')
Chelyabinsk_rayons.row('Отменить')

#Районы Бахчисарай
Bakhchisarai_rayons = telebot.types.ReplyKeyboardMarkup(True)
Bakhchisarai_rayons.row('Бахчисарай')
Bakhchisarai_rayons.row('Отменить')

#Районы Ачинск
Achinsk_rayons = telebot.types.ReplyKeyboardMarkup(True)
Achinsk_rayons.row('Ачинск', 'Малиновка')
Achinsk_rayons.row('Отменить')

#Районы Назарово
Nazarovo_rayons = telebot.types.ReplyKeyboardMarkup(True)
Nazarovo_rayons.row('Назарово')
Nazarovo_rayons.row('Отменить')

#Районы Магнитогорск
Magnitogorsk_rayons = telebot.types.ReplyKeyboardMarkup(True)
Magnitogorsk_rayons.row('Правобережный район', 'Орджоникидзевский район')
Magnitogorsk_rayons.row('Ленинский район')
Magnitogorsk_rayons.row('Отменить')

#Районы Шарыпово
Sharypovo_rayons = telebot.types.ReplyKeyboardMarkup(True)
Sharypovo_rayons.row('Шарыпово', 'Дубинино')
Sharypovo_rayons.row('Отменить')






#Варианты товара
tovar1 = telebot.types.ReplyKeyboardMarkup(True)
tovar1.row('Alpha PVP', 'Гашиш Euro')
tovar1.row('Амфетамин', 'Шишки (АК47)')
tovar1.row('Мефедрон', 'Героин HQ')
tovar1.row('Спайс', 'Шишко-План')
tovar1.row('Отменить')

tovar2 = telebot.types.ReplyKeyboardMarkup(True)
tovar2.row('Alpha PVP', 'Гашиш Euro')
tovar2.row('Амфетамин', 'Шишки (АК47)')
tovar2.row('Отменить')

tovar3 = telebot.types.ReplyKeyboardMarkup(True)
tovar3.row('Alpha PVP', 'Гашиш Euro')
tovar3.row('Амфетамин', 'Мефедрон')
tovar3.row('Спайс', 'Героин HQ')
tovar3.row('Отменить')

tovar4 = telebot.types.ReplyKeyboardMarkup(True)
tovar4.row('Alpha PVP', 'Гашиш Euro')
tovar4.row('Амфетамин', 'Мефедрон')
tovar4.row('Спайс', 'Героин HQ')
tovar4.row('Отменить')

tovar5 = telebot.types.ReplyKeyboardMarkup(True)
tovar5.row('Alpha PVP', 'Гашиш Euro')
tovar5.row('Амфетамин', 'Спайс')
tovar5.row('Отменить')

tovar6 = telebot.types.ReplyKeyboardMarkup(True)
tovar6.row('Alpha PVP', 'Гашиш Euro')
tovar6.row('Отменить')

tovar7 = telebot.types.ReplyKeyboardMarkup(True)
tovar7.row('Alpha PVP', 'Амфетамин')
tovar7.row('Отменить')

#Варианты фасовки
alpha_fas = telebot.types.ReplyKeyboardMarkup(True)
alpha_fas.row('0.3г (900 руб)', '0.5г (1300 руб)')
alpha_fas.row('1г (2200 руб)', '3г (5500 руб)')
alpha_fas.row('Отменить')

gash_fas = telebot.types.ReplyKeyboardMarkup(True)
gash_fas.row('1г (1100 руб)', '2г (2000 руб)')
gash_fas.row('5г (4000 руб)', '10г (6000 руб)')
gash_fas.row('Отменить')

amph_fas =  telebot.types.ReplyKeyboardMarkup(True)
amph_fas.row('1г (950 руб)', '2г (1800 руб)')
amph_fas.row('5г (4100 руб)', '10г (6500 руб)')
amph_fas.row('Отменить')

meph_fas =  telebot.types.ReplyKeyboardMarkup(True)
meph_fas.row('1г (1900 руб)', '2г (3700 руб)')
meph_fas.row('5г (8000 руб)')
meph_fas.row('Отменить')

shish_fas = telebot.types.ReplyKeyboardMarkup(True)
shish_fas.row('1г (1200 руб)', '2г (2200 руб)')
shish_fas.row('5г (4200 руб)')
shish_fas.row('Отменить')

gero_fas = telebot.types.ReplyKeyboardMarkup(True)
gero_fas.row('0.5 (1700 руб)')
gero_fas.row('Отменить')

spice_fas = telebot.types.ReplyKeyboardMarkup(True)
spice_fas.row('1г (500 руб)', '3г (1200 руб)')
spice_fas.row('Отменить')

plan_fas = telebot.types.ReplyKeyboardMarkup(True)
plan_fas.row('1г (550 руб)', '3г (1500 руб)')
plan_fas.row('Отменить')

