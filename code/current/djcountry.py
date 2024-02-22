''' country check '''
from countryinfo import CountryInfo


def main():
    ''' main '''
    country = input('Enter country name: ')
    country_information = CountryInfo(country)
    print(f'Country name         : {country_information.name()}')
    print(f'Country capital      : {country_information.capital()}')
    print(f'Country currency     : {country_information.currencies()}')
    print(f'Country languages    : {country_information.languages()}')
    print(f'Country borders      : {country_information.borders()}')
    print(f'Country other name   : {country_information.alt_spellings()}')
    print(f'Country calling code : {country_information.calling_codes()}')
    print(f'Country area         : {country_information.area()}')
    print(f'Country population   : {country_information.population()}')


if __name__ == '__main__':
    main()
