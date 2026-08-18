import streamlit as st

# List, Tuple, Set 
names = [] 
 
ai_basic_details = ("BabyBot",) 
 
greetings = { 
    "hello", "hi", "hey", "yo", "good morning", 
    "good afternoon", "good evening", "howdy", "hiya", "heya", 
    "hey there", "hi there", "hello there", "greetings", "sup", 
    "what's up", "whats up", "wassup", "how are you", "how's it going", 
    "hows it going", "how are things", "welcome", "morning", "afternoon", 
    "evening", "good day", "salutations", "hey hey", "hey buddy" 
} 
 
salutations = { 
    "bye", "farewell", "goodbye", "bye bye", "chat later", "later", 
    "see you", "see ya", "see you later", "catch you later", "take care", 
    "have a good day", "have a nice day", "until next time", "talk soon", 
    "talk to you later", "gotta go", "got to go", "I'm off", "I'm out", 
    "peace", "peace out", "see ya soon", "see you soon", "good night", 
    "have a good night" 
} 
 
#Functions 
def greet_user(): 
    print("BabyBot: Hello, I am BabyBot") 
    print("What is your name?") 
 
 
def get_user_name(): 
    userName = input().capitalize() 
    names.append(userName) 
    return userName 
 
 
def introduce_user(userName): 
    print(f"{userName}: {userName}") 
    print(f"BabyBot: Hello there {userName}") 
 
 
def respond_to_input(userInput, userName): 
     
    if userInput == "how are you": 
        print("BabyBot: I am doing good. How are you?") 
        return True 
 
    elif userInput in greetings: 
        print(f"BabyBot: Hello there {userName}, how can I assist you today?") 
        return True 
 
    elif userInput == "what is your name": 
        print(f"BabyBot: {ai_basic_details[0]}, a rule based assistant.") 
        return True 
 
    elif userInput == "what is my name": 
        print(f"BabyBot: Your name is {userName}!") 
        return True 
 
    elif userInput == "what can you do": 
        print("BabyBot: I can help you discuss your thoughts and provide helpful tips.") 
        return True 
 
    elif userInput in salutations: 
        print("BabyBot: Goodbye!") 
        return False 
 
    else: 
        print("BabyBot: I don't understand that yet!") 
        return True 


# ============================================================
# STREAMLIT
# ============================================================

st.set_page_config(
    page_title="BabyBot",
    page_icon="🤖"
)

st.title("🤖 BabyBot")

st.write(
    """
    **BabyBot** is a simple rule-based chatbot built with Python.

    BabyBot can respond to greetings, remember your name,
    answer basic questions about itself, and provide helpful tips.
    """
)

st.info(
    """
    **Try saying:**  
    `"hi"` • `"hello"` • `"how are you"` • `"what is your name"` •  
    `"what is my name"` • `"what can you do"` • `"goodbye"`
    """
)


# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Store user's name
if "userName" not in st.session_state:
    st.session_state.userName = None


# BabyBot's first message
if len(st.session_state.messages) == 0:

    st.session_state.messages.append({
        "role": "assistant",
        "content": "Hello, I am BabyBot. What is your name?"
    })


# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])


# Chat box
userInput = st.chat_input("Type your message...")


if userInput:

    # Show user's message
    st.session_state.messages.append({
        "role": "user",
        "content": userInput
    })

    with st.chat_message("user"):
        st.write(userInput)


    # First input = user's name
    if st.session_state.userName is None:

        st.session_state.userName = userInput.capitalize()

        names.append(st.session_state.userName)

        response = f"Hello there {st.session_state.userName}"

        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })

        with st.chat_message("assistant"):
            st.write(response)


    # Everything after the name
    else:

        userInput = userInput.lower()

        # Capture the output from your existing function
        import io
        from contextlib import redirect_stdout

        output = io.StringIO()

        with redirect_stdout(output):

            should_continue = respond_to_input(
                userInput,
                st.session_state.userName
            )

        response = output.getvalue().strip()

        # Save response
        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })

        # Display response
        with st.chat_message("assistant"):
            st.write(response)

        # Stop accepting conversation after goodbye
        if should_continue is False:
            st.session_state.messages.append({
                "role": "assistant",
                "content": "👋 Chat ended."
            })
