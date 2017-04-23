import gcs_client

credentials_file = 'HelloWorld-5b5ab5e9eba6.json'
project_name = 'helloworld-163119'

credentials = gcs_client.Credentials(credentials_file)
project = gcs_client.Project(project_name, credentials)

buckets = project.list()
objects = buckets[0].list()


def buckets(project):
    # Print buckets in the project
    buckets = project.list()
    print 'Buckets:\n\t-', '\n\t- '.join(map(str, buckets))

def bucketInfo(project,buckNo):
    # Print some information from first bucket
    buckets = project.list()
    bucket = buckets[buckNo]
    print 'Bucket %s is located in %s with storage class %s' % (bucket, bucket.location,bucket.storageClass)

def writeObject(project,buckNo,fileName,text):
    # Writing Object
    buckets = project.list()
    bucket = buckets[buckNo]
    with bucket.open(fileName, 'w') as obj:
        obj.write(text + '\n')

    with bucket.open(fileName) as obj:
        print obj.read()


def readObject(objects,fileNo):
    # Reading Object
    if objects:
        with objects[fileNo].open() as obj:
            print 'Contents of file %s are:\n' % obj.name, obj.read()


def deleteObject(objects,fileNo):
    if objects:
        obj = objects[0]
        print 'Deleting object %s' % obj
        obj.delete()


def listObject(buckets,buckNo):

    objects = buckets[0].list()
    bucket = buckets[buckNo]

    print 'Contents of bucket %s:' % bucket
    if objects:
        print '\t','\n\t'.join(map(lambda o: o.name + ' has %s bytes' % o.size, objects))
    else:
        print '\tThere are no objects'


if __name__ == "__main__":
    
    while True:
        operations = ["List Buckets","Get Bucket Info","Write Object to bucket", "Read Object from bucket", 
                                          "Delete Object from bucket", "List Objects of Bucket", "Exit"]

        for x in range(len(operations)):
            print x," ", operations[x]

        op = input("Enter the number of operation you want to perform: ")
        if op == 0:
            buckets(project)
        elif op == 1:
            buck = input("Enter the no of bucket you want info for: ")
            bucketInfo(project,buck-1)
        elif op == 2:
            buck = input("Enter the bucket no you want to write into: ")
            fileName = raw_input("Enter file name: ")
            text = raw_input("Enter Text: ")
            writeObject(project, buck-1, fileName, text)
        elif op == 3:
            buck = input("Enter bucket: ")
            buckets = project.list()
            objects = buckets[buck-1].list()
            for o in objects:
                print objects.index(o), " " , o.name
            fileNo = input("Enter the file no.: ") 
            readObject(objects,fileNo)
        elif op == 4:
            buck = input("Enter bucket: ")
            buckets = project.list()
            objects = buckets[buck-1].list()
            for o in objects:
                print objects.index(o), " " , o.name
            fileNo = input("Enter the file no.: ") 
            deleteObject(objects,fileNo)
        elif op == 5:
            buckets = project.list()
            for b in buckets:
                print buckets.index(b), " ", b.name
            buckNo = input("Enter Bucket no.: ")
            listObject(buckets,buckNo)
        elif op == 6:
            break
