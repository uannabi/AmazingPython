
import request as req

url: str = 'https://checkip.amazonaws.com'
request = req.get(url)
ip: str = request.text

print('IP:',ip)
