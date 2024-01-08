from tkinter import *
from tkinter import messagebox # it is not class, its module
import pyperclip
import json

COLOR = "#D2E3C8"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
import random
def generate_pass():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  nr_letters = random.randint(8, 10)
  nr_symbols = random.randint(2, 4)
  nr_numbers = random.randint(2, 4)


  password_letters = [random.choice(letters) for char in range(nr_letters)]
  password_symbol = [random.choice(symbols) for char in range(nr_symbols) ]
  password_numbers = [random.choice(numbers) for char in range(nr_numbers)]

  password_list = password_letters + password_symbol + password_numbers

  random.shuffle(password_list)

  # inplace of loop

  password = "".join(password_list) # eg. -> "#".join(list) -> kl#pl#bh { list=[kl,pl,bh] }
  password_entry.insert(0, password)

  pyperclip.copy(password) # use for to copy the pass with out copying it on clipboard and you
  # can instantly paste it to a website for which you generate a password.
  


  """
  password = ""
  for char in password_list:
    password += char

  print(f"Your password is: {password}")
  """
#------------------------------- find password ------------------------------#


def find_password():

  website = website_entry.get()
  try:
    with open("data.json", "r") as file:
      data = json.load(file)

  except FileNotFoundError:
     messagebox.showinfo(title="Error", message=f"No data file found")
  else:
    
    if website in data:
      email = data[website]["email"]
      password = data[website]["password"]
      messagebox.showinfo(title=website, message=f"Email: {email}\n Password: {password}")
    else:
      
      messagebox.showinfo(title="Error", message=f"No detail for {website} found")
        
        

  

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_info():
    website = website_entry.get()  # get use to get entry data
    email =   email_entry.get()
    password = password_entry.get()
    new_data = {website : {
                  "email": email,
                  "password": password
              }   }
            

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty. ")
    
    else:
      
      is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                               f"\nPassword: {password}\nIs it ok to save it in data file?")


      if is_ok:
          try:
              with open("data.json", "r") as data_file:
                  # Reading old data
                  data = json.load(data_file)
                  #print("Current data:", data)
          except (FileNotFoundError, json.decoder.JSONDecodeError) as e:
             # print(f"Error reading data.json: {e}")
              # If the file is not found or empty, create a new one with the new_data
              with open("data.json", "w") as data_file:
                  json.dump(new_data, data_file, indent=4)
          else:
              # Updating old data with new data
              data.update(new_data)
              with open("data.json", "w") as data_file:
                  # Saving updated data
                  json.dump(data, data_file, indent=4)
          finally:
              website_entry.delete(0, END)
              password_entry.delete(0, END)

      
      # it return a boolean value so

"""
      if is_ok:

        try:
          
          with open("data.json", "r") as file: 
              # Reading old data
            data = json.load(file)
        except FileNotFoundError:

          with open("data.json", "w") as data_file:              
              #saving updated data to json file
            json.dump(new_data, data_file, indent=4)

        else:
          # Updating old data with new data
          data.update(new_data)

          with open("data.json", "w") as data_file:

              #saving updated data to json file
              json.dump(data, data_file, indent=4)
        finally:
          #indent for indentation in file
              #f.write(f"{website} | {email} | {password}\n")
          website_entry.delete(0, END)
              #email_entry.delete(0, END)
          password_entry.delete(0, END) # delete use when some one add data than all the data will delete from entries
              # delete have range from ( from to where like 0 to end )     

"""
        
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=COLOR)


canvas = Canvas(width=200, height=200, bg=COLOR, highlightthickness=0)
image = PhotoImage(file=r"D:\python_new projects\password generator\logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=0)


website_label = Label(text="Website:", font="helvetica 12", bg=COLOR, fg = "#192655")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:", font="Tahoma 12", bg=COLOR, fg = "#192655")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:", font="Verdana 12", bg=COLOR, fg = "#192655")
password_label.grid(row=3, column=0)


website_entry = Entry(width=18, bg= "#D6C7AE")
website_entry.grid(row=1, column=1)
website_entry.focus() # when you start the app the cursor at the first entry box
email_entry = Entry(width=34, bg= "#D6C7AE")
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "")  # insert already populated thing or END use for to start with end of that mail or id and 0 at the starting.
password_entry = Entry(width=18, bg= "#D6C7AE")
password_entry.grid(row=3, column=1)


search_button = Button(text="Search", fg="#186F65", font="helvetica 12", bg="#A7D397", command=find_password)
search_button.grid(row=1, column=2)
generate_password_button = Button(text="Generate Password", command=generate_pass, fg="#186F65", font="helvetica 12", bg="#A7D397")
generate_password_button.grid(row=4, column=1)
add_button = Button(text="Add", width=16, command=save_info, font="helvetica 12",fg="#186F65", bg="#A7D397")
add_button.grid(row=5, column=1)

window.mainloop()










