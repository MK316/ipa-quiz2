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
    'm': 'bilabial nasal',
    'n': 'alveolar nasal',
    'ŋ': 'velar nasal',  # Eng
    'l': 'alveolar lateral approximant',
    'r': 'alveolar approximant',
    'w': 'labio-velar approximant',
    'j': 'palatal approximant',
    'ʧ': 'voiceless palato-alveolar affricate',  # Tsh
    'ʤ': 'voiced palato-alveolar affricate'  # Dzh
}

# Initialize session state
if 'remaining' not in st.session_state:
    st.session_state.remaining = list(ipa_symbols.keys())
if 'current_symbol' not in st.session_state:
    st.session_state.current_symbol = random.choice(st.session_state.remaining)
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'trials' not in st.session_state:
    st.session_state.trials = 0

# Start button and app functionality
st.title("👏 Phonetic description: 24 English Consonant Practice")
st.caption("Notes: 1. Use '-' for two-word description (e.g., palato-alveolar). \n2. Use minimal description: e.g., /m/ is bilabial nasal. \n3. Use 'palato-alveolar' instead of 'alveo-palatal' or 'postalveolar'.") 
st.caption("When 24 sounds are all answered correctly, the app will finish. If you answer incorrectly, the symbol will reappear.")
if st.button("Show a symbol"):
    st.session_state.started = True

if 'started' in st.session_state and st.session_state.started:
    if len(st.session_state.remaining) > 0:
        # Display a random symbol
        symbol_to_guess = st.session_state.current_symbol
        st.write(f"What is the description for the IPA symbol '{symbol_to_guess}'?")

        # User input for the answer
        user_answer = st.text_input("Type your answer here", key=str(st.session_state.trials))

        # Check the answer
        if st.button("Submit Answer"):
            st.session_state.trials += 1
            if user_answer.lower().strip() == ipa_symbols[symbol_to_guess].lower():
                st.success("Correct!")
                st.session_state.score += 1
                st.session_state.remaining.remove(symbol_to_guess)
            else:
                st.error("Wrong answer. Try again!")
            
            # Update the symbol to guess only if there are remaining symbols
            if st.session_state.remaining:
                st.session_state.current_symbol = random.choice(st.session_state.remaining)
    else:
        st.balloons()
        st.write(f"You've completed the practice with a score of {st.session_state.score} out of {st.session_state.trials}. Good job!")

# Display score and trials
if 'score' in st.session_state and 'trials' in st.session_state:
    st.write(f"Score: {st.session_state.score}")
    st.write(f"Trials: {st.session_state.trials}")
