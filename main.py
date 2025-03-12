import streamlit as st
import re
# Setting up a page
st.set_page_config(
  page_title="Pasword Strength Meter",
  page_icon="icon.png"
)
# Add Heading Of a Page
st.markdown("""# Pasword Strength Meter by [Abdullah Shaikh](https://www.linkedin.com/in/abdullah-shaikh-29699b302/)""")
# Weak Passwords Array
weak_passwords = [
    "123456", "password", "123456789", "12345", "12345678", "qwerty", "1234567", 
    "111111", "123123", "abc123", "password1", "1234", "qwerty123", "1q2w3e4r", 
    "iloveyou", "654321", "666666", "987654321", "123", "1qaz2wsx", "dragon", 
    "monkey", "qazwsx", "121212", "asdfghjkl", "123abc", "123qwe", "zxcvbnm", 
    "555555", "112233", "7777777", "123123123", "11111111", "222222", "1234qwer", 
    "qwerty1", "123654", "159753", "1q2w3e", "123456a", "qwe123", "1q2w3e4r5t", 
    "123321", "aa12345678", "000000", "1234567890", "asdasd", "a123456", 
    "123456789a", "qwertyuiop","Hello123","hello123","Hello1234","hello1234",
    "Hello12345","hello12345"
]

# Check Password Function
def check_pasword_strength(password:str):
    score : int = 0
    if not password:
        st.write("Your Password field is empty")
    elif password in weak_passwords:
        st.error("❌This is such a weak password and absolutely not recommended")
    else:
        if len(password)>=8:
            score+=1
        else:
            st.markdown("+ 🔑Password Length Should atleast of 8 chrachters")
        if re.search(r"[A-Z]", password):
            score+=1
        else:
            st.markdown("+ 🔑Your Password Should contain at least one capital letter")
        if re.search(r"[a-z]", password):
            score+=1
        else:
            st.markdown("+ 🔑Your Password Should contain at least one small letter")
        if re.search("\d",password):
            score+=1
        else:
            st.markdown("+ 🔑Your Password Should Contain atleast one Digit")
        if re.search(r"[!@#$%^&*]",password):
            score+=1
        else:
            st.markdown("+ 🔑Your Password Should Contain atleast one Special Chrachter Like: (!@#$%^&*). ")
        if score==5:
            st.success("✅Your Password is safe and strong")
        elif score==4:
            st.warning("Your Password is moderate but not good follow above suggestion for strong password")
        else:
            st.error("❌Very Weak Password follow above suggesstions to make it strong")
# Taking Password From User
password : str = st.text_input("Enter Password Here: ",placeholder="Write Here",type="password")
if st.button("Check My Password's Strength"):
    check_pasword_strength(password)
