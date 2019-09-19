# RANDOM AYAT (VERSES) GENERATOR
# This program generates random ayat (verses) from the Quran.
# A single random ayah can be generated or a list of consecutive ayat based on the input parameter in the main() function

import json
import urllib.request
from random import randrange


# def write_json_object_to_file():
#     jsonObject = get_json_object_from_url("http://api.alquran.cloud/v1/ayah/1:1/editions/quran-uthmani,en.sahih")
#     with open('test-ayah.json', 'w') as json_file:
#         json.dump(jsonObject, json_file)
#     print("Test JSON ayah successfully created")


# def get_ayah_by_reference_from_local_json(surah, verse):
#     with open('quran-ar.json') as quran_ar_json_file:
#         quran_ar_json = json.load(quran_ar_json_file)
#
#     with open('quran-en-sahih.json') as quran_en_json_file:
#         quran_en_json = json.load(quran_en_json_file)
#
#     try:
#         print(quran_ar_json["data"]["surahs"][surah - 1]["ayahs"][verse - 1]["text"])
#         print(quran_en_json["data"]["surahs"][surah - 1]["ayahs"][verse - 1]["text"])
#     except IndexError as err:
#         print("IndexError encountered, probably wrong ayah reference provided")


def get_json_object_from_url(url):
    try:
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        return data
    except urllib.request.HTTPError as err:
        if err.code == 404:
            print("HTTP ERROR 404 - Probably an invalid ayah reference provided")
        else:
            raise


# def get_ayah_by_reference(surah, ayah):
#     url = "http://api.alquran.cloud/v1/ayah/" + str(surah) + ":" + str(ayah) + "/editions/quran-uthmani,en.sahih"
#     print_json_from_url(url)


# def print_json_from_url(url):
#     try:
#         response = urllib.request.urlopen(url)
#         data = json.loads(response.read())
#         print(json.dumps(data, indent=2, sort_keys=False))
#         # print(data["data"]["text"])
#     except urllib.request.HTTPError as err:
#         if err.code == 404:
#             print("HTTP ERROR 404 - Probably an invalid ayah reference provided")
#         else:
#             raise


# def get_first_ayah():
#     url = "http://api.alquran.cloud/v1/ayah/1:1/editions/quran-uthmani,en.sahih"
#     print_json_from_url(url)


# def list_english_language_translations():
#     url = "http://api.alquran.cloud/v1/edition/language/en"
#     print_json_from_url(url)


def import_quran_arabic_into_json():
    jsonObject = get_json_object_from_url("http://api.alquran.cloud/v1/quran/quran-uthmani")
    with open('quran-ar.json', 'w') as json_file:
        json.dump(jsonObject, json_file)
    print("quran-ar.json successfully created")


def import_quran_english_into_json():
    jsonObject = get_json_object_from_url("http://api.alquran.cloud/v1/quran/en.sahih")
    with open('quran-en-sahih.json', 'w') as json_file:
        json.dump(jsonObject, json_file)
    print("quran-en-sahih.json successfully created")


def get_random_ayah(number_of_ayat=3):
    if number_of_ayat <= 0:
        number_of_ayat = 3

    try:
        with open('quran-ar.json') as quran_ar_json_file:
            quran_ar_json = json.load(quran_ar_json_file)
    except FileNotFoundError:
        print("Local quran-ar.json file not found, downloading now...")
        import_quran_arabic_into_json()

    try:
        with open('quran-en-sahih.json') as quran_en_json_file:
            quran_en_json = json.load(quran_en_json_file)
    except FileNotFoundError:
        print("Local quran-en-sahih.json file not found, downloading now...")
        import_quran_english_into_json()

    surah = randrange(114)
    ayah = randrange(286)

    # print(surah, ayah)
    try:
        # ayah1_ar = quran_ar_json["data"]["surahs"][surah]["ayahs"][ayah]["text"]
        # ayah1_en = quran_en_json["data"]["surahs"][surah]["ayahs"][ayah]["text"]
        # ayah2_ar = quran_ar_json["data"]["surahs"][surah]["ayahs"][ayah + 1]["text"]
        # ayah2_en = quran_en_json["data"]["surahs"][surah]["ayahs"][ayah + 1]["text"]
        # ayah3_ar = quran_ar_json["data"]["surahs"][surah]["ayahs"][ayah + 2]["text"]
        # ayah3_en = quran_en_json["data"]["surahs"][surah]["ayahs"][ayah + 2]["text"]
        # print(ayah1_ar)
        # print(ayah1_en)
        # print(ayah2_ar)
        # print(ayah2_en)
        # print(ayah3_ar)
        # print(ayah3_en)
        ayah_list = []
        for i in range(number_of_ayat):
            ayah_list.append(quran_ar_json["data"]["surahs"][surah]["ayahs"][ayah+i]["text"])
            ayah_list.append(quran_en_json["data"]["surahs"][surah]["ayahs"][ayah+i]["text"])
        for ayat in ayah_list:
            print(ayat)
        # print(ayah_list)
        if number_of_ayat>1:
            print("[" + str(surah + 1) + ":" + str(ayah + 1) + "-" + str(ayah+number_of_ayat + 1) + "]")
        else:
            print("[" + str(surah + 1) + ":" + str(ayah + 1) + "]")
    except IndexError:
        # print("IndexError")
        get_random_ayah(number_of_ayat)


def main(x):
    # list_english_language_translations()
    # get_first_ayah()
    # get_ayah_by_reference(1, 1)
    # jsonObject = get_json_object_from_url("http://api.alquran.cloud/v1/ayah/1:1/editions/quran-uthmani,en.sahih")
    # print(json.dumps(jsonObject, indent=2, sort_keys=False))
    # write_json_object_to_file()
    # import_quran_arabic_into_json()
    # import_quran_english_into_json()
    # get_ayah_by_reference_from_local_json(2, 1)
    get_random_ayah(x)


if __name__ == "__main__":
    # Modify this parameter to generate desired number of ayat (verses) from the Quran
    number_of_ayat_to_generate = 5

    main(number_of_ayat_to_generate)

