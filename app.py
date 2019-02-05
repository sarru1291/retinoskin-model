from flask import Flask,jsonify,request
import json
import predict as pr
import requests,shutil

app = Flask(__name__)

@app.route('/api/model/test',methods=['POST'])
def imageTestPost():
    incomingData=request.data

    incomingDataDic=json.loads(incomingData)
    imageURL=incomingDataDic['url']
    option=incomingDataDic['option']
    # print(incomingDataDic['url'])
    # image=Image.open(urllib.urlopen(imageURL))
    response=requests.get(imageURL,stream=True).raw
    # print(image.format)
    with open('my_image.jpg', 'wb') as file:
        shutil.copyfileobj(response, file)
    del response
    # print(response)
    if option=='retinopathy':
        output=pr.classifyDiabeticRetinopathy('my_image.jpg')
    else:
        output=pr.classifySkinLesion('my_image.jpg')

    print(output)
    return jsonify({'output':output})

@app.route('/api/model/test',methods=['GET'])
def imageTestGet():
    message='you have selected GET method'
    return jsonify({'message':message})

if __name__ == '__main__':
    app.run(debug=True)