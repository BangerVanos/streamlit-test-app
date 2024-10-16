import streamlit as st
import logging
import hashlib


logger = logging.getLogger('st-app')
logging.basicConfig(filename='logs.log', filemode='a', encoding='utf-8', level=logging.INFO)


HASH = 'e5089e403ce9873d8e9af3abd5cbde11929d2938c6bdaff6d4255b499877904b'


def guess_try(guess: str) -> bool:
    guess_hash = hashlib.sha256(bytes(guess, encoding='utf-8')).hexdigest()
    return guess_hash == HASH


st.write("## Try to guess string from it's SHA-256 hash")
with st.form('guess_form'):
    name = st.text_input('Your name', value='Anonimus', placeholder='Put your name here!',
                         key='name')
    guess = st.text_input('Your guess', placeholder='Your original string guess, for example: Hello, world!',
                          key='guess')
    submit = st.form_submit_button('Try to guess!', icon=':material/emoticon:')
    if submit:
        if not name:
            st.error("You must put your name to guess")
            logger.error("Someone tried to guess, but didn't put their name!")
        if not guess:
            st.error("How do you want to guess without guess?")
            logger.error(f"{'Someone' if not name else name} tried to guess, but didn't put any guess!")
        if name and guess:
            is_correct = guess_try(guess)
            if is_correct:
                st.success(f'You are right! Original string was: {guess}')
                logger.info(f'{name} made right guess!')
            else:
                st.error(f"'{guess}' was not the right string!")
                logger.warning(f'{name} made wrong guess!')
