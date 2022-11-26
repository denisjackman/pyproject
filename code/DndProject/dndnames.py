''' dnd name generator '''
__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 1.00 $"
__date__ = "$Date: 2022/11/25 00:00:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"

from pathlib import Path
import json
from random import choice
from dnddice import dice

FILEPATH = Path(__file__).parent
# pylint: disable=too-many-locals

def angelic_name():
    ''' angelic names '''
    with open(f"{FILEPATH}/referencedata/AngelNames.json", "r", encoding='utf8') as file:
        data = json.load(file)
    prefix = choice(data['angel_prefix'])
    suffix = choice(data['angel_suffix'])
    result = f'{prefix}{suffix}'
    return result.capitalize()

def barbarian_name():
    ''' barbarian names '''
    with open(f"{FILEPATH}/referencedata/BarbarianNames.json", "r", encoding='utf8') as file:
        data = json.load(file)

    roll = dice(2)
    if roll == 1:
        part1 = choice(data["barbarian_names"]).capitalize()
        part2 = part1
        while part1 == part2:
            part2 = choice(data["barbarian_names"])
        result = f'{part1}{part2}'
    else:
        prefix = choice(data["barbarian_prefix"]).capitalize()
        suffix = choice(data["barbarian_suffix"])
        result = f"{prefix} {suffix}"
    return result

def build_demon_name():
    ''' build a name '''
    with open(f"{FILEPATH}/referencedata/DemonNames.json", "r", encoding='utf8') as file:
        data = json.load(file)
    syllable = choice(data["demon_syllable"])
    roll = dice(7)
    if roll <= 2:
        result = f"'{syllable}"
    elif roll <= 3:
        result = f"-{syllable}"
    else:
        result = syllable
    return result

def demon_name_one():
    ''' demon name generator '''
    with open(f"{FILEPATH}/referencedata/DemonNames.json", "r", encoding='utf8') as file:
        data = json.load(file)
    syllable = choice(data["demon_syllable"])
    roll = dice(7)
    result = ''
    if roll <= 4:
        result = build_demon_name() + build_demon_name()
    elif roll <= 6:
        result = build_demon_name() + build_demon_name() + build_demon_name()
    else:
        result = build_demon_name() + build_demon_name() + \
            build_demon_name() + build_demon_name()

    return f"{syllable.capitalize()}{result}"

def demon_name_two():
    ''' demon name generator'''
    with open(f"{FILEPATH}/referencedata/DemonNames.json", "r", encoding='utf8') as file:
        data = json.load(file)

    result = ''
    truename = ''
    usename = ''
    roll = dice(100)
    number = 0

    if roll <= 8:
        number = 1
    elif roll <= 18:
        number = 2
    elif roll <= 29:
        number = 3
    elif roll <= 42:
        number = 4
    elif roll <= 56:
        number = 5
    elif roll <= 71:
        number = 6
    elif roll <= 79:
        number = 7
    elif roll <= 86:
        number = 8
    elif roll <= 92:
        number = 9
    elif roll <= 96:
        number = 10
    elif roll <= 99:
        number = 11
    else:
        number = 12
    for _ in range(number):
        item = choice(data["demon_truename_elements"])
        truename = f'{truename}{item}'
    usename = f'{choice(data["demon_usename_elements"])}{choice(data["demon_usename_elements"])} {choice(data["demon_usename_elements"]).title()}{choice(data["demon_usename_elements"])}'
    result = f'{truename.capitalize()}({usename})'
    return result

def demon_name():
    ''' demon name generator '''
    if dice(2) == 1:
        return demon_name_one()
    return demon_name_two()

def dwarven_name(gender=None):
    ''' dwarven name generator '''
    firstname = ''
    lastname = ''

    with open(f"{FILEPATH}/referencedata/DwarvenNames.json", "r", encoding='utf8') as file:
        data = json.load(file)

    prefix = choice(data["dwarven_name_prefix"])
    suffixmale = choice(data["dwarven_name_suffixmale"])
    suffix = choice(data["dwarven_name_suffix"])
    clanprefix = choice(data["dwarven_clan_prefix"])
    clansuffix = choice(data["dwarven_clan_suffix"])

    if gender is None:
        if dice(2) == 1:
            female = False
            firstname = f'{prefix}{suffixmale}'
        else:
            female = True
            firstname = f'{prefix}{suffix}'
    elif gender.lower() == 'female':
        female = True
        firstname = f'{prefix}{suffixmale}'
    else:
        female = False
        firstname = f'{prefix}{suffixmale}'

    if dice(3) == 1:
        father = f'{prefix}{suffixmale}'
        if female:
            lastname = f"{father}ssdottir"
        else:
            lastname = f"{father}son"
    else:
        lastname = f'{clanprefix}{clansuffix}'

    result = f'{firstname.capitalize()} {lastname.capitalize()}'
    if female:
        result = f"{result} (f.)"
    return result

