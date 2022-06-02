# Helpo

<a href='https://helpo-t10.herokuapp.com//'><img src='ProjectManagement\static\img\Logo.png' type='image' width="80" align ="center"></a>

Halpo is a website that centralizes all the associations registered in Israel for volunteers and managers of associations, it allows users a convenient search of associations in which they can volunteer or be helped.
Association owners will be able to edit the profile of the associations and receive request messages from users of the site.
The system allows 3 types of users, a volunteer, an association manager and a system administrator. In order to register as an association director, you must be registered in the association register of GOV Israel and wait for the approval of the system director.
On the site you can:
Publish posts, create profile pages and upload photos of associations, send requests to association managers, report users and posts, send feedback to improve the site to the administrator, search associations, search users, filter search, and lots more!

- Link to the site: [Helpo](https://helpo-t10.herokuapp.com//))

## Install.

1. Install python (version: 3.9 or above).
2. Downloat the project to your computer. 
3. Install requirements packages (use the command: ```pip install -r requirements.txt```).
4. Run the project (use the command: ```python manage.py runserver```).

## Updating the Associations data base from GOV data csv.
open shell: python manage.py shell
then:       import associations.utils as au
            au.InsertAssociationData()

## Tools used for the project
<a href="https://www.djangoproject.com/"><img height="40" src="https://w7.pngwing.com/pngs/159/366/png-transparent-django-python-computer-icons-logo-python-text-label-rectangle.png"></a> <a href="https://www.python.org/"><img height="40" src="https://d31ezp3r8jwmks.cloudfront.net/6cYH8JcSU5PvVajahP7MtRfc"></a> <a href="https://github.com/"><img height="40" src="https://git-scm.com/images/logos/downloads/Git-Logo-1788C.png"></a> <a href="https://www.jenkins.io/"><img height="40" src="https://e7.pngegg.com/pngimages/815/9/png-clipart-jenkins-docker-continuous-delivery-installation-software-deployment-github-fictional-character-plugin-thumbnail.png"></a> <a href="https://www.atlassian.com/software/jira?&aceid=&adposition=&adgroup=95003645449&campaign=9124878702&creative=542638212647&device=c&keyword=jira&matchtype=e&network=g&placement=&ds_kids=p51242189318&ds_e=GOOGLE&ds_eid=700000001558501&ds_e1=GOOGLE&gclid=CjwKCAjwv-GUBhAzEiwASUMm4i9DEFz5MD6NnG4D6XW4l6Qik9cR3Ynwy9hoQ7uQpda6lMvS6z2pZBoCLhUQAvD_BwE&gclsrc=aw.ds"><img height="40" src="https://www.ambient-it.net/wp-content/uploads/2022/04/Logo-Jira-200x175-2.png"></a> <a href="https://html-css-js.com/"><img height="40" src="https://www.freepnglogos.com/uploads/html5-logo-png/html5-logo-devextreme-multi-purpose-controls-html-javascript-3.png"></a><a href="www.mongodb.com"><img height="40" src="https://toppng.com/uploads/preview/mongo-db-design-mongodb-logo-mongodb-11562879783bwj2cknalk.png"></a> <a href="https://code.visualstudio.com/"><img height="40" src="https://pngset.com/images/vscode-icons-horizontal-label-text-alphabet-word-transparent-png-2658501.png"></a>

## License & copyright

© Itzik Rahamim, Gil Ben Hamo, Daniel Dahan, Yovel Aloni

This project was developed as part of the "Software Project Management" course at SCE College.

Contact us: Team-10@gmail.com
Engoy:)