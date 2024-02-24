import csv
def List_job(jenkins_url,jenkins_user,jenkins_pass):
    import jenkins
    jen_server = jenkins.Jenkins(jenkins_url, username=jenkins_user, password = jenkins_pass)
    user = jen_server.get_whoami()
    jobs = jen_server.get_jobs()
    job_stats=[]
    for i in jobs:
        job_name = i["name"]
        job_url = i['url']
        job_status = i['color']
        job_stats.append([job_name,job_url,job_status])
    return job_stats
#c=List_job('http://ec2-18-233-99-3.compute-1.amazonaws.com:8080','devops','devops')

#print(c)  
# with open('example.txt','a') as f:
#     content = "adding date into file\n"
#     f.write(content)

# with open('example.txt','r') as file:
#     cont = file.read()
#     print(cont)
data = List_job('http://ec2-18-233-99-3.compute-1.amazonaws.com:8080','devops','devops')
with open("jenkins_object.csv",'w') as j:
    write_row = csv.writer(j)
    write_row.writerow(['JOB_NAME', 'JOB_URL', 'JOB_STATUS'])
    for item in data:
        write_row.writerow(data)