def elfname_generator():
    '''Generates an Elf Name'''
    with open(f"{FILEPATH}/referencedata/ElfNames.json", "r", encoding='utf8') as file:
        data = json.load(file)
    result = ''
    firstname = ""
    surname = f"{choice(data['elf_surname_prefix'])}{choice(data['elf_surname_suffix'])}"
    roll = dice()
    if roll <= 4:
        firstname = f"{choice(data['elf_prefix'])}{choice(data['elf_mid'])}{choice(data['elf_suffix'])}"
    elif roll <= 5:
        firstname = f"{choice(data['elf_prefix'])}{choice(data['elf_mid'])}{choice(data['elf_mid'])}{choice(data['elf_suffix'])}"
    else:
        firstname = f"{choice(data['elf_prefix'])}{choice(data['elf_suffix'])}"
    result = f"{firstname.capitalize()} {surname.capitalize()}"
    return result

def hyborian_name_generator():
    '''Generates a Hyborian Name'''
    result = ''
    with open(f"{FILEPATH}/referencedata/HyborianNames.json", "r", encoding='utf8') as file:
        data = json.load(file)
    prefix = choice(data["hyborian_prefix"])
    suffix = choice(data["hyborian_suffix"])
    result = f"{prefix}{suffix}"
    return result

def lizardman_name_generator():
    '''Generates a random lizardman name'''
    result = ''

    with open(f"{FILEPATH}/referencedata/LizardNames.json", "r", encoding='utf8') as file:
        data = json.load(file)

    if dice(3) == 3:
        apos = "'"
    else:
        apos = ""
    cc = choice(data["lizard_cc"])
    cv = choice(data["lizard_cv"])
    vv = choice(data["lizard_vv"])
    vc = choice(data["lizard_vc"])

    if dice(4) <= 3:
        roll = dice(8)
        if roll == 1:
            newcc = choice(data["lizard_cc"])
            result = f"{cc}{apos}{newcc}"
        elif roll == 2:
            result = f"{cv}{cc}"
        elif roll == 3:
            newcv = choice(data["lizard_cv"])
            result = f"{cv}{newcv}"
        elif roll == 4:
            result = f"{vc}{apos}{cc}"
        elif roll == 5:
            result = f"{vc}{apos}{cv}"
        elif roll == 6:
            newvc = choice(data["lizard_vc"])
            result = f"{vc}{apos}{newvc}"
        elif roll == 7:
            result = f"{vv}{cc}"
        else:
            result = f"{vv}{cv}"
        # twosyllable
    else:
        roll = dice(11)
        newcc = choice(data["lizard_cc"])
        newcv = choice(data["lizard_cv"])
        newvc = choice(data["lizard_vc"])
        if roll == 1:
            if dice(3) == 3:
                newapos = "'"
            else:
                newapos = ""
            supcc = choice(data["lizard_cc"])
            result = f"{cc}{apos}{newcc}{newapos}{supcc}"
        elif roll == 2:
            result = f"{cc}{apos}{vv}{newcc}"
        elif roll == 3:
            result = f"{cc}{vv}{cc}"
        elif roll == 4:
            result = f"{vc}{vv}{cv}"
        elif roll == 5:
            result = f"{cv}{vc}{vc}"
        elif roll == 6:
            supcv = choice(data["lizard_cv"])
            result = f"{cv}{newcv}{supcv}"
        elif roll == 7:
            supvc = choice(data["lizard_vc"])
            result = f"{vc}{newvc}{supvc}"
        elif roll == 8:
            result = f"{vv}{cc}{vc}"
        elif roll == 9:
            newvv = choice(data["lizard_vv"])
            result = f"{vv}{cc}{newvv}"
        elif roll == 10:
            result = f"{vv}{cv}{newcv}"
        else:
            result = f"{vc}{cc}{newcc}"
        # threesyllable
    return result.capitalize()

def celtic_name_generator(gender=None):
    '''Generates a random Celtic name'''
    with open(f"{FILEPATH}/referencedata/CelticNames.json", "r", encoding='utf8') as file:
        data = json.load(file)

    prefix_male = choice(data["celtic_prefix_male"])
    middle_male = choice(data["celtic_middle_male"])
    suffix_male = choice(data["celtic_suffix_male"])
    prefix_female = choice(data["celtic_prefix_female"])
    middle_female = choice(data["celtic_middle_female"])
    suffix_female = choice(data["celtic_suffix_female"])

    if gender is None:
        if dice(2) == 1:
            female = False
        else:
            female = True
    elif gender.lower() == 'female':
        female = True
    else:
        female = False

    if female:
        result = f"{prefix_female}{middle_female}{suffix_female} (.f)"
    else:
        result = f"{prefix_male}{middle_male}{suffix_male}"

    return result

