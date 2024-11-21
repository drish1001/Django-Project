# Music-Project

This repository contains a Django-based web application that focuses on managing and displaying music-related content. It includes features for user authentication, media handling, and a functional music application with a user-friendly interface.

## **Features** 

- **🎶 Music App**:
  - Browse and interact with music-related content.
  - Manage and display songs, album covers, and other media files.

- **🔒 User Authentication**:
  - Supports user registration, login, logout, and profile management.
  - Includes pre-built templates for authentication workflows such as signup and login.

- **📂 Media Management**:
  - Handles media files like images (e.g., album covers) and audio (e.g., songs).
  - Sample media files included:
    - Images: *avengers1.jpg*, *ironman.jpeg*, *titanic.jpg*.
    - Audio: *Titanic-Ringtone.mp3*.

- **🎨 Customizable Templates**:
  - Pre-designed templates for pages like home, navigation, song saving, and user authentication.

## **Project Structure** 

```
Django-Project/
├── myproject/
│   ├── manage.py             
│   ├── db.sqlite3            
│   ├── musico/               # Main app for music-related functionality
│   │   ├── templates/music/  
│   │   ├── models.py         
│   │   ├── views.py          # Logic for handling requests
│   │   ├── urls.py           
│   │   └── admin.py          
│   ├── userauth/             # App for user authentication
│   │   ├── templates/userauth/
│   │   ├── models.py         
│   │   ├── views.py          # Logic for handling authentication requests
│   │   ├── forms.py          
│   │   └── urls.py           
├── media/                    # Directory for media files (images, audio)
├── static/                   
└── requirements.txt          
```

## **Installation** ⚙️

1. Clone the repository:
   ```bash
   git clone https://github.com/drish1001/Django-Project.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Django-Project
   ```
3. Set up a virtual environment (optional but recommended):
   ```bash
   python3 -m venv myprojectenv
   source myprojectenv/bin/activate  # On Windows: myprojectenv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Apply migrations to set up the database:
   ```bash
   python manage.py migrate
   ```
6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## **Usage**

1. Access the application at `http://127.0.0.1:8000` in your browser.
2. Explore the music app to view songs and related media.
3. Use the user authentication system to register, log in, or manage your account.

## **Media Files**

The project includes sample media files located in the `media/` directory:

- **Images**: Examples include *avengers1.jpg*, *ironman.jpeg*, *titanic.jpg*.
- **Audio**: Example file is *Titanic-Ringtone.mp3*.

Feel free to replace these with your content!

## **Customization** 🛠️

- Modify templates in the `templates/` directory to change the look and feel of the application.
- Update models in `models.py` to add or alter database fields.
- Add new views or routes in `views.py` and `urls.py`.

## **Contributing** 🤝

Contributions are welcome! If you have ideas for new features or improvements:

1. Fork this repository.
2. Create a new branch (`feature/new-feature`).
3. Commit your changes and push them to your forked repository.
4. Submit a pull request with a detailed description of your changes.
