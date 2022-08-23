def aniumal_schema(animal):
    return {
        "roll_no":int(animal["roll_no"]),
        "Animal_name":str(animal["Animal_name"]),
        "age":int(animal["age"]),
        "gender":str(animal["gender"])
    }

def animal_serial(animals):
    return [aniumal_schema(animal) for animal in animals]


