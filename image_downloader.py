import requests # request img from web
import shutil # save img locally
import datetime

t1=str(datetime.datetime.now().strftime("%d--%m--%Y %H-%M-%S"))


url = 'https://source.unsplash.com/300x300?nature,water' #prompt user for img url
file_name = 'one-numan'+ str(t1)+'.jpg'

res = requests.get(url, stream = True)

if res.status_code == 200:
    with open(file_name,'wb') as f:
        shutil.copyfileobj(res.raw, f)
    print('Image sucessfully Downloaded: ',file_name)
else:
    print('Image Couldn\'t be retrieved')
