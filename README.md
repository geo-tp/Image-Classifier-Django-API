Image Classifer Django API
===================

Submit an image and get predictions of its content with tensorflow ResNet50 model through an API endpoint.

Example
----

![](p1.webp)
![](p2.png)


Installation
-----

Created with python 3.10.6

- ### Create Python Virtual Env
    ```
    python -m venv env_name
    ```

- ### Use Python Virtual Env
    ```
    source env_name/bin/activate
    ```

- ### Install requirement
    ```
    python -m pip install -r requirements.txt
    ```

- ### Lauch dev server
    ```
    python manage.py runserver
    ```


Endpoint
--------

While dev server is launched, you can access `http://localhost:8000/api/v1/image-classifier` with browser. You can use the debug interface to list and get predictions.

![](p3.png)


Storage
------

Images are stored into `/media/` folder, predictions data are stored into database. 
You can configure database with `/config/settings.py`