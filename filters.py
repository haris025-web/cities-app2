
def filter_population(df, min_value, max_value):
    return df[
        (df["population"] >= min_value) &
        (df["population"] <= max_value)
    ]

def filter_country(df, countries):
    return df[df["country_code"].isin(countries)]
