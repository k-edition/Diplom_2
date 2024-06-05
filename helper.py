import data


class ModifyData:
    @staticmethod
    def modify_create_user_payload(key, value):
        payload = data.generate_payload_for_user().copy()
        payload[key] = value

        return payload

    @staticmethod
    def modify_payload_for_login_user(payload):
        new_payload = payload.copy()
        del new_payload["name"]
        return new_payload

    @staticmethod
    def modify_ingredients_for_order(ingredients):
        invalid_ingredients = []
        for ingredient in ingredients:
            invalid_ingredient = ingredient[1:]
            invalid_ingredients.append(invalid_ingredient)
        return invalid_ingredients
