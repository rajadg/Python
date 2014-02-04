
import urllib2
import os
import time
import sys
import base64


# The parameters used in this sample
nuxeo_ip = "172.29.242.248"
nuxeo_port = "8888"
nuxeo_user = "Administrator"
nuxeo_pwd = "Administrator"


# Return the automation url for the given API
def automation_url(ip_address, port=None, api=None):
    if (port == None or port == 0 or str(port) == "") :
        return "http://" + ip_address + "/nuxeo/site/automation/" + api
    else:
        return "http://" + ip_address + ":" + str(port) + "/nuxeo/site/automation/" + api

# Make the authorization header for the given credentials
def authorization_header(user, pwd) :
    return "Basic " + base64.b64encode(user + ":" + pwd)

# Create a Http Request
def create_request(url, headers=None, request_data=None):
    '''
        Make a Http request given url, headers and request-body
    '''
    # Create the request and set params
    request = urllib2.Request(url)
    # Configure headers
    if not headers == None:
        for key in headers.keys():
            request.add_header(key, headers[key])
    # Configure the request body
    request.data = request_data
    # open the url and return the connection
    return urllib2.urlopen(request)

# Convert json string data to a python object
def json_to_pyobj(json_data) :
    result = json_data.replace('null', 'None')
    result = result.replace('true', 'True')
    result = result.replace('false', 'False')
    #result = result.replace('null', 'None')
    return eval(result)

# Make a Nuxeo Automation request and provide the result as a python object
def make_nuxeo_request(url, headers=None, request_data=None, user=None, pwd=None):
    if headers == None :
        headers = { }
    if None == user :
        headers["Authorization"] = authorization_header(nuxeo_user, nuxeo_pwd)
    else :
        headers["Authorization"] = authorization_header(user, pwd)
    if not None is request_data :
        headers["content-type"] = "application/json+nxrequest"
        headers["X-Nxdocumentproperties"] = "*"
        headers["Accept"] = "application/json+nxentity, */*"
    conn = create_request(url, headers, request_data)
    return json_to_pyobj(conn.read())

# print the list of files/folders from the collection (List)
def print_contents(collection) :
    for item in collection:
        print item["type"] + ": " + item["title"] + \
              (" created by " + item["properties"]["dc:creator"] \
                   if item.has_key('properties') and item["properties"].has_key("dc:creator") else "")

# Get Automation info
'''target_url = automation_url(nuxeo_ip, nuxeo_port, "")
result = make_nuxeo_request(target_url)
print result'''

# Query Other Docs for a given user
target_url = automation_url(nuxeo_ip, nuxeo_port, "Clouddesk.OtherDocsList")
result = make_nuxeo_request(target_url, user='load04', pwd='password', request_data = '{"params": {}}')
#print result

print "Other docs list: "
print_contents(result["entries"])

# Query the UserWorkspace.Get API to get workspace information
target_url = automation_url(nuxeo_ip, nuxeo_port, "UserWorkspace.Get")
result = make_nuxeo_request(target_url, user='load04', pwd='password', request_data = '{"params": {}}')
print "response for UserWorkspace.Get: "
print "uid : " + result["uid"]
workspace_id = result['uid']

# Query Children of workspace (top level folders)
get_children_workspace = '{"params": {"id": "org.nuxeo.drive.hierarchy.permission.factory.PermissionTopLevelFactory#"}}'
target_url = automation_url(nuxeo_ip, nuxeo_port, "NuxeoDrive.GetChildren")
result = make_nuxeo_request(target_url, user='load04', pwd='password', request_data = get_children_workspace )
#print "response for NuxeoDrive.GetChildren for User Workspace : "
#for folder in result :
#    print folder["name"]



template_doc_query = \
'''{"params": {"query": "SELECT * FROM Document WHERE
    ecm:parentId = 'FOLDER_ID' AND
    ecm:currentLifeCycleState != 'deleted' AND
    ecm:mixinType = 'Folderish' AND
    ecm:mixinType != 'HiddenInNavigation' AND
    ecm:isCheckedInVersion = 0"}}'''.replace('\n', '\\n')

# Query contents of my docs
get_children_request_template = '{"params": {"id": "FOLDER_ID"}}'
get_children_sub_folder_request_template = '{"params": {"id": "defaultFileSystemItemFactory#default#FOLDER_ID"}}'
target_url = automation_url(nuxeo_ip, nuxeo_port, "Document.Query")
result = make_nuxeo_request(target_url, user='load04', pwd='password', request_data = template_doc_query.replace('FOLDER_ID', workspace_id) )
#print "response for Document.Query for contents of My Docs : "
#print_contents(result["entries"])



