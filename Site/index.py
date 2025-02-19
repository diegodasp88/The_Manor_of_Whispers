import streamlit as st
from time import sleep

# ===============================================
# Function to switch pages
def switch_page():
    st.session_state.page += 1

# Class to play an audio
class Play_audio():
    def __init__(self, file_name:str, autoplay:bool = True, loop:bool = False):
        """[file_name: insert the audio file path], 
        [autoplay: True/False], 
        [loop: True/False]"""
        self.file_name = file_name
        self.autoplay = autoplay
        self.loop = loop
        st.audio(data=self.file_name, autoplay=self.autoplay, loop=self.loop)
        st.markdown('''<style> audio { display: none; } </style>''', unsafe_allow_html=True)

# ===============================================
# Starting the story

if 'page' not in st.session_state:
    st.session_state.page = 0

st.title('The Manor of Whispers')
st.write('''The air was heavy with the scent of rain-soaked earth as Liam pushed open the rusted gates of Blackthorn Manor. It had been years since anyone dared to enter the abandoned estate that loomed at the edge of the village. Legends whispered of its cursed halls and the souls trapped within. But Liam had no choice; his 9 year-old sister, Ellie, had disappeared two nights ago, and the villagers last saw her near the manor's overgrown gardens.''')
st.image('/images/pic1.jpg')
if st.session_state.page == 0:
    st.button('Continue...', on_click=switch_page)


if st.session_state.page >= 1:
    st.write('''Lightning forked across the sky, illuminating the twisted trees and the gaping maw of the manor's entrance.''')
    if st.session_state.page == 1:
        Play_audio(file_name='sounds/lightning.mp3')
        st.button('Liam gets closer to the manor...', on_click=switch_page)


if st.session_state.page >= 2:
    st.write('''The door creaked open as if inviting him in. A shiver crawled up his spine, but he stepped forward. The door slammed shut behind him, plunging him into darkness.''')
    if st.session_state.page == 2:
        Play_audio(file_name='sounds/opening_door.mp3')
        st.button('Liam checks the interior of the manor...', on_click=switch_page)


if st.session_state.page >= 3:
    st.write('''The air inside was suffocating. Dust motes floated in the faint light seeping through boarded windows. Shadows danced on the walls, and whispers seemed to echo from nowhere. Liam pulled out his flashlight, its beam cutting through the gloom. Ahead, a grand staircase spiraled upward into darkness, but before he could take a step, a voice, low and rasping, filled the room.''')
    st.image('images/pic2.jpg')
    if st.session_state.page == 3:
        Play_audio(file_name='sounds/door_slam.mp3')
        st.button('Liam listens to the voice...', on_click=switch_page)
    if 3 <= st.session_state.page <= 5:
        sleep(5)
        Play_audio(file_name='sounds/whispering_echo.mp3', loop=True)


if st.session_state.page >= 4:
    with st.container(border=True):
        st.markdown('#### *To proceed, you must answer*')
    st.write('A large, ornate mirror against the wall began to ripple like water, and text appeared on its surface:')
    if st.session_state.page == 4:
        Play_audio(file_name='sounds/voice_1.mp3')
        st.button('Liam reads the text...', on_click=switch_page)

   
if st.session_state.page >= 5:
    with st.container(border=True):
        # Riddle #1:
        st.markdown('#### I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?')
        riddle1 = st.selectbox('', options=['A ghost', 'The wind', 'An echo', 'A shadow'], index=None, placeholder='Answer the riddle')
        if riddle1:    
            if riddle1 == 'An echo':
                st.success('Correct! You are allowed to proceed.', icon='✅')
                if st.session_state.page == 5:
                    Play_audio(file_name='sounds/correct.mp3')
                    st.button('Continue deeper into the manor...', on_click=switch_page)
            else:
                st.error("You failed! You may try again or you'll never see your sister again!", icon='⛔')
                st.session_state.page = 5
                if st.session_state.page == 5:
                    Play_audio(file_name='sounds/evil_laugh.mp3')


