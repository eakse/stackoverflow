from os import environ

if "GCLOUD_PROJECT" not in environ:
    environ['GCLOUD_PROJECT'] = 'fake-project-id'
