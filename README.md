# retinoskin-model
## API for retinoskin ml model
* CNN Model for Image classification.
* Kaggle Dataset for Diabetic Retinopathy.
* ISIC Dataset for Skin Cancer.
* Data processing through Flask REST APIs.
<br>

> POST    /api/model/test    
```
{
	"url":"https://res.cloudinary.com/example/notLoggedInUsers/melanoma.jpg",
	"option":"retinopathy"
}
```
