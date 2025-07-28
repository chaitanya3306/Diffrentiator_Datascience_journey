# this file cleans :
import re
def clean(data):
    cleaned_data=[info.strip().title() for info in data if info.strip() ]
    filtered_names=[name for name in cleaned_data if re.match(r'^[A-Za-z]',name)]
    
    return filtered_names
    