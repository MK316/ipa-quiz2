import streamlit as st
import random

# Dictionary of IPA symbols and their descriptions
ipa_symbols = {
    'p': 'voiceless bilabial stop',
    'b': 'voiced bilabial stop',
    't': 'voiceless alveolar stop',
    'd': 'voiced alveolar stop',
    'k': 'voiceless velar stop',
    'g': 'voiced velar stop',
    'f': 'voiceless labio-dental fricative',
    'v': 'voiced labio-dental fricative',
    'θ': 'voiceless dental fricative',  # Theta
    'ð': 'voiced dental fricative',  # Eth
    's': 'voiceless alveolar fricative',
    'z': 'voiced alveolar fricative',
    'ʃ': 'voiceless palato-alveolar fricative',  # Esh
    'ʒ': 'voiced palato-alveolar fricative',  # Ezh
    'h': 'voiceless glottal fricative',
    'm': 'voiced bilabial nasal',
    'n': 'voiced alveolar nasal',
    'ŋ': 'voiced velar nasal',  # Eng
    'l': 'voiced alveolar lateral approximant',
    'r': 'voiced alveolar approximant',
    'w': 'voiced labio-velar approximant',
    'j': 'voiced palatal approximant',
    'ʧ': 'voiceless palato-alveolar affricate',  # Tsh
    'ʤ': 'voiced palato-alveolar affricate'  # Dzh
}


# Initialize session state
if 'remaining' not in st.session_state:
    st.session_state.remaining = list(ipa_symbols.keys())
if 'current_symbol' not in st.session_state:
    st.session_state.current_symbol = random.choice(st.session_state.remaining)

# Start button and app functionality
st.title("English Consonant Practice App")

if st.button("Start Practice"):
    st.session_state.started = True

if 'started' in st.session_state and st.session_state.started:
    if len(st.session_state.remaining) > 0:
        # Display a random symbol
        symbol_to_guess = st.session_state.current_symbol
        st.write(f"What is the description for the IPA symbol '{symbol_to_guess}'?")

        # User input for the answer
        user_answer = st.text_input("Type your answer here", key='answer')

        # Check the answer
        if st.button("Submit Answer"):
            if user_answer.lower().strip() == ipa_symbols[symbol_to_guess].lower():
                st.success("Correct!")
                st.session_state.remaining.remove(symbol_to_guess)
                if st.session_state.remaining:
                    st.session_state.current_symbol = random.choice(st.session_state.remaining)
            else:
                st.error("Wrong answer. Try again!")
    else:
        st.balloons()
        st.success("You've completed the practice. Good job!")

# Reset button to restart the practice
if st.button("Restart"):
    st.session_state.remaining = list(ipa_symbols.keys())
    st.session_state.current_symbol = random.choice(st.session_state.remaining)
    st.session_state.started = False
    st.experimental_rerun()
