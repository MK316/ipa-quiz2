import streamlit as st
import random

# Dictionary of IPA symbols and their descriptions for consonants and vowels
ipa_consonants = {
    'p': 'voiceless bilabial stop', 'b': 'voiced bilabial stop',
    't': 'voiceless alveolar stop', 'd': 'voiced alveolar stop',
    'k': 'voiceless velar stop', 'g': 'voiced velar stop',
    'f': 'voiceless labio-dental fricative', 'v': 'voiced labio-dental fricative',
    'θ': 'voiceless dental fricative', 'ð': 'voiced dental fricative',
    's': 'voiceless alveolar fricative', 'z': 'voiced alveolar fricative',
    'ʃ': 'voiceless palato-alveolar fricative', 'ʒ': 'voiced palato-alveolar fricative',
    'h': 'voiceless glottal fricative', 'm': 'bilabial nasal',
    'n': 'alveolar nasal', 'ŋ': 'velar nasal',
    'l': 'alveolar lateral approximant', 'r': 'alveolar approximant',
    'w': 'labio-velar approximant', 'j': 'palatal approximant',
    'ʧ': 'voiceless palato-alveolar affricate', 'ʤ': 'voiced palato-alveolar affricate'
}

ipa_vowels = {
    'i': 'high front tense', 'ɪ': 'high front lax', 'ɛ': 'mid front lax',
    'æ': 'low front lax', 'ʌ': 'low central lax', 'ə': 'mid central lax',
    'ɑ': 'low back tense', 'ɒ': 'low back rounded tense', 'ɔ': 'mid back rounded tense',
    'ʊ': 'high back rounded lax', 'u': 'high back rounded tense'
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
choice = st.radio("Choose a symbol set to practice:", ('Consonant Symbols', 'Monophthong Vowel Symbols'))

# Initialize or reset session state upon choice or first load
if 'last_choice' not in st.session_state or st.session_state.last_choice != choice:
    st.session_state.data = load_data(choice)
    st.session_state.remaining = list(st.session_state.data.keys())
    random.shuffle(st.session_state.remaining)
    st.session_state.current_symbol = st.session_state.remaining.pop() if st.session_state.remaining else None
    st.session_state.score = 0
    st.session_state.trials = 0
    st.session_state.started = False
    st.session_state.answered = False
    st.session_state.last_choice = choice

# Start or continue the practice
if st.button("Start Practice / Next Symbol"):
    if not st.session_state.started or not st.session_state.remaining:
        st.session_state.remaining = list(st.session_state.data.keys())
        random.shuffle(st.session_state.remaining)
        st.session_state.started = True
    if st.session_state.remaining:
        st.session_state.current_symbol = st.session_state.remaining.pop()
        st.session_state.answered = False  # Reset answered flag for the new symbol
    else:
        st.balloons()
        st.success(f"🎉 You've completed the practice with a score of {st.session_state.score} out of {st.session_state.trials}. Well done!")
        st.session_state.started = False

# Display the current symbol and collect user input
if st.session_state.started and st.session_state.current_symbol:
    st.write(f"What is the description for the IPA symbol '{st.session_state.current_symbol}'?")
    user_answer = st.text_input("Type your answer here", key=st.session_state.current_symbol)

    if st.button("Submit Answer") and not st.session_state.answered:
        st.session_state.trials += 1
        if user_answer.lower().strip() == st.session_state.data[st.session_state.current_symbol].lower():
            st.success("😍 Good job!")
            st.session_state.score += 1
        else:
            st.error(f"Incorrect. The correct answer is: {st.session_state.data[st.session_state.current_symbol]}")
        st.session_state.answered = True  # Set the answered flag to True after a submission
        st.session_state.remaining.append(st.session_state.current_symbol)  # Add symbol back for retry
        random.shuffle(st.session_state.remaining)

# Display score and trials
if st.session_state.trials > 0:
    st.write(f"Status: {st.session_state.score} out of {st.session_state.trials}")
