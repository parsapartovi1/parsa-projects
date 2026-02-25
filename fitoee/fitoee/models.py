from django.db import models

# Create your models here.




class  Input(models.Model):
    user_input = models.TextField(
        blank=True,
        null=True,
    )


    def maker(self,user_input:str):
        letter_dict = {
            "ض": "q",
            "ص": "w",
            "ث": "e",
            "ق": "r",
            "ف": "t",
            "غ": "y",
            "ع": "u",
            "ه": "i",
            "خ": "o",
            "ح": "p",

            "ش": "a",
            "س": "s",
            "ی": "d",
            "ب": "f",
            "ل": "g",
            "ا": "h",
            "ت": "j",
            "ن": "k",
            "م": "l",

            "ظ": "z",
            "ط": "x",
            "ز": "c",
            "ر": "v",
            "ذ": "b",
            "د": "n",
            "پ": "m",
        }

        while True:
            temp = ""
            for letter in user_input:
                if letter in letter_dict:
                    temp += letter_dict[letter]
                else:
                    temp += letter
            return temp