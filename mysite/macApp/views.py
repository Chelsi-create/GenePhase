from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from macApp.models import PicUpload
from macApp.forms import ImageForm

# Create your views here.
def index(request):

    image_path = ''
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            newdoc = PicUpload(imagefile=request.FILES['imagefile'])
            newdoc.save()

            return HttpResponseRedirect(reverse('index'))

    else:
        form = ImageForm()

    documents = PicUpload.objects.all()
    for document in documents:
        image_path = document.imagefile.name
        image_path = '/' + image_path
        document.delete()
    
    request.session['image_path'] = image_path

    return render(request, 'index.html',
    {'documents':documents, 'image_path': image_path, 'form': form}
    )


    return render(request, 'index.html')


# import os
# import json

# import h5py
# import numpy as np
# import pickle as pk
# from PIL import Image

# # keras imports
# from keras.models import load_model
# from keras.preprocessing import img_to_array, load_img
# from keras.applications.vgg16 import VGG16, preprocess_input
# from keras.preprocessing import image
# from keras.models import Model
# from keras import backend as K
# import tensorflow as tf

# def prepare_img_224(img_path):
#     img = load_img(img_path, target_size=(224, 224))
#     x = img_to_array(img)
#     x = np.expand_dims(x, axis = 0)
#     x = preprocess_input(x)
#     return x


# global graph
# graph = tf.get_default_graph()


# CLASS_INDEX_PATH = 'static/imagenet_class_index.json'

# def get_predictions(preds, top = 5):

#     global CLASS_INDEX
#     CLASS_INDEX = json.load(open(CLASS_INDEX_PATH))

#     results = []
#     for pred in preds:
#         top_indices = pred.argsort()[-top:][::-1]
#         result = [tuple(CLASS_INDEX[str(i)]) + (pred[i],) for i in top_indices]
#         result.sort(key=lambda x: x[2], reverse = True)
#         results.append(result)
#     return results

# def graph_color_map(img_224):
#     color_map = load_model('static/')
#     print("Color Mappings.....")
#     out = color_map.predict(img_224)



