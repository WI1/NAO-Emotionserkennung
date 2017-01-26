class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)

    def onLoad(self):
        #put initialization code here

        pass


    def onUnload(self):
        #put clean-up code here
        pass

    def onInput_onStart(self):
        #self.onStopped() #activate the output of the box

        import sys
        import time
        from naoqi import ALProxy
        import httplib, urllib, base64
        import json

        tts = ALProxy("ALTextToSpeech")

        headers = {
        # Request headers
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': 'API_KEY',
        }

        params = urllib.urlencode({
        # Request parameters
        'language': 'unk',
        'detectOrientation ': 'true',
        })

        data = open('/home/nao/recordings/cameras/image.jpg', 'rb').read()

        conn = httplib.HTTPSConnection('api.projectoxford.ai')
        conn.request("POST", "/emotion/v1.0/recognize?%s" % params, data, headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()


        data2 = json.loads(data)

        #print data2
        #tts.say(data2)

        #print data2[0]['faceRectangle']

        if data2[0]['scores']['happiness'] > data2[0]['scores']['contempt']:
            tts.say("You seem happy")
            self.onStopped()
        elif data2[0]['scores']['anger'] > data2[0]['scores']['contempt']:
            tts.say("You seem angry")
            self.output1()





    def onInput_onStop(self):
        self.onUnload() #it is recommended to reuse the clean-up as the box is stopped
        self.onStopped() #activate the output of the box