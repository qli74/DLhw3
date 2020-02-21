import logging,subprocess

from random import randint

from flask import Flask, render_template

from flask_ask import Ask, statement, question, session


app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@ask.launch

def new_game():

    welcome_msg = 'Welcome to my skill!'#render_template('welcome')

    return question(welcome_msg)


@ask.intent("SuperIntent",  convert={'Text': str})

def next_round(Text):
    #############################
    # Launch a command with pipes
    p = subprocess.Popen(['python -m parlai.scripts.interactive -mf ../model2/myhred'], shell=True,
                         stdout=subprocess.PIPE,
                         stdin=subprocess.PIPE)

    while 1:
        line = p.stdout.readline()
        line = line.strip().decode()
        #print(line)
        if line[:23] == '[  warmup_updates: -1 ]':
            break
    # Send the data and get the output
    # p.communicate('cd /Users/lexine/Documents/DLforDialog/ParlAI')
    p.stdin.write(bytes(Text, 'utf-8'))
    p.stdin.write(bytes("\n", 'utf-8'))
    p.stdin.flush()
    # To interpret as text, decode
    line = p.stdout.readline()
    # p.stdout.flush()
    line = line.strip().decode()
    line = line.split('[hred]: ')
    print(line[-1])

    return question(line[-1])




if __name__ == '__main__':

    app.run(debug=True)