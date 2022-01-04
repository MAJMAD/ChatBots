import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"

def unknown():
    response = ['Could you please re-phrase that?',
                "...",
                "Sounds about right",
                "What does that mean?",
                "I haven't learned that phrased yet"][random.randrange(5)]
    return response
