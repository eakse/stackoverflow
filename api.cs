string tenant = "";

string client_id = "your_client_id_here";

// https://docs.microsoft.com/en-us/onedrive/developer/rest-api/concepts/permissions_reference?view=odsp-graph-online
string scope = "Files.ReadWrite.All";



string url = "login.microsoftonline.com/common/oauth2/v2.0/";
WebRequest request = WebRequest.Create(url);
request.Method = "GET";
using (WebResponse response = request.GetResponse())
{
    using (Stream stream = response.GetResponseStream())
    {
        StreamReader reader = new StreamReader(stream);
        string text = reader.ReadToEnd();
    }
}

