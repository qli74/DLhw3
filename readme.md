## steps

**1. Creat the skill**
* create a skill with the interaction_model.json in this repo 
* build model

**2. Train the model**
```
git clone https://github.com/qli74/ParlAI
cd ParlAI
python -m parlai.scripts.train_model -mf ../model/myhred -t moviedialog:Task:4 -m hred -df ./Training_dict -stim 10 -ttim 100 -bs 80 -bms 20 -lr 0.001
#If you don't want to wait too long, just kill it when it starts running eval
```
**or download the model**
* unzip the files in ./model: myhred.zip.001 & myhred.zip.002
* change the path in codes

test it:
```
python -m parlai.scripts.interactive -mf ../model/myhred
```


**3. Set up local server**
```
pip install flask-ask
python flask_hred.py
 ./ngrok http 5000
```
now edit the Endpoint in Alexa Developer Console

* Service Endpoint Type: https

* Default Region: Enter the URL given by ngrok, for example https://c4e2ea6b.ngrok.io

* Select the second SSL certificate type
                
* Save Endpoint


**4. Test it in Alexa Developer Console - Test**

* say 'qianwei test' to start this skill
* say anything you like
* it takes about 5 seconds to respond

## Evaluate
Unfortunately, my chatbot is still very stupid. Here are some examples.

-
<img src="https://github.com/qli74/DLhw3/blob/master/im4.png" width="400" >

-
<img src="https://github.com/qli74/DLhw3/blob/master/im3.png" width="400" >

-
<img src="https://github.com/qli74/DLhw3/blob/master/im2.png" width="400" >

-
<img src="https://github.com/qli74/DLhw3/blob/master/im1.png" width="400" >

Training loss : ~ 3e5

Bleu4: ~ 2e-11

gnorm: ~ 4.5

## Issues and future works
* The responses are not really meaningful or not even sentences. Perhaps the training time is not long enough. 
* The word vector and loss function need to be improved 




