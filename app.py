from flask import Flask,jsonify,request
import json
import predict as pr
import requests

app = Flask(__name__)

@app.route('/api/model/test',methods=['POST'])
def imageTestPost():
    incomingData=request.data
    incomingDataDic=json.loads(incomingData)
    imageURL=incomingDataDic['url']
    option=incomingDataDic['option']
    r=requests.get(imageURL,stream=True)

    if r.status_code!=200:
        output='Model: Image fetching failed'
    else:    
        with open('my_image.jpg', 'wb') as fd:
            for chunk in r.iter_content(chunk_size=128):
                fd.write(chunk)

        if option=='retinopathy':
            output=pr.classifyDiabeticRetinopathy('my_image.jpg')
        # output=pr.classifyDiabeticRetinopathy(imageURL);
        else:
            output=pr.classifySkinLesion('my_image.jpg')
        # output=pr.classifySkinLesion(imageURL)
    
    return jsonify({'output':output})

@app.route('/api/model/test',methods=['GET'])
def imageTestGet():
    message='you have selected model GET method'
    return jsonify({'message':message})
    # if option=='retinopathy':
    # output=pr.classifyDiabeticRetinopathy('/home/sarru/Downloads/test/kaggle-skincancer/5_left.jpeg');
        # output=pr.classifySkinLesion('/home/sarru/Downloads/test/kaggle-skincancer/5_left.jpeg')
    # return jsonify({'output':output})

if __name__ == '__main__':
    app.run(debug=True)