if st.session_state.page >= 6:
    st.write('''The mirror returned to its normal state once Liam gave his answer, and the whispers subsided. The air seemed to shift, the temperature dropping as he ascended the staircase.''')
    if st.session_state.page == 6:
        st.button('Liam gets upstairs...', on_click=switch_page)


if st.session_state.page >= 7:
    st.write('''Each creak of the wooden steps echoed like a gunshot in the stillness. At the top, a long hallway stretched into the shadows, lined with faded portraits. Their eyes seemed to follow him as he walked.''')
    st.image('images/pic3.jpg')
    if st.session_state.page == 7:
        Play_audio(file_name='sounds/steps_wood.mp3')
        st.button('Liam walks through the corridor...', on_click=switch_page)


if st.session_state.page >= 8:
    st.write('''Halfway down the corridor, a door creaked open on its own. Inside was a study, its walls lined with rotting books and a desk piled high with papers. A single candle burned on the desk. As Liam stepped inside, the candle flickered, and another voice - this one softer, almost childlike — whispered:''')
    if st.session_state.page == 8:
        sleep(2)
        Play_audio(file_name='sounds/opening_door.mp3')
        st.button('Liam listens another voice carefully...', on_click=switch_page)


if st.session_state.page >= 9:
    with st.container(border=True):
        st.markdown('#### *Find the key, but beware the wrong drawer.*')

    st.write('The desk had three drawers, each marked with a number: 1, 2, and 3. Above the desk, scratched into the wood, was another riddle:')
    st.image('images/pic4.jpg')
    if st.session_state.page == 9:
        Play_audio(file_name='sounds/voice_2.mp3')
        st.button('Liam reads the riddle on the wall...', on_click=switch_page)


if st.session_state.page >= 10:
    with st.container(border=True):
        # Riddle #2
        st.markdown('#### The more you take, the more you leave behind. What am I?')
        riddle2 = st.selectbox('', options=['Drawer #1: Footsteps', 'Drawer #2: Time', 'Drawer #3: Memories'], index=None, placeholder='Choose the correct drawer.')
        if riddle2: 
            if riddle2 == 'Drawer #1: Footsteps':
                st.success("Correct! You have just found the key!", icon='🗝️')
                if st.session_state.page == 10:
                    Play_audio(file_name='sounds/correct.mp3')
                    st.button('Liam escapes the study...', on_click=switch_page)
            else:
                st.error('You have just failed!', icon='⛔')
                st.write("The door has just slammed shut and you are trapped in the study until you solve this riddle successfully. Try again.")
                st.session_state.page = 10
                if st.session_state.page == 10:
                    Play_audio('sounds/door_slam.mp3')
                    sleep(2)
                    Play_audio('sounds/evil_laugh.mp3')   


if st.session_state.page >= 11:
    st.write('''When he finally escaped the study, he found himself back in the hallway. The walls seemed to close in, and the whispers grew louder.
             
At the end of the corridor, a heavy iron door barred his way. The key fit, but before the door would open, a series of ghostly voices echoed around him:''')
    st.image('images/pic5.jpg')
    if st.session_state.page == 11:
        sleep(3)
        Play_audio(file_name='sounds/whispering_echo.mp3')
        st.button('Liam listens carefully...', on_click=switch_page)

if st.session_state.page >= 12: 
    with st.container(border=True):
        st.markdown('#### *I’m always running, but I never move. What am I?*')
    st.write('''A chilling wind surged through the hallway. Liam hesitated. If he answered correctly, the door would open. If he was wrong, the walls would begin to close in, the shadows reaching for him with cold, claw-like fingers, their whispers turning into agonized screams. Bad things would happen to him.''')    
    if st.session_state.page == 12:
        Play_audio(file_name='sounds/voice_3.mp3')
        sleep(6)
        Play_audio(file_name='sounds/wind.mp3')
        st.button('Liam thoughtfully tries to answer this new riddle...', on_click=switch_page)


