# APP-Engine-Resume

## Creating a website to host on Google App Engine
This guide uses the following structure for the project:

app.yaml: Configure the settings of your App Engine application.
www/: Directory to store all of your static files, such as HTML, CSS, images, and JavaScript.
* css/: Directory to store stylesheets.
  * style.css: Basic stylesheet that formats the look and feel of your site.
* images/: Optional directory to store images.
* index.html: An HTML file that displays content for your website.
* js/: Optional directory to store JavaScript files.
Other asset directories.

## Creating the app.yaml file
The app.yaml file is a configuration file that tells App Engine how to map URLs to your static files. In the following steps, you will add handlers that will load www/index.html when someone visits your website, and all static files will be stored in and called from the www directory.

Create the app.yaml file in your application's root directory:

1. Create a directory that has the same name as your project ID. You can find your project ID in the Console.
2. In directory that you just created, create a file named app.yaml.
3. Edit the app.yaml file and add the following code to the file:
runtime: python27
api_version: 1
threadsafe: true
```
handlers:
- url: /send_mail
  script: send_mail.app

- url: /
  static_files: www/index.html
  upload: www/index.html

- url: /(.+)
  static_files: www/\1
  upload: www/(.+)
```  

## Creating the index.html file
Create an HTML file that will be served when someone navigates to the root page of your website. Store this file in your www directory.

```
<html>
  <head>
    <title>Hello, world!</title>
    <link rel="stylesheet" type="text/css" href="/css/style.css">
  </head>
  <body>
    <h1>Hello, world!</h1>
    <p>
      This is a simple static HTML file that will be served from Google App
      Engine.
    </p>
  </body>
</html>
```

## Deploying your application to App Engine
When you deploy your application files, your website will be uploaded to App Engine. To deploy your app, run the following command from within the root directory of your application where the app.yaml file is located:
```
gcloud app deploy
```
Optional flags:

Include the --project flag to specify an alternate GCP Console project ID to what you initialized as the default in the gcloud tool. Example: --project [YOUR_PROJECT_ID]
Include the -v flag to specify a version ID, otherwise one is generated for you. Example: -v [YOUR_VERSION_ID]

## Viewing your application
To launch your browser and view the app at http://[YOUR_PROJECT_ID].appspot.com, run the following command:
```
gcloud app browse
```
