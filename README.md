# MIDL website template

## Creating a new website

To initialize a new MIDL website from this template, follow these steps:

1. Create a new repository on GitHub with the name `midl-website-20XX`,
setting the description to "Website of the 20XX edition of the MIDL conference series" and making sure not to initialize the
repository with a readme or license file.

2. Give the "webmasters" (Admin) and the "midl20XX" (Write) teams access to this repository.

3. Disable the wiki feature in the settings.

4. Clone the template repository and reconfigure the remote location:

   ```
   git clone https://github.com/MIDL-Conference/midl-website-template.git midl-website-20XX
   cd midl-website-20XX
   git remote set-url origin https://github.com/MIDL-Conference/midl-website-20XX.git
   git push origin master
   ```

5. Create a new site on netlify that is linked with this repository. Change the site name to `midl-20XX`.

6. Replace the content of this readme file with the netlify deploy status button.

## Building the website locally

To build the website locally instead of building it automatically on netlify, make sure the following is installed:

* Python 3.7
* pipenv

Use pipenv to install the website builder and all dependencies:

```
cd midl-website-20XX
pipenv sync
```

Then run the builder:

```
pipenv run python -m mwb . output/
```

This builds the website at `.` and writes the generated output into the directory `output/`.