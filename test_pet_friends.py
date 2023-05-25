/test_pet_friends.py

File metadata and controls

Code

Blame

def test_post_add_new_pet_with_invalid_name(name='fghfhdhdshfjhajavajfjhajhfajhfhafbjhabfjkbajhbafhjasjahjbjhafsjhbfsjh', animal_type='собака', age='1', pet_photo='images/IMG_8521.jpeg'):

from api import PetFriends

from settings import valid_email, valid_password, invalid_email, invalid_password

import os

pf = PetFriends()

invalid_auth_key = "uaig1ef3uogfwu6hgfsl654df88ghlih"

def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):

    status, result = pf.get_api_key(email, password)

    assert status == 200

    assert 'key' in result

def test_get_all_pets_with_valid_key(filter=''):

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 200

    assert len(result['pets']) > 0

def test_post_add_new_pet_with_valid_data(name='Арчи', animal_type='собака', age='1', pet_photo='images/IMG_8521.jpeg'):

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.post_add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200

    assert result['name'] == name

# А что, если список питомцев пуст, и мы не можем добавить нового? Например, если не реализован такой функционал.

# И в этом случае нам приходится самим выбрасывать исключение как в тесте обновления информации о питомце:

#

# def test_successful_update_self_pet_info(self, name='Мурзик',

#                                          animal_type='Котэ', age=5):

#    _, auth_key = self.pf.get_api_key(valid_email, valid_password)

#    _, my_pets = self.pf.get_list_of_pets(auth_key, "my_pets")

#

#    if len(my_pets['pets']) > 0:

#        status, result = self.pf.update_pet_info(auth_key, my_pets['pets'][0]['id'],

#                                                 name, animal_type, age)

#        assert status == 200

#        assert result['name'] == name

#    else:

#        raise Exception("There is no my pets")

def test_successful_delete_self_pet():

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) == 0:

        pf.add_new_pet(auth_key, "Суперкот", "кот", "3", "images/cat1.jpg")

        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

        pet_id = my_pets['pets'][0]['id']

        status, _ = pf.delete_pet(auth_key, pet_id)

        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

        assert status == 200

        assert pet_id not in my_pets.values()

def test_successful_update_self_pet_info(name='Мурзик', animal_type='Котэ', age=5):

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) > 0:

        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        assert status == 200

        assert result['name'] == name

    else:

        raise Exception("There is no my pets")

# первая часть задания: тесты к дополненным 2 методам библиотеки # # # # # # # # # # #

def test_post_add_new_pet_without_photo(name='Арчи', animal_type='собака', age=12):

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.post_add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 200

    assert result['name'] == name

def test_post_add_photo_of_pet(pet_photo='images/IMG_8563.jpeg'):

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) > 0:

        status, result = pf.post_add_photo_of_pet(auth_key, my_pets['pets'][0]['id'], pet_photo)

        assert status == 200

        # assert result['pet_photo'] == pet_photo

    else:

        raise Exception("Питомцы отсутствуют")

# вторая часть задания (негативные тесты, 10 штук) # # # # # # # # # # #

# 1

def test_get_api_key_for_invalid_user(email=invalid_email, password=invalid_password):

    status, result = pf.get_api_key(email, password)

    assert status == 400 or 401 or 402 or 403 or 404 or 405

# 2

def test_get_all_pets_with_invalid_filter(filter='not_my_pets'):

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 400 or 401 or 402 or 403 or 404 or 405

# 3

def test_post_add_new_pet_with_invalid_name(name='fghfhdhdshfjhajavajfjhajhfajhfhafbjhabfjkbajhbafhjasjahjbjhafsjhbfsjh', animal_type='собака', age='1', pet_photo='images/IMG_8521.jpeg'):

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.post_add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400 or 401 or 402 or 403 or 404 or 405

# 4

def test_post_add_new_pet_with_none_name(name='', animal_type='собака', age='1', pet_photo='images/IMG_8521.jpeg'):

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.post_add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400 or 401 or 402 or 403 or 404 or 405

# 5
