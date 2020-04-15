

def recommend_clothes(wind_speed, temp, condition):
    wind_speed = int(wind_speed)
    temp = int(temp)
    if wind_speed >= 5:
        is_wind_strong = True
    else:
        is_wind_strong = False

    if temp < -5:
        temp = "cold"
    elif -5 <= temp < 15:
        temp = "warm"
    elif temp >= 15:
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
        return " In such a cold weather it is better to wear three layers of " \
               "clothing and the warmest "\
               "jacket. Be prepared for snow and wind. Or better order a taxi"
    elif temp == "cold" and condition == "rain_or_snow" and not is_wind_strong:
        return " In such a cold weather it is better to wear three layers of " \
               "clothing and the warmest "\
               "jacket."
    elif temp == "cold" and condition == "overcast":
        return "Warm up and get ready for a little snow. Choose warm "\
               "down jacket and do not forget the hat"
    elif temp == "cold" and condition == "clear":
        return "It's time to warm up! However, you can choose a stylish winter "\
               "coat option without fear of snow"
    elif temp == "warm" and condition == "rain_or_snow" and is_wind_strong:
        return "Choose a warm demi-season version of a coat with a hood and "\
               "get ready for severe weather and wind. Today is not the best" \
               "time to wear a skirt or walk without a hat."
    elif temp == "warm" and condition == "rain_or_snow" and not is_wind_strong:
        return "Choose a warm demi-season version of a coat with a hood and "\
               "get ready for bad weather. Choose insulated boots and don't" \
               "neglect the advice to wear a hat."
    elif temp == "warm" and condition == "overcast":
        return "Choose a warm demi-season option and be armed with an " \
               "umbrella and hood, and also think of waterproof shoes. Then" \
               "the walk is not scary!"
    elif temp == "warm" and condition == "clear" and is_wind_strong:
        return "Choose a warm version of demi-season clothing, and do not be" \
               " afraid precipitation, it is not expected today! But take a" \
               " jacket in case of wind"
    elif temp == "warm" and condition == "clear" and not is_wind_strong:
        return "It's time to walk! Choose an insulated version of " \
               "semi-season clothing, and do not be afraid of the wind or " \
               "bad weather, they are not expected today!"
    elif temp == "hot" and condition == "rain_or_snow":
        return "Today, an umbrella and closed shoes will be necessary! " \
               "Get ready for heavy rain."
    elif temp == "hot" and condition == "overcast":
        return "Grab an umbrella and a waterproof jacket from the rain, " \
               "still choose closed shoes. "\
                "A warm day is expected!"
    elif temp == "hot" and condition == "clear" and is_wind_strong:
        return "Choose a light outfit, but do not forget the raincoat!"
    elif temp == "hot" and condition == "clear" and not is_wind_strong:
        return "Choose your favorite outfit and grab sunglasses; " \
               "you can’t think of a better weather! " \
               "Time to wear shorts and T-shirts. But grab a light jacket too"
