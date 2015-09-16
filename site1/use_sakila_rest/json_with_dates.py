__author__ = 'bsetzer'

import datetime
import re
import json

# based on http://stackoverflow.com/questions/11875770/how-to-overcome-datetime-datetime-not-json-serializable-in-python
# answer by fiatjaf
def dateDefault(obj):
    if type(obj) is datetime.date or type(obj) is datetime.datetime:
        #return obj.isoformat()
        return obj.strftime('%Y-%m-%dT%H:%M:%S')
    else:
        raise TypeError

# based on http://stackoverflow.com/questions/8793448/how-to-convert-to-a-python-datetime-object-with-json-loads
# answer by Nicola Iarocci
# this version does not ignore exceptions
def dateHook(dct):
    for k, v in dct.items():
        if isinstance(v,str):
            match = re.fullmatch("(\d\d\d\d-\d\d-\d\d)[T ](\d\d:\d\d:\d\d)(.\d*)?",v)
            if   match:
                tmp = match.group(1) + "T" + match.group(2)
                dct[k] = datetime.datetime.strptime(tmp,'%Y-%m-%dT%H:%M:%S')
    return dct

def dumps(obj, **kwargs):
    return json.dumps(obj, default=dateDefault, **kwargs)

def loads(jsn, **kwargs):
    return json.loads(jsn, object_hook=dateHook, **kwargs)

def dateHook_v1(dct):
    for k, v in dct.items():
        if isinstance(v,str):
            match = re.fullmatch("(\d\d\d\d-\d\d-\d\d)[T ](\d\d:\d\d:\d\d)(.\d*)?",v)
            if   match:
                tmp = match.group(1) + "T" + match.group(2)
                #print('date-time match: ', v)
                dct[k] = datetime.datetime.strptime(tmp,'%Y-%m-%dT%H:%M:%S')
                #print('converted to: ', dct[k])
    return dct