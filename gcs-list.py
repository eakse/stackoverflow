from google.cloud import storage
from os import makedirs


# use a downloaded credentials file to create the client, see
# https://cloud.google.com/storage/docs/reference/libraries#setting_up_authentication
# this docs tells you to export the file location, but I personally 
# prefer the method used below as it allows for different credentials 
# within the same application.
# IMHO separation of what each serviceaccount can access increases
# security by tenfold. It's also usefull when dealing with different
# projects in the same app.


# Note that you'll also have to give the serviceaccount the
# permission "Storage Object Viewer", or one with more permissions.
# Always use the least needed to due to security considerations
# https://cloud.google.com/storage/docs/access-control/iam-roles


cred_json_file_path = 'path/to/file/credentials.json'
client = storage.Client.from_service_account_json(cred_json_file_path)


def download_blob(bucket: storage.Bucket, remotefile: str, localpath: str='.'):
    """downloads from remotepath to localpath"""
    localrelativepath = '/'.join(remotefile.split('/')[:-1])
    totalpath = f'{localpath}/{localrelativepath}'
    filename = f'{localpath}/{remotefile}'
    makedirs(totalpath, exist_ok=True)
    print(f'Current file details:\n  remote file: {remotefile}\n  local file:  {filename}\n')
    blob = storage.Blob(remotefile, bucket)
    blob.download_to_filename(filename, client=client)


def download_blob_list(bucketname: str, bloblist: list, localpath: str='.'):
    """downloads a list of blobs to localpath"""
    bucket = storage.Bucket(client, name=bucketname)
    for blob in bloblist:
        download_blob(bucket, blob, localpath)


def list_blobs(bucketname: str, remotepath: str=None, filetypes: list=[]) -> list:
    """returns a list of blobs filtered by remotepath and filetypes
    remotepath and filetypes are optional"""
    result = []
    blobs = list(client.list_blobs(bucketname, prefix=remotepath))
    for blob in blobs:
        name = str(blob.name)
        # skip "folder" names
        if not name.endswith('/'):
            # do we need to filter file types?
            if len(filetypes) > 0:
                for filetype in filetypes:
                    if name.endswith(filetype):
                        result.append(name)
            else:
                result.append(name)
    return result



bucketname = 'bucketnamegoeshere'
foldername = 'foldernamegoeshere'
filetypes = ['.pdf', '.docx'] # list of extentions to return
bloblist = list_blobs(bucketname, remotepath=foldername, filetypes=filetypes)

# I'm just using the bucketname for localpath for download location.
# should work with any path
download_blob_list(bucketname, bloblist, localpath=bucketname)
