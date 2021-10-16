import re

"""
Welcome to the Game !

"""

def welcome_msg():
    print(
        """
        Please answer to the questions

        """
    )

    welcome_msg()

def read_template(fileContent):
  '''
  A function that read file test and return a strip of the file content, it will show error if the content is not correct
  '''
  try:
      with open(fileContent) as file:
        return file.read().strip()
  except :
        raise FileNotFoundError(f"({fileContent}) not found !!")

def parse_template(text):
    
    """
    A fuction that takes texts inside brackets and return it withour brackets
    """
    word_brackets=list(re.findall(r'{(.*?)}',text))
    text=re.sub('{.*?}','{}',text)
    return text,word_brackets

def userInput (inp):
    user_list=[]
    for i in inp:
        question=input(f'Please Enter {i} :')
        user_list+=[question]
        return user_list

def merge(text,word):
     """
     A function to merge the text with the user answer

     """
     return text.format(*word)


if __name__=="__main__":
    gametest=read_template("./assets/madlibGame.txt") 
    result1=parse_template(gametest)[1]
    result2=parse_template(gametest)[0]
    print(result2)
    answer=userInput(result1)
