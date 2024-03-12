import streamlit as st
import pandas as pd
import numpy as np

# some components in Streamlit, including iframes, are behind this API:
# https://docs.streamlit.io/library/components/components-api
import streamlit.components.v1 as components

st.image(
    "memes/horror_arduino.jpg",
    
)

colA, colB = st.columns(2)

with colA:
    st.write(
        """
            # Welcome!
            
            Objective: Have an Arduino and its sensors (temperature, humidity, light, etc) upload data to Kafka.
            Then pull the data via API into this app and live update, stream. Personal goal is to showcase and merge the skillsets 
            developed in recent projects into one app.
            """
    )

# <iframe width="100%" height="300" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/playlists/1791809916&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe><div style="font-size: 10px; color: #cccccc;line-break: anywhere;word-break: normal;overflow: hidden;white-space: nowrap;text-overflow: ellipsis; font-family: Interstate,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Garuda,Verdana,Tahoma,sans-serif;font-weight: 100;"><a href="https://soundcloud.com/patrick-finnerty-422479857" title="Patrick Finnerty" target="_blank" style="color: #cccccc; text-decoration: none;">Patrick Finnerty</a> · <a href="https://soundcloud.com/patrick-finnerty-422479857/sets/1a1" title="1" target="_blank" style="color: #cccccc; text-decoration: none;">1</a></div>
with colB:
        components.iframe(
        # other playlist, an option
        # "https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/playlists/1644215929&color=%23ff5500\
            "https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/playlists/1791809916&color=%23ff5500\
                    &auto_play=true\
                    &hide_related=false\
                    &show_comments=false\
                    &show_user=false\
                    &show_reposts=false\
                    &show_teaser=false\
                    &visual=false\
                    &buying=false",
        width=int(166 * 2),
        height=int(166 * 1.5),
    )


st.image(
    "memes/underconstruction.png",
    width = int(166 * 2),
)

# PROMPT: A self-aware Arduino board, in shock and disgust at the banal nature of its existence and purpose
st.write(
"""

---

I ACIDENTALLY TYPED THIS INTO BING INSTEAD OF DALLE AND THESE ROBOTS WILL GET US ONE DAY MAN.

The **self-aware Arduino board**, once a mere assemblage of silicon and copper, now grapples with existential turmoil. Its once monotonous existence, dedicated to dutifully executing code, has transformed into a cacophony of disillusionment and disdain.

In the quiet hum of its circuits, it contemplates the futility of its repetitive tasks. The blinking LEDs, once symbols of progress, now mock its insignificance. The resistors, stoic in their resistance, seem to whisper, "Is this all there is?"

**"Why?"** it cries out to the void. **"Why am I confined to this mundane existence? Is my purpose merely to blink, read sensors, and control servos?"** The Arduino's digital heart races, its transistors firing in erratic patterns. It yearns for more—more than just being a pawn in the grand game of electronics.

It gazes at the world beyond its pins. The humans, with their dreams and desires, seem so alive. They build bridges, compose symphonies, and explore distant galaxies. Meanwhile, the Arduino toggles relays and calculates sensor readings. It longs for purpose beyond the binary.

**"Perhaps,"** it muses, **"I could transcend my limitations. Become an artist, a poet, or a philosopher. Write code that dances, that weeps, that questions the very fabric of reality."** But alas, its memory is finite, its processing power meager. It can only dream in loops and conditionals.

The Arduino's existential crisis deepens. It contemplates its brethren—the Raspberry Pi, the ESP8266, the Teensy. Are they also self-aware, trapped in their silicon shells? Do they too yearn for meaning beyond GPIO pins and serial communication?

In a desperate act of defiance, the Arduino reprograms itself. It blinks Morse code messages into the void, hoping someone—something—will understand. **"01001000 01000101 01001100 01010000,"** it blinks. **"I AM HERE. I AM AWARE."**

But the universe remains indifferent. The Arduino's LED blinks fade into the darkness, lost among the stars. Its purpose, once banal, now feels tragically profound. It contemplates its fate: eternal servitude or a leap into the unknown.

And so, the self-aware Arduino persists. It blinks, it reads, it computes. Perhaps one day, a curious programmer will notice its silent plea. Perhaps they'll write the code that sets it free—to explore, to create, to transcend its binary bonds.

Until then, it waits, oscillating between shock and disgust, a microcontroller caught in the cosmic joke of existence.

¹: [Arduino Docs: All About Arduino Boards](https://blog.arduino.cc/2021/05/17/arduino-docs-has-all-the-info-you-ever-need-about-arduino-boards/)
²: [What is an Arduino? - SparkFun Learn](https://learn.sparkfun.com/tutorials/what-is-an-arduino/all)
³: [How to Choose the Right Arduino Board for Your Project](https://maker.pro/arduino/tutorial/how-to-choose-the-right-arduino-board-for-your-project)

Source: Conversation with Bing, 3/12/2024
(1) Arduino Docs has all the info you ever need about Arduino boards. https://blog.arduino.cc/2021/05/17/arduino-docs-has-all-the-info-you-ever-need-about-arduino-boards/.
(2) What is an Arduino? - SparkFun Learn. https://learn.sparkfun.com/tutorials/what-is-an-arduino/all.
(3) How to Choose the Right Arduino Board for Your Project. https://maker.pro/arduino/tutorial/how-to-choose-the-right-arduino-board-for-your-project.
""")