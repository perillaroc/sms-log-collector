# coding=utf-8
import datetime


class ValueSaver(object):
    def __init__(self):
        pass

    def set_item_value(self, item, value):
        pass


class StringSaver(ValueSaver):
    def __init__(self):
        ValueSaver.__init__(self)

    def set_item_value(self, item, value):
        item['text'] = value
        item['value'] = value
        item['data'] = value


class NumberSaver(ValueSaver):
    def __init__(self):
        ValueSaver.__init__(self)

    def set_item_value(self, item, value):
        data = float(value)
        item['text'] = value
        item['value'] = value
        item['data'] = data


class FullDateSaver(ValueSaver):
    def __init__(self):
        ValueSaver.__init__(self)

    def set_item_value(self, item, value):
        data = datetime.datetime.strptime(value, "%c")

        item['text'] = data.strftime("%m/%d %H:%M")
        item['value'] = value
        item['data'] = data

job_state_list = [
    { "name": "Canceled",           "abbreviation":"CA"    },
    { "name": "Checkpointing",      "abbreviation":"CK"    },
    { "name": "Completed",          "abbreviation":"C"     },
    { "name": "Complete Pending",   "abbreviation":"CP"    },
    { "name": "Deferred",           "abbreviation":"D"     },
    { "name": "Idle",               "abbreviation":"I"     },
    { "name": "Not Queued",         "abbreviation":"NQ"    },
    { "name": "Not Run",            "abbreviation":"NR"    },
    { "name": "Pending",            "abbreviation":"P"     },
    { "name": "Preempted",          "abbreviation":"E"     },
    { "name": "Preempt Pending",    "abbreviation":"EP"    },
    { "name": "Rejected",           "abbreviation":"X"     },
    { "name": "Reject Pending",     "abbreviation":"XP"    },
    { "name": "Removed",            "abbreviation":"RM"    },
    { "name": "Remove Pending",     "abbreviation":"RP"    },
    { "name": "Resume Pending",     "abbreviation":"MP"    },
    { "name": "Running",            "abbreviation":"R"     },
    { "name": "Starting",           "abbreviation":"ST"    },
    { "name": "System Hold",        "abbreviation":"S"     },
    { "name": "Terminated",         "abbreviation":"TX"    },
    { "name": "User & System Hold", "abbreviation":"HS"    },
    { "name": "User Hold",          "abbreviation":"H"     },
    { "name": "Vacated",            "abbreviation":"V"     },
    { "name": "Vacate Pending",     "abbreviation":"VP"    }
]


class JobStateSaver(ValueSaver):
    def __init__(self):
        ValueSaver.__init__(self)

    def set_item_value(self, item, value):
        value_length = len(value)
        if value_length == 1 or value_length == 2:
            item['text'] = value
            item['value'] = value
            item['data'] = value
            return

        for a_job_state in job_state_list:
            if a_job_state['name'] == value:
                item['text'] = a_job_state['abbreviation']
                item['value'] = a_job_state['abbreviation']
                item['data'] = a_job_state['abbreviation']
                return

        item['text'] = value
        item['value'] = value
        item['data'] = value
        return