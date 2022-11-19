import re
import requests
import json
def healthProductParser():
    barcode = "5449000000996"
    # barcode = re.sub("[^0-9]", "", barcode)
    barcode='27'+barcode
    print(barcode)

    url = 'https://world.openfoodfacts.org/api/v2/search?code=%'+barcode

    resp = requests.get(url=url)
    data = resp.json()  # Check the JSON Response Content documentation below
    print(data)

    allergens = data["products"][0]["allergens"].split(",")

    for i in range(len(allergens)):
        allergens[i] = allergens[i].replace("en:", "")

    ingredients_analysis_tags = []
    for i in range(len(data["products"][0]["ingredients_analysis_tags"])):
        ingredients_analysis_tags.append(data["products"][0]["ingredients_analysis_tags"][i].replace("en:", ""))

    product_name = data["products"][0]["product_name"]
    nutrition_grades = data["products"][0]["nutrition_grades"]

    nutrient_levels_tags = []
    for elem in data["products"][0]["nutrient_levels_tags"]:
        elem = elem.replace("en:", "")
        elem = elem.replace("-", " ")
        nutrient_levels_tags.append(elem)

    nova_groups_tags = data["products"][0]["nova_groups_tags"]
    #carbon_footprint_percent_of_known_ingredients = data["products"][0]["carbon_footprint_percent_of_known_ingredients"]
    packaging = data["products"][0]["packaging"]
    
    print(ingredients_analysis_tags)
    print(nutrient_levels_tags)
    print(nutrition_grades)
    print(product_name)
    print(nova_groups_tags)
    #print(carbon_footprint_percent_of_known_ingredients)
    print(packaging)

    result = {}
    result['product_name'] = product_name
    result['nutrition_grades'] = nutrition_grades
    result['ingredients_analysis_tags'] = ingredients_analysis_tags
    return result;



def main():
    #1
    result = healthProductParser();


#4
if __name__ == '__main__':
    main()