if st.session_state.page >= 13:
    with st.container(border=True):
        # Riddle #3
        st.markdown('#### I’m always running, but I never move. What am I?')
        riddle3 = st.selectbox('', options=['A heartbeat', 'A dream', 'A clock'], index=None, placeholder="What's the right answer? ")
        if riddle3: 
            if riddle3 == 'A clock':
                st.success("Correct! The iron door may be unlocked now.", icon='🗝️')
                if st.session_state.page == 13:
                    Play_audio(file_name='sounds/correct.mp3')
                    st.button('Liam unlocks the iron door with the key...', on_click=switch_page)
            else:
                st.error('Wrong!', icon='⛔')
                st.write("The walls begin to close in. The ghosted-figure shadows start to scream and get closer to him. Hurry up! Try again.")
                st.session_state.page = 13
                if st.session_state.page == 13:
                    Play_audio('sounds/evil_laugh.mp3')
                    sleep(2)
                    Play_audio('sounds/echoed_screams.mp3') 


if st.session_state.page >= 14:
    st.write("Beyond the door was a vast ballroom, its grandeur long faded. The chandeliers hung crookedly, their crystals dulled with age. A faint melody played from an unseen piano, the notes discordant and chilling. At the center of the room stood a figure, draped in tattered black robes, its face obscured by a veil. It pointed to Liam and spoke:")
    st.image('images/pic6.jpg')
    if st.session_state.page == 14:
        Play_audio(file_name='sounds/opening_iron_door.mp3')
        sleep(5)
        Play_audio(file_name='sounds/piano.mp3')
        st.button('Liam, shaking with fear, listens...', on_click=switch_page)


if st.session_state.page >= 15:
    with st.container(border=True):
        st.markdown('#### *You’ve come far, but the darkest truth lies ahead. Answer, or join the others.*')
    st.write('''The floor beneath Liam’s feet began to crack, revealing a swirling abyss below. The figure raised an arm, and another riddle appeared in the air, written in glowing red letters:''')
    st.image('images/pic7.jpg')
    if st.session_state.page == 15:
        Play_audio(file_name='sounds/voice_4.mp3')
        sleep(8)
        Play_audio(file_name='sounds/floor_cracking.mp3')
        st.button('Liam sees another riddle...', on_click=switch_page)
    

if st.session_state.page >= 16:
    with st.container(border=True):
        # Riddle #4
        st.markdown('#### I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I?')
        riddle4 = st.selectbox('', options=['A desert', 'A painting', 'A map', 'A book'], index=None, placeholder="Answer carefully ")
        if riddle4: 
            if riddle4 == 'A map':
                st.success("Correct!", icon='✅')
                if st.session_state.page == 16:
                    Play_audio(file_name='sounds/correct.mp3')
                    st.button('Continue...', on_click=switch_page)
            else:
                st.error('Wrong! Do you not want to see your sister again? Try again.', icon='⛔')
                st.session_state.page = 16
                if st.session_state.page == 16:
                    Play_audio('sounds/evil_laugh.mp3')


if st.session_state.page >= 17:
    st.write('''Each riddle brought Liam closer to the heart of the manor and the truth about his sister’s disappearance. But the deeper he went, the more the manor seemed alive, reshaping itself, taunting him with shadows and whispers. The final riddle awaited him in the cellar, where the air was thick with decay, and the walls seemed to pulse like a heartbeat. Here, a circle of candles surrounded a small wooden box. As he approached, the candles flared.''')
    st.image('images/pic8.jpg')
    st.write('''Liam picked up the small, locked box on floor. The lock required a three-digit code to open. He noticed some instructions on the left side of the box where he could read: ''')
    with st.container(border=True):
        # Riddle #5
        st.markdown("*Three numbers will set you free. The first is the age of the latest lost soul. The second is the number of riddles answered to get here. The last is the number of drawers the desk in the study had.*")
        riddle3 = st.text_input(label='Digit the number sequence of the lock 🔒.')
        if riddle3: 
            if riddle3 == '943':
                st.success("Correct! You've unlocked the box", icon='🔓')
                if st.session_state.page == 17:
                    Play_audio(file_name='sounds/correct.mp3')
                    st.button('Liam opens the box...', on_click=switch_page)
            else:
                st.error('Wrong! You will never see your sister again unless you find out the right sequence.', icon='⛔')
                st.session_state.page = 17
                if st.session_state.page == 17:
                    Play_audio('sounds/evil_laugh.mp3')


