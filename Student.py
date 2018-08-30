class Student:
    def __init__(self,name,email,contact,skills,ug=None,pg=None):

        self.email=email
        self.contact=contact
        self.name=name
        self.skills=[skills]
              
        self.edu={"ug":[ug],"pg":[pg]} 
    def __str__(self):
        return '{{email: "{email}", contact: "{contact}", name: "{name}", skills: "{skills}" , edu: "{edu}" }}'.format(email=self.email, contact=self.contact, name=self.name, skills=self.skills, edu=self.edu)

james=Student("James","j@j.com","+1 7789990007","Python","CS", "CS")

print(str(james))

import json
print(json.dumps(vars(james),sort_keys=True, indent=4))
