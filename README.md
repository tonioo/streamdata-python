# streamdata-python

Simple Python 3 app using [streamdata.io](https://streamdata.io/).

## Step by step setup

* Create a free account on streamdata.io https://portal.streamdata.io/#/register to get an App token

* Clone this repository

* Create a virtualenv and install requirements:

```bash
> cd streamdataio-python
> python3 -m venv streamdataio_env
> source streamdataio_env/bin/activate
> pip install -r requirements.txt
```

* Edit ``client.py`` and replace ``[YOUR_STREAMDATAIO_APP_TOKEN]`` with your App token

* Finally, launch the demo:

```python
> python client.py
```

You should see data and patches pushed in your application and
displayed on your terminal.

you can use the provided demo example API which simulates updating
stocks prices from a financial market:
'http://stockmarket.streamdata.io/v2/prices'.

Feel free to test it with any REST/Json API of your choice.
