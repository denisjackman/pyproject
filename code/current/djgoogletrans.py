'''     google trans example

        https://zetcode.com/python/googletrans/
'''
import os
import googletrans
from googletrans import Translator
RUN_NAME = os.path.basename(__file__)


def main():
    ''' main '''
    print(f'[-] {googletrans.LANGUAGES}')
    try:
        text1 = '''
        A Római Birodalom (latinul Imperium Romanum)
         az ókori Róma által létrehozott
        államalakulat volt a Földközi-tenger medencéjében
        '''

        text2 = '''
        Vysoké Tatry sú najvyššie pohorie na Slovensku
         a v Poľsku a sú zároveň jediným
        horstvom v týchto štátoch s alpským charakterom.
        '''

        translator = Translator()

        dt1 = translator.detect(text1)
        print(dt1)

        dt2 = translator.detect(text2)
        print(dt2)
    except Exception as ex:
        print(f'[-] Detect Exception: {ex}')

    try:
        translator = Translator()
        translated = translator.translate('Бороди́нское сраже́ние')
        print(f'{translated.src} -> {translated.dest}')
        print(translated.text)
    except Exception as ex:
        print(f'[-] Translate Exception: {ex}')


if __name__ == '__main__':
    print(f'[-] {RUN_NAME} Start')
    main()
    print(f'[-] {RUN_NAME} End')
