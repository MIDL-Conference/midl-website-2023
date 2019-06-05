# MIDL website template

To initialize a new MIDL website from this template, first create a new repository on GitHub with the name `midl-website-20XX`,
setting the description to "Website of the 20XX edition of the MIDL conference series" and making sure not to initialize the
repository with a readme file or anything else. Give the "webmasters" team access to this repository.

When the empty repository is created, disable the wiki feature in the settings.

Next, clone the template repository and reconfigure the remote location:

```
git clone https://github.com/MIDL-Conference/midl-website-template.git midl-website-20XX
cd midl-website-20XX
git remote set-url origin https://github.com/MIDL-Conference/midl-website-20XX.git
git push origin master
```

Create a new site on netlify that is linked with this repository. Change the site name to `midl-20XX`.

Finally, replace this readme file with the netlify deploy button.