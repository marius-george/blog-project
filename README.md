# ConspireHub

## Milestone Project 3 - Backend Development

<h2 align="center"><img src="blogproject/static/readme/images/blogproject-mockup.png"></h2>

* ConspireHub is a website where enthusiasts of conspiracy theories can create, read, edit, or delete articles about conspiracy theories.

* This is Milestone Project 3 for the Code Institute diploma in Web Application Development. This website was created using HTML, CSS, JavaScript, databases, and Flask.

## Live Project

[View the live project here.](https://blog-project-mp3-46d162068f45.herokuapp.com/)

## Repository

[Find the project repository here.](https://github.com/marius-george/blog-project)

# User Experience

## User stoires

### First-time Users

* As a first-time user, I want the landing page of the website to explain the purpose of the website and allow me to preview the content.

* As a first-time user, I want to be able to register for an account.

* As a first-time user, I want the website to work on any device.

### Returning Users

* As a returning user, I want to be able to log in to my account.

* As a returning user, I want to be able to create/ view/ edit/ delete my own articles.

* As a returning user, I want to be able to view other user’s articles.

* As a returning user, I want articles to include useful information such as a title, content, what user posted it and at what date. 

* As a returning user, I want to be able to get a quick overview of an article, but also view that article on its own page.

* As a returning user, I want to be able to access and use the website on any device.

### Buisness Owner

* As a business owner, I want users to be able to create, edit and delete their own articles.

* As a business owner, I want the adding, editing and deleting of articles to be limited to admin or those with permission. 

* As a business owner, I want it to be as easy as possible for users to submit articles, e.g. they can type the title and the paragraphs.

* As a business owner, I want the website to function and look good on any device.

## Design

- Distraction free blog text optimized for legibility with a menu bar interface that conveniently appears when you scroll up!
- Footer with social links and copyright information.
- Modern design with a subtle splash of color. Splash color used is a medium dark shade of cyan #0085A1

### Overview

- ConspireHub is a website dedicated to conspiracy theories. The name ConspireHub comes from a hub of conspiracies. The website features a simple and intuitive layout. Users can view articles without registering an account or can create, edit, and delete articles if they have registered with a new account.

### Colour

<h2 align="center"><img src="/workspaces/blog-project/blogproject/static/readme/images/colourPalette.png"></h2>

- These colors create a balanced and harmonious color palette that is both aesthetically pleasing and functionally effective. The teal provides a vibrant pop of color, drawing attention to key elements when hovered, while black, white, and grey create a neutral and professional backdrop that enhances readability and user experience.

### Typography

- Fonts used are Lora and Open Sans. These fonts used together indicates a balance between formality and approachability. Lora, with its serif elegance, provides a professional look while Open Sans offers a clean and modern feel for body text, ensuring excellent user experience and readability.

### Imagery 

- The image used as a banner is from (www.neurosciencenews.com). This is a splash image used to set the tone of the website.

### Icons

- I have used icons on social media footer to enhance the link used for each social media website. 

# Wireframes

- [View my wireframes in PDF form here](blogproject/static/readme/wireframes/conspirehub-wireframes.pdf).

# Features

## All Pages Features

### Nav Bar

<h2 align="center"><img src="blogproject/static/readme/images/conspirehub-navbar.png"></h2>
>

- The nav bar presents different options whether the user is logged in or logged out or an administrator.

- The links change colour on hover, to signal to the user which link they have the mouse over.

- The logo links back to the main landing page.

- The nav bar turns into a slide-out menu on smaller screen sizes

- Navbar expands when user is scrooling through the articles to make it easier to access menu buttons.

### Footer 

<h2 align="center"><img src="blogproject/static/readme/images/conspirehub-footer.png"></h2>

- The footer includes the website’s name. 

- It also features icons with links out to social media. These windows open in a new tab.

### Home

- The home page displays article titles. Below each title, it shows the name of the article's author and the date the article was published.

- When the article title is clicked it opens the article showing the article title, author, date that article was posted and article text.

- If user is logged in and the article opened is posted by him the website will show edit and delete buttons at the bottom of the page.

### About

- About page presents a description about the website purpose. It contains About, Our Mission, Our Approach and Join Us sections.

### Log In

- Log in page have email and password field needed to authenticate to the website to be able to post articles followed by Log in button.

### Register

- Register page has a form with email, desired username and password where user needs to input to be able to register.

### Account

- Here user can set a profile picture and update his email or password.

### Create article

- Here the user can write the title and the text of the article. and use post button to post it.


# Technologies Used

## Languages Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)

- [CSS3](https://en.wikipedia.org/wiki/CSS)

- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)

- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

## Frameworks Libraries and Programs

- [Heroku](https://id.heroku.com/login)
  - Heroku is the deployment source I used for this project. I'm also using it for the Postgres relational database

- [MongoDB](https://www.mongodb.com/)
    - I'm using MongoDB for my non-relational database.

- [Flask](https://flask.palletsprojects.com/en/2.2.x/templating/)
  - Templating language I've used with Python to add logic to my html templates.

- [Jinja](https://jinja.palletsprojects.com/en/3.0.x/)
  - Templating language I've used with Python to add logic to my html templates.

- [Materialize CSS](https://materializecss.com/)
  - Front-end library with HTML, CSS and Javascript based componants. I used features including Nav bar, Cards, Buttons and Forms.

- [jQuery](https://jquery.com/)
  - I used jQuery to add functionality to MaterialiseCSS componants.

- [Google Fonts](https://fonts.google.com/)
  - Two fonts are imported from google fonts.
  
- [Font awesome](https://fontawesome.com/)
  - I used icons from font awesome on buttons.

- [Git](https://git-scm.com/)
  - Git was used as a version control in the terminal.

- [Github](https://github.com/)
  - Github was used to create and store the project repository.

- [Gitpod](https://gitpod.io/)
  - Gitpod was used to create my files and where I wrote the code.

- [Balsamiq](https://balsamiq.com/)
  - Balsamiq was used to create Wireframes for the project during the initial planning stage.

- [Techsini](https://techsini.com/multi-mockup/)
  - Techsini was used to help check responsiveness and take screenshots of the page at different screen sizes.

- [Adobe Photoshop](https://www.adobe.com/ie/products/photoshop.html)
  - Photoshop was used to resize images for the website.

- [TinyPNG](https://tinypng.com/)
  - TinyPNG was used to compress images for a faster loading time.

- [WebFormatter](https://webformatter.com/html)
  - WebFormatter was used to help beautify the code.

- [Google Chrome Dev Tools](https://developer.chrome.com/docs/devtools/)
  - Google Chrome's Dev Tools were used while building the project to test responsiveness and for debugging.

- [dbdiagram](https://dbdiagram.io/)
  - Tool used to mock up database structure diagram.

- [Unsplash](https://unsplash.com/)
  - Unsplash was used to source the jumbatron imager.

# Testing

- Please refer [here](blogproject/static/readme/testing/testing.md) for more information on testing of the ConspireHub website

# Deployment

## Creating a Gitpod Workspace

The project was created in Gitpod using the Code Institute Gitpod Full Template using these steps:

1. Log in to GitHub and go to the [Code Institute student template for Gitpod](https://github.com/Code-Institute-Org/gitpod-full-template)
2. Click 'Use this Template' next to the Green Gitpod button.
3. Add a repository name and click 'Create reposiory from template'.
4. This will create a copy of the template in your own repository. Now you can click the green 'Gitpod' button to open a workspace in Gitpod.

## Forking the GitHub Repository

Forks are used to propose changes to someone else's project or to use someone else's project as a starting point for your own idea. By forking the GitHub Repository you make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository.

To Fork a Github Repository:

1. Log in to GitHub and go to the [GitHub Repository](https://github.com/marius-george/blog-project)
2. Locate the Fork button in the top-right corner of the page, click Fork.
3. You should now have a copy of the original repository in your GitHub account.

## Making a Local Clone

You will now have a fork of the repository, but you don't have the files in that repository locally on your computer.

To make a local clone:

1. Log in to GitHub and go to the [GitHub Repository](https://github.com/marius-george/blog-project)
2. Above the list of files, click  Code.
3. To clone the repository using HTTPS, under "Clone with HTTPS", click the 'Copy' icon. To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click Use SSH, then click the 'Copy' icon. To clone a repository using GitHub CLI, click Use GitHub CLI, then click the 'Copy' icon.
4. Open Git Bash.
5. Change the current working directory to the location where you want the cloned directory.
6. Type git clone, and then paste the URL you copied earlier. It will look like this, with your GitHub AE username instead of YOUR-USERNAME:

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `blogproject`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://docs.github.com/en/github-ae@latest/get-started/quickstart/fork-a-repo) for the GitHub quick start guide with images and more detailed explanations of the above process.

## Creating an application with Heroku

You will need to deploy the application using Heroku.

1. Create a requirements.txt file by typing ``` pip3 freeze --local > requirements.txt ``` into the Gitpod CLI. Ensure this is added to your .gitignore file.
2. Create a Procfile by typing ```echo web: python app.py > Procfile```. Open it and ensure it doesn't have a new line, as this can create errors. Ensure it starts with a capital P.
3. Add and commit these files to Github.
4. Go to [Heroku](https://dashboard.heroku.com/apps). Log in or create an account
5. Click the 'New' button and click 'Create new app'.
6. Enter a unique name for your project with no capital letters or spaces and select your region. Click 'Create App'.
7. Inside your project, go to the Resources tab and create a Heroku Postgres Database
8. Inside your project, go to the 'Settings' tab. Scroll down and click 'Reveal Config Vars'.
9. Add in the following variables
  - IP : 0.0.0.0
  - PORT : 5000
  - MONGO_DBNAME : Your MongoDB database name
  - MONGO_URI : This can be found on MongoDB by going to Clusters, Connect, Connect to your application
  - SECRET_KEY : Your secret key
10. Deploy your project by going to the Deploy tab and choose 'Connect to Github'
11. Find your repository name and select Connect.
12. To connect your Heroku database, go to 'More' in the top right and select run console. Enter ```python3``` to access the python intepreter.
13. Then type ```From blogproject import db```. Then type ```db.create_all()```. You can then exit the console.