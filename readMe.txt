This is a Django project for getting Transaction details and Summary details based on Name and category.

The Project was built using a Virtual interpreter, on PyCharm.
Kindly Install the packages mentioned in requirements.txt


The csv files are found on the root folder.
The CSV files have some random/dummy data created just for the project.

When the project is run, Kindly open the browser and put http://127.0.0.1:8000/.
It will show the API Urls.

If Pycharm is being used for running the project, then
    -In run config of PyCharm
        -Edit Configurations
            - Click on +
            - Django Server
            - Name it as anything You want
            - Port 8000
            - In Environment Section
                - Environment variables - PYTHONUNBUFFERED=1;DJANGO_SETTINGS_MODULE=djangoProject.settings (paste this)
            - CLick Apply and Ok
            (Screenshot of the Config is in the root folder)

You should be able to run the project now using PyCharms Run Button.

Postman was used to test API`s while running the code locally.

