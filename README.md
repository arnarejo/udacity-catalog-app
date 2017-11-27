# Udacity - Items Catalog Web App
This web app project is part of Udacity FullStack Nanodegree Program. The project requires building a sport products catalog app demonstrating CRUD functionality, 3rd party authentication/authorization via Google & Facebook and integrations for login and user permissions.

## About the project
Develop an application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.

## Requirements
- [Vagrant](https://www.vagrantup.com/)
- [VirtualBox](https://www.virtualbox.org/)
- [Python 2.7](https://www.python.org/)

## Dependencies
- [Vagrant](https://www.vagrantup.com/)
- [Udacity Vagrantfile](https://github.com/udacity/fullstack-nanodegree-vm)
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

## How to Install
1. Install Vagrant & VirtualBox
3. Go to Vagrant directory and either clone this repo or download and place zip here
3. Launch the Vagrant VM
`vagrant up`
4. Log into Vagrant VM
`vagrant ssh`
5. Navigate to `vagrant` folder as instructed in terminal
`cd /vagrant`
6. Navigate to `catalog` folder
`cd /vagrant`
7. Setup application database
`python database_setup.py`
8. Populate database
`python populate_db.py`
9. Run application
`python app.py`
10. Access the application locally using http://localhost:5000
