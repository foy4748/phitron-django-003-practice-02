# Instructions    

- DEMO Video - [Google Drive](https://drive.google.com/file/d/1tqz4hHNg7beeGxldBTezvg2VqPoscRS6/view?usp=drive_link)

- Requirement Doc **Module 15.5** : [Google Doc](https://docs.google.com/document/d/1zWnqCoXS4Y0Qzh87hHyZqzM0GLjTHpaDWVP2rvrEZQI/edit)    

- Requirement Doc  **Module 19.5** : [Google Doc \(Currently branch\)](https://docs.google.com/document/d/1ZWJidFtkLZFkKCY4lMSdvvPOWJsjddu65h_r0olNfPo/edit)    

After cloning this repository, you need to initiate a virtual environment. Then install necessary packages within it.

1. Go to project directory
```console
cd phitron-django-003-practice-02
```
Here `musicians_directory_project` is the project folder, where the `settings.py` is the root settings file for the whole project, `urls.py` is the main url pattern handler. (CEO Shaheb 😉)    


2. Run the command given below to create a virtual environment within the .venv directory
```console
# For Linux/MacOS
python3 -m venv .venv
```

```console
# For Windows
python -m venv .venv
```
**You need to do this once, after cloning the project. .venv folder is ignored within .gitignore file**    


3. Now run the command below to activate the virtual environment.
```console
# For Linux/MacOS
source .venv/bin/activate
```

```console
# For Windows
.\.venv\Scripts\activate
```


4. Now run this once to install all the packages
```console
pip install -r requirements.txt
```


5. You are good to go. To start the development server, simply run
```console
python manage.py runserver
```
**Make sure you are within the right directory by entering `ls` or `dir` command to check if manage.py exists**    