# Get contents of my docs folder
def nuxeo_doc_query(ip, port, user, pwd, folder_id = "") :
    result = make_nuxeo_request(url=automation_url(nuxeo_ip, nuxeo_port, "Document.Query"), \
                    user=user, pwd=pwd, \
                    request_data = template_doc_query.replace('FOLDER_ID', folder_id) )
    return result

# Get contents of others docs folder
def nuxeo_others_docs_list(ip, port, user, pwd) :
    result = make_nuxeo_request(url=automation_url(nuxeo_ip, nuxeo_port, "Clouddesk.OtherDocsList"), \
                    user=user, pwd=pwd, request_data = '{"params": {}}' )
    return result


# Get all folder contents in tree structure - recursively
def get_folders_recursive(ip, port, user, pwd, folder_id = "", folder_type='local') :
    template_folder_id = 'defaultFileSystemItemFactory#default#FOLDER_ID'
    if (folder_type == 'my docs'):
        template_folder_id = 'userSyncRootParentFactory#default#FOLDER_ID'
    elif (folder_type == 'shared'):
        template_folder_id = 'permissionSyncRootFactory#default#FOLDER_ID'
    elif (folder_type == 'others docs' or folder_type == 'other docs') :
        template_folder_id = 'sharedSyncRootParentFactory#'
    elif (folder_type == 'workspace'):
        template_folder_id = 'org.nuxeo.drive.hierarchy.permission.factory.PermissionTopLevelFactory#'

    if (folder_type == 'my docs'):
        result = nuxeo_doc_query(ip, port, user, pwd, folder_id)
    elif (folder_type == 'others docs' or folder_type == 'other docs') :
        result = nuxeo_others_docs_list(ip, port, user, pwd)
    else:
        result = make_nuxeo_request(url=automation_url(nuxeo_ip, nuxeo_port, "NuxeoDrive.GetChildren"), \
                        user=user, pwd=pwd, \
                        request_data = '{"params": {"id": "' + template_folder_id.replace('FOLDER_ID', folder_id) + '"}}' )


    def extract_children (child, contents, ftype):
        return {'_title' :  child["name"], \
                '_uid': child["id"].split('#')[-1], \
                '_folder' : str(child['folder']).lower() == 'true', \
                '_type' : ftype, \
                'contents' : contents }
    def extract_contents (child, contents, ftype) :
        return {'_title' :  child["title"], \
                '_uid': child["uid"], \
                '_folder' : str(child['type']).lower() == 'folder', \
                '_type' : ftype, \
                'contents' : contents }
    list = []
    if (folder_type == 'workspace' ):
        for top_level_item in result :
            child_id = top_level_item["id"].split('#')[-1]
            contents = [ 'error' ]
            try:
                contents = get_folders_recursive(ip, port, user, pwd, child_id, top_level_item["name"].lower())
            except Exception as e:
                contents = [ str(e) ]
            list.append(extract_children(top_level_item, contents, top_level_item["name"].lower()))
    elif (folder_type == 'my docs') or (folder_type == 'others docs' or folder_type == 'other docs'):
        for entry in result["entries"] :
            contents = []
            try:
                child_type = 'local'
                if (folder_type == 'others docs' or folder_type == 'other docs') :
                    child_type = 'shared'
                contents = get_folders_recursive(ip, port, user, pwd, entry['uid'], child_type)
            except Exception as e:
                contents = [ str(e) ]
            list.append(extract_contents(entry, contents, child_type))
    else:
        for entry in result:
            contents = []
            try:
                child_type = 'local'
                if (folder_type == 'others docs' or folder_type == 'other docs') :
                    child_type = 'shared'
                contents = get_folders_recursive(ip, port, user, pwd, entry['uid'], folder_type=child_type)
            except Exception as e:
                contents = [ str(e) ]
            list.append(extract_children(entry, contents, child_type))
    # print list
    return list

def create_folder_nuxeo(parent_id, folder_name) :
    target_url = automation_url(nuxeo_ip, nuxeo_port, "NuxeoDrive.CreateFolder")
    result = make_nuxeo_request(target_url, user='load04', pwd='password', request_data = '{"params": { "name" : "' + folder_name + '", "parentId": "'+ parent_id + '"}}')
    print result

# create the folders
create_folder_nuxeo(workspace_id, "gopala gopala")

# print get_folders_recursive("172.29.242.248", "8888", "load04", "password", folder_id = "", folder_type="workspace")

#print get_folders_recursive("172.29.242.248", "8888", "load04", "password", folder_id = "c96bb06c-a9fa-4cf2-9cd5-ac6ba17b26d0", folder_type="local")