def epyptian_name_generator():
    '''Generates a random Egyptian name'''
    result = ''
    with open(f"{FILEPATH}/referencedata/EgyptianNames.json", "r", encoding='utf8') as file:
        data = json.load(file)
    prefix = choice(data["egyptian_prefix"])
    middle = choice(data["egyptian_middle"])
    suffix = choice(data["egyptian_suffix"])
    roll = dice(7)
    if roll <= 4:
        result = f"{prefix}{suffix.capitalize()}"
    elif roll <= 6:
        newprefix = choice(data["egyptian_prefix"])
        newsuffix = choice(data["egyptian_suffix"])
        result = f"{prefix}{suffix.capitalize()}-{newprefix}{newsuffix.capitalize()}"
    else:
        roll2 = dice(3)
        temp = ''
        for _ in range(roll2):
            temp += choice(data["egyptian_middle"])
        result += f"{prefix.capitalize()}{temp}{suffix}"

    return result

def greek_name_generator():
    '''Generates a random greek name'''
    result = ''
    with open(f"{FILEPATH}/referencedata/GreekNames.json", "r", encoding='utf8') as file:
        data = json.load(file)
    prefix = choice(data["greek_prefix"])
    suffix = choice(data["greek_suffix"])
    begin = choice(data["greek_begin"])
    middle = choice(data["greek_middle"])
    end = choice(data["greek_end"])
    result = f"{prefix}{suffix}{begin}{middle}{end}"
    return result.capitalize()

def oldenglish_name_generator():
    '''Generates a random Old English name'''
    result = ''
    with open(f"{FILEPATH}/referencedata/OldEnglishNames.json", "r", encoding='utf8') as file:
        data = json.load(file)
    prefix = choice(data["oldenglish_prefix"])
    suffix = choice(data["oldenglish_suffix"])
    result = f"{prefix}{suffix}"
    return result.capitalize()

def sumerian_name_generator():
    '''Generates a random Sumerian name'''
    result = ''
    roll = dice(37)
    with open(f"{FILEPATH}/referencedata/SumerianNames.json", "r", encoding='utf8') as file:
        data = json.load(file)

    if roll == 1:
        result = f"{choice(data['sumerian_vcvc'])}{choice(data['sumerian_vcvc'])}"
    elif roll == 2:
        result = f"{choice(data['sumerian_vcvc'])}{choice(data['sumerian_mix'])}"
    elif roll == 3:
        result = f"{choice(data['sumerian_vcvc'])}{choice(data['sumerian_vcv'])}"
    elif roll == 4:
        result = f"{choice(data['sumerian_vcvc'])}{choice(data['sumerian_vcvc'])}"
    elif roll == 5:
        result = f"{choice(data['sumerian_ccvc'])}{choice(data['sumerian_vcvc'])}"
    elif roll == 6:
        result = f"{choice(data['sumerian_ccvc'])}{choice(data['sumerian_mix'])}"
    elif roll == 7:
        result = f"{choice(data['sumerian_ccvc'])}{choice(data['sumerian_vc'])}"
    elif roll == 8:
        result = f"{choice(data['sumerian_ccvc'])}{choice(data['sumerian_vccv'])}"
    elif roll == 9:
        result = f"{choice(data['sumerian_ccvc'])}{choice(data['sumerian_vcv'])}"
    elif roll == 10:
        result = f"{choice(data['sumerian_cv'])}{choice(data['sumerian_cv'])}"
    elif roll == 11:
        result = f"{choice(data['sumerian_cv'])}{choice(data['sumerian_ccvc'])}"
    elif roll == 12:
        result = f"{choice(data['sumerian_cvc'])}{choice(data['sumerian_vcvc'])}"
    elif roll == 13:
        result = f"{choice(data['sumerian_cvc'])}{choice(data['sumerian_mix'])}"
    elif roll == 14:
        result = f"{choice(data['sumerian_cvc'])}{choice(data['sumerian_ccvc'])}"
    elif roll == 15:
        result = f"{choice(data['sumerian_cvc'])}{choice(data['sumerian_ccvc'])}"
    elif roll == 16:
        result = f"{choice(data['sumerian_cvc'])}{choice(data['sumerian_vc'])}"
    elif roll == 17:
        result = f"{choice(data['sumerian_cvc'])}{choice(data['sumerian_vccv'])}"
    elif roll == 18:
        result = f"{choice(data['sumerian_cvc'])}{choice(data['sumerian_vcv'])}"
    elif roll == 19:
        result = f"{choice(data['sumerian_ccvc'])}{choice(data['sumerian_vcvc'])}"
    elif roll == 20:
        result = f"{choice(data['sumerian_ccvc'])}{choice(data['sumerian_vc'])}"
    elif roll == 21:
        result = f"{choice(data['sumerian_ccvc'])}{choice(data['sumerian_vcv'])}"
    elif roll == 22:
        result = f"{choice(data['sumerian_ccvc'])}{choice(data['sumerian_cv'])}"
    elif roll == 23:
        result = f"{choice(data['sumerian_ccvc'])}{choice(data['sumerian_cvcv'])}"
    elif roll == 24:
        result = f"{choice(data['sumerian_vc'])}{choice(data['sumerian_vcvc'])}"
    elif roll == 25:
        result = f"{choice(data['sumerian_vc'])}{choice(data['sumerian_vc'])}"
    elif roll == 26:
        result = f"{choice(data['sumerian_vc'])}{choice(data['sumerian_vccv'])}"
    elif roll == 27:
        result = f"{choice(data['sumerian_vc'])}{choice(data['sumerian_vcv'])}"
    elif roll == 28:
        result = f"{choice(data['sumerian_vccv'])}{choice(data['sumerian_ccvc'])}"
    elif roll == 29:
        result = f"{choice(data['sumerian_vccv'])}{choice(data['sumerian_cv'])}"
    elif roll == 30:
        result = f"{choice(data['sumerian_vccv'])}{choice(data['sumerian_ccvc'])}"
    elif roll == 31:
        result = f"{choice(data['sumerian_vccv'])}{choice(data['sumerian_cvc'])}"
    elif roll == 32:
        result = f"{choice(data['sumerian_vccv'])}{choice(data['sumerian_ccvc'])}"
    elif roll == 33:
        result = f"{choice(data['sumerian_vcv'])}{choice(data['sumerian_ccvc'])}"
    elif roll == 34:
        result = f"{choice(data['sumerian_vcv'])}{choice(data['sumerian_cv'])}"
    elif roll == 35:
        result = f"{choice(data['sumerian_vcv'])}{choice(data['sumerian_cvc'])}"
    elif roll == 36:
        result = f"{choice(data['sumerian_vcv'])}{choice(data['sumerian_ccvc'])}"
    else:
        result = f"{choice(data['sumerian_vcv'])}{choice(data['sumerian_cvcv'])}"

    return result.capitalize()

