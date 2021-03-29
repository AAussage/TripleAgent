#!/usr/bin/env python3


roles_description={
    "service":{
        "appear_as":"service",
        "in_virus_list":False,
        "agency":"service",
        "win_condition":"service",
        "grudge":None,
        "love":None
    },
    "virus":{
        "appear_as":"virus",
        "in_virus_list":True,
        "agency":"virus",
        "win_condition":"virus",
        "grudge":None,
        "love":None
    }

}


class Player:
    def __init__(self,name,ID,role):
        self.ID = ID
        self.name = name
        self.role = role
        self.starting_role = role

        self.spec_dict = roles_description[role]

    def export_attributes(self,list_of_key_required):
        to_send = {}
        for key in list_of_key_required:
            to_send[key]=self.spec_dict[key]

        return to_send

    def update_attributes(self,dict_of_attributes_to_upgrade):

        for key in dict_of_attributes_to_upgrade:
            self.spec_dict[key]=dict_of_attributes_to_upgrade[key]