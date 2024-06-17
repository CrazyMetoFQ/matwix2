from flask import Flask, render_template, request
import random
import itertools




font_familys =  ["serif","sans-serif","cursive","fantasy","monospace","Perpetua","Monaco","Didot","Brush Script","Copperplate","Comic Sans","Arial"]
font_styles  =  ["normal","italic"]
font_sizes = range(35,54,1)
font_weights =  range(100,1001, 100)
align_items = ["flex-start", 'center', "flex-end"]
justify_items = ["flex-start", 'center', "flex-end"]


all_things = (font_familys,font_styles, font_sizes,font_weights,align_items, justify_items)

totn = 15
all_l = [[random.choice(i) for i in all_things] for _ in range(totn)]

# def rnd_l():
#   for _ in range(totn):
#     yield [random.choice(i) for i in all_stuff]

# all_l = rnd_l() 


class items_stuff:
    
  alphabets_U = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  alphabets_L = alphabets_U.lower()

  nums = "1234567890"
  symbs = "+-*/()"

  # all_stuff = alphabets_L+alphabets_U+nums
  all_stuff = nums+symbs




  def __init__(self) -> None:
    self.iposat = -1
    self.sposat = -1
    self.tposat = -1
    self.cylce_num = 0
    self.is_over = False



  def getitem(self):
    
    if self.is_over:
      print("over")
      return False
    else:
      pass

    self.tposat += 1
    print("tposat",self.tposat)
    
    if self.tposat%totn == 0:
      print("ipos check",1)  

      if self.iposat < len(items_stuff.all_stuff)-1:
        self.iposat += 1
        print("ipos icrement",2)

      else:
        print("ipos greater",3)
        self.is_over = True
        return False
    
    if self.sposat < totn-1 :
        print("spos increment",4)
        self.sposat += 1
    else:
        print("spos reset",5)
        self.sposat = 0
    
    print(self.iposat,self.sposat)
    return (items_stuff.all_stuff[self.iposat],self.sposat,all_l[self.sposat])




itg = items_stuff()







app = Flask(__name__)

sym_text = "Click_me"
sl = all_l[0]
cstate = True
imno = "start"
svnm = "clickme"

@app.route("/", methods=["GET", "POST"])
def index():
  
  global sym_text
  global sl
  global cstate
  global imno
  global svnm
  
  if request.method == "POST":
    
    item = itg.getitem()
    print(item)

    if item == False:
      cstate = False
    else:
      sym_text,imno,sl = item
      
      svnm = sym_text.replace("*", "[multiply]").replace("/", "[divideforward]")
      # if sym_text.isnumeric():
      #   svnm += "-n"
      # if sym_text.isupper():
      #   svnm += "-u"
      # if sym_text.islower():
      #   svnm += "-l"
  
  if cstate == True:
    return render_template("index.html",
                          sym_text=sym_text,
                          save_name=f"img_{svnm}_{imno}.png",
                          font_family =  sl[0] ,
                          font_style  =  sl[1],
                          font_size   =  f"{sl[2]}px" ,
                          font_weight =  sl[3],
                          align_item = sl[4],
                          justify_item = sl[5]
                          )
  else:

    return render_template("over.html")

if __name__ == "__main__":
  app.run(debug=True)
