import streamlit as st
import random

# Dictionary of IPA symbols and their descriptions for consonants and vowels
# Dictionary of IPA symbols and their descriptions for consonants and vowels
ipa_consonants = {
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

ipa_vowels = {
    'i': 'high front tense',  # like in "see"
    'ɪ': 'high front lax',    # like in "sit"
    'ɛ': 'mid front lax',     # like in "set"
    'æ': 'low front lax',     # like in "sat"
    'ʌ': 'low central lax',   # like in "strut"
    'ə': 'mid central lax',   # like in "about"
    'ɑ': 'low back tense',    # like in "father"
    'ɒ': 'low back rounded tense',  # (British English "lot")
    'ɔ': 'mid back rounded tense',  # like in "thought"
    'ʊ': 'high back rounded lax',   # like in "foot"
    'u': 'high back rounded tense', # like in "boot"
}

# Function to load the correct dataset based on the user's choice
def load_data(choice):
    if choice == 'Consonant Symbols':
        return ipa_consonants
    elif choice == 'Monophthong Vowel Symbols':
        return ipa_vowels
    else:
        return {}

# UI for selection
st.title("👏 Phonetic Description Practice")
choice = st.radio("Choose a symbol set to practice:", ('Consonant Symbols', 'Monophthong Vowel Symbols'), on_change=lambda: st.session_state.update(change_dataset=True))

# Initialize or update the dataset when necessary
if 'change_dataset' in st.session_state and st.session_state.change_dataset or 'data' not in st.session_state:
    st.session_state.data = load_data(choice)
    st.session_state.remaining = list(st.session_state.data.keys())
    random.shuffle(st.session_state.remaining)  # Shuffle the order
    st.session_state.current_symbol = st.session_state.remaining.pop()
    st.session_state.score = 0
    st.session_state.trials = 0
    st.session_state.change_dataset = False
    st.session_state.started = False

if st.button("Start Practice / Next Symbol"):
    if not st.session_state.started or not st.session_state.remaining:
        # Reset or start the session
        st.session_state.remaining = list(st.session_state.data.keys())
        random.shuffle(st.session_state.remaining)
        st.session_state.started = True
    if st.session_state.remaining:
        st.session_state.current_symbol = st.session_state.remaining.pop()
    else:
        st.balloons()
        st.success(f"🎉🎉🎉 You've completed the practice with a score of {st.session_state.score} out of {st.session_state.trials}. Good job!")
        st.session_state.started = False

if st.session_state.started:
    symbol_to_guess = st.session_state.current_symbol
    st.write(f"What is the description for the IPA symbol '{symbol_to_guess}'?")
    user_answer = st.text_input("Type your answer here", key=symbol_to_guess)

    if st.button("Submit Answer"):
        st.session_state.trials += 1
        if user_answer.lower().strip() == st.session_state.data[symbol_to_guess].lower():
            st.success("😍 Good job!")
            st.session_state.score += 1
        else:
            st.error("Incorrect. Try again 😥")
            # Add symbol back to list for retry
            st.session_state.remaining.append(symbol_to_guess)
            random.shuffle(st.session_state.remaining)

# Display score and trials
if 'score' in st.session_state and 'trials' in st.session_state:
    st.write(f"Status: {st.session_state.score} out of {st.session_state.trials}")
