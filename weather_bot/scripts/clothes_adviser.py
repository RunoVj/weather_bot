

def recommend_clothes(wind_speed, temp, condition):
    wind_speed = int(wind_speed)
    temp = int(temp)
    if wind_speed >= 5:
        is_wind_strong = True
    else:
        is_wind_strong = False

    if temp < -10:
        temp = "cold"
    elif -10 <= temp < 10:
        temp = "warm"
    elif temp >= 10:
        temp = "hot"

    if condition in ("overcast-and-rain", "overcast-thunderstorms-with-rain",
                     "cloudy-and-rain", "partly-cloudy-and-rain",
                     "overcast-and-wet-snow", "partly-cloudy-and-snow",
                     "overcast-and-snow", "cloudy-and-snow"):
        condition = "rain_or_snow"
    elif condition in ("overcast partly-cloudy-and-light-rain",
                       "cloudy-and-light-rain", "overcast-and-light-rain",
                       "partly-cloudy-and-light-snow", "cloudy-and-light-snow",
                       "overcast-and-light-snow"):
        condition = "overcast"
    elif condition in ("clear", "partly-cloudy", "cloudy"):
        condition = "clear"

    if temp == "cold" and condition == "rain_or_snow" and is_wind_strong:
        return "В такой холод лучше надеть три слоя одежды и самую теплую "\
               "куртку. Будь готов к снегу и ветру, а лучше закажи такси и не "\
               "мерзни"
    elif temp == "cold" and condition == "rain_or_snow" and not is_wind_strong:
        return "В такой холод лучше надеть три слоя одежды и самую теплую " \
               "куртку."
    elif temp == "cold" and condition == "overcast":
        return "Утеплись и приготовься к небольшому снегу. Выбирай теплый" \
               " пуховик и не забудь шапку"
    elif temp == "cold" and condition == "clear":
        return "Пора утепляться! Однако можешь выбирать стильный зимний " \
               "вариант пальто, не боясь снега"

    elif temp == "warm" and condition == "rain_or_snow" and is_wind_strong:
        return "Выбери теплый демисезонный вариант пальто с капюшоном и " \
               "приготовься к сильной непогоде и ветру. Сегодня не лучшее " \
               "время носить юбку или ходить без шапки."
    elif temp == "warm" and condition == "rain_or_snow" and is_wind_strong:
        return "Выбери теплый демисезонный вариант пальто с капюшоном и " \
               "приготовься к непогоде. Выбирай утепленные сапоги и не " \
               "пренебрегай советом носить шапку."
    elif temp == "warm" and condition == "overcast":
        return "Выбери теплый демисезонный вариант и будь вооружен зонтом и " \
               "капюшоном, а также подумай о непромокаемой обуви. Тогда " \
               "прогулка не страшна!"
    elif temp == "warm" and condition == "clear" and is_wind_strong:
        return "Выбери утепленный вариант демисезонной одежды, и не бойся " \
               "осадков, их сегодня не ожидается! Но возьми куртку на случай " \
               "ветра"
    elif temp == "warm" and condition == "clear" and not is_wind_strong:
        return "Пора гулять! Выбери утепленный вариант демисезонной одежды, " \
               "и не бойся ветра или непогоды, их сегодня не ожидается!"

    elif temp == "hot" and condition == "rain_or_snow":
        return "Приготовься к сильному дождю, зонт и закрытая обувь будут очень кстати! Советуем "
    elif temp == "hot" and condition == "overcast":
        return "Захвати зонт и непромокаемую куртку от дождя, еще выбери закрытую обувь. Ожидается теплый день!"
    elif temp == "hot" and condition == "clear" and is_wind_strong == 1:
        return "Выбирай легкий наряд, но не забудь плащ от ветра!"
    elif temp == "hot" and condition == "clear" and is_wind_strong == 0:
        return "Выбирай свой любимый наряд и захвати солнечные очки, лучше " \
               "погоды не придумать! Время носить юбки, блузы и легкую " \
               "куртку или пиджак"