#sudo apt-get -y install python-pip
#curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
#python get-pip.py
#sudo pip install boto
#python c3.py in the same folder of code


#US West (Oregon) Region	This uses Amazon S3 servers in Oregon.	s3-us-west-2.amazonaws.com	us-west-2
#US West (Northern California) Region	This used Amazon S3 servers in Northern California.	s3-us-west-1.amazonaws.com	us-west-1
#EU (Ireland) Region	This uses Amazon S3 servers in Ireland.	s3-eu-west-1.amazonaws.com	EU
#Asia Pacific (Singapore) Region	This uses Amazon S3 servers in Singapore.	s3-ap-southeast-1.amazonaws.com	ap-southeast-1
#Asia Pacific (Sydney) Region	This uses Amazon S3 servers in Sydney.	s3-ap-southeast-2.amazonaws.com	ap-southeast-2
#Asia Pacific (Tokyo) Region	This uses Amazon S3 servers in Tokyo.	s3-ap-northeast-1.amazonaws.com	ap-northeast-1
#South America (San Paulo) Region	This uses Amazon S3 servers in San Paulo.	sa-east-1


from boto.s3.connection import S3Connection,Location
from boto.s3.key import Key
import boto

conn = S3Connection('AKIAJP3BDZM4BVZJDIEA','lzxyKI51aRoQf1lDB91MD5WGBG1RJrTFiVP+//GH')


if __name__ == "__main__":

    while True:
        operations = ["List Buckets","Create Bucket", \
                    "Create Bucket with Location","Delete Bucket", \
                     "Write Object","List Objects","Exit"]

        for x in range(len(operations)):
            print x," ", operations[x]

        op = input("Enter the number of operation you want to perform: ")

        if op == 0:
            list = conn.get_all_buckets()
            for b in list:
                print b.name +" "+b.creation_date + "\n"
        
        elif op == 1:
            while True:
                buck = raw_input("Enter the name for bucket: ")
                try:
                    done = conn.create_bucket(buck)
                    print ("Done\n")
                    break
                except Exception as e:
                    print "Name is already taken.!!!"
                    continue
        
        elif op == 2:
            print "Possible locations are: "
            print '\n'.join(i for i in dir(Location) if i[0].isupper())
            loc = raw_input("Enter the name of location: ")
            while True:
                buck = raw_input("Enter the name for bucket: ")
                try:
                    done = conn.create_bucket(buck,location=loc)
                    print ("Done\n")
                    break
                except Exception as e:
                    print "Name is already taken.!!!"
                    continue

        elif op == 3:
            print "List of Buckets available:"
            list = conn.get_all_buckets()
            for b in list:
                print b.name + "\n"
            delBuck = raw_input("Enter the name of bucket to be deleted: ")
            conn.delete_bucket(delBuck)
            print ("Done\n")
        
        elif op == 4:
            buck = raw_input("Enter name of bucket: ")
            nonexistent = conn.lookup(buck)
            if nonexistent is None:
                print "No such bucket!"
            b = conn.get_bucket(buck)
            k = Key(b)
            object = raw_input("Enter the key and object sperated by ',': ")
            ki ,data = object.split(",")
            k.key = ki
            k.set_contents_from_string(data)
            print ("Data entered successfully as: ", k.get_contents_as_string())
        
        elif op == 5:
            b = raw_input("Enter the name of Bucket: ")
            nonexistent = conn.lookup(b)
            if nonexistent is None:
                print "No such bucket!"
            for key in nonexistent.list():
                print "{name}\t{size}\t{modified}".format(
                name = key.name,
                size = key.size,
                modified = key.last_modified,
                )
        
        elif op == 6:
            break

