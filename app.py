import streamlit as st
import random

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

# Initialize session state
if 'data' not in st.session_state:
    st.session_state.data = {}

# UI for selection
st.title("👏 Phonetic Description Practice")
choice = st.radio("Choose a symbol set to practice:", ('Consonant Symbols', 'Monophthong Vowel Symbols'))

if choice == 'Consonant Symbols':
    st.session_state.data = ipa_consonants
elif choice == 'Monophthong Vowel Symbols':
    st.session_state.data = ipa_vowels

# Start button and practice functionality
if st.button("Start Practice"):
    st.session_state.remaining = list(st.session_state.data.keys())
    st.session_state.current_symbol = random.choice(st.session_state.remaining)
    st.session_state.started = True
    st.session_state.score = 0
    st.session_state.trials = 0

if 'started' in st.session_state and st.session_state.started:
    if st.session_state.remaining:
        symbol_to_guess = st.session_state.current_symbol
        st.write(f"What is the description for the IPA symbol '{symbol_to_guess}'?")
        user_answer = st.text_input("Type your answer here", key=str(st.session_state.trials))

        if st.button("Submit Answer"):
            st.session_state.trials += 1
            if user_answer.lower().strip() == st.session_state.data[symbol_to_guess].lower():
                st.success("😍 Good job!")
                st.session_state.score += 1
                st.session_state.remaining.remove(symbol_to_guess)
                if st.session_state.remaining:
                    st.session_state.current_symbol = random.choice(st.session_state.remaining)
            else:
                st.error("Try again 😥")
    else:
        st.balloons()
        st.success(f"🎉🎉🎉 You've completed the practice with a score of {st.session_state.score} out of {st.session_state.trials}. Good job!")
        st.session_state.started = False

# Display score and trials
if 'score' in st.session_state and 'trials' in st.session_state:
    st.write(f"Status: {st.session_state.score} out of {st.session_state.trials}")