if st.session_state.page >= 18:
    st.write('''As Liam turned the final digit of the lock, a soft click echoed through the cellar. He hesitated, his breath shallow, before slowly lifting the lid. Inside, he found…

A small, withered journal, its pages brittle and stained with time. The name Ellie was scrawled across the cover in faded ink. His sister’s name.''')
    st.image('images/pic9.jpg')
    st.write('''The candles flickered violently as he opened the journal. The first page was filled with frantic writing, detailing whispers in the walls, the feeling of being watched, and — most chillingly — a warning:''')
    with st.container(border=True):
        st.markdown('#### *The manor does not let go. If you are reading this… it knows you are here.*')
    if st.session_state.page == 18:
        Play_audio(file_name='sounds/unlocking.mp3')
        st.button('With "his hair standing on end", he keeps checking the journal...', on_click=switch_page)
    

if st.session_state.page >= 19:
    st.write('''As Liam flipped through the pages, something shifted in the air. The temperature plummeted. The walls seemed to breathe.

And then… a single whisper emerged from the darkness, growing louder, multiplying.''')
    if st.session_state.page == 19:
        st.button('Liam looks desperately around to try to notice what’s up...', on_click=switch_page)


if st.session_state.page >= 20:
    with st.container(border=True):
        st.markdown('#### *You shouldn’t have opened it!*')
    st.write('''A chilling wind howled through the room. The journal spoke of an ancient entity bound to the manor, feeding on fear, drawing in those who wandered too close. The missing villagers had been consumed, their souls trapped within the walls. The whispers were their voices, warning, begging.''')
    if st.session_state.page == 20:
        Play_audio(file_name='sounds/voice_5.mp3')
        sleep(3)
        Play_audio(file_name='sounds/wind.mp3')
        st.button('Continue...', on_click=switch_page)


if st.session_state.page >= 21:
    st.write('''A deafening shriek erupted from the darkness. The shadows coalesced into a monstrous form — a mass of writhing limbs and hollow, glowing eyes. The entity lunged.''')
    st.image('images/pic10.jpg')
    if st.session_state.page == 21:
        Play_audio(file_name='sounds/monster.mp3')
        st.button('Continue...', on_click=switch_page)
    

if st.session_state.page >= 22:
    st.write('''Liam acted on instinct. He grabbed a nearby lantern and hurled it at the creature. The flames licked at the shadows, causing the entity to recoil with an unearthly scream. As it writhed, the walls of the manor began to crack.''')
    st.image('images/pic11.jpg')
    if st.session_state.page == 22:
        sleep(8)
        Play_audio(file_name='sounds/shriek.mp3')
        sleep(3)
        Play_audio(file_name='sounds/floor_cracking.mp3')
        st.button('Continue...', on_click=switch_page)


if st.session_state.page >= 23:
    st.write('''The spirits, now free, rose from the walls, their ghostly forms merging into a blinding light. The manor shuddered violently, its very foundation trembling. With one final wail, the entity was pulled into the abyss, and the manor collapsed in on itself...''')
    st.image('images/pic12.jpg')
    if st.session_state.page == 23:
        Play_audio(file_name='sounds/spirits.mp3')
        sleep(10)
        Play_audio(file_name='sounds/destruction.mp3')
        st.button('Continue...', on_click=switch_page)


if st.session_state.page >= 24:
    st.write('''Liam awoke outside, rain pouring down as the ruins of Blackthorn Manor smoldered behind him. The whispers were gone. Ellie’s journal remained in his hands—a testament to the nightmare he had survived.

The villagers, once thought lost, could never return. But their souls had been freed, and the curse had been broken.

As Liam stood, he felt Ellie’s presence—a final whisper, but this one full of gratitude.

Then, silence.

The nightmare was over.

Or so he hoped.

***THE END.***''')
    if st.session_state.page == 24:
        Play_audio(file_name='sounds/rain.mp3')
