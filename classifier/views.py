import cv2
import numpy as np
from PIL import Image

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from .serializers import ImagePredictionSerializer
from .models import ImagePrediction
from .parsers import ClassifierParser

from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions


class ClassifierViewSet(viewsets.ModelViewSet):
    queryset = ImagePrediction.objects.all()
    serializer_class = ImagePredictionSerializer
    model = ResNet50(weights='imagenet')
    parser = ClassifierParser

    def create(self, request, *args, **kwargs):

        # to be sure an image is provided
        img_serializer = self.get_serializer(data=request.data)
        img_serializer.is_valid(raise_exception=True)

        # prepare image for classifier model
        img_mem = img_serializer.validated_data["img"]
        img = Image.open(img_mem)
        array_img = image.img_to_array(img)
        final_img = cv2.resize(array_img, (224, 224), interpolation=cv2.INTER_AREA)
        x = np.expand_dims(final_img, axis=0)
        x = preprocess_input(x)

        # predict img and format it
        preds = self.model.predict(x)
        decoded_preds = decode_predictions(preds, top=3)[0]
        parsed_preds = self.parser.format_predictions(decoded_preds)

        # Save image and prediction results
        image_prediction = ImagePrediction.objects.create(img=img_mem, predictions=parsed_preds)

        # Serialize it to JSON
        serializer = self.get_serializer(image_prediction)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
