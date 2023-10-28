from typing import Union
import functools

digital_data = {'context': {'geolocation': {'City': 'mumbai',
'Country': 'india', 'State': 'maharashtra', 'maxmindCountry':
'{"country_iso_code":"IN","country_name":"India","region":"MH","region_full":"Maharashtra","city_name":"Mumbai","postal_code":"400070","locale":{"localeCode":["en-IN","hi-IN","gu-IN","kn-IN","kok-IN","mr-IN","sa-IN","ta-IN","te-IN","pa-IN"]}}'},
'isInNativeApp': 'no'}, 'page': {'category': {'pageType':
'landingPage', 'primaryCategory': 'Chegg', 'subCategory1': 'Web',
'subCategory2': 'tb'}, 'pageInfo': {'experience': 'desktop',
'pageName': 'rent/buy books'}}, 'user': {'profile': {'authStatus':
'Logged Out', 'profileInfo': {'attributes': {'uvn':
'5a16faf86e09d180b65397b40c360b2e60c306a6d38a77.96671301'}, 'segment':
{'authStatus': 'Logged Out'}}}}}

def get_dict_value(dictionary: dict, dotted_key: str) -> Union[str, None]:
    """Function to get key value . Key can be a simple key or nested.
    Nested key is supplied in dot notation.
    Args:
        dictionary (dict): Description
        dotted_key (str): Description
    Returns:
        str: Dict key value
    """
    keys = dotted_key.split('.')
    try:
        key_value = functools.reduce(
            lambda d, key: (d.get(key) if d else None), keys, dictionary)
        return key_value
    except KeyError:
        return ''

print(get_dict_value(digital_data,'page.category.primaryCategory'))
print(get_dict_value(digital_data,'page.category.subCategory2'))
# logger.info(self.get_dict_value(digital_data,'page.category.primaryCategory'))
#             logger.info(self.get_dict_value(digital_data'page.category.subCategory2'))