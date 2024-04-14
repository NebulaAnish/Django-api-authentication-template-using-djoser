## Django JWT auth template with djoser
It is a readymade template for getting started quickly with authentication APIs in Django. 
The project is setup using Django & PostgreSQL. Djoser package is used along with simplejwt to handle JWT token based authentication.
You can access the API documentation from this [link](https://documenter.getpostman.com/view/28093502/2sA3Bj7ZJ9#7982be85-814e-4496-973a-b42141ebe4a7). For detailed understanding of available APIs and modifications, visit the djoser official [docs](https://djoser.readthedocs.io/en/latest/index.html).
## Features
- Custom User with email login.
- JWT authentication.
- Send mail for account create confirmation, forget password and more.

## Get started
1. Clone repository. <br>
    ```$ git clone <link-to-repository>```
2. Create vitural environment inside the backend folder. <br>
    ```$ python -m venv .venv```
3. Activate the virtual environment 
    - On Linux/Mac: ```$ source .venv/bin/activate```
    - On Windows: ```$ venv\Scripts\activate```
4. Install required dependencies. <br>
    ```$ pip install - requirements.txt```
5. Create `.env` at same level as `manage.py`.
6. Add the required credentials.
7. Run server and access the apis. <br>
    `$ python manage.py runserver`