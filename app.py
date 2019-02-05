from flask import Flask,jsonify,request
import json
from PIL import Image
import predict as pr
import urllib
import requests,shutil
from StringIO import StringIO
app = Flask(__name__)

@app.route('/api/test',methods=['POST'])
def imageTestPost():
    incomingData=request.data

    incomingDataDic=json.loads(incomingData)
    imageURL=incomingDataDic['url']
    # print(incomingDataDic['url'])
    # image=Image.open(urllib.urlopen(imageURL))
    response=requests.get(imageURL,stream=True).raw
    # print(image.format)
    with open('my_image.jpg', 'wb') as file:
        shutil.copyfileobj(response, file)
    del response
    # print(response)
    output=pr.classifyDiabeticRetinopathy('my_image.jpg')
    print(output)
    # print(output['Severe case'])
    # print(output['Mild case'])
    # print(output['Retinopathy not detected'])
    # joutput=json.dump(output)
    # json.loads(joutput)
    return jsonify({'output':output})

@app.route('/api/test',methods=['GET'])
def imageTestGet():
    message='you have selected GET method'
    return jsonify({'message':message})


if __name__ == '__main__':
    app.run(debug=True)