def orc_name_generator():
    '''Generates a random orc name'''
    result = ""
    roll = dice(4)

    with open(f"{FILEPATH}/referencedata/OrcNames.json", "r", encoding='utf8') as file:
        data = json.load(file)
    if dice(4) <= 3:
        if roll == 1:
            result = f"{choice(data['orc_seg'])}{choice(data['orc_seg'])}"
        elif roll == 2:
            result = f"{choice(data['orc_pref'])}{choice(data['orc_seg'])}"
        elif roll == 3:
            result = f"{choice(data['orc_seg'])}{choice(data['orc_suff'])}"
        else:
            result = f"{choice(data['orc_pref'])}{choice(data['orc_suff'])}"
    else:
        if roll == 1:
            result = f"{choice(data['orc_seg'])}{choice(data['orc_seg'])}{choice(data['orc_seg'])}"
        elif roll == 2:
            result = f"{choice(data['orc_pref'])}{choice(data['orc_seg'])}{choice(data['orc_seg'])}"
        elif roll == 3:
            result = f"{choice(data['orc_seg'])}{choice(data['orc_seg'])}{choice(data['orc_suff'])}"
        else:
            result = f"{choice(data['orc_pref'])}{choice(data['orc_seg'])}{choice(data['orc_suff'])}"
    result = result.capitalize()
    if dice(2) == 1:
        result = f"{result} {choice(data['orc_lastpref']).capitalize()}{choice(data['orc_lastsuff'])}"

    return result

def main():
    ''' main function '''
    print(f"Angelic Name            : {angelic_name()}")
    print(f"Barbarian Name          : {barbarian_name()}")
    print(f"Dwarven Name            : {dwarven_name()}")
    print(f"Dwarven Name            : {dwarven_name(gender='Male')}")
    print(f"Dwarven Name            : {dwarven_name(gender='female')}")
    print(f"Demon Name              : {demon_name()}")
    print(f'Elf Name                : {elfname_generator()}')
    print(f'Hyborian Name           : {hyborian_name_generator()}')
    print(f'Lizardman Name          : {lizardman_name_generator()}')
    print(f'Celtic Name             : {celtic_name_generator()}')
    print(f"Celtic Name             : {celtic_name_generator(gender='male')}")
    print(f"Celtic Name             : {celtic_name_generator(gender='female')}")
    print(f"Egyptian Name           : {epyptian_name_generator()}")
    print(f"Greek Name              : {greek_name_generator()}")
    print(f"Old English Name        : {oldenglish_name_generator()}")
    print(f"Sumerian Name           : {sumerian_name_generator()}")
    print(f"Orc Name                : {orc_name_generator()}")

if __name__ == '__main__':
    main()
